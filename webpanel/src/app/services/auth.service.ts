import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/internal/Observable';
import { UserRegister } from '../models/user.register';
import { UserLogin } from '../models/user.login';
import { map } from 'rxjs/operators'
import { environment } from 'src/environments/environment';
import { LoginResponse } from '../models/login.response';

@Injectable({
  providedIn: 'root'
})

export class AuthService {
  private baseUrl = environment.baseUrl

  constructor(private httpClient: HttpClient) { }

  public register(user: UserRegister): Observable<any> {
    return this.httpClient.post<any>(this.baseUrl + '/register', {
      "email":user.email,
      "password":user.password,
      "name": user.name,
      "surname": user.surname,
      "address": user.address,
      "is_admin": user.is_admin
    });
  }

  public login(user: UserLogin): Observable<any> {
    return this.httpClient.post<LoginResponse>(this.baseUrl + '/login', {
      "email":user.email,
      "password":user.password
    });
  }
}
