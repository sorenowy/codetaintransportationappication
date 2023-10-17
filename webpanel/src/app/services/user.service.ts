import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Route } from '../models/route';
import { environment } from 'src/environments/environment';
import { RouteResponse } from '../models/route.response';
import { UserResponse } from '../models/user.response';
import { User } from '../models/user';
@Injectable({
  providedIn: 'root'
})
export class UserService {
    private apiUrl = environment.baseUrl

  constructor(private http: HttpClient) {}

  getUsers(): Observable<UserResponse> {
    return this.http.get<UserResponse>(`${this.apiUrl}/users`);
  }

  deleteUser(id: number): Observable<any> {
    // Implement the logic to delete a route
    return this.http.delete(`${this.apiUrl}/users/${id}`);
  }
}