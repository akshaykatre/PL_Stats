import matplotlib.pyplot as plt
from numpy import arange

def shots(in_csv, teams):
    total_shots = {}
    avg_shots = {}
    on_target = {}
    for team in teams:
        shots = 0
        games = 0
        target = 0
        for h_team, hs, h_ot in zip(in_csv.HomeTeam, in_csv.HS, in_csv.HST):
            if h_team == team:
                shots += hs
                games += 1
                target += h_ot
        for a_team, As, a_ot in zip(in_csv.AwayTeam, in_csv.AS, in_csv.AST):
            if a_team == team:
                shots += As
                games += 1
                target += a_ot
        average = shots/float(games)
        avg_shots.update({team:average})
        total_shots.update({team:shots})
        on_target.update({team: target})
    return total_shots, avg_shots, on_target


# def totalshot_plot(total, m_teams):
#     t_names = []
#     t_shots = []
#     t_names_names = []
#     for i in sorted(total.iteritems()):
#         t_names.append(m_teams[i[0]])
#         t_shots.append(i[1])
#         t_names_names.append(i[0])

#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     plt.bar(t_names, t_shots, width=1)
#     plt.xticks(arange(1.2,21.2), (t_names_names), rotation=50)
#     plt.xlim([-1, 22])
#     for index, i in enumerate(t_shots):
#         ax.annotate(str(i), xy=(index+1.2,i), xytext=(0,20), textcoords='offset points')

#     return plt


def percent_vs_shot_plot(total, percent, names):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(total, percent, "bo")
    for x,y,name in zip(total, percent, names):
        ax.annotate(str(name), xy=(x,y), xytext=(-40, 0), textcoords='offset points')
   #     print name
    return plt

