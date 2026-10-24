import API from "../services/api";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
    Upload,
    Sparkles,
    Search,
    FileText,
    CloudUpload,
    CheckCircle2,
} from "lucide-react";

import ATSCard from "./ATSCard";
import BreakdownCard from "./BreakdownCard";
import SkillsCard from "./SkillsCard";
import RecommendationCard from "./RecommendationCard";
import RewriteCard from "./RewriteCard";

// ── Loading Skeleton ──────────────────────────────────────────────────────────
function AnalysisSkeleton() {
    return (
        <div className="mt-10 space-y-6">
            {[180, 140, 200, 160].map((h, i) => (
                <div
                    key={i}
                    className="skeleton-pulse rounded-2xl bg-white/5 border border-white/10"
                    style={{ height: h }}
                />
            ))}
        </div>
    );
}

// ── Tab Switcher ──────────────────────────────────────────────────────────────
const TABS = [
    { id: "breakdown",   label: "📊 Breakdown" },
    { id: "skills",      label: "🎯 Skills" },
    { id: "insights",    label: "💡 Insights" },
];

function ResultTabs({ analysis }) {
    const [activeTab, setActiveTab] = useState("breakdown");

    return (
        <div className="mt-10">
            {/* Tab bar */}
            <div className="flex gap-2 mb-6 p-1 bg-white/5 rounded-xl border border-white/10 w-fit">
                {TABS.map((tab) => (
                    <button
                        key={tab.id}
                        onClick={() => setActiveTab(tab.id)}
                        className={`px-5 py-2 rounded-lg text-sm font-semibold transition-all duration-200 ${
                            activeTab === tab.id
                                ? "bg-blue-600 text-white shadow-lg shadow-blue-500/25"
                                : "text-slate-400 hover:text-white hover:bg-white/5"
                        }`}
                    >
                        {tab.label}
                    </button>
                ))}
            </div>

            {/* Tab panels */}
            <AnimatePresence mode="wait">
                {activeTab === "breakdown" && (
                    <motion.div
                        key="breakdown"
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -10 }}
                        transition={{ duration: 0.2 }}
                    >
                        <BreakdownCard result={analysis} />
                    </motion.div>
                )}
                {activeTab === "skills" && (
                    <motion.div
                        key="skills"
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -10 }}
                        transition={{ duration: 0.2 }}
                    >
                        <SkillsCard result={analysis} />
                    </motion.div>
                )}
                {activeTab === "insights" && (
                    <motion.div
                        key="insights"
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0, y: -10 }}
                        transition={{ duration: 0.2 }}
                    >
                        <RecommendationCard result={analysis} />
                    </motion.div>
                )}
            </AnimatePresence>
        </div>
    );
}

// ── Main UploadCard ───────────────────────────────────────────────────────────
function UploadCard() {

    const [resume, setResume] = useState(null);
    const [jobDescription, setJobDescription] = useState("");
    const [analysis, setAnalysis] = useState(null);
    const [rewrite, setRewrite] = useState("");
    const [loading, setLoading] = useState(false);
    const [rewriteLoading, setRewriteLoading] = useState(false);

    // Drag-and-drop state
    const [dragging, setDragging] = useState(false);

    //----------------------------------

    const analyzeResume = async () => {

        if (!resume) {
            alert("Please upload a resume.");
            return;
        }

        if (!jobDescription.trim()) {
            alert("Please paste a Job Description.");
            return;
        }

        const formData = new FormData();
        formData.append("resume", resume);
        formData.append("job_description", jobDescription);

        try {
            setLoading(true);

            const response = await API.post(
                "/match",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );

            setAnalysis(response.data);

            // Auto-scroll to ATS results
            setTimeout(() => {
                document.getElementById("ats-section")?.scrollIntoView({ behavior: "smooth" });
            }, 100);
        }

        catch (err) {
            console.error(err);
            alert("Failed to analyze resume.");
        }

        finally {
            setLoading(false);
        }

    };

    //----------------------------------

    const rewriteResume = async () => {

        if (!resume) {
            alert("Please upload a resume.");
            return;
        }

        if (!jobDescription.trim()) {
            alert("Paste Job Description.");
            return;
        }

        const formData = new FormData();
        formData.append("resume", resume);
        formData.append("job_description", jobDescription);
        formData.append("ats_json", JSON.stringify(analysis));

        try {
            setRewriteLoading(true);

            const response = await API.post(
                "/rewrite",
                formData,
                {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
            );

            setRewrite(response.data.rewritten_resume);

            // Auto-scroll to the rewrite section
            setTimeout(() => {
                document.getElementById("rewrite-section")?.scrollIntoView({ behavior: "smooth" });
            }, 100);
        }

        catch (err) {
            console.error(err);
            const errorMsg = err.response?.data?.error || err.message;
            alert("Rewrite failed: " + errorMsg);
        }

        finally {
            setRewriteLoading(false);
        }

    };

    //----------------------------------
    // Dropzone handlers

    const handleDragOver = (e) => {
        e.preventDefault();
        setDragging(true);
    };

    const handleDragLeave = (e) => {
        e.preventDefault();
        setDragging(false);
    };

    const handleDrop = (e) => {
        e.preventDefault();
        setDragging(false);
        const file = e.dataTransfer.files[0];
        if (file && file.type === "application/pdf") setResume(file);
    };

    //----------------------------------
    // Score bar helpers

    const score = analysis?.total_score ?? 0;

    let scoreColor = "text-red-400";
    let status = "Needs Improvement";

    if (score >= 80) {
        scoreColor = "text-green-400";
        status = "Excellent Match";
    } else if (score >= 60) {
        scoreColor = "text-yellow-400";
        status = "Good Match";
    }

    const formatBytes = (bytes) => {
        if (bytes < 1024) return `${bytes} B`;
        if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
        return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
    };

    //----------------------------------

    return (

        <div className="max-w-7xl mx-auto px-8 py-12 pb-24">

            {/* ── Upload Card ── */}
            <div className="bg-white/5 backdrop-blur-xl rounded-2xl shadow-2xl border border-white/10 hover:border-white/20 transition-all p-8">

                <h2 className="text-3xl font-bold mb-6 flex items-center gap-3">
                    <Upload className="text-blue-400" />
                    Upload Resume
                </h2>

                {/* Drag-and-drop zone */}
                <div
                    onDragOver={handleDragOver}
                    onDragLeave={handleDragLeave}
                    onDrop={handleDrop}
                    className={`mb-6 min-h-[200px] flex flex-col items-center justify-center rounded-xl border-2 border-dashed transition-all duration-200 cursor-pointer select-none ${
                        dragging
                            ? "border-blue-400 bg-blue-500/10 shadow-[0_0_20px_rgba(59,130,246,0.3)]"
                            : resume
                            ? "border-green-500/60 bg-green-500/5"
                            : "border-white/20 bg-white/3 hover:border-blue-500/60 hover:bg-blue-500/5"
                    }`}
                    onClick={() => document.getElementById("resume-upload").click()}
                >
                    {resume ? (
                        /* File selected state */
                        <div className="flex flex-col items-center gap-3 p-6 text-center">
                            <CheckCircle2 size={40} className="text-green-400" />
                            <p className="text-green-300 font-semibold text-lg">{resume.name}</p>
                            <p className="text-slate-400 text-sm">{formatBytes(resume.size)}</p>
                            <p className="text-slate-500 text-xs mt-1">Click to replace</p>
                        </div>
                    ) : (
                        /* Empty / dragging state */
                        <div className="flex flex-col items-center gap-3 p-6 text-center">
                            <CloudUpload
                                size={48}
                                className={`transition-colors ${dragging ? "text-blue-400" : "text-slate-500"}`}
                            />
                            <p className="text-slate-300 font-medium">
                                {dragging ? "Drop your PDF here!" : "Drag & drop your PDF resume here"}
                            </p>
                            <p className="text-slate-500 text-sm">or</p>
                            <span className="text-blue-400 underline underline-offset-2 text-sm font-medium hover:text-blue-300">
                                Browse files
                            </span>
                            <p className="text-slate-600 text-xs mt-1">PDF files only</p>
                        </div>
                    )}
                </div>

                {/* Hidden file input */}
                <input
                    id="resume-upload"
                    type="file"
                    accept=".pdf"
                    className="hidden"
                    onChange={(e) => setResume(e.target.files[0])}
                />

                {/* Job Description */}
                <label className="text-lg font-semibold">Job Description</label>

                <textarea
                    rows={12}
                    value={jobDescription}
                    onChange={(e) => setJobDescription(e.target.value)}
                    className="mt-3 w-full rounded-xl bg-slate-950/80 border border-white/10 p-4 text-white outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                    placeholder="Paste Job Description here..."
                />

                <div className="flex gap-5 mt-8">

                    <button
                        onClick={analyzeResume}
                        disabled={loading}
                        className="bg-blue-600 hover:bg-blue-700 disabled:opacity-60 px-6 py-3 rounded-xl font-semibold flex items-center gap-2 transition-all"
                    >
                        <Search size={18} />
                        {loading ? "Analyzing..." : "Analyze Resume"}
                    </button>

                    <button
                        onClick={rewriteResume}
                        disabled={rewriteLoading}
                        className="bg-green-600 hover:bg-green-700 disabled:opacity-60 px-6 py-3 rounded-xl font-semibold flex items-center gap-2 transition-all"
                    >
                        <Sparkles size={18} />
                        {rewriteLoading ? "Rewriting..." : "Improve Resume"}
                    </button>

                </div>

            </div>

            {/* ── Results ── */}
            {loading && <AnalysisSkeleton />}

            {!loading && analysis && (
                <div id="ats-section">
                    <ATSCard result={analysis} />
                    <ResultTabs analysis={analysis} />
                </div>
            )}

            {rewrite && (
                <div id="rewrite-section">
                    <RewriteCard rewrite={rewrite} />
                </div>
            )}

            {/* ── Fixed bottom score bar ── */}
            <AnimatePresence>
                {analysis && (
                    <motion.div
                        initial={{ y: 100 }}
                        animate={{ y: 0 }}
                        exit={{ y: 100 }}
                        transition={{ type: "spring", damping: 20, stiffness: 200 }}
                        className="fixed bottom-0 left-0 right-0 z-50 bg-slate-950/90 backdrop-blur-xl border-t border-white/10 px-8 py-3 flex items-center justify-between"
                    >
                        <span className="text-slate-400 text-sm font-medium">ATS Score</span>
                        <span className={`text-2xl font-bold ${scoreColor}`}>
                            {analysis.total_score.toFixed(1)} / 100
                        </span>
                        <span className={`text-sm font-semibold ${scoreColor}`}>{status}</span>
                    </motion.div>
                )}
            </AnimatePresence>

        </div>

    );

}

export default UploadCard;
