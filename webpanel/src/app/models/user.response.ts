import { User } from "./user";

export interface UserResponse {
    detail: string,
    result: User[]
}