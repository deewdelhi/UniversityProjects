import { Component, OnInit  } from '@angular/core';
import { MultimediaFile } from '../multimediaFile';
import { GenericService } from '../generic.service'; 

@Component({
  selector: 'app-files',
  templateUrl: './files.component.html',
  styleUrls: ['./files.component.scss']
})
export class FilesComponent {

  files : MultimediaFile[] = [];

  constructor(private genericService: GenericService) { }

  ngOnInit(): void {
    console.log("ngOnInit called for StudentComponent");
  	this.getFiles();
  }

  
  getFiles(): void {
  	this.genericService.fetchFiles()
    	.subscribe(files => this.files = files);
  } 

  
  onSelect(file: MultimediaFile): void {
    console.log(file.title + " is selected.");
  } 


}

