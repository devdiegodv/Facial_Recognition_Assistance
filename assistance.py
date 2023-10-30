from cv2 import cv2
import face_recognition as fr
import os
import numpy

# create database
path = 'employes'
my_images = []
employes_name = []
employes_list = os.listdir(path)

for name in employes_list:
    actual_image = cv2.imread(f'{path}\{name}')
    my_images.append(actual_image)
    employes_name.append(os.path.splitext(name)[0])

print(employes_name)

# function to codify images
def codify(images):

    # create a new list
    codified_list = []

    # convert images to RGB
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # codify
        codified = fr.face_encodings(image)[0]

        # add to the list
        codified_list.append(codified)

    return codified_list

codified_list_employes = codify(my_images)

# take screenshot from web cam
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    # read screenshot from web cam
    success, image = capture.read()

    cv2.imshow("Taking screenshot", image)

    if not success:
        print("Capture could not be taken")
    else:
        # recognize face in capture
        face_capture = fr.face_locations(image)

        # codify face captured
        codified_face_capture = fr.face_encodings(image, face_capture)

        # search matches
        for facecodified, facelocation in zip(codified_face_capture, face_capture):
            matches = fr.compare_faces(codified_list_employes, facecodified)
            distances = fr.face_distance(codified_list_employes, facecodified)

            print(distances)

            # get the lower value
            index_matches = numpy.argmin(distances)

            # show matches
            if distances[index_matches] > 0.6:
                print("Does not match any of the employees")
            else:
                print("Welcome to the work")


    key = cv2.waitKey(1)
    if key == ord('q'):
        break