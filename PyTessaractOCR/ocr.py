import os

import cv2
import numpy as np
import pytesseract

image = cv2.imread("F:/images/NID Collection/snid2.jpg")
cv2.imshow("Original", image)
dilated_img = cv2.dilate(image[:, :, 1], np.ones((9, 9), np.uint8))
bg_img = cv2.medianBlur(dilated_img, 3)

# --- finding absolute difference to preserve edges ---
diff_img = 255 - cv2.absdiff(image[:, :, 1], bg_img)

# --- normalizing between 0 to 255 ---
norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
cv2.imshow('norm_img', cv2.resize(norm_img, (0, 0), fx=0.5, fy=0.5))
# --- Otsu threshold ---
th = cv2.threshold(norm_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, th)
cv2.imshow('th', cv2.resize(th, (0, 0), fx=0.5, fy=0.5))
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(filename, "eng+ben+Bengali+eng2+ben2+eng2b+Bengali2f+eng2f+ben2f+Bengali2n+eng2n"
                                             "+ben2n")
print(text)

cv2.waitKey(0)
cv2.destroyAllWindows()
