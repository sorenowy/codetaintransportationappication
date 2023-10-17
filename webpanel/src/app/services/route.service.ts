import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Route } from '../models/route';
import { environment } from 'src/environments/environment';
import { RouteResponse } from '../models/route.response';

@Injectable({
  providedIn: 'root'
})
export class RouteService {
    private apiUrl = environment.baseUrl

  constructor(private http: HttpClient) {}

  getRoutes(): Observable<RouteResponse> {
    return this.http.get<RouteResponse>(`${this.apiUrl}/routes`);
  }

  addRoute(route: Route): Observable<any> {
    return this.http.post<Route>(`${this.apiUrl}/routes`, {
      "start_location": route.start_location,
      "end_location": route.end_location,
      "price_per_km": route.price_per_km,
      "distance": route.distance,
      "date_of_execution": route.date_of_execution
    })
  }

  selectRoute(id: number): Observable<any> {
    return this.http.post(`${this.apiUrl}/routes/${id}/select`,{});
  }

  deleteRoute(id: number): Observable<any> {
    // Implement the logic to delete a route
    return this.http.delete(`${this.apiUrl}/routes/${id}`);
  }
}