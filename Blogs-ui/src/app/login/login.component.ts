import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AuthenticationService } from '../services/auth-service';
import { Login } from '../models/login.model';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  isLoader: Boolean = false;
  submitted = false;
  error: string;
  returnUrl: string
  login: Login = new Login();
  isLoginError: Boolean = false;
  isSubmitted = false;
  

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authenticationService: AuthenticationService
    ) { }

  ngOnInit()  {
    this.loginForm = this.formBuilder.group({
        email: ['', Validators.required],
        password: ['', Validators.required]
    });


}

get f() { return this.loginForm.controls; }
errorMessage=""
onSubmit() {
  this.submitted = true;

  // stop here if form is invalid
  if (this.loginForm.invalid) {
      return;
  }

 
  this.authenticationService.login(this.login)
      .subscribe((user: any) => {
        this.isLoader = false;
        window.localStorage.setItem("accessToken", user.token.access_token);
        window.localStorage.setItem("refreshToken", user.token.refresh_token);
  
      },
      (err: HttpErrorResponse) => {
   
        this.isLoginError = true;
        this.errorMessage = err.error.error;
        // this.toastr.error('UserName or Password is Invalid!');
        this.isLoader = false;
      });
}
}
