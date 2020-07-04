import { Injectable,Injector } from '@angular/core';
import { HttpInterceptor, HttpRequest, HttpHandler, HttpEvent, HttpErrorResponse, HttpResponse } from '@angular/common/http';
import { AuthGuardService } from './auth-guard.service';
import { Observable } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { Router } from '@angular/router';
@Injectable({
  providedIn: 'root'
})
export class TokenInterceptorService implements HttpInterceptor {

  constructor(private injector:Injector,private router:Router) { }
  intercept(req:HttpRequest<any>,next:HttpHandler):Observable<HttpEvent<any>>{
    let authService =this.injector.get(AuthGuardService);
   
    if (authService.getToken()!=null){
      let tokenizedReq = req.clone({
        setHeaders:{
          Authorization:`Bearer ${authService.getToken()}`
        }
      })
     
      return next.handle(tokenizedReq).pipe(
        catchError(err => {
            let errMsg = "";
            if(err.status == 401){
              this.router.navigate(['account/logout']);
            }
            else if(err.status == 404){
              this.router.navigate(['404']);
            }
            // if (err.error instanceof ErrorEvent) {
            //   console.log("++++")
            //  console.log(err)
            //  if
            // }
               
            // } else {
            //     // The backend returned an unsuccessful response code.
            //     // The response body may contain clues as to what went wrong,
            //     console.log("----")
            //     console.log(err)
            // }

            return throwError(
                'Something bad happened; please try again later.');
        })
    );
    
    }
    
      return next.handle(req)
    
  
  }
}
