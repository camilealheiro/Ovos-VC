import cv2

img = cv2.imread('Imagens_16bits\Picture9_position1.png', cv2.IMREAD_ANYDEPTH)

x = 115
w = 205

y = 120
h = 210

crop_img = img[x:w, y:h]
print(crop_img)
cv2.imshow('croped', crop_img)
cv2.imwrite('ovo533.png', crop_img)
cv2.waitKey(0)





























