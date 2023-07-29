import cv2

image = cv2.imread('res/20230322165500.tif', cv2.IMREAD_GRAYSCALE)


blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # 가우시안 블러 적용

_, binary_image = cv2.threshold(blurred_image, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', image)
cv2.imshow('Preprocessed Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
