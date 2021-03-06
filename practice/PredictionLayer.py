#import packages
import numpy as np
import pandas as pd
import os
#import matplotlib # check later 
#import matplotlib.pyplot as plt # check
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
import PIL
from PIL import Image
import warnings


#initializations
warnings.simplefilter("ignore")
label_names = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']


######## IMPORTING IMAGE AND LOADING MODEL #########

#import image
img = Image.open('static/images/selected_img.jpeg')  #point to js resource folder holding this file. hold trained model in the resoure folder as well


# load the saved model
model = load_model("models/final_model.h5")  # put in resource folder with selected image
print('Tensorflow keras Model loaded successfully')


# standardizing image
img = img.resize((48, 48), Image.ANTIALIAS) #resize the image using PIL's builtin function
img = np.array(img)
if len(img.shape) == 2:  #if the user is uploading a black and white image
    img=np.stack((img,)*3, axis=-1)
img = np.expand_dims(img,axis=0) # the size of the first
print(img.shape)
img = img/255.0


####### USING THE MODEL ON THE IMAGE #######


# process image through prediction model
pred = model.predict(img)

# softmax function rescales each element/dimension to lie between [0,1] and add up to 1.0
score = tf.nn.softmax(pred[0]) 
print(score)


# print prediction label and confidence level
print(
    "This expression is most likely {} with a {:.2f} share of distribution."
    .format(label_names[np.argmax(score)], 100 * np.max(score))
)
print(
    "This expression is least likely {} with a {:.2f} share of distribution."
    .format(label_names[np.argmin(score)], 100 * np.min(score))
)
# because we are using softmax this is not the standard statistical confidence level


###### CREATING BASIC RESULTS DF ########

# put together a pd dataframe with args and scores
results_df = pd.DataFrame({'Expression': label_names})

scores = np.array(score)
scores_s = pd.Series(scores)
results_df['Distribution'] = scores_s

results_df


# sort by scores from high to low
results_df = results_df.sort_values(by='Distribution', ascending=False)
# this code is not needed if only passing top 3.  use code below to pass top 3


##### TOP 3 DF ######


# select top 3 most likely expressions with images and confidence to return to the dashboard
top3_df = results_df.nlargest(3,'Distribution')
top3_sum = top3_df.Distribution.sum()
top3_df['PredictScore'] = top3_df['Distribution']/top3_sum
top3_df

# exporting to a JSON file
data = top3_df.to_json(orient='records')
print(data)




