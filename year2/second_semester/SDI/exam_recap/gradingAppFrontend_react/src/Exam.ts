import {Examiner} from "./Examiner"
export interface Exam {
    id?: number;
    title: string;
    guid: string;
    examiners: Examiner[];
}
