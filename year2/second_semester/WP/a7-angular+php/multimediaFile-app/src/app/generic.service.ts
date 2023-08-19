
import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http'
import { Observable, of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { MultimediaFile } from './multimediaFile';

@Injectable({
  providedIn: 'root'
})

export class GenericService {
  private backendUrl = 'http://localhost:81/lab8/controller/controller.php'; // URL to web api
  
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  constructor(private http: HttpClient) { }

  fetchFiles(): Observable<MultimediaFile[]>{
    return this.http.get<MultimediaFile[]>(this.backendUrl+'?action=selectAllFiles')
      .pipe(catchError(this.handleError<MultimediaFile[]>('fetchFiles', [])));
  }

  fetchTypes(): Observable<string[]>{
    let url = `${this.backendUrl}?action=getTypes`;
    return this.http.get<string[]>(url)
      .pipe(catchError(this.handleError<string[]>('fetchTypes', [])));
  }

  fetchFilesByType(type: string): Observable<MultimediaFile[]>{
    let url = `${this.backendUrl}?action=getFilteredFiles&type=${type}`;
    return this.http.get<MultimediaFile[]>(url)
      .pipe(catchError(this.handleError<MultimediaFile[]>('fetchFilesByType', [])));
  }


  /** POST: add a new MultimediaFile to the database */
  addFile(file: MultimediaFile): Observable<any>{
    // const body = JSON.stringify(doc);
    // return this.http.post<any>(this.backendUrl, body)
    //   .pipe(catchError(this.handleError<any>('addMultimediaFile')));

    let url = `${this.backendUrl}?action=addFile&id=${null}&title=${file.title}&formatType=${file.formatType}&genre=${file.genre}&path=${file.path}`;
    return this.http.get<string>(url)
      .pipe(catchError(this.handleError<string>('addFile', "")));
  }



  updateFile(file: MultimediaFile): Observable<any>{
    let url = `${this.backendUrl}?action=updateFile&id=${file.id}&title=${file.title}&formatType=${file.formatType}&genre=${file.genre}&path=${file.path}`;

    return this.http.get<string>(url)
      .pipe(catchError(this.handleError<string>('updateFile', "")));


  }

  deleteFile(id: number): Observable<any>{
    let url = `${this.backendUrl}?action=deleteFile&id=${id}`
    return this.http.get<string>(url)
      .pipe(catchError(this.handleError<string>('deleteFile', "")));
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