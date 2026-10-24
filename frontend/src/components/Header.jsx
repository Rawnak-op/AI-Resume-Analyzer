import { Sparkles, Upload, Search, TrendingUp } from "lucide-react";

function Header() {

    return (

        <header className="relative overflow-hidden border-b border-white/5 bg-slate-950/80 backdrop-blur-xl sticky top-0 z-40">

            {/* Animated background orbs */}
            <div className="pointer-events-none absolute inset-0 overflow-hidden">

                <div
                    className="orb-1 absolute -top-20 -left-20 w-80 h-80 rounded-full opacity-20 blur-3xl"
                    style={{ background: "radial-gradient(circle, #3b82f6, transparent)" }}
                />

                <div
                    className="orb-2 absolute -top-10 right-10 w-64 h-64 rounded-full opacity-15 blur-3xl"
                    style={{ background: "radial-gradient(circle, #8b5cf6, transparent)" }}
                />

                <div
                    className="orb-3 absolute top-5 left-1/2 w-56 h-56 rounded-full opacity-10 blur-3xl"
                    style={{ background: "radial-gradient(circle, #06b6d4, transparent)" }}
                />

            </div>

            <div className="relative max-w-7xl mx-auto px-8 py-8">

                {/* Title row */}
                <div className="flex items-center gap-4 mb-3">

                    <Sparkles size={36} className="text-blue-400 shrink-0" />

                    <h1
                        className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-400 via-violet-400 to-cyan-400 bg-clip-text text-transparent leading-tight"
                    >
                        AI Resume Intelligence Platform
                    </h1>

                </div>

                {/* Subtitle */}
                <p className="text-slate-400 text-lg ml-14 mb-6">
                    Analyze your resume, calculate ATS score, identify missing skills and rewrite using AI.
                </p>

                {/* How it works — 3-step row */}
                <div className="ml-14 flex flex-wrap gap-6">

                    <div className="flex items-center gap-2 text-sm text-slate-400">
                        <span className="flex items-center justify-center w-7 h-7 rounded-full bg-blue-500/20 border border-blue-500/40 text-blue-400 font-bold text-xs">
                            1
                        </span>
                        <Upload size={14} className="text-blue-400" />
                        <span>Upload Resume</span>
                    </div>

                    <div className="flex items-center gap-1 text-slate-600 text-sm">→</div>

                    <div className="flex items-center gap-2 text-sm text-slate-400">
                        <span className="flex items-center justify-center w-7 h-7 rounded-full bg-violet-500/20 border border-violet-500/40 text-violet-400 font-bold text-xs">
                            2
                        </span>
                        <Search size={14} className="text-violet-400" />
                        <span>Analyze with AI</span>
                    </div>

                    <div className="flex items-center gap-1 text-slate-600 text-sm">→</div>

                    <div className="flex items-center gap-2 text-sm text-slate-400">
                        <span className="flex items-center justify-center w-7 h-7 rounded-full bg-cyan-500/20 border border-cyan-500/40 text-cyan-400 font-bold text-xs">
                            3
                        </span>
                        <TrendingUp size={14} className="text-cyan-400" />
                        <span>Improve &amp; Rewrite</span>
                    </div>

                </div>

            </div>

        </header>

    );

}

export default Header;
