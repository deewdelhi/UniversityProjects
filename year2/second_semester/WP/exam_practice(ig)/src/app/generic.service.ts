import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { Person } from './person';
import { Channel } from './channel';

@Injectable({
  providedIn: 'root'
})
export class GenericService {

  private backendUrl = 'http://localhost:81/practice1/controller/controller.php'; // URL to web api
  
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) { }


  fetchChannels(): Observable<Channel[]>{
    return this.http.get<Channel[]>(this.backendUrl+'?action=selectAllChannels')
      .pipe(catchError(this.handleError<Channel[]>('fetchChannels', [])));
  }

  fetchOwners(): Observable<string[]>{
    let url = `${this.backendUrl}?action=getOwners`;
    return this.http.get<string[]>(url)
      .pipe(catchError(this.handleError<string[]>('fetchOwners', [])));
  }

  fetchChannelsByOwner(owner: string): Observable<Channel[]>{
    let url = `${this.backendUrl}?action=getFilteredChannels&owner=${owner}`;
    console.log(owner);
    return this.http.get<Channel[]>(url)
      .pipe(catchError(this.handleError<Channel[]>('fetchChannelsByOwner', [])));
  }

  login(username:string) {
    let url = `${this.backendUrl}?action=login=${username}`;
    return this.http.get<number>(url)
      .pipe(catchError(this.handleError<number>('login')));
  }

  // getCount(username:string):Observable<any> {
  //   let url = `${this.backendUrl}?action=login=${username}`;
  //   return this.http.get<number>(url)
  //     .pipe(catchError(this.handleError<number>('login')));
  //      }

  // fetchSubscribers(): Observable<string[]> {

  // }

  fetchSubscribers() {
    
  }

   /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
   private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      // TO DO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

}
