from pdf2image import convert_from_path
from PIL import Image
from pdf2image import convert_from_path
from PIL import Image
import cv2
import numpy
import src.util
from pytesseract import pytesseract
from patient_parser import patient
from presciption_parser import prescription_parse


def extract(file_path,file_format):
    pages = convert_from_path(file_path)
    document_text=''
    page=pages[0]
    processed = src.util.preprocess(page)
    text = pytesseract.image_to_string(processed, lang='eng')
    document_text='\n'+ text

    if file_format=="prescription":
        ob=prescription_parse(document_text).parse()

    elif file_format=="patient_details":
        ob =patient(document_text).parse()


    else :
        pass
    return ob


if __name__=="__main__":

  a=extract('/Users/shashankpatil/Desktop/medi1/resources /patient_details/pd_1.pdf','patient_details')
  print(a)

