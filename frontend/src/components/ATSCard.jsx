import { Trophy } from "lucide-react";
import { motion } from "framer-motion";

function ATSCard({ result }) {

    const score = result.total_score;

    let color = "text-red-400";
    let ring = "stroke-red-500";
    let status = "Needs Improvement";

    if (score >= 80) {
        color = "text-green-400";
        ring = "stroke-green-500";
        status = "Excellent Match";
    }
    else if (score >= 60) {
        color = "text-yellow-400";
        ring = "stroke-yellow-500";
        status = "Good Match";
    }

    const radius = 85;
    const circumference = 2 * Math.PI * radius;

    const progress =
        circumference -
        (score / 100) * circumference;

    return (

        <motion.div

            initial={{ opacity: 0, y: 30 }}

            animate={{ opacity: 1, y: 0 }}

            transition={{ duration: 0.4 }}

            className="bg-slate-900
            border border-slate-800
            rounded-2xl
            shadow-lg
            mt-10
            p-8"

        >

            <div className="flex items-center gap-3 mb-8">

                <Trophy
                    className="text-yellow-400"
                    size={34}
                />

                <h2 className="text-3xl font-bold">

                    ATS Score

                </h2>

            </div>

            <div className="flex flex-col items-center">

                <svg
                    width="220"
                    height="220"
                >

                    <circle

                        cx="110"

                        cy="110"

                        r={radius}

                        fill="none"

                        stroke="#334155"

                        strokeWidth="15"

                    />

                    <motion.circle

                        cx="110"

                        cy="110"

                        r={radius}

                        fill="none"

                        className={ring}

                        strokeWidth="15"

                        strokeLinecap="round"

                        strokeDasharray={circumference}

                        initial={{
                            strokeDashoffset:
                                circumference
                        }}

                        animate={{
                            strokeDashoffset:
                                progress
                        }}

                        transition={{
                            duration: 1.2
                        }}

                        transform="rotate(-90 110 110)"

                    />

                    <text

                        x="50%"

                        y="48%"

                        textAnchor="middle"

                        className="fill-white
                        text-4xl
                        font-bold"

                    >

                        {score.toFixed(1)}

                    </text>

                    <text

                        x="50%"

                        y="62%"

                        textAnchor="middle"

                        className="fill-slate-400
                        text-lg"

                    >

                        /100

                    </text>

                </svg>

                <h3
                    className={`text-2xl font-semibold mt-4 ${color}`}
                >

                    {status}

                </h3>

            </div>

        </motion.div>

    );

}

export default ATSCard;