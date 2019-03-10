import pickle
import flask
from flask import request
import pandas as pd
from enhancer import FeatureEnhancer
from sklearn.externals import joblib

app = flask.Flask(__name__)

#getting our trained model from a file we created earlier
model = pickle.load(open("pipe_with_module.pkl","rb"))

@app.route('/predict', methods=['POST'])
def predict():
    #grabbing a set of features from the request's body
    input_dataframe = # construct dataframe from request.get_json()
    
    #our model predicts price of flat based on dataframe
    prediction = model.predict(input_dataframe).tolist()
    
    #preparing a response object and storing the model's predictions
    response = {}
    response['prediction'] = prediction
    
    #sending our response object back as json
    return flask.jsonify(response)

