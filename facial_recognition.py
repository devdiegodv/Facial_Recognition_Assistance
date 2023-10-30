from cv2 import cv2
import face_recognition as fr

# load images
image_control = fr.load_image_file('images/imageB.jpg')
image_test = fr.load_image_file('images/imageA.jpg')

# transform color
image_control = cv2.cvtColor(image_control, cv2.COLOR_BGR2RGB)
image_test = cv2.cvtColor(image_test, cv2.COLOR_BGR2RGB)

# get face
place_face_A = fr.face_locations(image_control)[0]
codified_face_A = fr.face_encodings(image_control)[0]

place_face_B = fr.face_locations(image_test)[0]
codified_face_B = fr.face_encodings(image_test)[0]

# show rectangle
cv2.rectangle(image_control,
              (place_face_A[3], place_face_A[0]),
              (place_face_A[1], place_face_A[2]),
              (0, 255, 0),
              2)

cv2.rectangle(image_test,
              (place_face_B[3], place_face_B[0]),
              (place_face_B[1], place_face_B[2]),
              (0, 255, 0),
              2)

# check comparation
result = fr.compare_faces([codified_face_A], codified_face_B)

# distance between photos
distance = fr.face_distance([codified_face_A], codified_face_B)

# show results
cv2.putText(image_test,
            f'{result} {distance.round(2)}',
            (50, 50), # location on screen
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

# show images
cv2.imshow('Image 1', image_control)
cv2.imshow('Image 2', image_test)

# keep program opened
cv2.waitKey(0)