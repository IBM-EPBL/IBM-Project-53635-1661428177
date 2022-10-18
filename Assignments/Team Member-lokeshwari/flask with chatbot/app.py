from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/home')
def login():

    return render_template('editportfolio.html')

@app.route('/result',methods=['POST', 'GET'])
def onLogin():
    formData = request.form.to_dict()
    name = formData['name']
    if(name == 'ALWA'):
        return render_template('editportfolio.html', name=name)
    else:
        return render_template('home.html',name=name)





if __name__ == '__main__':
    app.run()
