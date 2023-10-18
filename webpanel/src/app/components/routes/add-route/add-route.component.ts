import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RouteService } from 'src/app/services/route.service';
import { Route } from 'src/app/models/route';

@Component({
  selector: 'app-add-route',
  templateUrl: './add-route.component.html',
  styleUrls: ['./add-route.component.css']
})
export class AddRouteComponent {
  start_destination: string = '';
  end_destination: string = '';
  price_per_km: number = 0;
  distance: number = 0;
  date_of_execution!: Date;

  constructor(private routeService: RouteService, private router: Router) {}

  onSubmit() {
    const route: Route = {
      start_location: this.start_destination,
      end_location: this.end_destination,
      price_per_km: this.price_per_km,
      distance: this.distance,
      date_of_execution: this.date_of_execution
    };

    this.routeService.addRoute(route).subscribe((response: any) => {
        this.router.navigate(['/routes'])
    }, (error) => { alert(error.error.detail) }
    )
  }
}
