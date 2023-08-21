#to store or read/write the labels.
#Will use a labelsModel.py NN to classify it or something


#NOTE: DO I want to separately classify it LS, RS, Back, Stomach, Standing, and then classify hands?
    #classification will happen on same datapoints, so nah.
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
import threading
from ImageGUI import *

def main():
    NUM_PARTICIPANTS = 109
    NUM_SAMPLES_PER_PARTICIPANT = 45
    NUM_POSITIONS = 9
    POSITIONS = ["lying on back, hands by side",
                "lying on back, hands under head",
                "lying on stomach, hands by side",
                "lying on stomach, hands under head.",
                "lying on left side, hands under head.",
                "lying on left side, hands by side",
                "lying on right side, hands under head.",
                "lying on right side, hands by side",
                "Standing next to the bed."]
    #1-hot encoding
        #10, 11 are variations with covers, but our positions here are irrespective of covers
        #so just 1-9 will be used.

    #TODO: load array if exists
    label_confidences = np.zeros((NUM_PARTICIPANTS, NUM_SAMPLES_PER_PARTICIPANT, NUM_POSITIONS), dtype=float)
    label_confidences = userClassify(label_confidences, POSITIONS, 1, 1, 5, 1)

    #print(label_confidences[0][0])
    print(label_confidences[0])
    #TODO save array to file

def userClassify(labels, labelOptions, startParticipant=1, startSample=1, endSample=45, endParticipant=3):
    image_thread = ImageGUI()
    image_thread.start()
    for ii in range(startParticipant, endParticipant+1):
        parentFolder = "danaLab/" + (5-len(str(ii))) * '0' + str(ii) + '/'
        for jj in range(startSample, endSample+1):
            imgPath = parentFolder + 'RGB/uncover/image_' + (6-len(str(jj))) * '0' + str(jj) +'.png'
            image_thread.set_image_path(imgPath)

            labelIdx = inputValue("P" + str(ii) + " S" + str(jj) + "    Please enter the label number: ", 0, len(labelOptions))
            labels[ii-1][jj-1][labelIdx-1] = 1
    image_thread.stop()
    return labels

def printLabelOptions(labelOptions):
    for ii, label in enumerate(labelOptions):
        print(f"{ii}. {label}")

#Integer values only
def inputValue(prompt, min, max):
    error = "ERORR: value must be between " + str(min) + " and " + str(max)
    outStr = prompt   
    value = min - 1
    
    while value < min or value > max: 
        try:
            print(outStr)
            value = int(input())
            outStr = error + "\n" + prompt
        except ValueError:
            print()
            outStr = "ERROR: input must be an integer\n" + prompt
    return value 

if __name__ == "__main__":
    main()
