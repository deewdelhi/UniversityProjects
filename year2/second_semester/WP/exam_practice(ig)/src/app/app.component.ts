import { Component , OnInit} from '@angular/core';
import { GenericService } from './generic.service';
import { Channel } from './channel';
import { Person } from './person';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'practice1-app';
  userLoggedIn: number = 1;
  username: string = '';

  // ngOnInit(): void {
  //   this.login(this.username);
  // }

  ngOnInit(): void {
    this.login();
  }
  constructor(private genericService: GenericService) { }

  // login(username:string): void{
  //   this.genericService.login(username)
  //     .subscribe(userLogedIn=> this.userLoggedIn = userLogedIn);
  // }
  

  login() {
    this.genericService.login(this.username)
      .subscribe(response => {
        this.userLoggedIn = response;
        const resInt = + response; 
        console.log(resInt);
        this.userLoggedIn = resInt;
      });
    console.log(this.userLoggedIn);
    console.log(this.username);
    
        
  }

//   getCountFromService(){
//     this.genericService.getCount(this.username).subscribe((data)=>this.userLoggedIn =data)
//     }

 }




