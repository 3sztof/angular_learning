import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  h1Style: boolean = false;

  users: Object;

  constructor(private data: DataService) { }

  ngOnInit() {
    this.data.getUsers().subscribe(data => {
      this.users = data
      console.log(this.users);
    })
  }

  firstClick() {
    this.h1Style = ! this.h1Style;
    console.log('clicked, style changed');
    this.data.firstClick();                   // Same but using "global" method from a constructor
  }

}
