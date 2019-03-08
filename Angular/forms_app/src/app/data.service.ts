import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  firstClick() {
    return console.log('Data service says: clicked');
  }

  getUsers() {
    return this.http.get('https://reqres.in/api/users')     // Dummy testing API
  }

}
