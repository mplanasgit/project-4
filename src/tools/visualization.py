import matplotlib.pyplot as plt
from IPython.display import Image
import stylecloud

def add_labels_season(title, xlabel, num_seasons, ylim_min = -0.2, ylim_max = 0.2):
    # Adding figure legend and labels
    plt.ylim(ylim_min, ylim_max)
    plt.axhline(y = 0.05, color = 'red', linestyle = 'dotted', label = 'Positivity threshold', zorder=0)
    plt.axhline(y = -0.05, color = 'red', linestyle = 'dotted', label = 'Negativity threshold', zorder=0)
    plt.ylabel(ylabel = "Sentiment Compound [-1 to 1]")
    plt.xticks(ticks = range(0,num_seasons), labels = [str(n) for n in range(1,num_seasons+1)])
    plt.xlabel(xlabel = xlabel)
    plt.title(title, y = 1.02)
    plt.legend(bbox_to_anchor=(1.03, 1), loc="upper left")

 
def print_stylecloud(text, file_name, icon_name, palette):
    
    stylecloud.gen_stylecloud(text = text,
                         icon_name = icon_name,
                          palette = palette,
                          background_color = 'black',
                          gradient = 'horizontal', output_name = f"./output/{file_name}.jpg")

    return Image(filename = f'./output/{file_name}.jpg')

    