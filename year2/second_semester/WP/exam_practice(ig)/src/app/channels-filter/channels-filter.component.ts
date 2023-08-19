
import { Component, OnInit } from '@angular/core';
import { GenericService } from '../generic.service';
import { Channel } from '../channel';
import { Person } from '../person';

@Component({
  selector: 'app-channels-filter',
  templateUrl: './channels-filter.component.html',
  styleUrls: ['./channels-filter.component.scss']
})
export class ChannelsFilterComponent implements OnInit {


  
  selectedOption: string = '';
  owners: string[] = [];
  // formats: string[] = [];
  filteredChannels: Channel[] = [];

  prevOption: string = 'None';
  optionHistory: string[] = ["None"];

  constructor(private genericService: GenericService) { }

  ngOnInit(): void {
    this.getOwners();
    // this.getFormats();
  }

  getOwners(): void{
    this.genericService.fetchOwners()
      .subscribe(owners => this.owners = owners);
  }


  getFilteredChannels(): void{
    this.prevOption = this.optionHistory[this.optionHistory.length - 1];
    this.optionHistory.push(this.selectedOption);
    this.genericService.fetchChannelsByOwner(this.selectedOption)
      .subscribe(cahnnels => {
        this.filteredChannels = cahnnels;
      });
  }
}
