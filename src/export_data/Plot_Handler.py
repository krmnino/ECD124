from matplotlib.figure import Figure
import numpy as np
import warnings

from CSV_Parser import Table

class Plot_Handler:
    warnings.filterwarnings('ignore')

    fig = None
    ax = None

    def __init__(self, data, default_title):
        #self.fig = Figure(figsize=(800/100, 480/100), dpi=100)
        self.fig = Figure(figsize=(10, 7), dpi=100)

        # add subplots (2 x 2, nth subplot)
        self.ax1 = self.fig.add_subplot(2,2,1)
        self.ax2 = self.fig.add_subplot(2,2,2)
        self.ax3 = self.fig.add_subplot(2,2,3)
        self.ax4 = self.fig.add_subplot(2,2,4)

        self.ax1.set_autoscale_on(True)
        self.ax1.autoscale_view(True,True,True)

        #self.fig.tight_layout()
        self.fig.subplots_adjust(left=0.05, bottom=0.10, right=0.98, top=0.97, wspace=0.15, hspace=0.38)

        # line colors for each plot line
        self.tl_color = '#4894DF'
        self.tr_color = '#D43D3D'
        self.bl_color = '#7EC84B'
        self.br_color = '#F89022'

        # Default data display
        data_displayed = data.get_fields()[1]
        self.tl_data_shown = data_displayed
        self.tr_data_shown = data_displayed 
        self.bl_data_shown = data_displayed
        self.br_data_shown = data_displayed

        self.line1, = self.ax1.plot(data.get_column('Date')[-24:], data.get_column(self.tl_data_shown)[-24:], color=self.tl_color)
        self.dots1, = self.ax1.plot(data.get_column('Date')[-24:], data.get_column(self.tl_data_shown)[-24:], 'ko')
        self.ax1.set_title(self.tl_data_shown)
        self.ax1.tick_params(axis='x',labelrotation=90)
        self.ax1.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
        self.ax1.grid()

        self.line2, = self.ax2.plot(data.get_column('Date')[-24:], data.get_column(self.tr_data_shown)[-24:], color=self.tr_color)
        self.dots2, = self.ax2.plot(data.get_column('Date')[-24:], data.get_column(self.tr_data_shown)[-24:], 'ko')
        self.ax2.set_title(default_title)
        self.ax2.tick_params(axis='x',labelrotation=90)
        self.ax2.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
        self.ax2.grid()

        self.line3, = self.ax3.plot(data.get_column('Date')[-24:], data.get_column(self.bl_data_shown)[-24:], color=self.bl_color)
        self.dots3 = self.ax3.plot(data.get_column('Date')[-24:], data.get_column(self.bl_data_shown)[-24:], 'ko')
        self.ax3.set_title(default_title)
        self.ax3.tick_params(axis='x',labelrotation=90)
        self.ax3.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
        self.ax3.grid()

        self.line4, = self.ax4.plot(data.get_column('Date')[-24:], data.get_column(self.br_data_shown)[-24:], color=self.br_color)
        self.dots4 = self.ax4.plot(data.get_column('Date')[-24:], data.get_column(self.br_data_shown)[-24:], 'ko')
        self.ax4.set_title(default_title)
        self.ax4.tick_params(axis='x',labelrotation=90)
        self.ax4.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
        self.ax4.grid()

    def get_figure(self):
        return self.fig

    def update_top_left(self, data):
        self.ax1.cla()
        self.line1, = self.ax1.plot(data.get_column('Date')[-24:], data.get_column(self.tl_data_shown)[-24:], color=self.tl_color)
        self.dots1, = self.ax1.plot(data.get_column('Date')[-24:], data.get_column(self.tl_data_shown)[-24:], 'ko')
        self.ax1.set_title(self.tl_data_shown)
        self.ax1.tick_params(axis='x',labelrotation=90)
        self.ax1.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
        self.ax1.grid()
        self.ax1.relim()
        self.ax1.autoscale_view(True,True,True)
        return

    def update_top_right(self, data):
        self.ax2.cla()
        self.line1, = self.ax2.plot(data.get_column('Date')[-24:], data.get_column(self.tr_data_shown)[-24:], color=self.tr_color)
        self.dots1, = self.ax2.plot(data.get_column('Date')[-24:], data.get_column(self.tr_data_shown)[-24:], 'ko')
        self.ax2.set_title(self.tr_data_shown)
        self.ax2.tick_params(axis='x',labelrotation=90)
        self.ax2.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
        self.ax2.grid()
        self.ax2.relim()
        self.ax2.autoscale_view(True,True,True)
        return

    def update_bottom_left(self, data):
        self.ax3.cla()
        self.line1, = self.ax3.plot(data.get_column('Date')[-24:], data.get_column(self.bl_data_shown)[-24:], color=self.bl_color)
        self.dots1, = self.ax3.plot(data.get_column('Date')[-24:], data.get_column(self.bl_data_shown)[-24:], 'ko')
        self.ax3.set_title(self.bl_data_shown)
        self.ax3.tick_params(axis='x',labelrotation=90)
        self.ax3.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
        self.ax3.grid()
        self.ax3.relim()
        self.ax3.autoscale_view(True,True,True)
        return

    def update_bottom_right(self, data):
        self.ax4.cla()
        self.line1, = self.ax4.plot(data.get_column('Date')[-24:], data.get_column(self.br_data_shown)[-24:], color=self.br_color)
        self.dots1, = self.ax4.plot(data.get_column('Date')[-24:], data.get_column(self.br_data_shown)[-24:], 'ko')
        self.ax4.set_title(self.br_data_shown)
        self.ax4.tick_params(axis='x',labelrotation=90)
        self.ax4.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
        self.ax4.grid()
        self.ax4.relim()
        self.ax4.autoscale_view(True,True,True)
        return

    def change_plot_data(self, index, field, data):
        if(index == 1):
            self.tl_data_shown = field
            self.ax1.cla()
            self.line1, = self.ax1.plot(data.get_column('Date')[-24:], data.get_column(self.tl_data_shown)[-24:], color=self.tl_color)
            self.dots1, = self.ax1.plot(data.get_column('Date')[-24:], data.get_column(self.tl_data_shown)[-24:], 'ko')
            self.ax1.set_title(field)
            self.ax1.tick_params(axis='x',labelrotation=90)
            self.ax1.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
            self.ax1.grid()
        elif(index == 2):
            self.tr_data_shown = field
            self.ax2.cla()
            self.line2, = self.ax2.plot(data.get_column('Date')[-24:], data.get_column(self.tr_data_shown)[-24:], color=self.tr_color)
            self.dots2, = self.ax2.plot(data.get_column('Date')[-24:], data.get_column(self.tr_data_shown)[-24:], 'ko')
            self.ax2.set_title(field)
            self.ax2.tick_params(axis='x',labelrotation=90)
            self.ax2.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
            self.ax2.grid()
        elif(index == 3):
            self.bl_data_shown = field
            self.ax3.cla()
            self.line3, = self.ax3.plot(data.get_column('Date')[-24:], data.get_column(self.bl_data_shown)[-24:], color=self.bl_color)
            self.dots3, = self.ax3.plot(data.get_column('Date')[-24:], data.get_column(self.bl_data_shown)[-24:], 'ko')
            self.ax3.set_title(field)
            self.ax3.tick_params(axis='x',labelrotation=90)
            self.ax3.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
            self.ax3.grid()
        elif(index == 4):
            self.br_data_shown = field
            self.ax4.cla()
            self.line4, = self.ax4.plot(data.get_column('Date')[-24:], data.get_column(self.br_data_shown)[-24:], color=self.br_color)
            self.dots4, = self.ax4.plot(data.get_column('Date')[-24:], data.get_column(self.br_data_shown)[-24:], 'ko')
            self.ax4.set_title(field)
            self.ax4.tick_params(axis='x',labelrotation=90)
            self.ax4.set_xticklabels(labels=data.get_column('Date')[-24:], fontsize=9)
            self.ax4.grid()
 