# Team_A_Final_Project

# Team_Members
Chris Morgan
Gregory Morales
Naomi Shields
Regina Negrycz

# Content

Selected Topic: Learning facial expressions from an image.

# Reason Topic Selected

We are interested in working with the Machine Learning algorithm Convolutional Neural Network to classify images of facial recognition.

# Description of the data source

Dataset FER-2013 is a Kaggle dataset consisting of 48x48 pixel grayscale images of faces. The faces have been automatically registered so that the face is more or less centered and occupies about the same amount of space in each image.

The task is to categorize each face based on the emotion shown in the facial expression into one of seven categories (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral). The training set consists of 28,709 examples and the public test set consists of 3,589 examples.

# Question

By uploading images of facial expressions, can we accurately predict the facial expression?

# Communication Protocols

We will be using Zoom for scheduled class times as well as meetings outside of class, our Group-A Slack channel, and GitHub.

# Technologies

Data Cleaning and Analysis
Leverage Python, Tensorflow, and Keras to preprocess images (e.g. sizing, normalizing, encoding) to improve model classification efficacy.

# Database Storage

N/A

# Machine Learning

Tensorflow will be used to build a convolutional neural network (CNN) classification model that will be used to classify expressions of uploaded black and white headshots. Google Colab was used to code the model and import all necessary python libraries to build initial saved model in a hdf (.h5) file format. The Colab file was then saved as a python file.

# Benefits of a CNN Model

Automatically detects the important features without human supervision. High accuracy rate for image classification and recognition. CNN is also proven effective with video, pattern and face recognition. The algorithm is fast and simple.

# Limitations of a CNN Model

Missing pixels can have a detrimental effect on the verification process of the model. If the CNN has several layers then the training process takes a lot of time if the computer doesn't consist of a good GPU. Requires a large dataset to process and train the neural network.

# Dashboard

FINAL DELIVERABLE - v1.0: User uploads a black and white head shot to the dashboard which sets off an event for the image to be processed by a convolutional neural network model that classifies the expression on the headshot. The top 3 identified classifications will be presented to the user along with the model's confidence level per classification of the prediction.

Bootstrap, HTML, and Javascript will be used to build the front end user interface (dashboard) with the ability to upload (with event listener) a black and white image for the classification model. Leverage Flask as the integration layer between the python model and the Javascript front end. Team is considering the option to include top 3 possible expression classifications sorted by model confidence level.

# Google Slides Presentation

Link to Slides: https://docs.google.com/presentation/d/1f8iF0860x5iSciTA6Nh4J3bSiO9BHCsGyO3rkhl06po/edit?pli=1#slide=id.gf0cf7b0833_0_45

Link to PDF file in GitHub: https://github.com/genlgist/Team_A_Final_Project/blob/main/Final%20Presentation.pdf

# Live Presentation

Link to video of dashboard demo:  
https://github.com/genlgist/Team_A_Final_Project/blob/main/Demo_Video.mp4

# Future Development
v1.1 Add the ability to confirm or correctly classify the expression of the headshot. Once confirmed or correctly classified the image is saved along with model outputs for trends and stats on how well the model is performing. The images may be used for future updates and model refitting to better classify new images.

v1.2 Database of classification results are kept for dashboarding and model health.

v2.1 Zoom 'self-awareness' plug-in that captures camera feed at a set frequency to provide a trend of expressions being telegraphed to other Zoom participants during the course of a meeting. Dashboard includes a timeline trend.

v3.1 Zoom plug-in to provide people with autism a support tool that monitors the expressions of others on the Zoom call. Would include an expanded set of expressions that may be particularly helpful for people with autism.

# ML Tech Diagram
https://github.com/genlgist/Team_A_Final_Project/blob/main/technology.md

# Screenprint of Dashboard

https://github.com/genlgist/Team_A_Final_Project/blob/main/DashboardLayout.png

