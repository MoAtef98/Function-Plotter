"""
Info : Simple GUI to plot input function from the user

Creator : Mohamed Atef Helal

"""
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import tkinter as GUI


def exit_app():
    """ a function to exit the GUI window"""
    main_window.quit()

def plot_equation():
    """ a function to get parameters value from entry boxes and plot the function"""
    a  = int(entery_a.get())
    b  = int(entery_b.get())
    c  = int(entery_c.get())
    d  = int(entery_d.get())
    min_x= int(entery_min.get())
    max_x= int(entery_max.get())
        
    if min_x > max_x :
        messagebox.showerror("Error","Max x must be bigger than Min x")
    else :
        x = np.arange(min_x,max_x,1)
        y = a*(x**3)+b*(x**2)+c*x+d  
        plt.plot(x,y)
        plt.title("Function Plotting")
        plt.xlabel("Values of x")
        plt.ylabel("Values of y")
        plt.show()
        


# Creating a GUI Window called main_window
main_window = GUI.Tk()

#Give some options to the window
main_window.title("Function Plotter")
main_window.geometry("515x300+450+150")
main_window.resizable(False,False)
main_window.configure(background="darkcyan")

#**********************Creating labels of the window***********************************

label_function_shape = GUI.Label(main_window,text="Main Equation :   a*(x^3)+b*(x^2)+c*x+d",background="lavender",font="arial")
label_note=GUI.Label(main_window,text="Please Enter your function parameters below.They must be decimal values",background="orange",font="arial")

label_a  =GUI.Label(main_window,text="a",background="gold",font="arial")
label_b  =GUI.Label(main_window,text="b",background="gold",font="arial")
label_c  =GUI.Label(main_window,text="c",background="gold",font="arial")
label_d  =GUI.Label(main_window,text="d",background="gold",font="arial")
label_max=GUI.Label(main_window,text="Max x ",background="greenyellow",font="arial")
label_min=GUI.Label(main_window,text="Min x ",background="coral",font="arial")


#************************Creating entery boxes of the window******************************************

entery_a  =GUI.Entry(main_window,width=3,font="arial",background="plum")
entery_b  =GUI.Entry(main_window,width=3,font="arial",background="plum")
entery_c  =GUI.Entry(main_window,width=3,font="arial",background="plum")
entery_d  =GUI.Entry(main_window,width=3,font="arial",background="plum")
entery_max=GUI.Entry(main_window,width=5,font="arial",background="peru")
entery_min=GUI.Entry(main_window,width=5,font="arial",background="peru")

#*************************Creating two buttons of the window************************************************

plot_button = GUI.Button(main_window,text="Plot",command=plot_equation,activebackground="green",background="green",font="arial")
exit_button = GUI.Button(main_window,text="Exit",command=exit_app,activebackground="red",background="red",font="arial")


#************************Give a location for every wedgiet on the main_window ********************************
#Labels
label_function_shape.place(x=95,y=20)
label_note.place(x=0,y=70)
label_a.place(x=55,y=120)
label_b.place(x=155,y=120)
label_c.place(x=255,y=120)
label_d.place(x=355,y=120)
label_min.place(x=115,y=180)
label_max.place(x=235,y=180)
#Entry boxes 
entery_a.place(x=85,y=120)
entery_b.place(x=175,y=120)
entery_c.place(x=275,y=120)
entery_d.place(x=375,y=120)
entery_min.place(x=168,y=180)
entery_max.place(x=291,y=180)
#buttons 
plot_button.place(x=135,y=260)
exit_button.place(x=295,y=260)


main_window.mainloop()














