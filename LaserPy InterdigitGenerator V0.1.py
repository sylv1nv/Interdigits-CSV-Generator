#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from os import path 
from tkinter import Menu


def main():

    def restart_program():
        window.destroy()
        main()

    class points:
        cutHx0=[]
        cutHy0=[]
        cutHx1=[]
        cutHy1=[]
        cutVx0=[]
        cutVy0=[]
        cutVx1=[]
        cutVy1=[]


    def plot_result():
            #Plotting generated interdigits
            plt.plot([points.cutHx0,points.cutHx1],[points.cutHy0,points.cutHy1],'b-')
            plt.plot([points.cutVx0,points.cutVx1],[points.cutVy0,points.cutVy1],'b-')
            plt.show()          
   

    def About():
            messagebox.showinfo("About: Contact","GitHub: sylv1nv\nTwitter: @sylv1n_v\nVersion: 1.0\n\nMade with <3 by Sylvain V.")


    def digits_generator():
            startPointx = x0.get()
            startPointy = int(y0.get())
            digitsLenght = int(lenght.get())
            digitsHeight = int(height.get())
            safeCut = int(safecut.get())
            nbDigits = int(digits.get())
            hDigit = int(digitsHeight/(2*nbDigits))
            nbcutH = int(2*nbDigits+1)
            nbcutV = int(2*nbDigits)

            #X Vertical Cut
            for i in range(nbcutV):
                if i%2 == 0:
                    points.cutVx0.append(startPointx+digitsLenght)
                    points.cutVx1.append(startPointx+digitsLenght)
                else:
                    points.cutVx0.append(startPointx)
                    points.cutVx1.append(startPointx)

            #Y Vertical Cut
            for i in range(nbcutV):
                if i%2 == 0:
                    points.cutVy0.append(startPointy+i*hDigit-safeCut)
                    points.cutVy1.append(startPointy+i*hDigit+hDigit+safeCut)
                else:
                    points.cutVy0.append(startPointy+i*hDigit-safeCut)
                    points.cutVy1.append(startPointy+i*hDigit+hDigit+safeCut)

            #X0 Horizontal Cut
            for i in range(nbcutH):
                if i%2 == 0:
                    points.cutHx0.append(startPointx-safeCut)
                else:
                    points.cutHx0.append(startPointx+digitsLenght+safeCut)

            #X1 Horizontal Cut 
            for i in range(nbcutH):
                if i%2 == 0:
                    points.cutHx1.append(startPointx+digitsLenght+safeCut)
                else:
                    points.cutHx1.append(startPointx-safeCut)
            #Y0
            points.cutHy0.append(startPointy)
            for i in range(nbcutV):
                cuty0=startPointy+i*hDigit+hDigit
                points.cutHy0.append(cuty0)

            #Y1
            points.cutHy1.append(startPointy)
            for i in range(nbcutV):
                cuty1=startPointy+i*hDigit+hDigit
                points.cutHy1.append(cuty1)


            #CSV output
            startType = starting_way.get()
            print("startype = ", startType)
            if startType == "1":
                filename = str(digitsLenght)+'x'+str(digitsHeight)+'_'+str(nbDigits)+'_dgts_'+str(safeCut)+'safeCut_Hstart.csv'
                sys.stdout=open(filename,"w")
                for i in range(nbcutH-1):
                    print(points.cutHx0[i],",",points.cutHy0[i],',0,',points.cutHx1[i],",",points.cutHy1[i],',0')
                    print(points.cutVx0[i],",",points.cutVy0[i],',0,',points.cutVx1[i],",",points.cutVy1[i],',0')
                    
                i = nbcutV
                print(points.cutHx0[i],",",points.cutHy0[i],',0,',points.cutHx1[i],",",points.cutHy1[i],',0')
                sys.stdout.close()
            else:
                filename = str(digitsLenght)+'x'+str(digitsHeight)+'_'+str(nbDigits)+'_dgts_'+str(safeCut)+'safeCut_Vstart.csv'
                sys.stdout=open(filename,"w")
                i = 0
                print(points.cutVx0[i],",",points.cutVy0[i],',0,',points.cutVx1[i],",",points.cutVy1[i],',0')
                for i in range(1,nbcutH-1):
                    print(points.cutHx0[i],",",points.cutHy0[i],',0,',points.cutHx1[i],",",points.cutHy1[i],',0')
                    print(points.cutVx0[i],",",points.cutVy0[i],',0,',points.cutVx1[i],",",points.cutVy1[i],',0')
                sys.stdout.close()



#===========================================================================================================================
#WINDOW

    window = Tk()
    window.resizable(False, False)

    window.title("LaserPy : InterDigits CSV Generator")


    menu_bar = Menu(window)
    menu_bar.add_cascade(label="New", command=restart_program)
    menu_bar.add_cascade(label="Plot", command=plot_result)
    menu_bar.add_cascade(label="About", command=About)

    window.config(menu=menu_bar)


    tk.Label(window, text="LaserPy : InterDigits CSV Generator", fg="black", font = "Verdana 15 bold").grid(row=0, columnspan=6, sticky=N+S+W+E)



    #X0-----------------------------------------------------
    x0 = IntVar()
    Label(window, text ='\tX0 :').grid(row=1, sticky=E)
    x0_entry = Entry(window, textvariable=x0).grid(row=1, column = 1)



    #Y0-----------------------------------------------------
    y0 = IntVar()
    Label(window, text ='\tY0 :').grid(row=2, sticky=E)
    y0_entry = Entry(window, textvariable=y0).grid(row=2, column = 1)


    #Lenght-----------------------------------------------------
    lenght = IntVar()
    Label(window, text ='\tLenght - :').grid(row=1, column=3, sticky=E)
    lenght_entry = Entry(window, textvariable=lenght).grid(row=1, column=4)


    #Height-----------------------------------------------------
    height = IntVar()
    Label(window, text ='\tHeight | :').grid(row=2, column=3, sticky=E)
    height_entry = Entry(window, textvariable=height).grid(row=2, column=4)


    #Digits-----------------------------------------------------
    digits = IntVar()
    Label(window, text='Nb Digits :').grid(row=3, column=0, sticky=E)
    digits_entry = Entry(window, textvariable=digits).grid(row=3, column=1)


    #safeCut-----------------------------------------------------
    safecut = IntVar()
    Label(window, text='\tSafeCut :').grid(row=3, column=3, sticky=E)
    safecut_entry = Entry(window, textvariable=safecut).grid(row=3, column=4)


    #Starting Way-----------------------------------------------------
    starting_way = StringVar()
    Label(window, text ='\tStarting Way\t').grid(row=1, column=5, sticky=W)
    starting_way_H = Radiobutton(window, text="Horizontal", variable=starting_way, value=1).grid(row=2, column=5)
    starting_way_V = Radiobutton(window, text="Vertical", variable=starting_way, value=2).grid(row=3, column=5)




    go_btn = Button(window, text=("Go !"), command=digits_generator).grid(row=4, columnspan=6, sticky=W+E)



    window.mainloop()


main()
