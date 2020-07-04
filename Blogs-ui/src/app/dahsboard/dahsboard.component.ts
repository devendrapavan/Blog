import { Component, OnInit } from '@angular/core';
import { CommonService } from '../services/all-services';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-dahsboard',
  templateUrl: './dahsboard.component.html',
  styleUrls: ['./dahsboard.component.css']
})
export class DahsboardComponent implements OnInit {

  isLoader = false

  constructor(private commonService: CommonService) { }

  ngOnInit() {
    console.log('inside')
    this.getAllBlogs();
  }
  articles = []

  getAllBlogs() {
    console.log('inside')
    this.isLoader = true
    this.commonService.getAllBlogs().subscribe((data: any) => {
      this.isLoader = false
      this.articles = data;
      console.log(data);
    },
      (err: HttpErrorResponse) => {
        this.isLoader = false
        console.log(err);
      });

  }

}
