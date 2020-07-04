import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { HttpErrorResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate {
  constructor(private router: Router) {}
  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot):  boolean {
    
        if (this.getToken() != null) {
          console.log("normal");
          return true;
        }
  
    
      this.router.navigate(['/login']);
    return false;
  }

  getToken(){
    return localStorage.getItem("accessToken");
  }
}
