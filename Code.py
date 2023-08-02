#Make sure To install pip install PyMuPDF (also prev. known fitz)
#pip install PyMuPDF


import fitz  
import string
import tkinter as tk
from tkinter import ttk

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
    
    pdf_document.close()
    return encodedMsg
    

def decodingModuleNew(filename , encodedMsgIn2DArray):
    pdf_document = fitz.open(filename)
    realMsg = ""
    lineStoredInAList  = []
    for perWord in encodedMsgIn2DArray:
        page = pdf_document.load_page(perWord[0] - 1   )
        line =  page.get_text("text").splitlines()
        lineStoredInAList = line[perWord[1] - 1  ].split()
        realMsg +=  lineStoredInAList[perWord[2] - 1 ] + " "
    pdf_document.close()
    return removeSpecialCharacters(realMsg.lower())
    
    
def Encode():
     realmsg =  varForHoldingText.get()
     pathwithBackSlashes = inputForPathHoldingVar.get()
     pathwithForwardSlashes = pathwithBackSlashes.replace( "\\" , "/"  ) 
     outputHoldingVar.set(str(encodingModule(pathwithForwardSlashes , realmsg)))
def Decode():
    pathwithBackSlashes = inputForPathHoldingVar.get()
    pathwithForwardSlashes = pathwithBackSlashes.replace( "\\" , "/"  )
    encodedMsg = varForHoldingTextForDecodingFeild.get()
    listOfEncodedMsg = []
    singleWord = []
        
    
    listOfNumbers = []
    listOfNumbers = encodedMsg.split()
    for i in listOfNumbers:
        singleWord.append(int(i))  
    
        
        if len(singleWord) == 3:
            listOfEncodedMsg.append(singleWord)  
            singleWord = []  
     
        
    
    outputHoldingVarForDecodingField.set(decodingModuleNew( pathwithForwardSlashes , listOfEncodedMsg))

def on_entry_click(event):
    if varForHoldingText.get() == "Enter Plain Text Message":
        input_entry.delete(0, "end")  
        input_entry.config(fg="black")

def on_entry_focus_out(event):
    if varForHoldingText.get() == "":
        input_entry.insert(0, "Enter Plain Text Message")
        input_entry.config(fg="gray")  

def on_entry_click_Path(event):
    if inputForPathHoldingVar.get() == "For Example C:\\Users\\Hero\\Pictures\\SecretBook.pdf":
        inputFieldForPathOfPDFKey.delete(0, "end")  
        inputFieldForPathOfPDFKey.config(fg="black") 

def on_entry_focus_out_Path(event):
    if inputForPathHoldingVar.get() == "":
        inputFieldForPathOfPDFKey.insert(0, "For Example C:\\Users\\Hero\\Pictures\\SecretBook.pdf")
        inputFieldForPathOfPDFKey.config(fg="gray")  
        
def on_entry_click_Decode(event):
    if varForHoldingTextForDecodingFeild.get() == "For Example [[12,3,6],[15,56,3].... ] --> 12 3 6 15 56 3 ... ":
        inputEntryForDecoding.delete(0, "end")  
        inputEntryForDecoding.config(fg="black") 

def on_entry_focus_out_Decode(event):
    if varForHoldingTextForDecodingFeild.get() == "":
        inputEntryForDecoding.insert(0, "For Example [[12,3,6],[15,56,3].... ] --> 12 3 6 15 56 3 ... ")
        inputEntryForDecoding.config(fg="gray")  





if __name__ == "__main__":
    
    #----   Title   ---
    
    window = tk.Tk()
    window.title("BookCipher")
    window.geometry('500x500' )
    label1 = ttk.Label(master=window , text = "Book Cipher" , font = 'Calibri 24 '   )
    
    #-------------------
    
    
    
    label1.pack(pady = 10   )
    
    labelOfPath = ttk.Label(master=window , text = "Path To Secret Book (MUST)" , font = 'Calibri 10 '   )
    labelOfPath.pack(pady = 10)
    
    #------  Encoding Module -----
    
    outputHoldingVar = tk.StringVar()
    
    output = ttk.Label(  master = window  , text = 'Output' , textvariable = outputHoldingVar   )
    
    frame_ = ttk.Frame(  master = window  )
    
    inputForPathHoldingVar = tk.StringVar()
    inputForPathHoldingVar.set("For Example C:\\Users\\Hero\\Pictures\\SecretBook.pdf")
    inputFieldForPathOfPDFKey = ttk.Entry(master  = window , width='60' , textvariable = inputForPathHoldingVar   )
    inputFieldForPathOfPDFKey.bind("<FocusIn>", on_entry_click_Path)
    inputFieldForPathOfPDFKey.bind("<FocusOut>", on_entry_focus_out_Path)
    inputFieldForPathOfPDFKey.pack()
    labelOfEncodingModule = ttk.Label(master=frame_ , text = "Encoding Module" , font = 'Calibri 10 bold'   )   
    varForHoldingText = tk.StringVar()
    varForHoldingText.set("Enter Plain Text Message")
    input_entry = ttk.Entry( master = frame_  , textvariable = varForHoldingText , width='60' )
    
    button = ttk.Button(master = frame_ , text='Encode'  , command=Encode   )
    
    labelOfEncodingModule.pack(pady=10)
    input_entry.bind("<FocusIn>", on_entry_click)
    input_entry.bind("<FocusOut>", on_entry_focus_out)
    input_entry.pack(side= 'left' , padx='4'  )
    button.pack(side= 'left' )
    frame_.pack(pady =  20 )
    output.pack()

    #------  Encoding Module -----

    #------  Decoding Module -----

    outputHoldingVarForDecodingField = tk.StringVar()
    
    outputForDecodingModule = ttk.Label(  master = window  , text = 'Output' , textvariable = outputHoldingVarForDecodingField   )
    



    frameForDecodingModule = ttk.Frame(  master = window  )
    labelOfDecodingModule = ttk.Label(master=frameForDecodingModule , text = "Decoding Module" , font = 'Calibri 10 bold'   )   
    varForHoldingTextForDecodingFeild = tk.StringVar()
    varForHoldingTextForDecodingFeild.set("For Example [[12,3,6],[15,56,3].... ] --> 12 3 6 15 56 3 ... ")
    inputEntryForDecoding = ttk.Entry( master = frameForDecodingModule  , textvariable = varForHoldingTextForDecodingFeild , width='60' )
    buttonForDecoding = ttk.Button(master = frameForDecodingModule , text='Decode'  , command=Decode   )

    

    
    labelOfDecodingModule.pack(pady=10)
    inputEntryForDecoding.bind("<FocusIn>", on_entry_click_Decode)
    inputEntryForDecoding.bind("<FocusOut>", on_entry_focus_out_Decode)
    inputEntryForDecoding.pack(side= 'left' , padx='4' )
    buttonForDecoding.pack(side= 'left')
    frameForDecodingModule.pack(pady =  20)
    outputForDecodingModule.pack()



    #------  Decoding Module -----









    window.mainloop()
    
    
    
