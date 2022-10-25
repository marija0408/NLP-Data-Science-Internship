import numpy as np
from flask import Flask, request,render_template, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    input_feature = float_features[0]
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'Salary for {input_feature} years of experience should be ${output}')

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=9874)

