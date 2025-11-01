import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { IPlayer } from '../models/player';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  constructor(private http: HttpClient) { }

  getPlayers(): Observable<any[]> {
    return this.http.get<any[]>('/api');
  }
}
