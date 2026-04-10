from flask import Flask, render_template, request
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html', results=None)

    else:
        try:
            # Grab form values safely
            gender                    = request.form.get('gender')
            race_ethnicity            = request.form.get('race_ethnicity')
            parental_level_of_education = request.form.get('parental_level_of_education')
            lunch                     = request.form.get('lunch')
            test_preparation_course   = request.form.get('test_preparation_course')
            writing_score             = request.form.get('writing_score')
            reading_score             = request.form.get('reading_score')

            # Validate nothing is empty
            if not all([gender, race_ethnicity, parental_level_of_education,
                        lunch, test_preparation_course, writing_score, reading_score]):
                return render_template('home.html', results="Please fill in all fields.")

            # Build CustomData object
            data = CustomData(
    gender=gender,
    race_ethnicity=race_ethnicity,
    parental_level_of_education=parental_level_of_education,
    lunch=lunch,
    test_preparation_course=test_preparation_course,
    writing_score=int(writing_score),
    reading_score=int(reading_score),
    math_score=0          # ← add this dummy value
)

            pred_df = data.get_data_as_data_frame()
            print("Input DataFrame:\n", pred_df)

            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            print("Prediction:", results)

            return render_template('home.html', results=round(results[0], 2))

        except Exception as e:
            print("ERROR:", e)
            return render_template('home.html', results=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)