import { Component, OnInit } from '@angular/core';
import { Person } from '../person';
import { Channel } from '../channel';
import { GenericService } from '../generic.service'; 


@Component({
  selector: 'app-channels',
  templateUrl: './channels.component.html',
  styleUrls: ['./channels.component.scss']
})
export class ChannelsComponent {

  channels: Channel[] =[];
  constructor(private genericService: GenericService) { }

  ngOnInit(): void {
    console.log("ngOnInit called for ChannelsComponent");
  	this.getChannels();
  }

  
  getChannels(): void {
  	this.genericService.fetchChannels()
    	.subscribe(channels => this.channels = channels);
  } 

  
  onSelect(channel: Channel): void {
    console.log(channel.name + " is selected.");
  } 

}
