import { Component } from '@angular/core';
import { Route } from 'src/app/models/route';
import { Router } from '@angular/router';
import { RouteService } from 'src/app/services/route.service';

@Component({
  selector: 'app-routes',
  templateUrl: './routes.component.html',
  styleUrls: ['./routes.component.css']
})
export class RoutesComponent {
    routes: Route[] = [];
    displayedColumns: string[] = ['id', 'start_location', 'end_location', 'price_per_km', 'distance', 'date_of_execution', 'actions'];
    isAdmin: boolean = JSON.parse(localStorage.getItem('is_admin')!) === true; // Set this value based on your application logic

    constructor(private routeService: RouteService, private route: Router) {}

    ngOnInit(): void {
      this.routeService.getRoutes().subscribe((routes) => {
        this.routes = routes.result;
      }, (error) => { alert(error.error.detail) }
      );
    }

    deleteRoute(id: number) {
      this.routeService.deleteRoute(id).subscribe(() => {
        // Implement the logic to remove the route from the UI
          this.routes = this.routes.filter((route) => route.id !== id);
      }, (error) => { alert(error.error.detail) }
      );
    }

    selectRoute(id: number) { 
      this.routeService.selectRoute(id).subscribe(() => { }, (error) => { alert(error.error.detail) });
    }

    logout() {
      localStorage.removeItem("access-token");
      localStorage.removeItem("is_admin");
      this.route.navigate(['']);
    }
}
