import { motion } from "framer-motion";

function ProgressBar({
    title,
    value,
    color = "bg-blue-500",
    max = 20
}) {
    const percentage = Math.min(
        (value / max) * 100,
        100
    );

    return (
        <div className="mb-6">
            <div className="flex justify-between mb-2">
                <span className="font-medium">
                    {title}
                </span>
                <span className="text-slate-300">
                    {value.toFixed(2)} / {max}
                </span>

            </div>

            <div
                className="
                w-full
                h-3
                bg-slate-800
                rounded-full
                overflow-hidden"
            >

                <motion.div

                    initial={{ width: 0 }}

                    animate={{
                        width: `${percentage}%`
                    }}

                    transition={{
                        duration: 1
                    }}

                    className={`h-full rounded-full ${color}`}

                />

            </div>

        </div>

    );

}

export default ProgressBar;