import { motion } from "framer-motion";

function ProgressBar({
    title,
    value,
    color = "bg-blue-500",
    max = 20,
}) {

    const percentage = Math.min((value / max) * 100, 100);

    // Derive a matching glow color from the Tailwind color class
    const glowMap = {
        "bg-blue-500":   "rgba(59,130,246,0.6)",
        "bg-green-500":  "rgba(34,197,94,0.6)",
        "bg-yellow-500": "rgba(234,179,8,0.6)",
        "bg-pink-500":   "rgba(236,72,153,0.6)",
        "bg-purple-500": "rgba(168,85,247,0.6)",
        "bg-cyan-500":   "rgba(6,182,212,0.6)",
        "bg-orange-500": "rgba(249,115,22,0.6)",
    };

    const glowColor = glowMap[color] ?? "rgba(255,255,255,0.3)";

    return (

        <div className="mb-6">

            <div className="flex justify-between mb-2">
                <span className="font-medium text-slate-200">{title}</span>
                <span className="text-slate-400">{value.toFixed(2)} / {max}</span>
            </div>

            <div className="w-full h-4 bg-slate-800/80 rounded-full overflow-hidden">

                <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${percentage}%` }}
                    transition={{ duration: 1, ease: "easeOut" }}
                    className={`h-full rounded-full ${color}`}
                    style={{ boxShadow: `0 0 10px ${glowColor}` }}
                />

            </div>

        </div>

    );

}

export default ProgressBar;
