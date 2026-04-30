# Task 2 - Automated Report Generation

Overview
This project is part of Task 2 for my internship.  
It reads text data from a file (`information.txt`), analyzes the content, and generates a PDF report using the **FPDF** library.

The PDF report includes:
- Word count
- Character count
- Line count
- Longest word
- Shortest word
- Original file content

Requirements
- Python 3.x
- FPDF library

how to run
1. Clone or download this repository.
2. Install the required library:
   ```bash
   pip install -r requirements.txt

   - Make sure information.txt contains some text.
- Run the script:
python report.py
- The output will be saved as output.pdf.
Files- report.py → Python script for reading, analyzing, and generating PDF.
- information.txt → Input text file.
- output.pdf → Generated PDF report.
- requirements.txt → Dependencies list.
- README.md → Documentation.
ExampleIf information.txt contains:hi hello how are you i am fine
The PDF will show:- Word Count: 7
- Character Count: 29
- Line Count: 1
- Longest Word: hello
- Shortest Word: hi
Deliverables- Python script (report.py)
- Input file (information.txt)
- Generated PDF (output.pdf)
- Documentation (README.md)
- Dependencies (requirements.txt)
