import {User} from "./User"
export interface Channel {
    id? : number;
    guid: string;
    name:string;
    users: User[];
}