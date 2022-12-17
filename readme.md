
## Title: Vehicle Loan Analytics | Visualization Dashboard 📈

## 1. Methodology 🔣
![Methodology](https://i.ibb.co/RggGMPQ/Flowcharts-1.png)

## 2. Description 📚
- This project is developed using Python, Dash, and Plotly. This gives Vehicle Loan Analytics using the dataset LoanPricing.csv available in this repository. The gender option triggers the callback to serve visualization in accordance with the selected option. I hope you guys like it :).
- The dataset contains 34 Features, 18969 tuples for Vehicle Loan Analytics.

## 3. Input / Output 💻
The input to the application is a dropdown for gender, according to the dataset this field is generated. Upon selection the callback gets triggered and updates the Dashboard in real time.
- Dropdown: Selection of Gender. Example: Female, Male.
- Output: We get 4 different visualizations on the basis of selected dropdown field of the dataset.

## 4. Live Link 🔗
### The app is now deployed at http://bhavya-dashboard.centralindia.cloudapp.azure.com/

## 5. Screenshots 🖥️
![Data Visualisation Dashboard](https://i.ibb.co/cknwHJC/ss.png)

## 6. How to run the app: 👨🏻‍💻
1. Open the command prompt/terminal.
2. Clone the repo using

        git clone https://github.com/bhavyatyagi/visualization-dashboard.git
    
3. Go to the directory where the program is stored/cloned
4. Type: 

        python3 app.py
        
5. The program will run
6. If it asks for missing libraries then do:

        pip install requirements.txt
    OR      

        pip install dash pandas plotly
    Note: pip3 instead of pip if in case shows command not found.
7. Run the program again via step 4.
