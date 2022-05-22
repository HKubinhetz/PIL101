# Python Imaging
from PIL import Image, ImageGrab
import pytesseract
import cv2
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\CS317813\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


screen = ImageGrab.grab()
screen.save(fp='C:\\Users\\CS317813\\Desktop\\imagem.jpg')
img = cv2.imread('C:\\Users\\CS317813\\Desktop\\imagem.jpg')
(h, w) = img.shape[:2]
img = cv2.resize(img, (w*5, h*5))
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thr = cv2.threshold(gry, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
data = pytesseract.image_to_string(screen, output_type=pytesseract.Output.DICT, lang="por")
print(data)

