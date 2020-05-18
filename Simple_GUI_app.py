import tkinter
from tkinter import messagebox

# Callback function
def do_something():
	'''
	the following line of code show messagebox
	'''
	messagebox.showinfo(title = 'Response', message = 'You have clicked the button')

# Main window with a button
def Do_Something_Button():
	'''
	Create a root window

	# create button 
	# add one more configuration option
	# command = yourCallBackFunctionName
	'''
	root = tkinter.Tk()

	button = tkinter.Button(root, text = "Click me", command = do_something)
	button.pack()
	
	# Call the event loop
	root.mainloop()

# Executing a program upon entering a program
# i.e., "__main__" 
if (__name__ == "__main__"):
	Do_Something_Button()
