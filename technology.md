# Technologies Used
## Data Cleaning and Analysis
Do we want to use Beautiful Soup to scrape images from a web page for testing or for additional training?  Is there some preprocessing of the images required to improve the model efficacy (e.g. adding, removing, encoding?)

## Database Storage
AWS S3 bucket to store Kaggle images for training and testing.  Scrape and load other images for further model training and testing? Other metrics or data we would like to store with the images?

## Machine Learning
Tensorflow will be used to build a deep learning classification model that will be used to classify expressions of uploaded black and white headshots. Given that these are complex images multiple hidden layers will be required to build an effective model.  Use Jupyter notebooks or Google Colab to build the Tensorflow model?  Not just a simple single yes/no classification with a confusion matrix.  Will need to figure out how to assign to one of multiple classifications.

## Dashboard
Use Bootstrap, HTML, Javascript front end for dashboard with ability to upload (event listener) a black and white image for a deep learning engine to classify expressions of headshots.  Use Flask for python visuals or metrics on the model itself (e.g. runtime, probability or confidence of match?) It will be hosted on ______.
