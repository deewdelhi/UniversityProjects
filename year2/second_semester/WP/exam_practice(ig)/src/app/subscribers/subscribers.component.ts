
import { Person } from '../person';
import { Channel } from '../channel';
import { GenericService } from '../generic.service'; 
import { Component } from '@angular/core';

@Component({
  selector: 'app-subscribers',
  templateUrl: './subscribers.component.html',
  styleUrls: ['./subscribers.component.scss']
})
export class SubscribersComponent {
  subscribers: string[] =[];
  constructor(private genericService: GenericService) { }

  ngOnInit(): void {
    console.log("ngOnInit called for ChannelsComponent");
  	this.getSubscribers();

   
  }

  getSubscribers(): void {
    // this.genericService.fetchSubscribers()
    //   .subscribe(subscribers => this.subscribers = subscribers);
  } 
}



