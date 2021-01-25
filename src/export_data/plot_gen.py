import matplotlib.pyplot as plt
import numpy as np
import warnings

from read_file import parse_file

class GraphData:
    x_data = None
    y_data = None
    x_label = ''
    last_days = 0
    y_data_labels = []
    colors = []
    title = ''
    title_size = 0
    suptitle = ''
    path_filename = ''
    date = ''
    tick_markers = False
    legend = False
    y_max = -1
    y_min = -1

    def __init__(self, x_data_, y_data_, x_label_, y_label_, color_, title_, title_size_,
                    suptitle_, path_filename_, date_, tick_markers_, legend_, y_max_, y_min_):
        self.x_data = x_data_
        self.y_data = y_data_
        self.x_label = x_label_
        self.y_label = y_label_
        self.color = color_
        self.title = title_
        self.title_size = title_size_
        self.suptitle = suptitle_
        self.path_filename = path_filename_
        self.date = date_
        self.tick_markers = tick_markers_
        self.legend = legend_
        self.y_max = y_max_
        self.y_min = y_min_


def plot_loader(graph):
    warnings.filterwarnings('ignore')
    plt.figure(figsize=(14,10))
    plt.ticklabel_format(style='plain')
    plt.suptitle(graph.suptitle)
    plt.title(graph.title, fontdict={'fontsize' : graph.title_size})
    plt.plot(graph.x_data, graph.y_data, graph.color, label=graph.y_label)
    if(graph.tick_markers):
        plt.plot(graph.x_data, graph.y_data, 'ko')
    plt.xlabel(graph.x_label)
    plt.ylabel(graph.y_label)
    plt.xticks(rotation=90)
    if(graph.y_min != -1):
        plt.ylim(bottom=graph.y_min)
    if(graph.y_max != -1):
        plt.ylim(top=graph.y_max)
    if(graph.legend):
        plt.legend(loc='upper left')
    plt.grid()
    plt.savefig(graph.path_filename)
    print('Generated graph saved in ' + graph.path_filename)

csv_test = parse_file('data/test.csv')
graph = GraphData(
    csv_test['Timestamp'],
    csv_test['Voltage'],
    'Timestamp',
    'Voltage',
    'b',
    'Test graph',
    20,
    'Test graph',
    'data/test_graph.png',
    '2020-01-25',
    True,
    True,
    -1,
    -1
)
plot_loader(graph)