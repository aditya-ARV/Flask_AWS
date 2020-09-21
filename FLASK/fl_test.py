from flask import Flask, render_template
from forms import AddProduct, ViewProduct
app = Flask(__name__)

app.config['SECRET']='9db126da28c6987fff511fe4bbc2fe25'

data = [ {'Name':'STM32F207','Size':'32bit','Family' : 'ARM', 'Flash':'1MB'},
         {'Name':'ATMEGA328P-PU','Size':'8bit','Family' : 'AVR', 'Flash':'32kB'}]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',product=data)

@app.route("/test")
def test():
    return "<h1>Flask is testpage</h1>"

@app.route("/AddP")
def Add():
    form = AddProduct()
    return render_template('add.html',form=form)

@app.route("/ViewP")
def Add():
    form = ViewProduct()
    return render_template('view.html',form =form)
 
if __name__ == '__main__':
    app.run(debug=True)

    
