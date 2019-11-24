import os

import cv2
import numpy as np
import pytesseract

image = cv2.imread("F:/images/NID Collection/snid2.jpg")
cv2.imshow("Original", image)
th = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
roi = th[90:620, 280:730]
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, roi)
cv2.imshow('roi', cv2.resize(roi, (0, 0), fx=0.5, fy=0.5))
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(filename, "eng+ben+Bengali+eng2+ben2+eng2b+Bengali2f+eng2f+ben2f+Bengali2n+eng2n"
                                             "+ben2n")
print(text)

cv2.waitKey(0)
cv2.destroyAllWindows()
