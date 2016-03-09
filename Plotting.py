import matplotlib.pyplot as plt
from numpy import arange


def totals_plot(total, m_teams, xlabel=None, ylabel="Total "):
    t_names = []
    t_value = []
    t_names_names = []
    for i in sorted(total.iteritems()):
        t_names.append(m_teams[i[0]])
        t_value.append(i[1])
        t_names_names.append(i[0])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.bar(t_names, t_value, width=1)
    plt.xticks(arange(1.2,21.2), (t_names_names), rotation=50)
    plt.xlim([-1, 22])
    if xlabel != None:
        plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for index, i in enumerate(t_value):
        ax.annotate(str(i), xy=(index+1.2,i), xytext=(0,20), textcoords='offset points')

    return plt


def detailbars(total, home, away, m_teams, xlabel=None, ylabel=None):
#    print len(total)
    ind = arange(1,len(total)+1)
    width = 0.25
    t_names = [m_teams[i] for i in sorted(total.iterkeys())]
    t_names_names = [i for i in sorted(total.iterkeys())]
    t_value = [total[i] for i in sorted(total)]
    t_value_home = [home[i] for i in sorted(home)]
    t_value_away = [away[i] for i in sorted(away)]
    print t_value_home, t_value_away, t_names_names
    fig, ax = plt.subplots()
    plot_total = ax.bar(ind, t_value, width, color='r')
    plot_home = ax.bar(ind+width, t_value_home, width, color='b')
    plot_away = ax.bar(ind+width+width, t_value_away, width, color='g')

    plt.xticks(arange(1.2,21.2), (t_names_names), rotation=50)
    if ylabel != None:
        plt.ylabel(ylabel)
    return plt
