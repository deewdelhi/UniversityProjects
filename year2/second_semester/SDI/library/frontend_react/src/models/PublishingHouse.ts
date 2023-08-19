import { Book } from "./Book";

export interface PublishingHouse {
    id?: number;
    name: string;
    headquarters: string;
    founding_year: number;
    books?: Book[];
}


