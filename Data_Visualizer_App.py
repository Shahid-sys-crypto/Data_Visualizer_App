import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog

def load_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"File type not supported: {file_path} , it should end with .csv or .xlsx")
current_canvas=None

def plot_data(df,column_x,column_y):
    global current_canvas
    fig=Figure(figsize=(6,4),dpi=100)
    ax=fig.add_subplot(111)
    ax.plot(df[column_x],df[column_y],marker='o')
    ax.set_title(f"{column_x} vs {column_y}")
    ax.set_xlabel(column_x)
    ax.set_ylabel(column_y)

    current_canvas=FigureCanvasTkAgg(fig,master=root)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack()

def update_dropdown(columns):
    x_dropdown.set("")
    y_dropdown.set("")
    x_menu["menu"].delete(0,"end")
    y_menu["menu"].delete(0,"end")
    for column in columns:
        x_menu["menu"].add_command(label=column,command=lambda value=column:x_dropdown.set(value))
        y_menu["menu"].add_command(label=column,command=lambda value=column:y_dropdown.set(value))

def open_file():
    file_path=filedialog.askopenfilename(filetypes=[("CSV files","*.csv"),("XLSX files","*.xlsx")])
    print(f"file selected : {file_path}")
    return file_path

def handle_file_path():
    global df
    file_path=open_file()
    try:
        df=load_data(file_path)
        update_dropdown(df.columns)
        print(f"columns available: {df.columns}")
    except Exception as e:
        print(e)

def handle_plot():
    global current_canvas
    if current_canvas:
        current_canvas.get_tk_widget().destroy()
    try:
        column_x=x_dropdown.get()
        column_y=y_dropdown.get()
        if not column_x or not column_y:
            print("please select both X and Y axes")
            return
        plot_data(df,column_x,column_y)
    except Exception as e:
        print(e)




root=tk.Tk()
root.title("Data Visualizer")
root.geometry("800x600")

upload_button=tk.Button(root,text="upload",command=handle_file_path)
upload_button.pack(pady=5)

x_label=tk.Label(root,text="select X Axis")
x_label.pack(pady=5)
x_dropdown=tk.StringVar()
x_menu=tk.OptionMenu(root,x_dropdown,[])
x_menu.pack(pady=5)

y_label=tk.Label(root,text="select Y Axis")
y_label.pack(pady=5)
y_dropdown=tk.StringVar()
y_menu=tk.OptionMenu(root,y_dropdown,[])
y_menu.pack(pady=5)

plot_button=tk.Button(root,text="plot",command=handle_plot)
plot_button.pack(pady=5)

root.mainloop()