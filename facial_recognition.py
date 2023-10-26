from cv2 import cv2
import face_recognition as fr

# load images
image_control = fr.load_image_file('images/PhotoC.jpg')
image_test = fr.load_image_file('images/PhotoD.jpg')
image_test2 = fr.load_image_file('images/PhotoE.jpg')

# transform color
image_control = cv2.cvtColor(image_control, cv2.COLOR_BGR2RGB)
image_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2RGB)
image_test2 = cv2.cvtColor(image_test2, cv2.COLOR_BGR2RGB)

# show images
cv2.imshow('Image 1', image_control)
cv2.imshow('Image 2', image_test)
cv2.imshow('Image 3', image_test2)

# keep program opened
cv2.waitKey(0)