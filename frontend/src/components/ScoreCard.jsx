function ScoreCard({ result }) {

    return (

        <div
            style={{
                border: "1px solid gray",
                padding: "20px",
                marginTop: "30px",
                borderRadius: "10px"
            }}
        >

            <h2>ATS Score</h2>

            <h1>{result.total_score.toFixed(2)}/100</h1>

            <hr />

            <p>
                Semantic Score:
                {" "}
                {result.breakdown.semantic}
            </p>

            <p>
                Skills:
                {" "}
                {result.breakdown.skills}
            </p>

            <p>
                Experience:
                {" "}
                {result.breakdown.experience}
            </p>

            <p>
                Projects:
                {" "}
                {result.breakdown.projects}
            </p>

            <p>
                Keywords:
                {" "}
                {result.breakdown.keywords}
            </p>

            <p>
                Resume Sections:
                {" "}
                {result.breakdown.sections}
            </p>

            <p>
                Resume Quality:
                {" "}
                {result.breakdown.quality}
            </p>

        </div>

    );

}

export default ScoreCard;