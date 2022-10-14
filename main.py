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
    os.mkdir(f"./FRAMES_{arguments[1]}")
except FileExistsError:
    pass

success, image = vidcap.read()
count = 0

while success:
    # save frame as JPEG file

    if count % steps == 0:
        cv2.imwrite(f"./FRAMES_{arguments[1]}/frame_#{count}.jpg", image)
        success, image = vidcap.read()
        print('Read a new frame: ', success)

    count += 1
