import { CheckCircle2, XCircle } from "lucide-react";
import { motion } from "framer-motion";

function SkillBadge({ text, type }) {

    const styles = {

        success:
            "bg-green-500/20 text-green-300 border-green-500",

        danger:
            "bg-red-500/20 text-red-300 border-red-500"

    };

    return (

        <span

            className={`
            px-4
            py-2
            rounded-full
            border
            text-sm
            font-medium
            ${styles[type]}
            `}

        >

            {text}

        </span>

    );

}

function SkillsCard({ result }) {

    return (

        <motion.div

            initial={{
                opacity:0,
                y:30
            }}

            animate={{
                opacity:1,
                y:0
            }}

            transition={{
                duration:0.5
            }}

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

            <div className="grid md:grid-cols-2 gap-10">

                {/* Matched */}

                <div>

                    <div className="flex items-center gap-3 mb-5">

                        <CheckCircle2

                            className="text-green-400"

                            size={30}

                        />

                        <h2 className="text-2xl font-bold">

                            Matched Skills

                        </h2>

                    </div>

                    <div className="flex flex-wrap gap-3">

                        {

                            result.matched_required.length ?

                            result.matched_required.map(

                                (skill)=>(

                                    <SkillBadge

                                        key={skill}

                                        text={skill}

                                        type="success"

                                    />

                                )

                            )

                            :

                            <p className="text-slate-400">

                                No matched skills

                            </p>

                        }

                    </div>

                </div>

                {/* Missing */}

                <div>

                    <div className="flex items-center gap-3 mb-5">

                        <XCircle

                            className="text-red-400"

                            size={30}

                        />

                        <h2 className="text-2xl font-bold">

                            Missing Skills

                        </h2>

                    </div>

                    <div className="flex flex-wrap gap-3">

                        {

                            result.missing_required.length ?

                            result.missing_required.map(

                                (skill)=>(

                                    <SkillBadge

                                        key={skill}

                                        text={skill}

                                        type="danger"

                                    />

                                )

                            )

                            :

                            <p className="text-slate-400">

                                No missing skills 🎉

                            </p>

                        }

                    </div>

                </div>

            </div>

        </motion.div>

    );

}

export default SkillsCard;