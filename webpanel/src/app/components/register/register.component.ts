import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms'
import { UserRegister } from 'src/app/models/user.register';
import { AuthService } from 'src/app/services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  email: string = '';
  password: string = '';
  name: string = '';
  surname: string = '';
  address: string = '';
  is_admin: boolean = JSON.parse(localStorage.getItem('is_admin')!) === true;

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit() {
    const credentials: UserRegister = {
      email: this.email,
      password: this.password,
      name: this.name,
      surname: this.surname,
      address: this.address,
      is_admin: this.is_admin
    };

    this.authService.register(credentials).subscribe((response: any) => {
      console.log(response)
      const token = response.result.token;
      console.log(token) // Adjust this based on your API response
      localStorage.setItem('access-token', token);
      this.router.navigate(['']); // Navigate to your dashboard or desired route
    });
  }
}
