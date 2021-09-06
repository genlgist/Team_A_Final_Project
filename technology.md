# Technologies Used

![image_name](https://github.com/genlgist/Team_A_Final_Project/blob/ChrisAdd/FinalProjectTechDiagram%202021-0905.001.jpeg)

## Data Cleaning and Analysis
Leverage Python, Tensorflow, and Keras to preprocess images (e.g. sizing, normalizing, encoding) to improve model classification efficacy. 

## Database Storage
Leveraging AWS S3 bucket to store Kaggle images for training and testing.  Consider adding a S3 bucket to keep history of new images uploaded for classification along with key model outputs for future development.

## Machine Learning
Tensorflow will be used to build a convolutional neural network (CNN) classification model that will be used to classify expressions of uploaded black and white headshots.  Google Colab was used to code the model and import all necessary python libraries.  

## Dashboard
FINAL DELIVERABLE - v1.0:
User uploads a black and white head shot to the dashboard which sets off an event for the image to be processed by a convolutional neural network model that classifies the expression on the headshot.  The identified classification will be presented to the user along with the model's confidence level of the prediction.

Bootstrap, HTML, and Javascript will be used to build the front end user interface (dashboard) with the ability to upload (with event listener) a black and white image for the classification model.  Leverage Flask as the integration layer between the python model and the Javascript front end.  Team is considering the option to include top 3 possible expression classifications sorted by model confidence level.

## Future Development
- v1.1 Add the ability to confirm or correctly classify the expression of the headshot.  Once confirmed or correctly classified the image is saved along with model outputs for trends and stats on how well the model is performing.  The images may be used for future updates and model refitting to better classify new images.
- v1.2 Database of classification results are kept for dashboarding and model health.  
- v2.1 Zoom 'self-awareness' plug-in that captures camera feed at a set frequency to provide a trend of expressions being telegraphed to other Zoom participants during the course of a meeting.  Dashboard includes a timeline trend.
- v3.1 Zoom plug-in to provide people with autism a support tool that monitors the expressions of others on the Zoom call. Would include an expanded set of expressions that may be particularly helpful for people with autism.


