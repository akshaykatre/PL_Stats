import pandas
from Shots import shots, totalshot_plot, percent_vs_shot_plot

x = pandas.read_csv("2013-2014.csv")
teams = x.HomeTeam.unique()

m_teams = {}
for index, t in enumerate(sorted(teams)):
    m_teams.update({t:index+1})
    

total, average, on_target = shots(x, sorted(teams))

ts_plot = totalshot_plot(total, m_teams)
on_plot = totalshot_plot(on_target, m_teams)

percent_target = {}
for shots, target in zip(total.iterkeys(), on_target.iterkeys()):
    percent = round(on_target[target]/float(total[shots]) *100, 2)
    percent_target.update({shots:percent})

percent_plot = totalshot_plot(percent_target, m_teams)


totalshots = []
percentshots = []
teamnames = []
for t in sorted(teams):
    totalshots.append(total[t])
    percentshots.append(percent_target[t])
    teamnames.append(t)

p_vs_ts_plot = percent_vs_shot_plot(totalshots, percentshots, teamnames)
