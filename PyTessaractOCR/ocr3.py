import os

import cv2
import pytesseract

image = cv2.imread("F:/images/NID Collection/snid2.jpg")
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.medianBlur(gray, 3)

gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

cv2.imshow("Gray", gray)
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

text = pytesseract.image_to_string(filename, "eng+ben+Bengali+eng2+ben2+eng2b+Bengali2f+eng2f+ben2f+Bengali2n+eng2n"
                                             "+ben2n")
os.remove(filename)
print(text)

cv2.waitKey(0)
cv2.destroyAllWindows()
