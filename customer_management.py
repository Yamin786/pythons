# Hotel Management System
from tkinter import *

root = Tk()



'''def enter_customer_name():
    Label(bill_frame,text=f"Your customer Mr.{customer_name_entry.get()}'s bill bellow: ",font=15).grid(row=1,column=0)

'''
items_price_list = []
def add():
    Label(bill_frame,text=f"Your customer Mr.{customer_name_entry.get()}'s bill bellow: ",font=15,pady=10).grid(row=1,column=0)
    selected_items = [list.get(i) for i in list.curselection()]
    for item in selected_items:
        each_item_price = foods_dict[item]
        items_price_list.append(each_item_price)
    total_cost = sum(items_price_list)
    bill_with_cupon(total_cost)
    Label(bill_frame,text=f"Here is the items Mr.{customer_name_entry.get()} have ordered :\n{selected_items}",pady=5,font=12).grid(row=4,column=0)

def bill_with_cupon(total_cost):
    if radio_selected.get()=="yes":
        Label(bill_frame,text=f"{customer_name_entry.get()} have a cupon with 22% discount ",fg="blue",pady=5).grid(row=2,column=0)
        with_cupon_bill = total_cost - (total_cost*22)/100
        Label(bill_frame,text=f"Total bill with cupon's discount {with_cupon_bill}",font=35,fg="green",pady=10).grid(row=3,column=0)
    else:
        Label(bill_frame,text=f"Total bill with cupon's discount {total_cost}",font=35,fg="green",pady=10).grid(row=3,column=0)

logo_frame = Frame(root)
logo_frame.grid(row=0,column=0)
Label(logo_frame,text="Welcome to Yamin's Cafe ",font=30,bg="blue",fg="white",height=5,width=35).pack()

entry_frame = Frame(root)
entry_frame.grid(row=1,column=0, pady=10)
Label(entry_frame,text="Customer's Name ",font=15).grid(row=0,column=0,)
customer_name_entry = Entry(entry_frame,font=15)
customer_name_entry.grid(row=0,column=1)
#Button(entry_frame,text="submit",command=enter_customer_name,font=12).grid(row=1,column=0,columnspan=2,pady=5)



cupon_frame = Frame(root)
cupon_frame.grid(row=2,column=0,pady=20)
radio_selected = StringVar()
radio_selected.set("no")
Label(cupon_frame,text="Do you have the cupon ??",font=20).grid(row=0,column=0,pady=10)
Radiobutton(cupon_frame,text="Yes I have the Cupon card ",variable=radio_selected,value="yes").grid(row=1,column=0,padx=20)
Radiobutton(cupon_frame,text="No I don't have the Cupon card ",variable=radio_selected,value="no").grid(row=1,column=1,padx=20)



ordered_frame = Frame(root)
ordered_frame.grid(row=3,column=0,pady=30)
foods_dict = {
    "pizza":150,
    "pasta":100,
    "burger":200,
    "sandwitch":200,
    "hotdog":150,
    "kabab":250,
    "nan-grill":250,
    "biriyani":300
}
Label(ordered_frame,text="Select the foods below customer have ordered : ",font=20).pack()
foods_list = ["pizza","pasta","burger","sandwitch","hotdog","kabab","nan-grill","biriyani"]
list = Listbox(ordered_frame,selectmode='multiple',
               font=15)
for item in foods_list:
    list.insert(END,item)
list.config(height=list.size(),cursor='hand2')
list.pack()
Button(ordered_frame,text="submit",font=12,command=add).pack()



bill_frame = Frame(root)
bill_frame.grid(row=0,column=1)
Label(bill_frame,text="Here is customers bill : ",font=30,bg="green",fg="white",height=5,width=35).grid(row=0,column=0)








root.mainloop()