import PySimpleGUI as sg
import time

layout = [[sg.Text("this is a text")]]

# Create the window
window = sg.Window("Cube System v4.0", layout=[[]], margins=(500, 250))

time.sleep(5)

# Create an event loop
#while True:
 #   event, values = window.read()
    # End program if user closes window or
    # presses the OK button
  #  if event == "OK" or event == sg.WIN_CLOSED:
   #     break

window.close()