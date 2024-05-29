export interface DataType {
    length: number;
    words: string[];
    coords: number[][];
    scores: number[];
}

export interface ResultType {
    key: string;
    value: ValueObject;
}

interface ValueObject {
    coords: number[];
    score: number;
}