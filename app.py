from flask import Flask
from flask import render_template,request
from audio_input_and_analyser import predict_audio
app=Flask(__name__)
@app.route("/")
def hello():
    return render_template('sam1.html')
@app.route("/predict", methods=["POST"])
def predict():
    audio = request.files["audio"]
    result = predict_audio(audio)
    return str(result)
if __name__ == "__main__":
    app.run(debug=True)