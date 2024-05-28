import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from datetime import datetime

# my modules
from functions import *

options = ['Mpesa','Cash','Bank']
def create_menu(wnd):
    mainmenu = ttb.Menu(wnd)
    wnd.config(menu=mainmenu)

    # Add some options to the menu
    mainmenu.add_command(label="File", command=hello)
    mainmenu.add_command(label="Edit", command=hello)
    mainmenu.add_command(label="View", command=hello)
    mainmenu.add_command(label="Directories", command=hello)
    mainmenu.add_command(label="Tools", command=hello)
    mainmenu.add_command(label="Help", command=hello)



def create_button(wnd):
    buttonframe = ttb.Frame(wnd)
    buttonframe.grid(row=0,column=0,sticky='w')

    trans_but = ttb.Button(buttonframe,text='Transactions')
    trans_but.grid(row=0,column=0,padx=5,pady=5,rowspan=2,sticky='w')
    acc_but = ttb.Button(buttonframe,text='Accounts')
    acc_but.grid(row=0,column=1,padx=5,pady=5,rowspan=2,sticky='nw')
    categ_but = ttb.Button(buttonframe,text='Categories')
    categ_but.grid(row=0,column=2,padx=5,pady=5,rowspan=2,sticky='nw')
    rep_but = ttb.Button(buttonframe,text='Reports')
    rep_but.grid(row=0,column=3,padx=5,pady=5,rowspan=2,sticky='nw')

def create_date(wnd):
    dt_frame = ttb.Frame(wnd)
    dt_frame.grid(row=1,column=0,sticky='w')
    acc_lbl = ttb.Label(dt_frame,text="ACCOUNTS")
    acc_lbl.grid(row=0,column=0)

    #selector = ttb.OptionMenu(dt_frame,*options)
    #selector.grid(row=0,column=1)
    
    my_datep = ttb.DateEntry(dt_frame,bootstyle='warning',firstweekday=6, startdate=  datetime.today())#(2023,11,1))
    my_datep.grid(row=0,column=2,sticky='w')



def create_tree(wnd):
    treeframe = ttb.Frame(wnd)
    treeframe.grid(row=2,column=1,sticky='nw')

    my_tree = ttb.Treeview(treeframe,
                        bootstyle='success',
                        show='headings')

    my_tree.grid(row=0,column=0,sticky='w')

    my_tree['columns'] = ('Name',"Date","Amount",'Category','Family Member')

    my_tree.column('0', width=120, minwidth=25,stretch=20)
    my_tree.column('Name', width=120, minwidth=25, anchor=W)
    my_tree.column('Date', width=120, minwidth=25,anchor=CENTER)
    my_tree.column('Amount', width=120, minwidth=25,anchor=W)
    my_tree.column('Category', width=120, minwidth=25,anchor=W)
    my_tree.column('Family Member', width=120, minwidth=25,anchor=W)

    my_tree.heading('0',text='Label',anchor=E)
    my_tree.heading('Name', text = 'Description',anchor=W)
    my_tree.heading('Date', text = 'Date',anchor=CENTER)
    my_tree.heading('Amount', text = 'Amount', anchor=W)
    my_tree.heading('Category', text = 'T_Category', anchor=W)
    my_tree.heading('Family Member', text = 'Family Member', anchor=W)

    my_tree.insert(parent='',index='end', iid=1, text='Parent',values=("INCOME","",'','',''))
    my_tree.insert(parent='',index='end', iid=2, text='Parent',values=("","",'','',''))
    my_tree.insert(parent='',index='end', iid=3, text='Parent',values=("EXPENSE","",'','',''))


    # Add Child
    my_tree.insert(parent='1',index='end', iid=4, text='Child',values=("Photocopy",str(datetime.now()),'Python','mpesa','Try'),)
    my_tree.insert(parent='3',index='end', iid=5, text='Parent',values=("Mbs Purchase",str(datetime.now()),'Python','mpesa','Try'))

def accgridder(wnd):
    accframe = ttb.Frame(wnd,width=5)
    accframe.grid(row=2,column=0,sticky='nw',padx=1,pady=1)
    allacc = ttb.Label(accframe,text='All Accounts')
    allacc.grid(row=21,column=0)
    ovrbal = ttb.Label(accframe,text='Overall Balance')
    ovrbal.grid(row=1,column=0)
