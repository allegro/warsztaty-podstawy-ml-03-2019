import pickle
import flask
from flask import request

app = flask.Flask(__name__)

#getting our trained model from a file we created earlier
model = pickle.load(open("model.pkl","rb"))

@app.route('/predict', methods=['POST'])
def predict():
    #grabbing a set of features from the request's body
    feature_array = request.get_json()['feature_array']
    
    #our model rates flat based on the input array
    prediction = model.predict([feature_array]).tolist()
    
    #preparing a response object and storing the model's predictions
    response = {}
    response['predictions'] = prediction
    
    #sending our response object back as json
    return flask.jsonify(response)