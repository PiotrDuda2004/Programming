import COVID19Py
import tkinter as tk
from tkinter import *
import os
                
#################################################################
covid19 = COVID19Py.COVID19()
location = covid19.getLocationByCountryCode('PL')
deaths = location[0]['latest']['deaths']
confirmed = location[0]['latest']['confirmed']
recovered = location[0]['latest']['recovered']
print(covid19.getLatest())
##################################################################



root = Tk()
root.title("CoronaVirusChecker")



f = tk.Frame(root,width=800,height=600)
f.grid(row=0,column=0,sticky="NW")
f.grid_propagate(0)
f.update()

C = tk.Canvas(root, bg="blue", height=250, width=300)

background_label = tk.Label(root,)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

w = tk.Label(root,text="Aktualne dane Covid-19 w Polsce:")
w.place(x=400, y=200, anchor="center")
w.config(font=("Courier", 30))


l = tk.Label(root,text="Przypadki: "+str(confirmed)+"\n"+" Śmierci:"+str(deaths)+"\n"+" Wyleczeni: "+str(recovered))
l.place(x=400, y=300, anchor="center")
l.config(font=("Courier", 30))



root.mainloop()




#
# Piotr Duda
#