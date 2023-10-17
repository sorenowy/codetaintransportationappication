import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { User } from 'src/app/models/user';
import { UserService } from 'src/app/services/user.service';
@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css']
})
export class AdminComponent {
  users: User[] = []
  displayedColumns: string[] = ['id', 'email', 'name', 'surname', 'address', 'is_admin', 'is_verified', 'actions'];
  isAdmin: boolean = JSON.parse(localStorage.getItem('is_admin')!) === true;

  constructor(private userService: UserService, private router: Router) {}

  ngOnInit(): void {
    this.userService.getUsers().subscribe((users) => {
      this.users = users.result;
      console.log(users)
    });
  }

  deleteUser(id: number) {
    this.userService.deleteUser(id).subscribe(() => {
      // Implement the logic to remove the route from the UI
        this.users = this.users.filter((user) => user.id !== id);
    })
  }

  logout() {
    localStorage.removeItem("access-token");
    localStorage.removeItem("is_admin");
    this.router.navigate(['']);
  }
}
