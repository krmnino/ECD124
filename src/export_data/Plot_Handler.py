from matplotlib.figure import Figure
import numpy as np
import warnings

from CSV_Parser import parse_file

class Plot_Handler:
    fig = None
    ax = None
    x_data = None
    y_data = None

    def __init__(self, x_data_, y_data_):
        self.fig = Figure(figsize=(10, 7), dpi=100)
        self.fig.add_subplot(111)
        
        self.ax = self.fig.get_axes()[0]
        self.x_data = x_data_
        self.y_data = y_data_

        self.ax.plot(self.x_data, self.y_data)
        self.ax.scatter(self.x_data, self.y_data)
        
        self.ax.tick_params(axis='x',labelrotation=90)

    def get_figure(self):
        return self.fig