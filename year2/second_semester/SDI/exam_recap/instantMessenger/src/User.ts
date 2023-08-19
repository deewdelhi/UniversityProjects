import {Message} from "./Message"

export interface User {
    id? : number;
    nickname: string;
    messages: Message[];
}