// import { NgModule } from '@angular/core';
// import { RouterModule, Routes } from '@angular/router';

// const routes: Routes = [];

// @NgModule({
//   imports: [RouterModule.forRoot(routes)],
//   exports: [RouterModule]
// })
// export class AppRoutingModule { }


import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FilesHomeComponent } from './files-home/files-home.component';
import { FilesFilterComponent } from './files-filter/files-filter.component';
import { FilesCrudComponent } from './files-crud/files-crud.component';

const routes: Routes = [
  {path: '', redirectTo: '/files-home', pathMatch: 'full'},
  {path: 'files-crud', component: FilesCrudComponent},
   {path: 'files-filter', component:FilesFilterComponent},
   {path: 'files-home', component:FilesHomeComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }