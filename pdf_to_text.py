import os
import PyPDF2

def pdf_to_text(pdf_path, txt_path):
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return
    
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        with open(txt_path, 'w', encoding='utf-8') as text_file:
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    text_file.write(text)
                    text_file.write("\n\n")
    # print("done")

pdf_path = r'C:\Users\pooja\Wingify\data\blood_sample_report.pdf'
txt_path = r'C:\Users\pooja\Wingify\data\blood_test_report.txt'
pdf_to_text(pdf_path, txt_path)
