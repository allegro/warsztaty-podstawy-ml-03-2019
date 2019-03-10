Install flask: 
pip3 install flask

Launch the app: 
export FLASK_APP=ai_service.py; flask run

Get predictions: 
curl 'http://localhost:5000/predict' -d '{"feature_array":[71,3]} ' -XPOST -H "Content-type: application/json"

Should result in something like:
{"predictions":[[419191.0334601513]]}

