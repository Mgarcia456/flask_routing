from flask import Flask  
app = Flask(__name__)    



@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')          
def dojo():
    return 'welcome to the dojo!'  

@app.route('/say/flask')          
def flask():
    return 'Hi flask!'  

@app.route('/say/michael')          
def michael():
    return 'Hi michael!'  

@app.route('/say/john')          
def john():
    return 'Hi john!'  
#    this one will work for all of the last things for number 4
@app.route('/repeat/<int:times>/<someVar>')          
def repeat(times, someVar):
    print(times, someVar)
    return f'<p>{someVar}<p>'*times  





if __name__=="__main__":   
    app.run(debug=True, port = 5000)    

