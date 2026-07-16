function Footer() {

    const year = new Date().getFullYear();

    return (

        <footer className="mt-16 border-t border-slate-800">

            <div className="max-w-7xl mx-auto px-8 py-8 text-center">

                <h3 className="text-xl font-bold text-white">

                    AI Resume Intelligence Platform

                </h3>

                <p className="text-slate-400 mt-2">

                    Analyze • Optimize • Rewrite your Resume using AI

                </p>

                <p className="text-slate-500 mt-6">

                    © {year} AI Resume Intelligence Platform by Rawnak Yadav

                </p>

            </div>

        </footer>

    );

}

export default Footer;