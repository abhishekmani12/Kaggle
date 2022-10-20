from flask import Flask, jsonify, request
from sklearn.ensemble import GradientBoostingClassifier
import pickle as pkl
import pandas as pd
import sys

app=Flask(__name__)

@app.route("/pred", methods=['POST'])

def pred():
    
    jfile=request.json;
    qdf=pd.DataFrame(jfile);
    pred=list(model.predict(qdf));

    return jsonify({'pred': str(pred)})

if __name__ == '__main__':

    try:
        port =int(sys.argv[1])
    except:
        port =12345

    mfile = open ("C:/Users/Abhis/Desktop/apitest/gbmodel.pkl", "rb")
    model= pkl.load(mfile)


    app.run(debug=True)