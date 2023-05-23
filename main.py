from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from tabula import read_pdf
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
app.config.from_pyfile("config.py")
db = SQLAlchemy(app)

class BalanceSheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    value = db.Column(db.Float, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if not file.filename.lower().endswith('.pdf'):
            flash('File is not a PDF')
            return redirect(request.url)
        
        try:
            # Extract tables from PDF using Tabula
            tables = read_pdf(file, pages='all')

            # Iterate over tables and store in database
            for table in tables:
                for index, row in table.iterrows():
                    if not pd.isnull(row[0]) and not pd.isnull(row[1]):
                        try:
                            bs = BalanceSheet(title=row[0], value=float(row[1]))
                            db.session.add(bs)
                        except ValueError:
                            flash('Invalid data in PDF')
                            return redirect(request.url)
            db.session.commit()
        except Exception as e:
            flash('Error processing PDF')
            return redirect(request.url)

        flash('File processed successfully')
        return redirect(url_for('visualization'))
    
    return render_template('upload.html')

@app.route('/visualization')
def visualization():
    # Query data from database
    data = BalanceSheet.query.all()

    # Create a DataFrame from the data
    df = pd.DataFrame([(d.title, d.value) for d in data], columns=['Title', 'Value'])

    # Plot the data
    plt.figure(figsize=(10,6))
    plt.bar(df['Title'], df['Value'])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('static/plot.png')

    return render_template('visualization.html')

if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)
