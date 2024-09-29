from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values (?)', (task_string ,))    
        list_update()    
        task_field.delete(0, 'end')  
    
def list_update():    
    clear_list()    
    for task in tasks:    
        task_listbox.insert('end', task)  
  
def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:  
            tasks.remove(the_value)    
            list_update()   
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:    
        while(len(tasks) != 0):    
            tasks.pop()    
        the_cursor.execute('delete from tasks')   
        list_update()  
   
def clear_list():   
    task_listbox.delete(0, 'end')  
  
def close():    
    print(tasks)   
    guiWindow.destroy()  
    
def retrieve_database():    
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
   
if __name__ == "__main__":   
    guiWindow = Tk()   
    guiWindow.title("TO-DO LIST APP")  
    guiWindow.geometry("720x450+500+200")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#F5F5F5")  
   
    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  
    
    tasks = []  
    
    functions_frame = Frame(guiWindow, bg = "#D3D3D3")  
    functions_frame.pack(side = "top", expand = True, fill = "both")  
 
    task_label = Label(functions_frame, text="TO-DO-LIST \n Enter Your Tasks:",  
        font=("Arial", "14", "bold"),  
        background="#A9A9A9",  
        foreground="#000000"   
    )    
    task_label.place(x = 20, y = 30)  
    
    task_field = Entry(  
        functions_frame,  
        font=("Arial", "14"),  
        width=42,  
        foreground="black",
        background="white",  
    )    
    task_field.place(x = 220, y = 30)  
    
    add_button = Button(  
        functions_frame,  
        text="ENTER",  
        width=15,
        bg='#32CD32',  
        fg='black',
        font=("Arial", "14", "bold"),
        command=add_task,  
    )  
    del_button = Button(  
        functions_frame,  
        text="DELETE",  
        width=15,
        bg='#FF6347',  
        fg='white',
        font=("Arial", "14", "bold"),
        command=delete_task,  
    )  
    del_all_button = Button(  
        functions_frame,  
        text="DELETE ALL",  
        width=15,
        font=("Arial", "14", "bold"),
        bg='#FF4500',  
        fg='white',
        command=delete_all_tasks  
    )
    
    exit_button = Button(  
        functions_frame,  
        text="Exit / Close",  
        width=52,
        bg='#B22222',  
        fg='white',
        font=("Arial", "14", "bold"),
        command=close  
    )    
    add_button.place(x = 18, y = 80,)  
    del_button.place(x = 240, y = 80)  
    del_all_button.place(x = 460, y = 80)  
    exit_button.place(x = 17, y = 380)  
    
    task_listbox = Listbox(  
        functions_frame,  
        width=70,  
        height=9,  
        font=("Arial", "12", "bold"),
        selectmode='SINGLE',  
        background="white",
        foreground="black",    
        selectbackground="#4682B4",  
        selectforeground="white"  
    )    
    task_listbox.place(x = 17, y = 140)  
    
    retrieve_database()  
    list_update()    
    guiWindow.mainloop()    
    the_connection.commit()  
    the_cursor.close()  
