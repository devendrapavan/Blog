import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Urls } from '../const/urls';

@Injectable({
  providedIn: 'root'
})

export class CommonService {
    
    constructor(private http: HttpClient){

    }

    getAllBlogs(){
        const reqHeader = new HttpHeaders({ 'Content-Type': 'Application/json',
         'Authorization':'Bearer'+' '+localStorage.getItem("accessToken") });
        return this.http.get(Urls.ALLBLOGS, { headers: reqHeader });
    }

    postArticle(article:any){
      const reqHeader = new HttpHeaders({ 'Content-Type': 'Application/json',
       'Authorization':'Bearer'+' '+localStorage.getItem("accessToken") });
      return this.http.post(Urls.CREATE,article, { headers: reqHeader });
  }

  updateArticle(article:any){
    const reqHeader = new HttpHeaders({ 'Content-Type': 'Application/json',
     'Authorization':'Bearer'+' '+localStorage.getItem("accessToken") });
    return this.http.post(Urls.UPDATE,article, { headers: reqHeader });
}

getArticleDetails(id:any){
  const reqHeader = new HttpHeaders({ 'Content-Type': 'Application/json',
     'Authorization':'Bearer'+' '+localStorage.getItem("accessToken") });
    return this.http.get(Urls.ARTICLEDETAILS+id, { headers: reqHeader });
}

}