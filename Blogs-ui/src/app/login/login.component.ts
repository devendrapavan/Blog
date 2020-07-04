import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators, NgForm } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AuthenticationService } from '../services/auth-service';
import { Login } from '../models/login.model';
import { HttpErrorResponse } from '@angular/common/http';
import { stringify } from '@angular/core/src/util';

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

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      email: ['', Validators.required],
      password: ['', Validators.required]
    });


  }

  get f() { return this.loginForm.controls; }
  errorMessage = ""



  userlogin(form: NgForm) {

    this.authenticationService.login(this.login)
      .subscribe((user: any) => {
        this.isLoader = false;
        window.localStorage.setItem("accessToken", user.access);
        window.localStorage.setItem("refreshToken", user.refresh);
        this.router.navigate(['/dashboard'])

      },
        (err: HttpErrorResponse) => {

          this.isLoginError = true;
          this.errorMessage = err.error.error;
          alert(this.errorMessage)
          this.isLoader = false;
        });
  }

}



