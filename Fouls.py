import matplotlib.pyplot as plt
from numpy import arange



def fouls(in_csv, teams):
    total_fouls = {}
    home_fouls = {}
    away_fouls = {}
    total_yellows = {}
    home_yellows = {}
    away_yellows = {}
    total_reds = {}
    home_reds = {}
    away_reds = {}
    
    for team in teams:
        fouls = 0
        h_fouls = 0
        a_fouls = 0
        h_yell = 0
        a_yell = 0 
        h_red = 0
        a_red = 0
        games = 0
        for h_team, hf, hy, hr in zip(in_csv.HomeTeam, in_csv.HF, in_csv.HY, in_csv.HR):
            if h_team == team:
                h_fouls += hf
                h_yell += hy
                h_red += hr
                games += 1
        for a_team, af, ay, ar in zip(in_csv.AwayTeam, in_csv.HF, in_csv.AY, in_csv.AR):
            if a_team == team:
                a_fouls += af
                a_yell += ay
                a_red += hr
                games += 1

        total_fouls.update({team: h_fouls+a_fouls})
        home_fouls.update({team:h_fouls})
        away_fouls.update({team:a_fouls})
        total_yellows.update({team: h_yell+a_yell})
        home_yellows.update({team:h_yell})
        away_yellows.update({team:a_yell})
        total_reds.update({team: h_red+a_red})
        home_reds.update({team:h_red})
        away_reds.update({team:a_red})

    return total_fouls, home_fouls, away_fouls, total_yellows, home_yellows, away_yellows, total_reds, home_reds, away_reds
