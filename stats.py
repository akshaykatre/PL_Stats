import pandas
from Shots import shots, percent_vs_shot_plot
from Fouls import fouls
from Plotting import totals_plot, detailbars 
import matplotlib.pyplot as plt

x = pandas.read_csv("2013-2014.csv")
teams = x.HomeTeam.unique()

m_teams = {}
for index, t in enumerate(sorted(teams)):
    m_teams.update({t:index+1})
    
# Compute the total, average and the number of shots
# on target for all the teams and store them in maps
total, average, on_target = shots(x, sorted(teams))

# Plot the total number of shots and the those on 
# target for all the teams
ts_plot = totals_plot(total, m_teams, xlabel="Teams", ylabel="Total shots")
on_plot = totals_plot(on_target, m_teams, xlabel="Teams", ylabel="Shots on target")

# Compute the % of shots on target for each team
percent_target = {}
for shots, target in zip(total.iterkeys(), on_target.iterkeys()):
    percent = round(on_target[target]/float(total[shots]) *100, 2)
    percent_target.update({shots:percent})

# Plot the percentage of shots on target for each team
percent_plot = totals_plot(percent_target, m_teams, ylabel="% shots on target")

# Plot the % of shots on target against the total number of shots
# This is to sort of understand the "wastefulness" of the shots 
# taken
totalshots = []
percentshots = []
teamnames = []
for t in sorted(teams):
    totalshots.append(total[t])
    percentshots.append(percent_target[t])
    teamnames.append(t)

# Plotting % on target as a function of total shots
p_vs_ts_plot = percent_vs_shot_plot(totalshots, percentshots, teamnames)

# Use the fouls module to get detailed information on the 
# fouls and cards for each team
total_fouls, home_fouls, away_fouls, total_yellows, home_yellows, away_yellows, total_reds, home_reds, away_reds = fouls(x, sorted(teams))

# Plotting the total number of fouls
tfouls_plot = totals_plot(total_fouls, m_teams, xlabel='Teams', ylabel='Total fouls')

# Bar graphs showing the total number of fouls and yellow cards 
# for each team
foulbars = detailbars(total_fouls, home_fouls, away_fouls, m_teams)
yellowbars = detailbars(total_yellows, home_yellows, away_yellows, m_teams)


# The ratio of the number of yellow cards recieved at home and 
# away
times_away_yellow = {m:round(z/float(y),2) for m,y,z in zip(home_yellows.iterkeys(), home_yellows.itervalues(), away_yellows.itervalues())}

times_away_yellow_plot = totals_plot(times_away_yellow, m_teams, ylabel="Yellow cards away/ yellow cards at home")


# Estimating the number of fouls before being shown a yellow 
# card per team; This idea is extended to home and away teams 
# as well showing that home teams have an advantage
prone_yellows = {m:round(total_fouls[m]/float(total_yellows[m]),2) for m in sorted(total_yellows)}
home_prone_yellows = {m:round(home_fouls[m]/float(home_yellows[m]),2) for m in sorted(home_yellows)}
away_prone_yellows = {m:round(away_fouls[m]/float(away_yellows[m]),2) for m in sorted(away_yellows)}

# Bar graph showing the number of fouls per yellow card
yellow_proneness = detailbars(prone_yellows, home_prone_yellows, away_prone_yellows, m_teams, ylabel="Number of fouls per yellow card")

