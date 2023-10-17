import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { RoutesComponent } from './components/routes/routes.component';
import { AdminComponent } from './components/admin/admin.component';
import { AddRouteComponent } from './components/routes/add-route/add-route.component';

const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'routes', component: RoutesComponent },
  { path: 'admin', component: AdminComponent },
  { path: 'routes/add', component: AddRouteComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
