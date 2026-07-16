import API from "../services/api";
import { useState } from "react";
import axios from "axios";
import {
    Upload,
    Sparkles,
    Search,
    FileText
} from "lucide-react";

import ATSCard from "./ATSCard";
import BreakdownCard from "./BreakdownCard";
import SkillsCard from "./SkillsCard";
import RecommendationCard from "./RecommendationCard";
import RewriteCard from "./RewriteCard";


function UploadCard() {

    const [resume, setResume] = useState(null);

    const [jobDescription, setJobDescription] = useState("");

    const [analysis, setAnalysis] = useState(null);

    const [rewrite, setRewrite] = useState("");

    const [loading, setLoading] = useState(false);

    const [rewriteLoading, setRewriteLoading] = useState(false);

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

                        "Content-Type":
                            "multipart/form-data"

                    }

                }

            );

            setAnalysis(response.data);

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

        try {

            setRewriteLoading(true);

            const response = await API.post(

                "/rewrite",

                formData,

                {

                    headers: {

                        "Content-Type":
                            "multipart/form-data"

                    }

                }

            );

            setRewrite(

                response.data.rewritten_resume

            );

        }

        catch (err) {

            console.error(err);

            alert("Rewrite failed.");

        }

        finally {

            setRewriteLoading(false);

        }

    };

    //----------------------------------

    return (

        <div className="max-w-7xl mx-auto px-8 py-12">

            {/* Upload Card */}

            <div className="bg-slate-900 rounded-2xl shadow-xl border border-slate-800 p-8">

                <h2 className="text-3xl font-bold mb-6 flex items-center gap-3">

                    <Upload className="text-blue-400"/>

                    Upload Resume

                </h2>

                <div className="mb-6">

                    <label
                      htmlFor="resume-upload"
                      className="
                          inline-flex
                          items-center
                          gap-2
                          bg-blue-600
                          hover:bg-blue-700
                          text-white
                          font-semibold
                          px-5
                          py-3
                          rounded-lg
                          cursor-pointer
                          transition
                      "
                    >

                      <Upload size={20} />

                           Choose Resume

                    </label>

                    <input

                        id="resume-upload"

                        type="file"

                        accept=".pdf"

                        className="hidden"

                        onChange={(e) =>

                            setResume(e.target.files[0])

                        }

                    />

                    {

                        resume &&

                        <p className="text-green-400 mt-3">

                            📄 {resume.name}

                        </p>

                    }

                </div>

                <label className="text-lg font-semibold">

                    Job Description

                </label>

                <textarea

                    rows={12}

                    value={jobDescription}

                    onChange={(e)=>

                        setJobDescription(

                            e.target.value

                        )

                    }

                    className="mt-3 w-full rounded-xl
                    bg-slate-950 border border-slate-700
                    p-4 text-white outline-none
                    focus:ring-2 focus:ring-blue-500"

                    placeholder="Paste Job Description here..."

                />

                <div className="flex gap-5 mt-8">

                    <button

                        onClick={analyzeResume}

                        disabled={loading}

                        className="bg-blue-600 hover:bg-blue-700
                        px-6 py-3 rounded-xl font-semibold
                        flex items-center gap-2"

                    >

                        <Search size={18}/>

                        {

                            loading ?

                            "Analyzing..."

                            :

                            "Analyze Resume"

                        }

                    </button>

                    <button

                        onClick={rewriteResume}

                        disabled={rewriteLoading}

                        className="bg-green-600 hover:bg-green-700
                        px-6 py-3 rounded-xl font-semibold
                        flex items-center gap-2"

                    >

                        <Sparkles size={18}/>

                        {

                            rewriteLoading ?

                            "Rewriting..."

                            :

                            "Improve Resume"

                        }

                    </button>

                </div>

            </div>

            {/* Results */}

            {

                analysis &&

                <>

                    <ATSCard

                        result={analysis}

                    />

                    <BreakdownCard

                        result={analysis}

                    />

                    <SkillsCard

                        result={analysis}

                    />

                    <RecommendationCard

                        result={analysis}

                    />

                </>

            }

            {

                rewrite &&

                <RewriteCard

                    rewrite={rewrite}

                />

            }

        </div>

    );

}

export default UploadCard;