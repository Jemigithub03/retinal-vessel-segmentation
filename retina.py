import cv2
import numpy as np

def segment_vessels():
    # 1. Read the image
    img = cv2.imread(r"C:\Users\anabs\Downloads\Image processing project\retina.jpg")
    if img is None:
        print("Error: Could not read image.")
        return
        
    # 2. Extract the Green Channel
    b, g, r = cv2.split(img)
    
    # 3. Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_g = clahe.apply(g)
    
    # 4. Morphological Black-Hat Transform
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    blackhat = cv2.morphologyEx(enhanced_g, cv2.MORPH_BLACKHAT, kernel)
    
    # 5. Thresholding
    ret, thresh = cv2.threshold(blackhat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 6. Post-Processing: Noise Removal (Morphological Opening)
    kernel_opening = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    clean_mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_opening)
    
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Original", 600, 500)
    cv2.imshow("Original", img)
 
    cv2.namedWindow("Green Channel", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Green Channel", 600, 500)
    cv2.imshow("Green Channel", g)
 
    cv2.namedWindow("Enhanced (CLAHE)", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Enhanced (CLAHE)", 600, 500)
    cv2.imshow("Enhanced (CLAHE)", enhanced_g)
 
    cv2.namedWindow("Black-Hat", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Black-Hat", 600, 500)
    cv2.imshow("Black-Hat", blackhat)

    cv2.namedWindow("5 - Binary Thresholding", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("5 - Binary Thresholding", 600, 500)
    cv2.imshow("5 - Binary Thresholding", thresh)
    
    cv2.namedWindow("Final Segmented Vessels", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Final Segmented Vessels", 600, 500)
    cv2.imshow("Final Segmented Vessels", clean_mask) 
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

segment_vessels()
