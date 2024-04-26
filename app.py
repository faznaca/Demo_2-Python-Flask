from flask import Flask, render_template, request
import pickle

# Initialize Flask app
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction form submission
@app.route('/prediction', methods = ['GET', 'POST'])
def predict():
    if request.method == 'POST':

        # Get user inputs from the form
        age = int(request.form['age'])
        salary = int(request.form['salary'])

        # Make prediction using the loaded Random Forest model
        features = [[age, salary]]

    
        rf_clf = pickle.load(open('random_forest_model.pkl', 'rb'))
        prediction =  rf_clf.predict(features)


        # Convert prediction to a meaningful string
        result = "The person will purchase the product " if prediction[0] == 1 else "The person will not purchase the product"


    # Render prediction result template with the result
    return render_template('prediction_result.html', prediction = result)

if __name__ == '__main__':
    app.run(debug=True)
