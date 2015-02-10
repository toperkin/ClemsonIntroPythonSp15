import cv2

img = cv2.imread('usf_cloister_banyan.jpg')

for threshold in range(10, 250, 20):
    edgy = cv2.Canny(img, threshold, threshold)
    #cv2.imshow(str(threshold), edgy)
    #cv2.waitKey(0)
    cv2.imwrite('threshold'+str(threshold)+'.png', edgy)
