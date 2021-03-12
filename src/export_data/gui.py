import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

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

    def create_frames(self):
        self.left_frame = tk.Frame(width=300, height=720, background='#C7C7C7')
        self.left_frame.grid_propagate(1)
        self.left_frame.grid(row=0, column=0)

        self.right_frame = tk.Frame(width=1000, height=720, background='#FFFFFF')
        self.right_frame.grid_propagate(0)
        self.right_frame.grid(row=0, column=1)     

    def create_control_frame_buttons(self):
        self.button1 = tk.Button(self.left_frame, text='Resume ' + u'\u23F5')
        self.button1.grid(row=0, column=0, padx=30, pady=60)

        self.button2 = tk.Button(self.left_frame, text='Pause ' + u'\u23F8')
        self.button2.grid(row=1, column=0, padx=30, pady=60)

        self.button3 = tk.Button(self.left_frame, text='Save Plot')
        self.button3.grid(row=2, column=0, padx=30, pady=130)

        self.button4 = tk.Button(self.left_frame, text='Quit')
        self.button4.grid(row=3, column=0, padx=30, pady=60)

    def create_plot(self):
        self.fig = Figure(figsize=(10, 7), dpi=100)
        #t = np.arange(0, 3, .01)
        #self.fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.right_frame)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=0, column=0)


if __name__ == '__main__':
    root = tk.Tk()
    main_app =  MainApplication(root)
    root.mainloop()