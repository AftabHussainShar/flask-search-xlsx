from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the Excel file into a DataFrame
df = pd.read_excel('data.xlsx')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    roll_number = request.form['roll_number']
    result = df[df['Roll Number'] == int(roll_number)]
    
    if result.empty:
        return f"No data found for Roll Number: {roll_number}"
    else:
        return render_template('results.html', tables=[result.to_html(classes='data')], titles=result.columns.values)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7777)
