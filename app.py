from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('data/sales_data.csv')

@app.route('/')
def home():
    # Basic visualization logic
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True) 
