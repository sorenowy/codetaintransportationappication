import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './components/login/login.component';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http'
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { RegisterComponent } from './components/register/register.component';
import { RoutesComponent } from './components/routes/routes.component';
import { AdminComponent } from './components/admin/admin.component';
import { MatTableModule } from '@angular/material/table';
import { TokenInterceptor } from './components/interceptor/TokenInterceptor';
import { AddRouteComponent } from './components/routes/add-route/add-route.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    RoutesComponent,
    AdminComponent,
    AddRouteComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatTableModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: TokenInterceptor,
    multi: true,
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
