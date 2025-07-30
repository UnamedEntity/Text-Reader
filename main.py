import pyttsx3
import PyPDF2
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = PyPDF2.PdfReader(book)
page = len(pdfreader.pages)


for num in range(0, page):
    pdfpage = pdfreader.pages[num]
    text = pdfpage.extract_text()
    
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

