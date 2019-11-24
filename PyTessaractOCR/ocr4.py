import cv2
import numpy as np

# load image as HSV and select saturation
import pytesseract

img = cv2.imread("F:/images/NID Collection/snid2.jpg")
cv2.imshow("Original", img)
hh, ww, cc = img.shape

# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold the grayscale image
ret, thresh = cv2.threshold(gray, 165, 255, 0)

# create black image to hold results
results = np.zeros((hh, ww))

# find contours
cntrs = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cntrs = cntrs[0] if len(cntrs) == 2 else cntrs[1]

# Contour filtering and copy contour interior to new black image.
for c in cntrs:
    area = cv2.contourArea(c)
    if area > 1000:
        x, y, w, h = cv2.boundingRect(c)
        results[y:y + h, x:x + w] = thresh[y:y + h, x:x + w]

# invert the results image so that have black letters on white background
results = (255 - results)

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(results, "eng+ben+Bengali+eng2+ben2+eng2b+Bengali2f+eng2f+ben2f+Bengali2n+eng2n"
                                            "+ben2n")
print(text)

cv2.imshow("THRESH", thresh)
cv2.imshow("RESULTS", results)
cv2.waitKey(0)
cv2.destroyAllWindows()
