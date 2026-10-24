function Footer() {

    const year = new Date().getFullYear();

    return (

        <footer className="mt-16 border-t border-white/5 bg-slate-950/50 backdrop-blur-xl">

            <div className="max-w-7xl mx-auto px-8 py-8 text-center">

                <h3 className="text-xl font-bold bg-gradient-to-r from-blue-400 via-violet-400 to-cyan-400 bg-clip-text text-transparent">
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
