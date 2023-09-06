#TODO:
    #Load the HRPose model from HRpose/
        #I will probably need the class files for HRpose.
    #run all the training data through HRpose to get the joints data
        #Or run it as we run the model 
            #This will be slower, but the final model will need to pass through all the classifiers.
            #Don't do this for training!
    #Create a basic NN classifer and train it on the joint data from the HRpose model and the labels I created
    #Use the output labels from this classifer + the joint data and labels to create the hand classifing model
    #put the 3 models together as a stacked algorithm and make sure it works for inference through all 3.