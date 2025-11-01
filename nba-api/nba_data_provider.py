import time
from nba_api.stats.endpoints import playercareerstats

class NbaDataProvider:
    def get_players(self):
        
        res = playercareerstats.PlayerCareerStats(player_id=2544)
        return res.get_dict()



