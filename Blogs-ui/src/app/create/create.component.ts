import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, NgForm } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { CommonService } from '../services/all-services';
import { Article } from '../models/login.model';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {
  articlePost: FormGroup;
  article: Article = new Article();
  constructor(private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private commonService: CommonService,
    private router: Router,) { }

  ngOnInit() {

    this.articlePost = this.formBuilder.group({
      header: ['', Validators.required],
      body: ['', Validators.required]
    });
  }

  
  createArticle(form: NgForm) {
    console.log(this.article)

    this.commonService.postArticle(this.article)
      .subscribe((user: any) => {
        alert('success')
        this.router.navigate(['/dashboard'])

      },
        (err: HttpErrorResponse) => {
          console.log(err)
        
        });
  }

}
