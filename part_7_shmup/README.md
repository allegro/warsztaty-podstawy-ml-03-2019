
To prepare training data run

```
python3 shmup-train.py > training.log
```

This should output numeric data about your gameplay. 

```
tail -n +3 training.log > train.csv
```

You can play with data and tweak model in ai_model.ipynb notebook. This notebook shoulld output ai_model.pkl, which is used by shmup-play.py.

To launch your model use:

```
python3 shmup-play.py
```
