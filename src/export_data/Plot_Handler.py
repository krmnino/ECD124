from matplotlib.figure import Figure
import numpy as np
import warnings

from CSV_Parser import Table

class Plot_Handler:
    warnings.filterwarnings('ignore')

    fig = None
    ax = None

    def __init__(self, x_data, y_data, default_title):
        #self.fig = Figure(figsize=(800/100, 480/100), dpi=100)
        self.fig = Figure(figsize=(10, 7), dpi=100)

        x_data = self.trim_date(x_data)

        # add subplots (2 x 2, nth subplot)
        self.ax1 = self.fig.add_subplot(2,2,1)
        self.ax2 = self.fig.add_subplot(2,2,2)
        self.ax3 = self.fig.add_subplot(2,2,3)
        self.ax4 = self.fig.add_subplot(2,2,4)
        #self.fig.tight_layout()
        self.fig.subplots_adjust(left=0.05, bottom=0.10, right=0.98, top=0.97, wspace=0.15, hspace=0.38)

        self.line1 = self.ax1.plot(x_data, y_data, color='#4894DF')
        self.dots1 = self.ax1.scatter(x_data, y_data, color='k')
        self.ax1.set_title(default_title)
        self.ax1.tick_params(axis='x',labelrotation=90)
        self.ax1.set_xticklabels(labels=x_data, fontsize=9)
        self.ax1.grid()

        self.line2 = self.ax2.plot(x_data, y_data, color='#D43D3D')
        self.dots2 = self.ax2.scatter(x_data, y_data, color='k')
        self.ax2.set_title(default_title)
        self.ax2.tick_params(axis='x',labelrotation=90)
        self.ax2.set_xticklabels(labels=x_data, fontsize=9)
        self.ax2.grid()

        self.line3 = self.ax3.plot(x_data, y_data, color='#7EC84B')
        self.dots3 = self.ax3.scatter(x_data, y_data, color='k')
        self.ax3.set_title(default_title)
        self.ax3.tick_params(axis='x',labelrotation=90)
        self.ax3.set_xticklabels(labels=x_data, fontsize=9)
        self.ax3.grid()

        self.line4 = self.ax4.plot(x_data, y_data, color='#F89022')
        self.dots4 = self.ax4.scatter(x_data, y_data, color='k')
        self.ax4.set_title(default_title)
        self.ax4.tick_params(axis='x',labelrotation=90)
        self.ax4.set_xticklabels(labels=x_data, fontsize=9)
        self.ax4.grid()

    def get_figure(self):
        return self.fig

    def change_plot_data(self, index, new_x_data, new_y_data, title):
        if(index == 1):
            self.ax1.cla()
            self.line1 = self.ax1.plot(new_x_data, new_y_data, color='#4894DF')
            self.dots1 = self.ax1.scatter(new_x_data, new_y_data, color = 'k')
            self.ax1.set_title(title)
            self.ax1.tick_params(axis='x',labelrotation=90)
            self.ax1.set_xticklabels(labels=new_x_data, fontsize=9)
            self.ax1.grid()
        elif(index == 2):
            self.ax2.cla()
            self.line2 = self.ax2.plot(new_x_data, new_y_data, color='#D43D3D')
            self.dots2 = self.ax2.scatter(new_x_data, new_y_data, color = 'k')
            self.ax2.set_title(title)
            self.ax2.tick_params(axis='x',labelrotation=90)
            self.ax2.set_xticklabels(labels=new_x_data, fontsize=9)
            self.ax2.grid()
        elif(index == 3):
            self.ax3.cla()
            self.line3 = self.ax3.plot(new_x_data, new_y_data, color='#7EC84B')
            self.dots3 = self.ax3.scatter(new_x_data, new_y_data, color = 'k')
            self.ax3.set_title(title)
            self.ax3.tick_params(axis='x',labelrotation=90)
            self.ax3.set_xticklabels(labels=new_x_data, fontsize=9)
            self.ax3.grid()
        elif(index == 4):
            self.ax4.cla()
            self.line4 = self.ax4.plot(new_x_data, new_y_data, color='#F89022')
            self.dots4 = self.ax4.scatter(new_x_data, new_y_data, color = 'k')
            self.ax4.set_title(title)
            self.ax4.tick_params(axis='x',labelrotation=90)
            self.ax4.set_xticklabels(labels=new_x_data, fontsize=9)
            self.ax4.grid()
        

    def update_data(self, new_x_data, new_y_data):
        print('placeholder')

    def trim_date(self, x_data):
        for i in range(0, len(x_data)):
            temp = x_data[i].split(' ')
            x_data[i] = temp[1]
        return x_data
 