import { BarChart3 } from "lucide-react";

import { motion } from "framer-motion";

import ProgressBar from "./ProgressBar";

function BreakdownCard({ result }) {

    const b = result.breakdown;

    return (

        <motion.div

            initial={{
                opacity: 0,
                y: 30
            }}

            animate={{
                opacity: 1,
                y: 0
            }}

            transition={{
                duration: 0.5
            }}

            className="
            bg-slate-900
            border
            border-slate-800
            rounded-2xl
            shadow-lg
            mt-8
            p-8"

        >

            <div className="flex items-center gap-3 mb-8">

                <BarChart3
                    className="text-blue-400"
                    size={32}
                />

                <h2 className="text-3xl font-bold">

                    ATS Breakdown

                </h2>

            </div>

            <ProgressBar
                title="Semantic Match"
                value={b.semantic}
                color="bg-blue-500"
                max={20}
            />

            <ProgressBar
                title="Skills"
                value={b.skills}
                color="bg-green-500"
                max={25}
            />

            <ProgressBar
                title="Experience"
                value={b.experience}
                color="bg-yellow-500"
                max={15}
            />

            <ProgressBar
                title="Projects"
                value={b.projects}
                color="bg-pink-500"
                max={10}
            />

            <ProgressBar
                title="Keywords"
                value={b.keywords}
                color="bg-purple-500"
                max={10}
            />

            <ProgressBar
                title="Resume Sections"
                value={b.sections}
                color="bg-cyan-500"
                max={10}
            />

            <ProgressBar
                title="Resume Quality"
                value={b.quality}
                color="bg-orange-500"
                max={10}
            />

        </motion.div>

    );

}

export default BreakdownCard;