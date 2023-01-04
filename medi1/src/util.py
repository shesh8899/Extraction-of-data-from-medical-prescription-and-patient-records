from pdf2image import convert_from_path
from PIL import Image
from pdf2image import convert_from_path
from PIL import Image
import cv2
import numpy
from pytesseract import pytesseract


def preprocess(img):
    np_img = numpy.array(img)
    grey = cv2.cvtColor(np_img, cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(grey, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
    pro = cv2.adaptiveThreshold(resize, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 61, 11)
    return Image.fromarray(pro)