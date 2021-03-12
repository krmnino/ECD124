import matplotlib.pyplot as plt
import numpy as np
import warnings

from CSV_Parser import parse_file

class GraphData:
    ax = None
    x_data = None
    y_data = None

    def __init__(self, fig_, x_data_, y_data_):
        self.ax = fig_.get_axes()[0]
        self.x_data = x_data_
        self.y_data = y_data_
        self.ax.tick_params(axis='x',labelrotation=90)