import { Sparkles } from "lucide-react";

function Header() {

    return (

        <header className="border-b border-slate-800">

            <div className="max-w-7xl mx-auto px-8 py-10">

                <div className="flex items-center gap-3">

                    <Sparkles
                        size={34}
                        className="text-blue-400"
                    />

                    <h1 className="text-5xl font-bold text-white">

                        AI Resume Intelligence Platform

                    </h1>

                </div>

                <p className="mt-4 text-slate-400 text-lg">

                    Analyze your resume, calculate ATS score,
                    identify missing skills and rewrite your resume
                    using AI.

                </p>

            </div>

        </header>

    );

}

export default Header;