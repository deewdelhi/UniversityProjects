import { Person } from './person';
export interface Channel {
    id: number;
    ownerId: number;
    name: string;
    description: string;
    subscribers: Person[];
}