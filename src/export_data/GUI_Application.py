import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import CSV_Parser
from Plot_Handler import Plot_Handler

import numpy as np

class MainApplication(tk.Frame):
    def __init__(self, master):
        self.current_plot = 0
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.load_config_file()
        self.configure_gui()
        self.create_control_frame_buttons()
        self.create_dropdown_menus()
        self.create_plots()
        

    def load_config_file(self):
        self.config = {}
        with open('Config.dat') as file:
            for line in file:
                split_line = line.split('=')
                self.config[split_line[0]] = split_line[1]

    def configure_gui(self):
        self.master.title('GUI')
        self.master.geometry('1400x720')
        self.master.resizable(False, False)

        # Create three main regions in GUI (left: control panel, center: plot, right: data/status monitor)
        self.left_frame = tk.Frame(width=205, height=720, background='#C7C7C7')
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
        self.button_resume.grid(row=0, column=0, padx=30, pady=(10, 0))

        self.button_pause = tk.Button(self.left_frame, width = 15, height = 1, text='Pause ' + u'\u23F8')
        self.button_pause.grid(row=1, column=0, padx=30, pady=(10, 0))

        self.button_save_plot = tk.Button(self.left_frame, width = 15, height = 1, text='Save Plot')
        self.button_save_plot.grid(row=11, column=0, padx=30, pady=(240, 0))

        self.button_quit = tk.Button(self.left_frame, width = 15, height = 1, text='Quit')
        self.button_quit.grid(row=12, column=0, padx=30, pady=(10, 0))

    def create_dropdown_menus(self):
        self.fields = self.config['Fields'].split(',')
        self.fields = self.fields[1:len(self.fields)]
        for i in range(0, len(self.fields)):
            self.fields[i] = self.fields[i].replace('\n', '')
        
        self.dd_variable1 = tk.StringVar(self.master)
        self.dd_variable1.set(self.fields[0])
        self.dd_plot1 = tk.OptionMenu(self.left_frame, self.dd_variable1, *self.fields, command = lambda x: self.change_plot(1))
        self.dd_plot1.config(width=15)
        self.dd_plot1.grid(row=3, column=0, padx=10, pady=(170,0))
        
        self.dd_variable2 = tk.StringVar(self.master)
        self.dd_variable2.set(self.fields[0])
        self.dd_plot2 = tk.OptionMenu(self.left_frame, self.dd_variable2, *self.fields, command = lambda x: self.change_plot(2))
        self.dd_plot2.config(width=15)
        self.dd_plot2.grid(row=4, column=0, padx=10, pady=(10,0))
        
        self.dd_variable3 = tk.StringVar(self.master)
        self.dd_variable3.set(self.fields[0])
        self.dd_plot3 = tk.OptionMenu(self.left_frame, self.dd_variable3, *self.fields, command = lambda x: self.change_plot(3))
        self.dd_plot3.config(width=15)
        self.dd_plot3.grid(row=5, column=0, padx=10, pady=(10,0))
        
        self.dd_variable4 = tk.StringVar(self.master)
        self.dd_variable4.set(self.fields[0])
        self.dd_plot4 = tk.OptionMenu(self.left_frame, self.dd_variable4, *self.fields, command = lambda x: self.change_plot(4))
        self.dd_plot4.config(width=15)
        self.dd_plot4.grid(row=6, column=0, padx=10, pady=(10,0))

    def create_plots(self):
        self.data_log = CSV_Parser.Table('./data/test_data.csv')
        default_title = self.config['Fields'].split(',')
        default_title = default_title[1]
        self.plot = Plot_Handler(self.data_log.get_column('Date')[-24:], self.data_log.get_column('Battery_Voltage')[-24:], self.fields[0])
        self.canvas = FigureCanvasTkAgg(self.plot.get_figure(), master=self.center_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)

    def change_plot(self, index):
        temp = ''
        if(index == 1):
            temp = self.dd_variable1.get()
        elif(index == 2):
            temp = self.dd_variable2.get()
        elif(index == 3):
            temp = self.dd_variable3.get()
        elif(index == 4):
            temp = self.dd_variable4.get()
        self.plot.change_plot_data(index, self.data_log.get_column('Date')[-24:], self.data_log.get_column(temp)[-24:], temp)
        self.canvas.draw()

    def fetch_new_data(self):
        self.data_log.update_data()
        root.after(5000, main_app.fetch_new_data)
        print('Fetch')

if __name__ == '__main__':
    root = tk.Tk()
    main_app =  MainApplication(root)
    
    root.after(5000, main_app.fetch_new_data)
    root.mainloop()
