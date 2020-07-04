import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { DahsboardComponent } from './dahsboard/dahsboard.component';
import { AuthGuardService } from './services/auth-guard.service';
import { CreateComponent } from './create/create.component';
import { UpdateComponent } from './update/update.component';

const routes: Routes = [
  {
    path: 'login', component: LoginComponent
  },
  {
    path: 'dashboard', component: DahsboardComponent, canActivate: [AuthGuardService],

  },
  {
    path: 'create', component: CreateComponent, canActivate: [AuthGuardService]
  },
  {
    path: 'update', component: UpdateComponent, canActivate: [AuthGuardService]
  }
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
