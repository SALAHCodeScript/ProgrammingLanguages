import cv2

image = cv2.imread("D:\\Data\\SALAH\\home\\salah\\Pictures\\Favor\\Yoru.jpg")   # Load image
cv2.imshow("Image", image)                                                      # Show image
cv2.waitKey(0)                                                                  # Wait for key press
cv2.destroyAllWindows()                                                         # Close window
