import { PublishingHouse } from "./PublishingHouse";
import { Author } from "./Author";

export interface Book {
    id?: number;
    title: string;
    publishing_house: PublishingHouse;
    description:string;
    releasing_year: number;
    authors: Author[]
}




