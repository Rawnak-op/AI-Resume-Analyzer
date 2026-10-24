"""
cache.py

Redis-based caching layer for the ATS pipeline.

Three cache layers:
  1. Embeddings      — keyed by MD5 of the input text         (TTL: 6h)
  2. LLM Extraction  — keyed by MD5 of input text             (TTL: 24h)
  3. Full ATS result — keyed by MD5 of resume + JD combined   (TTL: 30min)

If Redis is unavailable (e.g., REDIS_URL not set, or connection fails),
every function degrades gracefully and returns None so the caller
falls through to the real computation.
"""

import os
import json
import hashlib
import logging

import redis

logger = logging.getLogger(__name__)

# ------------------------------------
# TTLs (seconds)
# ------------------------------------

TTL_EMBEDDING = 6 * 60 * 60       # 6 hours
TTL_LLM       = 24 * 60 * 60      # 24 hours
TTL_ATS       = 30 * 60           # 30 minutes


# ------------------------------------
# Client
# ------------------------------------

def _make_client():
    """
    Returns a Redis client if REDIS_URL is configured, otherwise None.
    Uses decode_responses=False so we can store raw bytes (numpy arrays).
    """
    url = os.getenv("REDIS_URL")
    if not url:
        logger.warning("REDIS_URL not set — caching disabled.")
        return None
    try:
        client = redis.from_url(url, decode_responses=False, socket_connect_timeout=2)
        client.ping()
        logger.info("Redis connection established.")
        return client
    except Exception as e:
        logger.warning(f"Redis unavailable: {e} — caching disabled.")
        return None


# Singleton client — created once at import time.
_client = _make_client()


# ------------------------------------
# Key helpers
# ------------------------------------

def _md5(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def embedding_key(text: str) -> str:
    return f"emb:{_md5(text)}"


def resume_key(text: str) -> str:
    return f"resume:{_md5(text)}"


def job_key(text: str) -> str:
    return f"job:{_md5(text)}"


def ats_key(resume_text: str, jd_text: str) -> str:
    combined = _md5(resume_text) + _md5(jd_text)
    return f"ats:{_md5(combined)}"


# ------------------------------------
# Generic get / set
# ------------------------------------

def cache_get(key: str):
    """Return cached bytes, or None on miss / error."""
    if _client is None:
        return None
    try:
        return _client.get(key)
    except Exception as e:
        logger.warning(f"Redis GET failed for key={key}: {e}")
        return None


def cache_set(key: str, value: bytes, ttl: int):
    """Store bytes in Redis with a TTL. Silently fails if Redis is down."""
    if _client is None:
        return
    try:
        _client.setex(key, ttl, value)
    except Exception as e:
        logger.warning(f"Redis SET failed for key={key}: {e}")


# ------------------------------------
# Layer 1 — Embedding cache
# ------------------------------------

def get_cached_embedding(text: str):
    """
    Returns a Python list (the embedding vector) from cache, or None on miss.
    """
    raw = cache_get(embedding_key(text))
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except Exception:
        return None


def set_cached_embedding(text: str, embedding):
    """
    Stores a numpy array or list as JSON bytes in Redis.
    """
    try:
        # numpy arrays aren't JSON-serialisable directly
        value = json.dumps(embedding.tolist() if hasattr(embedding, "tolist") else embedding)
        cache_set(embedding_key(text), value.encode("utf-8"), TTL_EMBEDDING)
    except Exception as e:
        logger.warning(f"Failed to cache embedding: {e}")


# ------------------------------------
# Layer 2 — LLM extraction cache
# ------------------------------------

def get_cached_llm(key: str):
    """
    Returns a dict (parsed JSON) from cache, or None on miss.
    key should be resume_key(text) or job_key(text).
    """
    raw = cache_get(key)
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except Exception:
        return None


def set_cached_llm(key: str, pydantic_obj):
    """
    Serialises a Pydantic model to JSON and stores it in Redis.
    """
    try:
        value = pydantic_obj.model_dump_json()
        cache_set(key, value.encode("utf-8"), TTL_LLM)
    except Exception as e:
        logger.warning(f"Failed to cache LLM result: {e}")


# ------------------------------------
# Layer 3 — Full ATS result cache
# ------------------------------------

def get_cached_ats(resume_text: str, jd_text: str):
    """
    Returns a dict (the full ATS JSON) from cache, or None on miss.
    """
    raw = cache_get(ats_key(resume_text, jd_text))
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except Exception:
        return None


def set_cached_ats(resume_text: str, jd_text: str, ats_obj):
    """
    Serialises a Pydantic ATSAnalysis model to JSON and stores it.
    """
    try:
        value = ats_obj.model_dump_json()
        cache_set(ats_key(resume_text, jd_text), value.encode("utf-8"), TTL_ATS)
    except Exception as e:
        logger.warning(f"Failed to cache ATS result: {e}")
