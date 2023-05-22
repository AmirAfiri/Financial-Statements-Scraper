import pandas as pd
import pdfplumber
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Function to extract text from pdf
def extract_text_from_pdf(file):
    pdf = pdfplumber.open(file)
    page = pdf.pages[0]
    text = page.extract_text()
    pdf.close()
    return text

# Connect to your database
engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')

# Iterate over your pdf files
for file in ['file1.pdf', 'file2.pdf', 'file3.pdf']:
    text = extract_text_from_pdf(file)
    lines = text.split('\n')
    
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['Title', 'Value'])
    
    # Logic to extract balance sheet values from the lines and store in DataFrame
    # This will highly depend on your PDF structure, you will need to customize this
    for line in lines:
        if 'balance sheet' in line.lower():
            title, value = line.split(':')  # assuming each line is "title: value"
            df = df.append({'Title': title, 'Value': float(value)}, ignore_index=True)
            
    # Save DataFrame to SQL
    df.to_sql('balance_sheet', engine, if_exists='append')

# Query data from SQL and plot
df = pd.read_sql_query('SELECT * FROM balance_sheet', engine)
df.plot(kind='bar', x='Title', y='Value')
plt.show()
