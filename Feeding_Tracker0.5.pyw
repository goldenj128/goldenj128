from tkinter.ttk import *
from tkinter import *
from tkinter import Menu
import tkinter 
import datetime, csv

d = datetime.datetime.now()
DATESTAMP = d.strftime("%m/%d/%y")
TIMESTAMP = d.strftime("%I:%M %p")
SHORT_YEAR = d.strftime("%y")
#file open
f = open("matthew_feeding.txt", "a")

window = Tk()
c1 = tkinter.BooleanVar()

H_VALUES = ('01','02','03','04','05','06','07','08','09','10','11','12')
M_VALUES = ('00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59')
AMPM = ('AM','PM')
OZ_VALUES = (0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0)
MONTHS_OF_YEAR = ('January','Febuary','March','April','May','June','July','August','September','October','November','December')


#set comboboxes to value when program opened
DOM = StringVar(window)
DOM.set(d.day)
MOY = d.strftime("%m")
MOY = int(MOY)
CURR_HOUR1 = StringVar(window)
CURR_HOUR1.set(d.hour)
CURR_MIN1 = StringVar(window)
CURR_MIN1.set(d.minute)
CURR_HOUR2 = StringVar(window)
CURR_HOUR2.set(d.hour)
CURR_MIN2 = StringVar(window)
CURR_MIN2.set(d.minute)

window.title("Feeding Tracker v0.5")
window.geometry('600x400')
window.resizable(0,0)
baby_photo = PhotoImage(file = r"matthew_golden.gif")

#Button Function
def monthindex(MONTH):
	if MONTH in MONTHS_OF_YEAR:
		RESULT = MONTHS_OF_YEAR.index(MONTH)
		RESULT = int(RESULT + 1)
		return(RESULT)

def clicked():
	if c1.get() == True:
		string1 = "Newday-Log Successful! \n" 
		string2 = combo1.get() + " oz. on " + combo2.get() + " " + dayspin.get() + " @ " + hourcombo1.get() + ":" + mincombo1.get() + ampmcombo1.get()
		NEWDAY = (int(dayspin.get()) + 1)
		string3 = " to " + combo2.get() + " " + str(NEWDAY) + " @ " + hourcombo2.get() + ":" + mincombo2.get() + ampmcombo2.get() 
		stringmsg = string1 + string2 + string3
		stringlog = string2 + string3
		msglabel1.configure(text=stringmsg, fg='green')
		f.write(stringlog + "\n")
		MONTH = combo2.get()
		FINAL = monthindex(MONTH)
		FINAL = str(FINAL)
		csvlog = combo1.get() + "," + FINAL + "/" + dayspin.get() + "/" + SHORT_YEAR + "," + hourcombo1.get() + ":" + mincombo1.get() + ampmcombo1.get() + "," + hourcombo2.get() + ":" + mincombo2.get() + ampmcombo2.get() + "," + str(c1.get())
		print(csvlog)
	elif c1.get() == False:
		string1 = "Log Succcessful! \n"
		string2 = combo1.get() + " oz. on " + combo2.get() + " " + dayspin.get() + " @ " + hourcombo1.get() + ":" + mincombo1.get() + ampmcombo1.get() + " to "
		string3 = hourcombo2.get() + ":" + mincombo2.get() + ampmcombo2.get()
		stringmsg = string1 + string2 + string3
		stringlog = string2 + string3
		msglabel1.configure(text=stringmsg, fg="green")
		f.write(stringlog + "\n")
		MONTH = combo2.get()
		FINAL = monthindex(MONTH)
		FINAL = str(FINAL)
		csvlog = combo1.get() + "," + FINAL + "/" + dayspin.get() + "/" + SHORT_YEAR + "," + hourcombo1.get() + ":" + mincombo1.get() + ampmcombo1.get() + "," + hourcombo2.get() + ":" + mincombo2.get() + ampmcombo2.get() + "," + str(c1.get())
		print(csvlog)

def refresh():
	d = datetime.datetime.now()
	DATESTAMP = d.strftime("%d-%b")
	TIMESTAMP = d.strftime("%I:%M %p")
	label2.configure(text=TIMESTAMP, font=('Arial', 20))

def quit():
	f.close()
	window.quit()

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='New Entry (coming soon)')
new_item.add_command(label='Generate Report (coming soon)')
new_item.add_command(label='Exit', command=quit)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

bglabel = Label(window, image=baby_photo)
bglabel.place(x=20,y=0)
label1 = Label(window, text="Matthew S. Golden", font=("Arial Bold", 10))
label1.place(x=10, y=100)
label2 = Label(window, text=TIMESTAMP, font=('Arial', 20))
label2.place(x=10, y=300)
button2 = Button(window, text='Refresh',command=refresh, bg="blue", fg="white", height = 1, width = 7)
button2.place(x=65, y=360)

#textbox1 = Entry(window, width=10, state='normal')
#textbox1.grid(column=0, row=2)

combo1 = Combobox(window, width=5)
combo1['values']= OZ_VALUES
combo1.current(9) # set the selected item
combo1.place(x=20, y=145)
label3 = Label(window, text='Oz. Drank', font=('Arial Bold', 11))
label3.place(x=10, y=120)


label6 = Label(window, text=' ', font=('Arial', 11))
label6.grid(column=0, row=8)
button1 = Button(window, text='ENTER',command=clicked, bg="Green", fg="Lime")
button1.place(x=10, y=360)

label4 = Label(window, text='Month', font=('Arial Bold', 11))
label4.place(x=320, y=120)
label5 = Label(window, text='Day', font=('Arial Bold', 11))
label5.place(x=440, y=120)

dayspin = Spinbox(window, from_=1, to=31, textvariable=DOM, width=5)
dayspin.place(x=440, y=145)
combo2 = Combobox(window, width=12)
combo2['values']= MONTHS_OF_YEAR
combo2.current(MOY - 1)
combo2.place(x=320, y=145)

start_label = Label(window, text='Start Time:', font=('Arial', 15), fg='blue')
start_label.place(x=10, y=200)
end_label = Label(window, text='End Time:', font=('Arial', 15), fg='red')
end_label.place(x=19, y=230)
label6 = Label(window, text='Hour', font=('Arial Bold', 11))
label6.place(x=130, y=170)
label7 = Label(window, text='Min', font=('Arial Bold', 11))
label7.place(x=190, y=170)
#Hour/Min Comboboxes
hourcombo1 = Combobox(window, width=4)
hourcombo1['values'] = H_VALUES
hourcombo1.current(0)
mincombo1 = Combobox(window, width=4)
mincombo1['values'] = M_VALUES
mincombo1.current(0)
ampmcombo1 = Combobox(window, width=4)
ampmcombo1['values'] = AMPM
ampmcombo1.current(0)
hourcombo2 = Combobox(window, width=4)
hourcombo2['values'] = H_VALUES
hourcombo2.current(0)
mincombo2 = Combobox(window, width=4)
mincombo2['values'] = M_VALUES
mincombo2.current(0)
ampmcombo2 = Combobox(window, width=4)
ampmcombo2['values'] = AMPM
ampmcombo2.current(0)
#Hour/Min Comboboxes Placement
hourcombo1.place(x=130, y=205)
hourcombo2.place(x=130, y=235)
mincombo1.place(x=190, y=205)
mincombo2.place(x=190, y=235)
ampmcombo1.place(x=250, y=205)
ampmcombo2.place(x=250, y=235)


chkbx1 = Checkbutton(window, text='New Day', variable=c1)
chkbx1.place(x=20, y=270)

msglabel1 = Label(window, text='',font=('Arial Bold', 8),fg='red')
msglabel1.place(x=280, y=285)

combo2.focus()

window.mainloop()
