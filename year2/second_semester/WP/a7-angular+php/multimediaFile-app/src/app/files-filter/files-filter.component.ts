
import { Component, OnInit } from '@angular/core';
import { GenericService } from '../generic.service';
import { MultimediaFile } from '../multimediaFile';

@Component({
  selector: 'app-files-filter',
  templateUrl: './files-filter.component.html',
  styleUrls: ['./files-filter.component.scss']
})
export class FilesFilterComponent implements OnInit {

  selectedOption: string = '';
  types: string[] = [];
  // formats: string[] = [];
  filteredFiles: MultimediaFile[] = [];

  prevOption: string = 'None';
  optionHistory: string[] = ["None"];

  constructor(private genericService: GenericService) { }

  ngOnInit(): void {
    this.getTypes();
    // this.getFormats();
  }

  getTypes(): void{
    this.genericService.fetchTypes()
      .subscribe(types => this.types = types);
  }


  getFilteredFiles(): void{
    this.prevOption = this.optionHistory[this.optionHistory.length - 1];
    this.optionHistory.push(this.selectedOption);
    this.genericService.fetchFilesByType(this.selectedOption)
      .subscribe(docs => {
        this.filteredFiles = docs;
      });
  }
  

}