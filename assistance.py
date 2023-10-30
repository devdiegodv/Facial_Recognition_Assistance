from cv2 import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

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

# log assistance
def log_assistance(person):
    f = open('log.csv', 'r+')
    data_list = f.readlines()
    names_log = []

    for line in data_list:
        log = line.split(',')
        names_log.append(log[0])

    # avoid duplicated names
    if person not in names_log:
        now = datetime.now()
        string_now = now.strftime('%H:%M:%S')
        f.writelines(f'\n{person}, {string_now}')

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
                # find the employe's name found
                name = employes_name[index_matches]

                # show rectangle and employe's name in screenshot
                y1, x2, y2, x1 = facelocation
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                log_assistance(name)

                # show the screenshot got
                cv2.imshow('Web cam', image)

                # keep screen opened
                cv2.waitKey(0)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break