import { useState } from "react";
import ReactMarkdown from "react-markdown";
import { Sparkles, Copy, Check } from "lucide-react";
import { motion } from "framer-motion";

function RewriteCard({ rewrite }) {

    const [copied, setCopied] = useState(false);

    const handleCopy = async () => {
        await navigator.clipboard.writeText(rewrite);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (

        <motion.div

            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}

            className="bg-white/5 backdrop-blur-xl border border-white/10 hover:border-white/20 transition-all rounded-2xl shadow-2xl mt-8 p-8"

        >

            <div className="flex justify-between items-center mb-8">

                <div className="flex items-center gap-3">
                    <Sparkles className="text-yellow-400" size={30} />
                    <h2 className="text-3xl font-bold">AI Resume Rewrite</h2>
                </div>

                <button
                    onClick={handleCopy}
                    className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-lg transition-all font-medium"
                >
                    {copied ? <Check size={18} /> : <Copy size={18} />}
                    {copied ? "Copied" : "Copy"}
                </button>

            </div>

            <div
                className="prose prose-invert prose-headings:text-blue-300 prose-strong:text-white prose-li:text-slate-300 prose-p:text-slate-300 max-w-none"
            >
                <ReactMarkdown>{rewrite}</ReactMarkdown>
            </div>

        </motion.div>

    );

}

export default RewriteCard;
