from cv2 import cv2
import face_recognition as fr
import os

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
print(len(codified_list_employes))plññ{{{{{}}}}}