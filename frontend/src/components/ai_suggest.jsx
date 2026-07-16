import ReactMarkdown from "react-markdown";

function AISuggestions({ suggestions }) {
    return (
        <div className="bg-gray-800 rounded-xl p-6 mt-8 shadow-lg">

            <h2 className="text-3xl font-bold mb-6 text-yellow-400">
                🤖 AI Resume Suggestions
            </h2>

            <div className="prose prose-invert max-w-none">
                <ReactMarkdown>
                    {suggestions}
                </ReactMarkdown>
            </div>

        </div>
    );
}

export default AISuggestions;