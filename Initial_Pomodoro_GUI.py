try:
    import tkinter as tk # for Python 3
except:
    import Tkinter as tk # for Python 2.7
    
import time 


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, bg='khaki')
        tk.Label(self, text="Start page", font=('MathJax_SansSerif-Bold', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="README", font=('MathJax_SansSerif-Bold', 18, "bold"),
                  command=lambda: master.switch_frame(READMEPage)).pack(fill='x', pady = 10)
        tk.Button(self, text="START POMODORO", font=('MathJax_SansSerif-Bold', 18, "bold"),
                  command=lambda: master.switch_frame(PomodoroPage)).pack(fill='x', pady = 10)

class READMEPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='brown')
        tk.Label(self, text="README", font=('MathJax_SansSerif-Bold', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        tk.Button(self, text="Go back", font=('MathJax_SansSerif-Bold', 14, "bold"),
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Label(self, text="Here goes the description what this app does.", font=('MathJax_SansSerif-Bold', 18, "bold")).pack(side="top", fill="both")
        tk.Button(self, text="Go back", font=('MathJax_SansSerif-Bold', 14, "bold"),
                  command=lambda: master.switch_frame(StartPage)).pack()

class PomodoroPage(tk.Frame):
    def __init__(self, master):
        
        
        self.Message = "Time to Work"
        
        tk.Frame.__init__(self, master)      
        
        tk.Frame.configure(self,bg='green')
        self.LabelMessage = tk.Label(self, text=self.Message, font=('MathJax_SansSerif-Bold', 18, "bold"))
        
        
        label_font = ('MathJax_SansSerif-Bold', 40)
        self.time_str = tk.StringVar()
        self.LabelTime = tk.Label(self, textvariable=self.time_str, font=label_font, bg='white', 
                 fg='blue', relief='raised', bd=3)
        
        self.StartButton = tk.Button(self, text='Start Pomodoro',  font=('MathJax_SansSerif-Bold', 14, "bold"))
        
        self.PauseButton = tk.Button(self, text='Pause Pomodoro',  font=('MathJax_SansSerif-Bold', 14, "bold"))
        
        self.goBackButton = tk.Button(self, text="Go back", font=('MathJax_SansSerif-Bold', 14, "bold"),
                  command=lambda: master.switch_frame(StartPage))
        
        self.show_widgets()

            
            
            
    def show_widgets(self):
        self.LabelTime.pack(fill='x', padx=5, pady=5)
        self.LabelMessage.pack(side="top", fill="x", pady=5)
        
        self.StartButton.pack(fill='x', pady = 10)
        self.PauseButton.pack(fill='x', pady = 10)
        self.goBackButton.pack(fill='x', pady = 10)

        
if (__name__ == "__main__"):
    app = SampleApp()
    app.mainloop()
