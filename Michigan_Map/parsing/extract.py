import PyPDF2
import json
import re

def pdf_to_json(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        text_lines = []
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text_lines.extend(page.extract_text().split('\n'))

    # Remove the unwanted lines
    unwanted_lines = [
        "Total Millage for",
        "Principal Residence",
        "or Ag Exemption School DistrictTotal Millage",
        "NonHomesteadTotal Millage for",
        "Principle Residence",
        "or Ag ExemptionTotal Millage",
        "NonHomesteadw/ AdValorem Special Assessment Millage",
        "Total Millage",
        "Commercial",
        "Personal (CPP)TOTAL PROPERTY TAX RATES IN MICHIGA N 2022",
        "Total Millage",
        "Industrial",
        "Personal (IPP)",
    ]

    text_lines = [line for line in text_lines if not line.startswith("Page") and line not in unwanted_lines]

    # Remove numbers after Twp or City using regular expressions
    text_lines = [re.sub(r'(Twp|City)\d+', r'\1', line) for line in text_lines]

    # Keep only the first number in each line
    text_lines = [re.sub(r'(\d+\.\d+).*', r'\1', line) for line in text_lines]

    # Create a dictionary with text as a list of lines
    pdf_data = {'text': text_lines}

    # Write the extracted data to a JSON file
    with open('parsing/output.json', 'w') as json_file:
        json.dump(pdf_data, json_file, indent=2)

# Path to your PDF file
pdf_file_path = 'parsing/2022_rate.pdf'

# Call the function with the PDF file path
pdf_to_json(pdf_file_path)
