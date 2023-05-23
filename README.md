# FinancialStatementsScraper
Simple tool extracting data from financial statements in a PDF format, transferring the balance sheet values into a database, and transforming the data into charts and tables.

Tools used : Python libraries such as PyPDF2 or PDFPlumber to extract text from the PDFs, Pandas for data manipulation, SQLalchemy for database operations, and Matplotlib for plotting. With the Flask application provided, the user can upload a PDF file from their local computer directly through the web interface


Install the required libraries using pip:
pip install flask flask_sqlalchemy tabula-py matplotlib pandas
