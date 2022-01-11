import cv2 as cv

def con(im):
    img = cv.imread(im)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.blur(gray, (10,10))
    ret, thresh = cv.threshold(blur, 1, 255, cv.THRESH_OTSU)
    contours, heirarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0,0,0), 3)
    cv.namedWindow('Contours',cv.WINDOW_NORMAL)
    cv.namedWindow('Thresh',cv.WINDOW_NORMAL)
    cv.imshow('Contours', img)
    cv.imshow('Thresh', thresh)
    
    if cv.waitKey(0):
        cv.destroyAllWindows()