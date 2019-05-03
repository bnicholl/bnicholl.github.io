from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for



app = Flask(__name__)
app.debug = True






@app.route('/')    
def ContractorClientPage():
    return render_template('ContractorClientPage.html')

@app.route('/ContractorPage')    
def ContracotrPage():
    return render_template('ContractorPage.html')

@app.route('/HomeOwnerPage')    
def FirstHomeOwnerPage():
    return render_template('HomeOwnerPage.html')



@app.route('/HomeOwnerPage/decks')    
def decks():
    return render_template('HomeOwnerForms/decks.html')

@app.route('/HomeOwnerPage/flooring')    
def flooring():
    return render_template('HomeOwnerForms/flooring.html')

@app.route('/HomeOwnerPage/outdoorwalkway')    
def carpentry():
    return render_template('HomeOwnerForms/outdoorwalkway.html')

@app.route('/HomeOwnerPage/labor')    
def labor():
    return render_template('HomeOwnerForms/labor.html')

@app.route('/HomeOwnerPage/hardscaping')    
def hardscaping():
    return render_template('HomeOwnerForms/hardscaping.html')

@app.route('/HomeOwnerPage/plumbing')    
def plumbing():
    return render_template('HomeOwnerForms/plumbing.html')

@app.route('/HomeOwnerPage/electrical')    
def electrical():
    return render_template('HomeOwnerForms/electrical.html')

@app.route('/HomeOwnerPage/landscaping')    
def landscaping():
    return render_template('HomeOwnerForms/landscaping.html')





if __name__ == '__main__':
    #app.debug = True
    app.run(host= '0.0.0.0')