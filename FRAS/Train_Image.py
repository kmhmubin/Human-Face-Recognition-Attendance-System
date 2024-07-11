import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread

# Ensure the directory exists
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# -------------- image labels ------------------------
def getImagesAndLabels(path):
    # Ensure the directory exists
    create_directory(path)
    
    # Debugging line to check if the directory exists
    print(f"Directory checked/created: {path}")

    # get the path of all the files in the folder
    try:
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return [], []
    
    # Debugging line to check the image paths
    print(f"Image paths: {imagePaths}")
    
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilImage = Image.open(imagePath).convert('L')
        imageNp = np.array(pilImage, 'uint8')
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids

# -------------- training the images ---------------------
def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces, Id = getImagesAndLabels("TrainingImage")
    
    # Debugging line to check the number of faces and Ids
    print(f"Number of faces: {len(faces)}, Number of Ids: {len(Id)}")
    
    try:
        recognizer.train(faces, np.array(Id))
        recognizer.save("TrainingImageLabel/Trainner.yml")
        print("Images trained successfully.")
    except cv2.error as e:
        print(f"Error in training: {e}")
    
    # Make the program sleep for 3 seconds
    time.sleep(3)
