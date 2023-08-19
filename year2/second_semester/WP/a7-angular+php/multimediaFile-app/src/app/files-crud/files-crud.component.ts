import { Component, OnInit } from '@angular/core';
// import { type } from 'os';
import { MultimediaFile } from '../multimediaFile';
import { GenericService } from '../generic.service';

@Component({
  selector: 'app-files-crud',
  templateUrl: './files-crud.component.html',
  styleUrls: ['./files-crud.component.scss']
})
export class FilesCrudComponent implements OnInit {

  files: MultimediaFile[] = [];


  constructor(private genericService: GenericService) { }

  ngOnInit(): void {
    console.log("ngOnInit called for CarCrudComponent");
    this.getFiles();
  }

  getFiles(): void{
    this.genericService.fetchFiles()
      .subscribe(files => this.files = files);
  }

  onUpdate(file: MultimediaFile): void{
    (<HTMLInputElement>document.getElementById("id2")).value = String(file.id);
    (<HTMLInputElement>document.getElementById("title2")).value = (file.title);
    (<HTMLInputElement>document.getElementById("formatType2")).value = (file.formatType);
    (<HTMLInputElement>document.getElementById("genre2")).value = file.genre;
    (<HTMLInputElement>document.getElementById("path2")).value = (file.path);

    let displayVal:string = document.getElementById('update_form')!.style.display;
    if (displayVal === "none")
    document.getElementById('update_form')!.style.display = "inline";
    else document.getElementById('update_form')!.style.display = "none";

  }

  onDelete(fileID: number): void{

    var result = confirm("Are you sure to delete ");
    if(result) {
      this.genericService.deleteFile(fileID).
    subscribe(r => {
      console.log(r.result);
      this.ngOnInit();
    });
    alert("SUCCESS");
    }
    
  }

  addFile( newTitle: HTMLInputElement, newFormatType: HTMLInputElement, newGenre: HTMLInputElement, newPath: HTMLInputElement){

    var valid = 1;
    if (newTitle.value.length < 5){
      valid = 0;
    }
    if (newFormatType.value.length < 3){
      valid = 0;
    }
    if (newGenre.value.length < 5){
      valid = 0;
    }
    if (newPath.value.length < 5){
      valid = 0;
    }
    if (newPath.value.search(":") < 0){
      valid = 0;
     
    }
    if(valid){
      console.log(newTitle.type)
      let addedFile: MultimediaFile = {id: 0,
      title: newTitle.value,
      formatType: newFormatType.value,
      genre: newGenre.value,
      path: newPath.value
    };
      this.genericService.addFile(addedFile)
      .subscribe(r => {
        console.log(r.result);
        this.ngOnInit();
      });
      alert("SUCCESS");
      (<HTMLInputElement>document.getElementById("id1")).value = ' ';
      (<HTMLInputElement>document.getElementById("title1")).value = ' ';
      (<HTMLInputElement>document.getElementById("formatType1")).value = ' ';
      (<HTMLInputElement>document.getElementById("genre1")).value = ' ';
      (<HTMLInputElement>document.getElementById("path1")).value = ' ';

      
    }
    else{
      alert("the file is not valid, try again");
    }
  

   


  }

  updateFile( newID:HTMLInputElement, uTitle: HTMLInputElement, uFormatType: HTMLInputElement , uGenre: HTMLInputElement, uPath: HTMLInputElement){

    var valid = 1;
    if (uTitle.value.length < 5){
      valid = 0;
    }
    if (uFormatType.value.length < 5){
      valid = 0;
    }
    if (uGenre.value.length < 5){
      valid = 0;
    }
    if (uPath.value.length < 5){
      valid = 0;
    }

    if ( valid){

      let updatedFile: MultimediaFile = {id: +newID.value,
        title: uTitle.value,
        formatType: uFormatType.value,
        genre: uGenre.value,
        path: uPath.value
      };
  
      console.log(updatedFile.id);
  
      this.genericService.updateFile(updatedFile)
        .subscribe(r => {
          console.log(r.result);
          document.getElementById('update_form')!.style.display = "none";
          this.ngOnInit();
        });

        alert("SUCCESS");
    }
    else{ alert("try again");}
     

  }

}