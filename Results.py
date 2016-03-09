import matplotlib.pyplot as plt
from numpy import arange
import pdb
def organising_results(home_or_away, total, result, ishome):
    if (result=="H" and ishome==True) or (result=="A" and ishome==False):
        home_or_away['wins'] += 1
        total['wins'] += 1
        return
    if result == "D":
        home_or_away['draws'] += 1
        total['draws'] += 1
        return
    if (result=="A" and ishome==True) or (result=="H" and ishome==False):
        home_or_away['loses'] += 1
        total['loses'] += 1
        return


## I need another variable(s) that on each game computes
## if it went from draw-> win/ loss or any other combination
## Important would be: losses from drawing/ winning positions
## wins from drawing/ losing position

def results(in_csv, teams):
    total_ft = {}
    home_ft = {}
    away_ft = {}
    total_ht = {}
    home_ht = {}
    away_ht = {}
    
    for team in teams:
        total_ft.update({team: {'wins': 0, 'loses': 0, 'draws': 0}})
        home_ft.update({team: {'wins': 0, 'loses': 0, 'draws': 0}})
        away_ft.update({team: {'wins': 0, 'loses': 0, 'draws': 0}})
        total_ht.update({team: {'wins': 0, 'loses': 0, 'draws': 0}})
        home_ht.update({team: {'wins': 0, 'loses': 0, 'draws': 0}})
        away_ht.update({team: {'wins': 0, 'loses': 0, 'draws': 0}})

        for h_team, ht_result, ft_result in zip(in_csv.HomeTeam, in_csv.HTR, in_csv.FTR):
            if h_team == team:
                organising_results(home_ht[team], total_ht[team], ht_result, ishome=True)
                organising_results(home_ft[team], total_ft[team], ft_result, ishome=True)
        for a_team, ht_result, ft_result in zip(in_csv.AwayTeam, in_csv.HTR, in_csv.FTR):
            if a_team == team:
                organising_results(away_ht[team], total_ht[team], ht_result, ishome=False)
                organising_results(away_ft[team], total_ft[team], ft_result, ishome=False)

    return total_ft, home_ft, away_ft, total_ht, home_ht, away_ht
