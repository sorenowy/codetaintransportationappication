import { Injectable } from '@angular/core';
import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler,
  HttpEvent,
} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class TokenInterceptor implements HttpInterceptor {
  intercept(
    request: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    // Get the token from local storage
    const token = localStorage.getItem('access-token');
    if (token) {
      // Clone the request and add an Authorization header with the token
      request = request.clone({
        setHeaders: {
          Authorization: `${token}`,
        },
      });
    }

    // Pass the request on to the next handler
    return next.handle(request);
  }
}