import PySimpleGUI as sg
from core import *

def add_window():
    db = create_connect()
    layout = [[sg.Text("Add Customer")],
              [sg.Text("Id            :"), sg.Input(size=(20,20))],
              [sg.Text("Name          :"), sg.Input(size=(20,20))],
              [sg.Text("Address       :"), sg.Input(size=(20,20))],
              [sg.Text("Item          :"), sg.Input(size=(20,20))],
              [sg.Text("Amount        :"), sg.Input(size=(20,20))],
              [sg.Text("Unit Price    :"), sg.Input(size=(20,20))],
              [sg.Text("Total Price   :"), sg.Input(size=(20,20))],
              [sg.Button("Add",key="addbutton",size=(20, 1))],
              [sg.Text("",key="errtext")]
              ]
    window = sg.Window("Add Customer", layout, modal=True,element_justification="center")
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "addbutton":
            try:
                id = values[0]
                name = values[1]
                address = values[2]
                item = values[3]
                amount = values[4]
                uprice = values[5]
                tprice = values[6]
                insert_data(db,id,name,address,item,amount,uprice,tprice)
            
            except sql.IntegrityError:
                window["errtext"].update("Please use input fields accordingly!")
        
        
    window.close()
    
def delete_window():
    db = create_connect()
    layout = [[sg.Text("Delete Customer")],
              [sg.Text("Id              :"), sg.Input(size=(20,20))],
              [sg.Button("Delete",key="delbutton",size=(20, 1))],
              [sg.Text("",key="errtext")]
              ]
    window = sg.Window("Delete Customer", layout, modal=True,element_justification="center")
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "delbutton":
            try:
                id = int(values[0])
                delete_data(db,id)
            except ValueError:
                window["errtext"].update("Please use input fields accordingly!")
        
        
    window.close()

def update_table(window):
    window["errtext"].update("")
    db = create_connect()
    table = get_posts(db)
    values = table.values.tolist()
    window.Element("table").update(values=values)


def main():
    db = create_connect()
    table = get_posts(db)
    headers = {"Id":[], "Name":[], "Address":[], "Item":[], "Amount":[], "Unit Price":[], "Total Price":[],}
    headings = list(headers)
    dtvalues = table.values.tolist()
    sg.theme("DarkBlue3")
    sg.set_options(font=("Courier New", 16))
    layout = [[sg.Table(values = dtvalues, headings = headings, justification="center", auto_size_columns=False, col_widths=(5,20,20,20,10,15,15),key="table",enable_events=True,select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
              [sg.Button("Add Customer",key="add"),sg.Button("Delete Customer with ID",key="del"),sg.Button("Delete Selected Customer",key="delsel")],
              [sg.Text("",key="errtext")]
             
             ]
    window = sg.Window('Customers',  layout,element_justification="center")
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
        elif event == "add":
            add_window()
            update_table(window)
            
        elif event == "del":
            delete_window()
            update_table(window)
        
        elif event == "delsel":
            try:
                selectedid = [values["table"][0]]
                delete_data(db,selectedid[0]+1)
                update_table(window)
            except IndexError:
                window["errtext"].update("Please select an entry")
            
    window.close()

if __name__ == "__main__":
    main()