from matplotlib.figure import Figure
import numpy as np
import warnings

from CSV_Parser import Table

class Plot_Handler:
    fig = None
    ax = None
    x_data = None
    y_data = None

    def __init__(self, x_data_, y_data_):
        self.fig = Figure(figsize=(10, 7), dpi=100)
        
        
        self.ax = self.fig.add_subplot(111)
        self.x_data = x_data_
        self.y_data = y_data_
        self.line = self.ax.plot(self.x_data, self.y_data)
        self.dots = self.ax.scatter(self.x_data, self.y_data)
        self.ax.tick_params(axis='x',labelrotation=90)
        self.ax.grid()

    def get_figure(self):
        return self.fig

    def change_plot_data(self, new_y_data):
        self.ax.cla()
        self.y_data = new_y_data
        self.line = self.ax.plot(self.x_data, self.y_data)
        self.dots = self.ax.scatter(self.x_data, self.y_data)
        self.ax.tick_params(axis='x',labelrotation=90)
        self.ax.grid()

    def update_data(self, new_x_data, new_y_data):
        print('placeholder')
