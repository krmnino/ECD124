import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import CSV_Parser
import Plotter

import numpy as np

class MainApplication(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.master.title('GUI')
        self.master.geometry('1400x720')
        self.master.resizable(False, False)

    def create_widgets(self):
        self.create_frames()
        self.create_control_frame_buttons()
        self.create_plot()

    # Create three main regions in GUI (left: control panel, center: plot, right: data/status monitor)
    def create_frames(self):
        self.left_frame = tk.Frame(width=175, height=720, background='#C7C7C7')
        self.left_frame.grid_propagate(0)
        self.left_frame.grid(row=0, column=0)

        self.center_frame = tk.Frame(width=1000, height=720, background='#FFFFFF')
        self.center_frame.grid_propagate(0)
        self.center_frame.grid(row=0, column=1)

        self.right_frame = tk.Frame(width=225, height=720, background='#C7C7C7')
        self.right_frame.grid_propagate(0)
        self.right_frame.grid(row=0, column=2)     

    def create_control_frame_buttons(self):
        self.button_resume = tk.Button(self.left_frame, width = 15, height = 1, text='Resume ' + u'\u23F5')
        self.button_resume.grid(row=0, column=0, padx=30, pady=10)

        self.button_pause = tk.Button(self.left_frame, width = 15, height = 1, text='Pause ' + u'\u23F8')
        self.button_pause.grid(row=1, column=0, padx=30, pady=0)

        self.button_save_plot = tk.Button(self.left_frame, width = 15, height = 1, text='Save Plot')
        self.button_save_plot.grid(row=2, column=0, padx=30, pady=130)

        self.button_quit = tk.Button(self.left_frame, width = 15, height = 1, text='Quit')
        self.button_quit.grid(row=3, column=0, padx=30, pady=60)

    def create_plot(self):
        self.fig = Figure(figsize=(10, 7), dpi=100)
        self.data_log = CSV_Parser.parse_file('./data/test_data.csv')
        self.fig.add_subplot(111)

        #t = np.arange(0, 3, .01)
        #self.fig.add_subplot(111).plot(self.data_log['Date'][-30:], self.data_log['Battery_Voltage'][-30:])
        self.ax = Plotter.GraphData(self.fig, self.data_log['Date'][-30:], self.data_log['Battery_Voltage'][-30:])
        self.ax.ax.tick_params(axis='x',labelrotation=90)
        

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.center_frame)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)


if __name__ == '__main__':
    root = tk.Tk()
    main_app =  MainApplication(root)
    root.mainloop()