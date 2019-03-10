Install flask: 
pip3 install flask

Launch the app: 
export FLASK_APP=ai_service.py; flask run

Get predictions: 
curl 'http://localhost:5000/predict' -d '{"sqrMeters":71, "rooms":2, "location":"Wilda"} ' -XPOST -H "Content-type: application/json"

Should result in something like:
{"prediction":[[419191.0334601513]]}

