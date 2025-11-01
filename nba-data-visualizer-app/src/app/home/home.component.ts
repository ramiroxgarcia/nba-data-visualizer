import { Component, inject } from '@angular/core';
import { ApiService } from '../api/api.service';
import { IPlayer } from '../models/player';

@Component({
  selector: 'ndv-home',
  imports: [],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss',
})
export class HomeComponent {
  players: any[] = [];

  constructor(private apiServ: ApiService) { }

  ngOnInit() {
    

    this.apiServ.getPlayers().subscribe(players => 
      {
        console.log('api returned', players)
        this.players = players;
      });

      console.log(this.players)

  }

}
