import easyocr
import cv2
import matplotlib.pyplot as plt
import numpy as np
import deskew
from skimage.transform import rotate


def dskew_img(img):
    angle = deskew.determine_skew(img)
    img = rotate(img, angle, resize=True) * 255
    print(f'Angle of Rotation:{angle}')
    return img.astype(np.uint8)


def noise_removal(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.fastNlMeansDenoising(img, None, 10, 7, 21)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 12)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img


def extract_text_easyocr(img):
    reader = easyocr.Reader(['en'], gpu=False)
    text = reader.readtext(img)
    for bbox, txt, conf in text:
        cv2.polylines(img, np.int32([bbox]), 2, (0, 255, 0), 2)
    return text, img


if __name__ == '__main__':
    image = cv2.imread('Resources/c_6.jpg')
    image_deskew = dskew_img(image)
    image_filter = noise_removal(image_deskew)
    text_easyocr, bbox_img = extract_text_easyocr(image_filter)
    for bbox, txt, conf in text_easyocr:
        print(txt)
    plt.imshow(bbox_img)
    plt.show()
