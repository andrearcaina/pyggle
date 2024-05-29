import { DataType, ResultType } from '@/types/types';

export default function Result({ output }: Readonly<{ output: DataType | undefined }>) {
    if (!output) {
        return;
    }

    const words = output.words;
    const coords = output.coords;
    const scores = output.scores;

    let results: ResultType[] = [];

    for (let i = 0; i < words.length; i++) {
        let result: ResultType = {
            key: words[i],
            value: {
                coords: coords[i],
                score: scores[i]
            }
        };
        results.push(result);
    }

    return (
        <div className={"flex flex-col items-center justify-center mt-5 text-white"}>
            <table className={"table-auto text-white"}>
                <thead>
                <tr>
                    <th className={"px-4 py-2"}>Word</th>
                    <th className={"px-4 py-2"}>Coords on Board</th>
                    <th className={"px-4 py-2"}>Score</th>
                </tr>
                </thead>

                <tbody>
                {results.map((result: ResultType) => {
                    return (
                        <tr key={result.key}>
                            <td className={"border px-4 py-2"}>{result.key}</td>
                            <td className={"border px-4 py-2"}>{JSON.stringify(result.value.coords)}</td>
                            <td className={"border px-4 py-2"}>{result.value.score}</td>
                        </tr>
                    );
                })}
                </tbody>
            </table>
        </div>
    );
}