
# Temperature Data Analysis Project   

This project focuses on **temperature data analysis** using **Machine Learning (TensorFlow/Keras)**, with a **Flask-based model** and a **Django web application** for interactive dashboards.  
The Temperature Data Analysis Project is a Python-based web application that uses machine learning and data visualization to study temperature patterns. It integrates TensorFlow for model building, Flask for serving the model, and Django for creating an interactive web interface where users can view state-wise analysis, trend reports, and dashboards.


## Prerequisites  

1. **Install Python 3.10 or Higher**  
   - Download from: [Python Downloads](https://www.python.org/downloads/)  
   - During installation, ensure ✅ **Add Python to PATH** is checked.  
   - Verify installation:  
    In command prompt:python --version

2. **Install IDE (Visual Studio Code recommended)**  
   - Download: [Visual Studio Code](https://code.visualstudio.com/)  



## Required Packages / Libraries  

Open your terminal or command prompt and install the required packages.  

**1. Model Building (TensorFlow/Keras)**

pip install tensorflow matplotlib numpy

**2. Flask Web Application**
pip install flask pillow

**3. Django Project with TensorFlow Model Integration**
pip install django      

## Project Setup

1.Create a folder named DESCRIPTIVE_ANALYSIS**
2.Clone this repository into the folder:** 

## To Run the Django Application

**Run initial migrations:**
In terminal(visual studio code): python manage.py migrate

**Start the development server:**
In terminal(visual studio code): python manage.py runserver

**Open a browser and visit:**
http://127.0.0.1:8000/

**State-wise Temperature Analysis**
http://127.0.0.1:8000/temperature_by_state/

**Temperature Trend Analysis (Year-Month)**
http://127.0.0.1:8000/temperature_trend/

**Dashboard**
http://127.0.0.1:8000/dashboard/   


