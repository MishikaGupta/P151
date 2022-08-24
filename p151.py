# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:36:00 2022

@author: Beautiful Mishika
"""

from tkinter import *
import random 

label_month =  Label(root)
label_profit = Label(root)
label_minimum_profit= Label(root)
label_maximum_profit = Label(root)

month = ("January", "February" , "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (20000,45000,78000,97000,12000,6000,65000,54000,80300,30000,70000,90000)

label_month["text"] = "month" + str(month)

label_profit["text"] = "profits" + str(profits)

def maxProfit() :
    
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    print(max_profit_index)

    max_profit_month = month[max_profit_index]
    print("The maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month))

    label_maximum_profit["text"] = "The maximum profit of " + str((max_profit) + " was recorded in the month of " + str(max_profit_month)

def minProfit() :
                                                                      
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    print(min_profit_index)

    min_profit_month = month[min_profit_index]
    print("The minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month))

    label_minimum_profit["text"] = "The minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month)

btn_max= Button(root, text=Maximum Profit, command=maxProfit)
btn_min = Button(root, text=Minimum Profit, command=minProfit)

label_month.place(relx=0.5, rely=0.2, anchor=CENTER)
label_profit.place(relx=0.5, rely=0.3, anchor=CENTER)
label_minimum_profit.place(relx=0.5, rely=0.5, anchor=CENTER)
label_maximum_profit.place(relx=0.5, rely=0.6, anchor=CENTER)
btn_max.place(relx=0.5, rely=0.7, anchor=CENTER)
btn_min.place(relx=0.6, rely=0.7, anchor=CENTER)

root.mainloop()