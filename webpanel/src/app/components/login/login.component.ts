import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';
import { UserLogin } from 'src/app/models/user.login';
import { JwtHelperService } from '@auth0/angular-jwt';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  password: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    const helper = new JwtHelperService()

    const credentials: UserLogin = {
      email: this.email,
      password: this.password
    };

    this.authService.login(credentials).subscribe((response: any) => {
      const token = response.result.token;
      const decoded_token = helper.decodeToken(token);
      for (var key in decoded_token) {
        if (key == 'is_admin') {
          var value = decoded_token[key]
          localStorage.setItem('is_admin', value);
        }
      }
      localStorage.setItem('access-token', token);
      this.router.navigate(['routes']); // Navigate to your dashboard or desired route
    }, (error) => { alert(error.error.detail) }
    );
  }
}