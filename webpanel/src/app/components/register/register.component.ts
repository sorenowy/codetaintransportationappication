import { Component } from '@angular/core';
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
  is_admin: boolean = false;

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
      const token = response.result.token;
      localStorage.setItem('access-token', token);
    }, (error) => { alert(error.error.detail) }
    );
    this.router.navigate(['']); 
  }
}
