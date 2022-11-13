import matplotlib.pyplot as plt

def add_labels_season(title, num_seasons):
    # Adding figure legend and labels
    plt.ylim(-0.2, 0.2)
    plt.axhline(y = 0.05, color = 'red', linestyle = 'dotted', label = 'Positivity threshold', zorder=0)
    plt.axhline(y = -0.05, color = 'red', linestyle = 'dotted', label = 'Negativity threshold', zorder=0)
    plt.ylabel(ylabel = "Sentiment Compound [-1 to 1]")
    plt.xticks(ticks = range(0,num_seasons), labels = [str(n) for n in range(1,num_seasons+1)])
    plt.xlabel(xlabel = "Season")
    plt.title(title, y = 1.02)
    plt.legend(bbox_to_anchor=(1.03, 1), loc="upper left")


def add_labels_episode(title, num_episodes):
    # Adding figure legend and labels
    plt.ylim(-1, 0.5)
    plt.axhline(y = 0.05, color = 'red', linestyle = 'dotted', label = 'Positivity threshold', zorder=0)
    plt.axhline(y = -0.05, color = 'red', linestyle = 'dotted', label = 'Negativity threshold', zorder=0)
    plt.ylabel(ylabel = "Sentiment Compound [-1 to 1]")
    plt.xticks(ticks = range(0,num_episodes), labels = [str(n) for n in range(1,num_episodes+1)])
    plt.xlabel(xlabel = "Episode")
    plt.title(title, y = 1.02)
    plt.legend(bbox_to_anchor=(1.03, 1), loc="upper left")
    
    

    