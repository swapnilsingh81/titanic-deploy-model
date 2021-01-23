
from flask import *
import pickle

app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('random_forest_titanic_model.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('index.html')
	
@app.route("/add", methods = ['POST'])
def predict():
	if request.method == 'POST':
		pclass = int(request.form['pclass'])
		gender = int(request.form['sex'])
		age = float(request.form['age'])
		sp = int(request.form['spouse'])
		sib = int(request.form['sib'])
		par = int(request.form['par'])
		child = int(request.form['child'])
		sibsp = sp+sib
		parch = par+child
		fare = float(request.form['fare'])
		embarked= int(request.form['embarked'])
		
		prediction = model.predict([[pclass, gender, age, sibsp, parch, fare, embarked]])
		pred = prediction[0]
		out = "Error"
		if pred ==1:out = "Survived"
		else: out = "Didn't Survived"
		return render_template('index.html', results = out)
	else:
		return render_template('index.html')
		
		

if __name__ == "__main__":
	app.run(debug = True)