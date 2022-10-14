import cv2
import sys
import os

arguments = sys.argv
print(enumerate(arguments))

steps = 1 if arguments.__len__() != 3 else int(arguments[2])

# Initalize the video itself
vidcap = cv2.VideoCapture(arguments[1])

# Create a folder/dir to hold the frames
try:
    os.mkdir(f"./FRAMES_{arguments[1].split('.')[0]}")
except FileExistsError:
    raise Exception(
        "There's a folder for that video already. If you wish to create another one, remove it.")


success, image = vidcap.read()
count = 0

while success:

    if count % steps == 0:
        # save frame as JPEG file
        cv2.imwrite(
            f"./FRAMES_{arguments[1].split('.')[0]}/frame_#{count}.jpg", image)
        success, image = vidcap.read()
        print('Read a new frame: ', success)

    count += 1
print(f"Succesfully created {count // steps} image (:")
