import { Trophy } from "lucide-react";
import { motion } from "framer-motion";
import { useMotionValue, useSpring } from "framer-motion";
import { useEffect, useState } from "react";

function ATSCard({ result }) {

    const score = result.total_score;

    let color = "text-red-400";
    let ring = "stroke-red-500";
    let status = "Needs Improvement";

    if (score >= 80) {
        color = "text-green-400";
        ring = "stroke-green-500";
        status = "Excellent Match";
    } else if (score >= 60) {
        color = "text-yellow-400";
        ring = "stroke-yellow-500";
        status = "Good Match";
    }

    const radius = 85;
    const circumference = 2 * Math.PI * radius;
    const progress = circumference - (score / 100) * circumference;

    // Count-up animation
    const count = useMotionValue(0);
    const spring = useSpring(count, { duration: 1500 });
    const [display, setDisplay] = useState(0);

    useEffect(() => {
        const unsubscribe = spring.on("change", (v) => setDisplay(v));
        count.set(score);
        return () => unsubscribe();
    }, [score]);

    return (

        <motion.div

            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4 }}

            className="bg-white/5 backdrop-blur-xl border border-white/10 hover:border-white/20 transition-all rounded-2xl shadow-2xl mt-10 p-8"

        >

            <div className="flex items-center gap-3 mb-8">

                <Trophy className="text-yellow-400" size={34} />

                <h2 className="text-3xl font-bold">ATS Score</h2>

            </div>

            <div className="flex flex-col items-center">

                <svg width="220" height="220">

                    {/* Track */}
                    <circle
                        cx="110"
                        cy="110"
                        r={radius}
                        fill="none"
                        stroke="#1e293b"
                        strokeWidth="15"
                    />

                    {/* Animated progress ring */}
                    <motion.circle
                        cx="110"
                        cy="110"
                        r={radius}
                        fill="none"
                        className={ring}
                        strokeWidth="15"
                        strokeLinecap="round"
                        strokeDasharray={circumference}
                        initial={{ strokeDashoffset: circumference }}
                        animate={{ strokeDashoffset: progress }}
                        transition={{ duration: 1.4, ease: "easeOut" }}
                        transform="rotate(-90 110 110)"
                    />

                    {/* Count-up score text */}
                    <text
                        x="50%"
                        y="48%"
                        textAnchor="middle"
                        dominantBaseline="middle"
                        fill="white"
                        fontSize="32"
                        fontWeight="bold"
                    >
                        {display.toFixed(1)}
                    </text>

                    <text
                        x="50%"
                        y="64%"
                        textAnchor="middle"
                        dominantBaseline="middle"
                        fill="#94a3b8"
                        fontSize="16"
                    >
                        / 100
                    </text>

                </svg>

                <h3 className={`text-2xl font-semibold mt-4 ${color}`}>
                    {status}
                </h3>

            </div>

        </motion.div>

    );

}

export default ATSCard;
