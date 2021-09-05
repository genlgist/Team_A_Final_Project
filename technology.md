# Technologies Used

![image_name](https://github.com/genlgist/Team_A_Final_Project/blob/ChrisAdd/FinalProjectTechDiagram%202021-0904.001.jpeg)

## Data Cleaning and Analysis
Python/Tensorflow/Keras to preprocess images to improve model efficacy (e.g. sizing, normalizing, encoding). 

## Database Storage
AWS S3 bucket to store Kaggle images for training and testing.  Consider adding a S3 bucket to keep history of new images uploaded for classification along with key model outputs.

## Machine Learning
Tensorflow will be used to build a convolutional neural network (CNN) classification model that will be used to classify expressions of uploaded black and white headshots.  Google Colab was used to code the model and import all necessary python libraries.  

## Dashboard
Use Bootstrap, HTML, and Javascript front end for dashboard with ability to upload (event listener) a black and white image to be sent to the classification model.  Use Flask as the integration layer between the python model and the Javascript front end.  the dashboard(e.g. runtime, probability or confidence of match?)  Do we use REST APIs to merge python back end with web front end.  Flask app interaction with MongoDB.. can we use with AWS S3.  Percent confidence generated using tensorflow as well?

###Final project - v1.0
User uploads a black and white head shot to the dashboard which sets off an event for the image to be processed by a convolutional neural network model that classifies the expression on the headshot.  The identified classification will be presented to the user along with the model's confidence level of correctly classifying.

###Time Permitting
- v1.1 Add the ability to confirm or correctly classify the expression of the headshot.  Once confirmed or correctly classified the image is saved along with model outputs for trends and stats on how well the model is performing.  The images may be used for future updates and fitting of the model to better classify new images.
- v1.2 Database of classification results are kept for dashboarding and model health.  
- v2.1 Zoom 'self-awareness' plug-in that captures camera feed at a set frequency to provide a trend of expressions being telegraphed to other Zoom participants during the course of a meeting.  Dashboard includes a timeline trend.
- v3.1 Zoom plug-in to provide people with autism a support tool that monitors the expressions of others on the Zoom call. Would include an expanded set of expressions that may be particularly helpful for people with autism.


