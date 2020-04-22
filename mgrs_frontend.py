#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:07:23 2020

@author: nicksclater1
"""

import tkinter as tk
import mgrs_backend
import numpy as np


window = tk.Tk()

mgrS = tk.StringVar()
result = tk.StringVar()
var = tk.IntVar()
var.set(1)


window.geometry('400x180')
window.resizable(False, False)
window.title('Co-ordinate Conversion Tool')



def cycle_RB(event):
    var.set(np.mod((var.get() + 1), 3))
    
    
def convert_pos(event):
    
    contents = mgrS.get()
    ddxdd = mgrs_backend.convert_mgrs_ddxdd(contents)
    
    request = var.get()
    if request == 0:
        if isinstance(ddxdd, tuple):
            res = np.round(ddxdd, 4)
            print(res[0])
            res = str(res[0]) + '  ' + str(res[1])
            result.set(res)
            ent1.config(bg='lime')
            
        else:
            result.set(ddxdd)
            ent1.config(bg='pink')
        
    elif request == 1:
        if isinstance(ddxdd, tuple):
            res = mgrs_backend.convert_ddxdd_ddmm(ddxdd)
            res = str(res[0]) + '  ' + str(res[1])
            result.set(res)
            ent1.config(bg='lime')
            
        else:
            result.set(ddxdd)
            ent1.config(bg='pink') 
    
    else:
        if isinstance(ddxdd, tuple):
            res = mgrs_backend.convert_ddxdd_ddmmss(ddxdd)
            res = str(res[0]) + '  ' + str(res[1])
            result.set(res)
            ent1.config(bg='lime')
            
        else:
            result.set(ddxdd)
            ent1.config(bg='pink')
        

window.bind('<Return>', convert_pos)
window.bind('<Shift_L>', cycle_RB)



label1 = tk.Label(window, font=('arial', 19), text='Co-ordinate Conversion Tool', padx=10, pady=5)
label1.grid(row=0, column=0, columnspan=3)

label2 = tk.Label(window, font=('arial', 17), text='Enter MGRS', padx=5, pady=5)
label2.grid(row=1, column=0)

tk.Radiobutton(window, text='DEG', variable=var, value=0, pady=5, font=('arial', 12)).grid(row=2, column=0, sticky='W')
tk.Radiobutton(window, text='DM', variable=var, value=1, pady=5, font=('arial', 12)).grid(row=3, column=0, sticky='W')
tk.Radiobutton(window, text='DMS', variable=var, value=2, pady=5, font=('arial', 12)).grid(row=4, column=0, sticky='W')


ent1 = tk.Entry(window, textvariable=mgrS, font=('arial', 20), just='center')
ent1.grid(row=1,column=1)

label5 = tk.Label(window, font=('arial', 20), textvariable=result, padx=10, pady=5)
label5.grid(row=3, column=1)


# btn1 = tk.Button(window, text='Convert', command=convert_pos)
# btn1.grid(row=4, column=0, columnspan=2)





window.mainloop()
