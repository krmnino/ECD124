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
        self.configure_gui()
        self.create_control_frame_buttons()
        self.create_radio_buttons()
        self.create_plot()

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

    def create_radio_buttons(self):
        self.radio_button_variable = tk.IntVar()
        tk.Radiobutton(
            self.left_frame,
            text="Battery_Voltage",
            variable=self.radio_button_variable,
            value=1,
            bg='#C7C7C7',
            command = lambda: self.change_plot(0)).grid(row=3, column=0, padx=10, pady=(120,0))

        tk.Radiobutton(
            self.left_frame,
            text="Battery_Current",
            variable=self.radio_button_variable,
            value=2,
            bg='#C7C7C7',
            command = lambda: self.change_plot(1)).grid(row=4, column=0, padx=10, pady=0)

        tk.Radiobutton(
            self.left_frame,
            text="Battery_Max_Discharge_Power",
            variable=self.radio_button_variable,
            value=3,
            bg='#C7C7C7',
            command = lambda: self.change_plot(2)).grid(row=5, column=0, padx=10, pady=0)
            
        tk.Radiobutton(
            self.left_frame,
            text="Battery_Max_Regen_Power",
            variable=self.radio_button_variable,
            value=4,
            bg='#C7C7C7',
            command = lambda: self.change_plot(3)).grid(row=6, column=0, padx=10, pady=0)

        tk.Radiobutton(
            self.left_frame,
            text="Battery_State",
            variable=self.radio_button_variable,
            value=5,
            bg='#C7C7C7',
            command = lambda: self.change_plot(4)).grid(row=7, column=0, padx=10, pady=0)

        tk.Radiobutton(
            self.left_frame,
            text="Battery_Temperature",
            variable=self.radio_button_variable,
            value=6,
            bg='#C7C7C7',
            command = lambda: self.change_plot(5)).grid(row=8, column=0, padx=10, pady=0)

        tk.Radiobutton(
            self.left_frame,
            text="WEMS_Target_Power",
            variable=self.radio_button_variable,
            value=7,
            bg='#C7C7C7',
            command = lambda: self.change_plot(6)).grid(row=9, column=0, padx=10, pady=0)

        tk.Radiobutton(
            self.left_frame,
            text="WEMS_Power_Direction",
            variable=self.radio_button_variable,
            value=8,
            bg='#C7C7C7',
            command = lambda: self.change_plot(7)).grid(row=10, column=0, padx=10, pady=0)

    def create_plot(self):
        self.data_log = CSV_Parser.parse_file('./data/test_data.csv')
        self.plot = Plot_Handler(self.data_log['Date'][-36:], self.data_log['Battery_Current'][-36:])
        self.canvas = FigureCanvasTkAgg(self.plot.get_figure(), master=self.center_frame)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)

    def change_plot(self, input):
        self.current_plot = input
        if(self.current_plot == 0):
            self.plot.change_plot_data()
        elif(self.current_plot == 1):
            print('placeholder')
        elif(self.current_plot == 2):
            print('placeholder')
        elif(self.current_plot == 3):
            print('placeholder')
        elif(self.current_plot == 4):
            print('placeholder')
        elif(self.current_plot == 5):
            print('placeholder')
        elif(self.current_plot == 6):
            print('placeholder')
        elif(self.current_plot == 7):
            print('placeholder')

    def fetch_new_data(self):
        self.data_log = CSV_Parser.parse_file('./data/test_data.csv')
        root.after(5000, main_app.fetch_new_data)
        print('Fetch')

if __name__ == '__main__':
    root = tk.Tk()
    main_app =  MainApplication(root)
    
    root.after(5000, main_app.fetch_new_data)
    root.mainloop()