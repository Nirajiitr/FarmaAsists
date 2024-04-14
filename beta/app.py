import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
from flask import Flask, render_template, request, jsonify, redirect, url_for,session
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import warnings
warnings.filterwarnings('ignore')
model=keras.models.load_model('beta\ML\model1.h5',compile=False)
print('Model loaded')
def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    show_img = image.load_img(img_path, grayscale=False, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = np.array(x, 'float32')
    x /= 255
    preds = model.predict(x)
    p=np.argmax(preds,axis=1)
    x=''
    if(p==0):
        x='Early Blight'
    elif(p==1):
        x='Late Blight'
    else:
        x='Healthy'
    return x



app=Flask(__name__)  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()  
@app.route('/')
def index():
    return render_template('register.html')   
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/register',methods=['GET','POST'])        
def register():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(name=name,email=email,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        img = request.files['file']
        img_path = 'beta/uploads/' + img.filename
        img.save(img_path)
        result = model_predict(img_path, model)
        return jsonify({'result': result})

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/home')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')
@app.route('/about')
def about():
    return render_template('about.html')
 
if __name__ == '__main__':
    app.run(debug=True)
