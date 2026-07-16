import {
    Star,
    AlertTriangle,
    Lightbulb,
} from "lucide-react";

import { motion } from "framer-motion";

function RecommendationCard({ result }) {

    return (

        <motion.div

            initial={{ opacity: 0, y: 30 }}

            animate={{ opacity: 1, y: 0 }}

            transition={{ duration: 0.5 }}

            className="
            bg-slate-900
            border
            border-slate-800
            rounded-2xl
            shadow-lg
            mt-8
            p-8
            "

        >

            <div className="grid lg:grid-cols-3 gap-8">

                {/* Strengths */}

                <div>

                    <div className="flex items-center gap-3 mb-5">

                        <Star
                            className="text-yellow-400"
                            size={28}
                        />

                        <h2 className="text-2xl font-bold">

                            Strengths

                        </h2>

                    </div>

                    <div className="space-y-3">

                        {

                            result.strengths.length ?

                            result.strengths.map(

                                (item,index)=>(

                                    <div

                                        key={index}

                                        className="
                                        bg-green-500/10
                                        border
                                        border-green-500/40
                                        rounded-xl
                                        p-4
                                        text-green-300"

                                    >

                                        {item}

                                    </div>

                                )

                            )

                            :

                            <p className="text-slate-400">

                                No strengths detected.

                            </p>

                        }

                    </div>

                </div>

                {/* Weaknesses */}

                <div>

                    <div className="flex items-center gap-3 mb-5">

                        <AlertTriangle

                            className="text-red-400"

                            size={28}

                        />

                        <h2 className="text-2xl font-bold">

                            Weaknesses

                        </h2>

                    </div>

                    <div className="space-y-3">

                        {

                            result.weaknesses.length ?

                            result.weaknesses.map(

                                (item,index)=>(

                                    <div

                                        key={index}

                                        className="
                                        bg-red-500/10
                                        border
                                        border-red-500/40
                                        rounded-xl
                                        p-4
                                        text-red-300"

                                    >

                                        {item}

                                    </div>

                                )

                            )

                            :

                            <p className="text-slate-400">

                                No weaknesses detected.

                            </p>

                        }

                    </div>

                </div>

                {/* Recommendations */}

                <div>

                    <div className="flex items-center gap-3 mb-5">

                        <Lightbulb

                            className="text-blue-400"

                            size={28}

                        />

                        <h2 className="text-2xl font-bold">

                            Recommendations

                        </h2>

                    </div>

                    <div className="space-y-3">

                        {

                            result.recommendations.length ?

                            result.recommendations.map(

                                (item,index)=>(

                                    <div

                                        key={index}

                                        className="
                                        bg-blue-500/10
                                        border
                                        border-blue-500/40
                                        rounded-xl
                                        p-4
                                        text-blue-300"

                                    >

                                        {item}

                                    </div>

                                )

                            )

                            :

                            <p className="text-slate-400">

                                No recommendations.

                            </p>

                        }

                    </div>

                </div>

            </div>

        </motion.div>

    );

}

export default RecommendationCard;