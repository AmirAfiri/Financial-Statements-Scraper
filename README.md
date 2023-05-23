# FinancialStatementsScraper

FinancialStatementsScraper is a powerful tool that extracts data from financial statements in PDF format, transfers the balance sheet values into a database, and transforms the data into informative charts and tables for better understanding and analysis.

## Features

- **PDF Data Extraction**: Extracts crucial data from financial statements in PDF format.
- **Data Transfer**: Effortlessly transfers balance sheet values into a database.
- **Data Visualization**: Transforms raw data into visually appealing charts and tables.

## Tools Used

FinancialStatementsScraper is developed using Python, and it leverages the following libraries for various functionalities:

- **PDF Parsing**: Uses libraries such as [PyPDF2](https://pypi.org/project/PyPDF2/) or [PDFPlumber](https://github.com/jsvine/pdfplumber) to extract text from the PDFs.
- **Data Manipulation**: Utilizes [Pandas](https://pandas.pydata.org/) for efficient data cleaning and manipulation.
- **Database Operations**: Employs [SQLAlchemy](https://www.sqlalchemy.org/) for ORM-based database operations.
- **Data Visualization**: Applies [Matplotlib](https://matplotlib.org/) for creating insightful plots and charts.
- **Web Interface**: Incorporates a [Flask](https://flask.palletsprojects.com/) application, allowing users to upload a PDF file directly through the web interface.

## Installation & Usage

To use FinancialStatementsScraper, ensure you have Python installed on your machine. Then, you can install the required libraries using pip:

```pip install flask flask_sqlalchemy tabula-py matplotlib pandas```

After installing the dependencies, you can run the Flask application, upload the PDF file from your local computer via the web interface, and start analyzing the data visualized in charts and tables.

## License

This project is licensed under the terms of the MIT license.
