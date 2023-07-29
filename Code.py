import fitz  # PyMuPDF
def decodingModule(filename ,pageNumOfCiper ,lineNumOfCiper , wordNumOfCiper):
    pdf_document = fitz.open(filename)
    lineIterator = 1
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        if (page_num + 1) == pageNumOfCiper:
            for line in page.get_text("text").splitlines():
                words = line.split()  
                if lineIterator == lineNumOfCiper:
                    print(words[wordNumOfCiper - 1]  )
                lineIterator += 1

    
    pdf_document.close()
if __name__ == "__main__":
    pdf_filename = "C:/Users/Crown Tech/Pictures/(Cliffs Notes) Robert Bruce - The Adventures of Huckleberry Finn -Cliffs Notes (2000).pdf"
    #give the path of saved pdf book on your pc
    
    pageNum, lineNum , wordNum  = 20 , 3 , 3 
    
    decodingModule(pdf_filename , pageNum ,lineNum , wordNum  )
      
