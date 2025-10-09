import PyPDF2
import os

#первые три тетради отдельно тупо удобнее прочитать
pdf_files = [
    "Рабочая тетрадь № 1.pdf",
    "Рабочая тетрадь № 2.pdf",
    "Рабочая тетрадь № 3.pdf"
]

pdf_dir = "docs"

for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_dir, pdf_file)
    print(f"\n{'='*80}")
    print(f"Читаю: {pdf_file}")
    print('='*80)
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            print(f"Количество страниц: {num_pages}\n")
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                print(f"\n--- Страница {page_num + 1} ---")
                print(text)
    except Exception as e:
        print(f"Ошибка при чтении {pdf_file}: {e}")


