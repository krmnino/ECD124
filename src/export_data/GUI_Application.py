import tkinter as tk
from tkinter import font as tkFont
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
        self.create_data_registers()
        

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
        self.left_frame = tk.Frame(width=180, height=720, background='#C7C7C7')
        self.left_frame.grid_propagate(0)
        self.left_frame.grid(row=0, column=0)

        self.center_frame = tk.Frame(width=1000, height=720, background='#FFFFFF')
        self.center_frame.grid_propagate(0)
        self.center_frame.grid(row=0, column=1)

        self.right_frame = tk.Frame(width=225, height=720, background='#C7C7C7')
        self.right_frame.grid_propagate(0)
        self.right_frame.grid(row=0, column=2)      

    def create_control_frame_buttons(self):
        #helv36 = tkFont.Font(family='Helvetica', size=5, weight='bold')
        self.button_resume = tk.Button(self.left_frame, width = 15, height = 1, text='Resume ' + u'\u23F5')
        #self.button_resume['font'] = helv36
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
        self.plot = Plot_Handler(self.data_log, self.fields[0])
        self.canvas = FigureCanvasTkAgg(self.plot.get_figure(), master=self.center_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)

    def create_data_registers(self):
        self.title_status_label = tk.Label(self.right_frame, text="Connection Statuses", background='#C7C7C7')
        self.title_status_label.grid(row=0, column=1, padx=0, pady=(10, 0))

        self.BMS_status_label = tk.Label(self.right_frame, text="BMS Status: ", background='#C7C7C7')
        self.BMS_status_label.grid(row=1, column=0, padx=0, pady=(10, 0))
        self.BMS_status = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.BMS_status, 'null')
        self.BMS_status.grid(row=1, column=1, padx=0, pady=(10, 0))

        self.WEMS_status_label = tk.Label(self.right_frame, text="WEMS Status: ", background='#C7C7C7')
        self.WEMS_status_label.grid(row=2, column=0, padx=0, pady=(10, 0))
        self.WEMS_status = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.WEMS_status, 'null')
        self.WEMS_status.grid(row=2, column=1, padx=0, pady=(10, 0))

        self.ACPower_status_label = tk.Label(self.right_frame, text="ACPow Status: ", background='#C7C7C7')
        self.ACPower_status_label.grid(row=3, column=0, padx=0, pady=(10, 0))
        self.ACPower_status = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.ACPower_status, 'null')
        self.ACPower_status.grid(row=3, column=1, padx=0, pady=(10, 0))

        self.battery_status_label = tk.Label(self.right_frame, text="Battery Status: ", background='#C7C7C7')
        self.battery_status_label.grid(row=4, column=0, padx=0, pady=(10, 0))
        self.battery_status = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.battery_status, 'null')
        self.battery_status.grid(row=4, column=1, padx=0, pady=(10, 0))

        self.retry_connection_button = tk.Button(self.right_frame, width = 15, height = 1, text='Retry Connections')
        self.retry_connection_button.grid(row=5, column=1, padx=(10, 0), pady=(10, 0))

        self.title_status_label = tk.Label(self.right_frame, text="Current Readings", background='#C7C7C7')
        self.title_status_label.grid(row=6, column=1, padx=0, pady=(250, 0))

        self.bat_voltage_label = tk.Label(self.right_frame, text="Battery Voltage: ", background='#C7C7C7')
        self.bat_voltage_label.grid(row=7, column=0, padx=0, pady=(10, 0))
        self.bat_voltage = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_voltage, 'null')
        self.bat_voltage.grid(row=7, column=1, padx=0, pady=(10, 0))

        self.bat_current_label = tk.Label(self.right_frame, text="Battery Current: ", background='#C7C7C7')
        self.bat_current_label.grid(row=8, column=0, padx=0, pady=(10, 0))
        self.bat_current = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_current, 'null')
        self.bat_current.grid(row=8, column=1, padx=0, pady=(10, 0))

        self.bat_max_discharge_label = tk.Label(self.right_frame, text="Bat MaxDschrg: ", background='#C7C7C7')
        self.bat_max_discharge_label.grid(row=9, column=0, padx=0, pady=(10, 0))
        self.bat_max_discharge = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_max_discharge, 'null')
        self.bat_max_discharge.grid(row=9, column=1, padx=0, pady=(10, 0))

        self.bat_max_regen_label = tk.Label(self.right_frame, text="Bat MaxRegen: ", background='#C7C7C7')
        self.bat_max_regen_label.grid(row=10, column=0, padx=0, pady=(10, 0))
        self.bat_max_regen = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_max_regen, 'null')
        self.bat_max_regen.grid(row=10, column=1, padx=0, pady=(10, 0))

        self.bat_state_label = tk.Label(self.right_frame, text="Battery State: ", background='#C7C7C7')
        self.bat_state_label.grid(row=11, column=0, padx=0, pady=(10, 0))
        self.bat_state = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_state, 'null')
        self.bat_state.grid(row=11, column=1, padx=0, pady=(10, 0))

        self.bat_temperature_label = tk.Label(self.right_frame, text="Battery Temp: ", background='#C7C7C7')
        self.bat_temperature_label.grid(row=12, column=0, padx=0, pady=(10, 0))
        self.bat_temperature = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_temperature, 'null')
        self.bat_temperature.grid(row=12, column=1, padx=0, pady=(10, 0))

        self.wems_target_pow_label = tk.Label(self.right_frame, text="WEMS TrgtPow: ", background='#C7C7C7')
        self.wems_target_pow_label.grid(row=13, column=0, padx=0, pady=(10, 0))
        self.wems_target_pow = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.wems_target_pow, 'null')
        self.wems_target_pow.grid(row=13, column=1, padx=0, pady=(10, 0))

        self.wems_pow_direction_label = tk.Label(self.right_frame, text="WEMS PowDir: ", background='#C7C7C7')
        self.wems_pow_direction_label.grid(row=14, column=0, padx=0, pady=(10, 0))
        self.wems_pow_direction = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.wems_pow_direction, 'null')
        self.wems_pow_direction.grid(row=14, column=1, padx=0, pady=(10, 0))

        
    def change_plot(self, index):
        field = ''
        if(index == 1):
            field = self.dd_variable1.get()
        elif(index == 2):
            field = self.dd_variable2.get()
        elif(index == 3):
            field = self.dd_variable3.get()
        elif(index == 4):
            field = self.dd_variable4.get()
        self.plot.change_plot_data(index, field, self.data_log)
        self.canvas.draw()

    def update_gui_register(self, button, value):
        button.config(state='normal')
        button.delete(0, 'end')
        button.insert(0, str(value))
        button.config(state='readonly')

    def fetch_new_data(self):
        self.data_log.update_data()
        self.plot.update_top_left(self.data_log)
        self.plot.update_top_right(self.data_log)
        self.plot.update_bottom_left(self.data_log)
        self.plot.update_bottom_right(self.data_log)
        self.canvas.draw()
        root.after(5000, main_app.fetch_new_data)
        print('Fetch')

if __name__ == '__main__':
    root = tk.Tk()
    main_app =  MainApplication(root)
    
    root.after(5000, main_app.fetch_new_data)
    root.mainloop()
