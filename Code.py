import fitz  # PyMuPDF
import string

def removeSpecialCharacters(inputString):
    translator = str.maketrans('', '', string.punctuation)
    resultString = inputString.translate(translator)
    return resultString
def encodingModule(filename ,  realMsgThatIsToBeEncoded  ):
    pdf_document = fitz.open(filename)
    num_pages = pdf_document.page_count
    encodedMsg = []    
    realMsgThatIsToBeEncoded = realMsgThatIsToBeEncoded.lower()
    realMsgThatIsToBeEncoded = removeSpecialCharacters(realMsgThatIsToBeEncoded)
    WordsOfLineStoredInAList = []
    WordsOfLineStoredInAList = realMsgThatIsToBeEncoded.split()
    
    for perWordNum in range(len(WordsOfLineStoredInAList)):
        iterateTheInnerLoops = True
        for pageNum in range(num_pages) :
            if iterateTheInnerLoops == True :
                page = pdf_document.load_page(pageNum)
                line =  page.get_text("text").splitlines()
                for lineNum in range(len(line)) :
                    if iterateTheInnerLoops == True :
                        lineStoredInAList = line[lineNum].split()
                        for wordNum in range(len(lineStoredInAList))  :
                            if iterateTheInnerLoops == True :
                                if WordsOfLineStoredInAList[perWordNum] == removeSpecialCharacters(lineStoredInAList[wordNum].lower()):
                                    encodedMsg.append([pageNum + 1 , lineNum + 1 , wordNum + 1 ]  )
                                    iterateTheInnerLoops = False
                            else:
                                break
                    else:
                        break
            else :
                break                
    
    print(encodedMsg)
    #decodingModuleNew(filename , encodedMsg)

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
    pdf_filename = "C:/Users/Crown Tech/Pictures/Alex Michaelides - The silent patient-Celadon Books (2019).pdf"
    #give the path of saved pdf book on your pc
    encodedMsgIn2DArray = [[30 , 6 , 9  ] ,[35 , 9 , 7]]
    #decodingModuleNew(pdf_filename , encodedMsgIn2DArray)   
    realMsgThatIsToBeEncoded = 'lover'
    encodingModule(pdf_filename, realMsgThatIsToBeEncoded)    
      
