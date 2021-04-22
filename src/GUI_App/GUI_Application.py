import tkinter as tk
from tkinter import font as tkFont
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import datetime

import CSV_Parser
from Plot_Handler import Plot_Handler

import numpy as np

class MainApplication(tk.Frame):
    def __init__(self, master, log_file_path, config_file_path):
        self.run_animation = True
        self.connection_statuses = {
            'bms_status' : 0,
            'wems_status' : 0,
            'ac_power_status' : 0,
            'battery_status' : 0
        }
        self.current_plot = 0
        self.master = master

        tk.Frame.__init__(self, self.master)
        self.load_config_file(config_file_path)
        self.configure_gui()
        self.create_control_frame_buttons()
        self.create_dropdown_menus()
        self.create_plots()
        self.create_data_registers()
        
    def load_config_file(self, config_file_path):
        self.config = {}
        with open(config_file_path) as file:
            for line in file:
                split_line = line.split('=')
                self.config[split_line[0]] = split_line[1]

    def configure_gui(self):
        self.master.title('Console v1.0')
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
        self.button_resume = tk.Button(self.left_frame, width = 15, height = 1, text='Resume ' + u'\u23F5', command = lambda : self.play_animation())
        #self.button_resume['font'] = helv36
        self.button_resume.grid(row=0, column=0, padx=30, pady=(10, 0))
        self.button_resume.config(relief='sunken')

        self.button_pause = tk.Button(self.left_frame, width = 15, height = 1, text='Pause ' + u'\u23F8', command = lambda : self.pause_animation())
        self.button_pause.grid(row=1, column=0, padx=30, pady=(10, 0))

        self.button_save_plot = tk.Button(self.left_frame, width = 15, height = 1, text='Save Plot', command = lambda : self.screenshot_plots())
        self.button_save_plot.grid(row=11, column=0, padx=30, pady=(240, 0))

        self.button_quit = tk.Button(self.left_frame, width = 15, height = 1, text='Quit', command=self.master.destroy)
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
        self.data_log = CSV_Parser.Table(log_file_path)
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

        self.retry_connection_button = tk.Button(self.right_frame, width = 15, height = 1, text='Retry Connections', command = lambda : self.retry_connections())
        self.retry_connection_button.grid(row=5, column=1, padx=(10, 0), pady=(10, 0))

        self.title_status_label = tk.Label(self.right_frame, text="Current Readings", background='#C7C7C7')
        self.title_status_label.grid(row=6, column=1, padx=0, pady=(250, 0))

        latest_data = self.data_log.get_latest_entry()
        self.bat_voltage_label = tk.Label(self.right_frame, text="Battery Voltage: ", background='#C7C7C7')
        self.bat_voltage_label.grid(row=7, column=0, padx=0, pady=(10, 0))
        self.bat_voltage = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_voltage, latest_data['Battery_Voltage'])
        self.bat_voltage.grid(row=7, column=1, padx=0, pady=(10, 0))

        self.bat_current_label = tk.Label(self.right_frame, text="Battery Current: ", background='#C7C7C7')
        self.bat_current_label.grid(row=8, column=0, padx=0, pady=(10, 0))
        self.bat_current = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_current, latest_data['Battery_Current'])
        self.bat_current.grid(row=8, column=1, padx=0, pady=(10, 0))

        self.bat_max_discharge_label = tk.Label(self.right_frame, text="Bat MaxDschrg: ", background='#C7C7C7')
        self.bat_max_discharge_label.grid(row=9, column=0, padx=0, pady=(10, 0))
        self.bat_max_discharge = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_max_discharge, latest_data['Battery_Max_Discharge_Power'])
        self.bat_max_discharge.grid(row=9, column=1, padx=0, pady=(10, 0))

        self.bat_max_regen_label = tk.Label(self.right_frame, text="Bat MaxRegen: ", background='#C7C7C7')
        self.bat_max_regen_label.grid(row=10, column=0, padx=0, pady=(10, 0))
        self.bat_max_regen = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_max_regen, latest_data['Battery_Max_Regen_Power'])
        self.bat_max_regen.grid(row=10, column=1, padx=0, pady=(10, 0))

        self.bat_state_label = tk.Label(self.right_frame, text="Battery State: ", background='#C7C7C7')
        self.bat_state_label.grid(row=11, column=0, padx=0, pady=(10, 0))
        self.bat_state = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_state, latest_data['Battery_State'])
        self.bat_state.grid(row=11, column=1, padx=0, pady=(10, 0))

        self.bat_temperature_label = tk.Label(self.right_frame, text="Battery Temp: ", background='#C7C7C7')
        self.bat_temperature_label.grid(row=12, column=0, padx=0, pady=(10, 0))
        self.bat_temperature = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.bat_temperature, latest_data['Battery_Temperature'])
        self.bat_temperature.grid(row=12, column=1, padx=0, pady=(10, 0))

        self.wems_target_pow_label = tk.Label(self.right_frame, text="WEMS TrgtPow: ", background='#C7C7C7')
        self.wems_target_pow_label.grid(row=13, column=0, padx=0, pady=(10, 0))
        self.wems_target_pow = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.wems_target_pow, latest_data['WEMS_Target_Power'])
        self.wems_target_pow.grid(row=13, column=1, padx=0, pady=(10, 0))

        self.wems_pow_direction_label = tk.Label(self.right_frame, text="WEMS PowDir: ", background='#C7C7C7')
        self.wems_pow_direction_label.grid(row=14, column=0, padx=0, pady=(10, 0))
        self.wems_pow_direction = tk.Entry(self.right_frame, width=20)
        self.update_gui_register(self.wems_pow_direction, latest_data['WEMS_Power_Direction'])
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

    def update_gui_register(self, text_field, value):
        text_field.config(state='normal')
        text_field.delete(0, 'end')
        text_field.insert(0, str(value))
        text_field.config(state='readonly')

    def update_gui_new_data(self):
        if(not self.run_animation):
            root.after(5000, main_app.update_gui_new_data)
            return

        # re-enable retry connections button
        self.retry_connection_button.config(relief='raised')

        # read and process new data 
        self.data_log.update_data()

        # update data registers
        latest_data = self.data_log.get_latest_entry()
        self.update_gui_register(self.bat_voltage, latest_data['Battery_Voltage'])
        self.update_gui_register(self.bat_current, latest_data['Battery_Current'])        
        self.update_gui_register(self.bat_max_discharge, latest_data['Battery_Max_Discharge_Power'])
        self.update_gui_register(self.bat_max_regen, latest_data['Battery_Max_Regen_Power'])
        self.update_gui_register(self.bat_state, latest_data['Battery_State'])
        self.update_gui_register(self.bat_temperature, latest_data['Battery_Temperature'])
        self.update_gui_register(self.wems_target_pow, latest_data['WEMS_Target_Power'])
        self.update_gui_register(self.wems_pow_direction, latest_data['WEMS_Power_Direction'])

        # animate GUI with new data
        self.plot.update_top_left(self.data_log)
        self.plot.update_top_right(self.data_log)
        self.plot.update_bottom_left(self.data_log)
        self.plot.update_bottom_right(self.data_log)
        self.canvas.draw()
        root.after(5000, main_app.update_gui_new_data)
        
    def play_animation(self):
        self.run_animation = True
        self.button_resume.config(relief='sunken')
        self.button_pause.config(relief='raised')
        return

    def pause_animation(self):
        self.run_animation = False
        self.button_resume.config(relief='raised')
        self.button_pause.config(relief='sunken')
        return 
        
    def screenshot_plots(self):
        now = datetime.datetime.now()
        current_time = now.strftime('%Y-%m-%d_%H-%M-%S')
        self.plot.get_figure().savefig('Screenshot_' + current_time)
        return 

    def retry_connections(self):
        self.retry_connection_button.config(relief='sunken')
        #TODO: interface with Keenan's code
        #   Call function to reconnect
        #   Retrieve connection status
        #   Update connection status dictionary appropriately
        return

if(__name__ == '__main__'):
    
    log_file_path = './data/test_data.csv'
    config_file_path = 'Config.dat'

    
    root = tk.Tk()
    main_app =  MainApplication(root, log_file_path, config_file_path)

    root.after(5000, main_app.update_gui_new_data)
    root.mainloop()
