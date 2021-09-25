#import packages
import numpy as np
import pandas as pd
import os
import tensorflow as tf
import urllib.request
from werkzeug.utils import secure_filename
from tensorflow import keras
from tensorflow.keras.models import load_model
import PIL
from PIL import Image
import warnings


# importing dependencies for flask 
from flask import Flask, render_template, redirect, request, url_for, send_file
from flask import jsonify

##### STORAGE LOCATION #####
UPLOAD_FOLDER = 'static/images/'

####### SETTING UP FLASK #########
# defining flask app
app = Flask(__name__)


""" app.config["CACHE_TYPE"] = "null"
# change to "redis" and restart to cache again

# some time later
cache.init_app(app) """

# All caching functions will simply call through
# to the wrapped function, with no caching
# (since NullCache does not cache).

## Flask configuration SECRET_KEY variable is needed for passing files into a POST request generates a new session. 
app.config['SECRET_KEY'] = "ABC123#RDX$678qwv3"

# Image Storage
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 48 * 48


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# load the saved model
model = load_model("models/final_model.h5")  # put in resource folder with selected image
print('Tensorflow keras Model loaded successfully')

######## CREATING ROUTES ########
# welcome/index route
@app.route("/")
def index():
    print("index is running!")
    return render_template('index.html')

@app.route("/", methods =['POST'])   
def upload_image():
    if 'file' not in request.files:
        print('No file part')
        return redirect(request.url)
    file = request.files['file']
    print(request)
    if file.filename == '':
        print('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'selected_img.jpeg'))
        #print('upload_image filename: ' + filename)
        print('Image successfully uploaded and displayed below')
        predict()    
        return render_template('index.html', filename='selected_img.jpeg')
    else:
        print('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
print("index is running!")


## redisplays the image on index
@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='images/' + filename), code=301)


## Verify valid image uploaded
@app.route('/read_file', methods=['GET'])
def read_uploaded_file():
    filename = secure_filename(request.args.get('filename'))
    try:
        if filename and allowed_file(filename):
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as f:
                print("successfully read image")
                return f.read()
    except IOError:
        pass
    return "Unable to read file"

# creating route that will run the model and create data for data.js
@app.route("/predict")
def predict():
    #initializations
    warnings.simplefilter("ignore")
    label_names = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

    
    ######## IMPORTING IMAGE #########

    #import image
    img = Image.open('./static/images/selected_img.jpeg')  #point to js resource folder holding this file. hold trained model in the resoure folder as well


    # load the saved model
   # model = load_model("models/final_model.h5")  # put in resource folder with selected image
   # print('Tensorflow keras Model loaded successfully')


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
    top3_df = top3_df.drop('Distribution', 1)
    top3_df = top3_df.rename(columns={"PredictScore": "EmoScore"})
    top3_df['EmoScore'] = top3_df['EmoScore'].map(lambda n: '{:.0%}'.format(n))
    top3_df


    # exporting to a JSON file
    data = top3_df.to_json(orient= 'records')
    print(data)
    # having route return JSON
    
    i=0
    # save top 3 emojis to javascript image folder 'emo3'
    while i<3:
        #use top 3 results df to pull emotions type from top 3 instad of random choice for final file
        emotion = top3_df.iloc[i]['Expression']
        print(emotion)
        path = './static/images/emoAll/'+emotion+'.png'  #filepath to use for local version... '../FrontEndDashboard/static/images/emoAll/'
        print(path)
        img = Image.open(path)
        i+=1
        exportPath = './static/images/emo3/emo'+str(i)+'.png'  #filepath to use for local version... '../FrontEndDashboard/static/images/emo3/emo'+str(i)+'.png'
        print(exportPath)
        img.save(exportPath)
    
    return(data)

    # return send_file(os.path.join('/static/images/', filename))
   
@app.errorhandler(500)
def server_error(error):
    return render_template('error.html'), 500    


if __name__ == "__main__":
    app.run(DEBUG=True)  




""" # prevent cached responses
@app.after_request
    if app.config["DEBUG"]:
        def after_request(response):
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
            response.headers["Expires"] = 0
            response.headers["Pragma"] = "no-cache"
            return response """