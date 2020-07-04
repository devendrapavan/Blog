import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { CommonService } from '../services/all-services';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.css']
})
export class UpdateComponent implements OnInit {
  id:any
  constructor(private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private commonService: CommonService,
    private router: Router) { }

  ngOnInit() {
    this.getArticle(this.id)
  }
  articles : any
  getArticle(id){
    this.commonService.getArticleDetails(this.id).subscribe((data: any) => {

      this.articles = data;
      console.log(data);
    },
    (err: HttpErrorResponse) => {
      console.log(err);
    });
  }

}
