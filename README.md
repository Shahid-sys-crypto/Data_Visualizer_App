# 📊 Data Visualizer App (Python + Tkinter + Pandas + Matplotlib)

A simple desktop **Data Visualizer Application** built using **Python**, **Tkinter**, **Pandas**, and **Matplotlib**.

This application allows users to:
- 📂 Upload CSV or Excel files
- 🔎 Select columns dynamically
- 📈 Plot data visually
- 🖥️ Display graphs inside a GUI window

---

## 🚀 Features

- Upload `.csv` and `.xlsx` files
- Automatically detect columns
- Dynamic X and Y axis selection
- Line graph plotting
- Embedded Matplotlib chart inside Tkinter
- Simple and beginner-friendly interface

---

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- Pandas (Data Processing)
- Matplotlib (Data Visualization)

---

## 📂 Project Structure

Data_Visualizer_App.py
Your_Data_File.csv / .xlsx
README.md


---

## 📄 Supported File Formats

- `.csv`
- `.xlsx`

If another file type is selected, the program will show an error.

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries

```bash
pip install pandas matplotlib openpyxl
openpyxl is required for reading Excel files.

2️⃣ Run the Application
python Data_Visualizer_App.py
The Data Visualizer window will open.

📝 How It Works
🔹 Upload File
Click the Upload button.

Select a .csv or .xlsx file.

🔹 Select Axes
Choose a column for the X-axis.

Choose a column for the Y-axis.

🔹 Plot Data
Click the Plot button.

A graph will appear inside the application window.

🔧 Functions Used in Code
Function	Purpose
load_data(file_path)	Loads CSV or Excel file
plot_data(df, column_x, column_y)	Creates line plot
update_dropdown(columns)	Updates axis selection menus
open_file()	Opens file selection dialog
handle_file_path()	Loads file and updates columns
handle_plot()	Handles plotting logic
📈 How Graph is Created
A Figure object is created using Matplotlib

A subplot is added

Data is plotted using ax.plot()

Graph is embedded in Tkinter using FigureCanvasTkAgg

