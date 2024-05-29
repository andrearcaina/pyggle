import { DataType } from '@/types/types';

export default function Form({ setData }: Readonly<{ setData: (data: DataType) => void; }>) {
    const handleFormInput = async (formData: FormData) => {
        const board: string = formData.get("board") as string;
        const words: string = formData.get("words") as string;
        let official: string = formData.get("official") as string;

        if (!board) {
            alert("Please fill out the board");
            return;
        }

        await fetchData(board, words, official == "true")
    }

    const fetchData = async (board: string, words: string, official: boolean) => {
        const uri = `http://127.0.0.1:8000/api/data/${board}?words=${words}&official=${official}`;

        await fetch(uri)
            .then((response) => response.json())
            .then(data => setData(data))
            .catch(err => console.log(err));
    }

    return (
        <form action={handleFormInput} className={"flex flex-col items-center justify-center space-y-4"}>
            <label className={"text-white"} htmlFor={"board"}>Board</label>
            <input className={"px-4 py-2 border border-gray-300 rounded-md"} type={"text"} name={"board"}/>

            <label className={"text-white"} htmlFor={"dictionary"}>Dictionary</label>
            <select className={"px-4 py-2 border border-gray-300 rounded-md"} name={"words"}>
                <option value={"3000"}>3000 words</option>
                <option value={"scrabble"}>Scrabble dictionary</option>
                <option value={"479k"}>479k dictionary</option>
            </select>

            <label className={"text-white"} htmlFor={"official"}>Official Rules</label>
            <select className={"px-4 py-2 border border-gray-300 rounded-md"} name={"official"}>
                <option value={"true"}>True</option>
                <option value={"false"}>False</option>
            </select>
            <br/>

            <input
                className={"px-4 py-2 bg-blue-500 text-white rounded-md cursor-pointer hover:bg-blue-600"}
                type={"submit"}
                value={"Submit"}
            />
        </form>
    )
}