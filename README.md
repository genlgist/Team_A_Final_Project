# Team_A_Final_Project

# Team_Members
- Chris Morgan
- Gregory Morales
- Naomi Shields
- Regina Negrycz

# Content 

## Selected Topic

Learning facial expressions from an image.

## Reason Topic Selected

We are interested in working with the Machine Learning algorithm Convolutional Neural Network to classify images of facial recognition. 

## Description of the data source

Dataset FER-2013 is a Kaggle dataset consisting of 48x48 pixel grayscale images of faces. The faces have been automatically registered so that the face is more or less centered and occupies about the same amount of space in each image.

The task is to categorize each face based on the emotion shown in the facial expression into one of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral). The training set consists of 28,709 examples and the public test set consists of 3,589 examples.


## Question

By uploading images of facial expressions, can we accurately predict the facial expression?


# Technologies

# Data Cleaning and Analysis

Python to help preprocessing of the images (Pandas?) to improve model efficacy (e.g. adding, removing, encoding?). jpeg files to be uploaded

# Database Storage

AWS S3 bucket to store Kaggle images for training and testing. Augment and join the dbase with new images after uploaded and classified?

# Machine Learning

Tensorflow will be used to build a deep learning classification model that will be used to classify expressions of uploaded black and white headshots. Given that these are complex images multiple hidden layers will be required to build an effective model. Google Colab to build the Tensorflow model. Will need to figure out how to assign to one of multiple classifications. Leverage MNIST model for black and white photos?

# Dashboard

Use Bootstrap, HTML, Javascript front end for dashboard with ability to upload (event listener) a black and white image for a deep learning engine to classify expressions of headshots. Use Flask for python visuals or metrics on the model itself (e.g. runtime, probability or confidence of match?) Do we use REST APIs to merge python back end with web front end. Flask app interaction with MongoDB.. can we use with AWS S3. Percent confidence generated using tensorflow as well?

Final project v1.0 Upload black and white head shot to be processed by a deep learning model that classifies the expression on the headshot. The identified classification will be presented to the user along with the model's confidence level of correctly classifying.

Time Permitting v1.1 Add the ability to confirm or correctly classify the expression of the headshot. Once confirmed or correctly classified the image is saved in the appropriate folder for future training or testing of the model. v1.2 Database of classification results are kept for dashboarding and model health.
