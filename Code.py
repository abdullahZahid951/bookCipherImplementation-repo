import fitz  # PyMuPDF
def decodingModuleNew(filename , encodedMsgIn2DArray):
    pdf_document = fitz.open(filename)
    realMsg = ""
    lineStoredInAList  = []
    for perWord in encodedMsgIn2DArray:
        page = pdf_document.load_page(perWord[0] - 1   )
        line =  page.get_text("text").splitlines()
        lineStoredInAList = line[perWord[1] - 1  ].split()
        realMsg += " " + lineStoredInAList[perWord[2] - 1 ]
    print(realMsg)
    pdf_document.close()
    
    
if __name__ == "__main__":
    pdf_filename = "C:/Users/Crown Tech/Pictures/(Cliffs Notes) Robert Bruce - The Adventures of Huckleberry Finn -Cliffs Notes (2000).pdf"
    #give the path of saved pdf book on your pc
    encodedMsgIn2DArray = [[30 , 6 , 9  ] ,[35 , 9 , 7]]
    decodingModuleNew(pdf_filename , encodedMsgIn2DArray)   
    
      
