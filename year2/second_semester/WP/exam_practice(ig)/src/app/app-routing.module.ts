import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ChannelsComponent } from './channels/channels.component';
import { ChannelsFilterComponent } from './channels-filter/channels-filter.component';

const routes: Routes = [
  {path: 'channels-filter', component:ChannelsFilterComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
