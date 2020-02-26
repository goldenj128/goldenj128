from tkinter.ttk import *
from tkinter import *
from tkinter import Menu
from tkinter import filedialog
import datetime, csv, math, time, configparser

window = Tk()

window.title("Main Program")
window.geometry('600x500')
#window.iconbitmap('money.gif')
pgrmclock = datetime.datetime.now()

'''
config = configparser.ConfigParser()
with open (window.fileName, newline="") as csvfile:
	mainreader = csv.reader(csvfile, delimiter=",")
	for row in mainreader:
		print(row)
'''

#Variables
TOTALDEBT = 0.00
TEMPLIST = []
BILL_LIST = []
BILL_VALUE = []
BILL_NAME = " "
fields = []
rows = []
billdept = []
DAYS = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'] 
MONTHS = ['1','2','3','4','5','6','7','8','9','10','11','12']
YEARS = ['2020','2021','2022','2023','2024','2025','2026','2027','2028']
radioselection1 = IntVar()
contenta = StringVar()
contentb = StringVar()
contentc = DoubleVar()
radioselection1.set(1)

#Program Function(s)
def editbtn():
	try:
		global TEMPLIST
		curItem = billtable.focus()
		#print(billtable.item(curItem))
		#content.set(billtable.item(curItem))
		savebutton["state"] = NORMAL
		cancelbutton["state"] = NORMAL
		editbutton["state"] = DISABLED
		addbutton["state"] = DISABLED
		removebutton["state"] = DISABLED
		tempdict = (billtable.item(curItem))
		templist = tempdict['values']
		tempname = str(templist[0])
		tempnum = str(templist[1])
		contenta.set(tempnum)
		contentb.set(tempname)
		templist[1] = float(templist[1])
		TEMPLIST = templist.copy()
	except IndexError:
		print("No row selected")
		savebutton["state"] = DISABLED
		cancelbutton["state"] = DISABLED
		editbutton["state"] = NORMAL
		addbutton["state"] = NORMAL
		removebutton["state"] = NORMAL

def savebtn():
	print(radioselection1.get())
	#print(contenta.get())
	q = contenta.get()
	print(contentb.get())
	print(contentc.get())
	print(q)

def cancelbtn():
	savebutton["state"] = DISABLED
	cancelbutton["state"] = DISABLED
	editbutton["state"] = NORMAL
	addbutton["state"] = NORMAL
	removebutton["state"] = NORMAL
	contenta.set('')
	contentb.set('')
	contentc.set(0.0)
	global TEMPLIST
	TEMPLIST = []

def testfn():
	try:
		print(rows)
		global TEMPLIST
		print(TEMPLIST)
		if TEMPLIST in rows:
			print("Yes")
		else:
			print("No")
	except IndexError:
		print("Please upload a data file.")

def viewrows():
	try:
		print(rows)
	except IndexError:
		print("Please upload a data file.")

def refreshconsole():
	global TOTALDEBT
	TTEXT1 = 'Total Debt\n${:.2f}'
	TTEXT2 = 'Total Surplus\n${:.2f}'
	if TOTALDEBT < 0.00:
		debttotal = Label(tab1, text=(TTEXT1.format(TOTALDEBT)), font=("Arial Bold", 12), fg='red')
		debttotal.place(x=355, y=120)
	else:
		debttotal = Label(tab1, text=(TTEXT2.format(TOTALDEBT)), font=("Arial Bold", 10), fg='green')
		debttotal.place(x=350, y=120)

def opencsvfile():
	datafile = filedialog.askopenfilename(filetypes=(("CSV Files", "csv"),))
	with open(datafile, mode='r') as maindata:
		#CSV Reader Object
		dataread = csv.reader(maindata)
		#Uncomment nextline if you have fieldnames
		#fields = dataread.next()
		global TOTALDEBT
		i = 0
		for row in dataread:
			rows.append(row)
			rows[i][1] = float(rows[i][1])
			TOTALDEBT = TOTALDEBT + rows[i][1]
			billtable.insert('',0,values=(rows[i]))
			i = i + 1
		print(str(dataread.line_num) + " row(s) imported successfully")
		refreshconsole()

def openconfig():
	window.inifile = filedialog.askopenfilename(filetypes=(("INI Files", "ini"),))
	config.read(window.inifile)
	for key in config['ALLOTMENTS_CURRENT']:
		BILL_LIST.append(key.upper())
	SURPLUS = config.getfloat('ACCOUNT_CURRENT', 'Surplus')

#mainwindow file menu layout
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Open Data File', command=opencsvfile)
new_item.add_command(label='Open Config File', command=openconfig)
new_item.add_command(label='Save')
new_item.add_command(label='Exit', command=quit)
menu.add_cascade(label='File', menu=new_item)
window.config(menu=menu)

def quit():
	window.quit()

#mainwindow tab layout
tab_control = ttk.Notebook(window)
tab0 = ttk.Frame(tab_control)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab0, text='Allotments')
tab_control.add(tab1, text='Bill Management')
tab_control.pack(expand=1, fill='both')

#TAB1 LAYOUT
financialentry = Entry(tab1, textvariable=contentc, width = 15)
financialentry.place(x=150, y=30)
paymentradio = Radiobutton(tab1, text='PAYMENT', value=1, variable=radioselection1) 
paymentradio.place(x=30, y=20)
debtradio = Radiobutton(tab1, text='DEBT', value=2, variable=radioselection1)
debtradio.place(x=30, y=40)
billnamelabel = Label(tab1, text='Bill Name: ', font=('Arial', 10))
billnamelabel.place(x=160, y=53)
billammountlabel = Label(tab1, text='Bill Ammount: ', font=('Arial', 10))
billammountlabel.place(x=160, y=73)
namelabel = Label(tab1, textvariable=contentb, text=contentb, font=('Arial', 10))
namelabel.place(x=230, y=53)
ammountlabel = Label(tab1, textvariable=contenta, text=contenta, font=('Arial', 10))
ammountlabel.place(x=250, y=73)
MDYlabel = Label(tab1, text='Month:      Day:      Year:', font=('Ariel Bold', 12))
MDYlabel.place(x=365,y=25)
monthselect = Combobox(tab1, values=MONTHS, width=4) 
monthselect.place(x=360,y=50)
dayselect = Combobox(tab1, values=DAYS, width=4) 
dayselect.place(x=420,y=50)
yearselect = Combobox(tab1, values=YEARS, width=4) 
yearselect.place(x=480,y=50)
updatebutton = Button(tab1, text='Refresh',width=7, command=refreshconsole,fg='powder blue', bg='blue')
updatebutton.place(x=20, y=430)
testbutton = Button(tab1, text='Test',width=7, command=testfn, bg='yellow')
testbutton.place(x=85, y=430)
emailbutton = Button(tab1, text="Email", width=7, bg='orange')
emailbutton.place(x=150, y=430)
savebutton = Button(tab1, text='Save', state=DISABLED, width=7, command=savebtn, bg='green', fg='lime')
savebutton.place(x=20, y=70)
cancelbutton = Button(tab1, text='Cancel', state=DISABLED, width=7, command=cancelbtn, bg='red', fg='pink')
cancelbutton.place(x=85, y=70)
editbutton = Button(tab1, text='Edit', width=7, command=editbtn, bg='powder blue')
editbutton.place(x=85, y=330)
addbutton = Button(tab1, text='Add', width=7, bg='lime')
addbutton.place(x=20, y=330)
removebutton = Button(tab1, text='Remove', width=7, bg='pink')
removebutton.place(x=150, y=330)


#Table in Tab1
billtable = ttk.Treeview(tab1, show='headings', selectmode='browse')
billtable.place(x=20,y=100)
billtable['columns'] = ('bill','ammount','date_due')
billtable.column('#0', width=20, minwidth=20, stretch=False)
billtable.column('bill', width=100, minwidth=50, anchor='w')
billtable.column('ammount', width=150, minwidth=50, anchor='w')
billtable.column('date_due', width=75, minwidth=50, anchor='center')
billtable.heading('bill', text='BILL', anchor='w')
billtable.heading('ammount', text='AMMOUNT DUE', anchor='w')
billtable.heading('date_due', text='DATE DUE', anchor='w')
#Row Levels
#billtable.insert('',0,values=('USAA',56.34,'1/12/22'))
#billtable.insert('',1,values=('Netflix',-7.24,'1/08/22'))

#Treeview virtual events are {Select,Open,&Close}
#Use these two methods below to determine the affected item that you are focused on in treeview. 
#Treeview.focus()
#Treeview.selection()

#window.after(1000, updateclock)
window.mainloop()