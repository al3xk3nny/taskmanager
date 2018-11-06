from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


@app.route("/")
def get_index():
    return render_template("index.html")


@app.route("/result")
def result():
    this_x = request.args['x']
    this_y = request.args['y']
    button_value = request.args['action']
    
    if button_value == "Add":
        return redirect(url_for("add", x=this_x, y=this_y)) 
        
    if button_value == "Mult":
        return redirect(url_for("mult", x=this_x, y=this_y))        


@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    s = x + y
    return "{0} + {1} = {2}".format(x, y, s)

    
@app.route("/mult/<int:x>/<int:y>")
def mult(x, y):
    s = x * y
    return "{0} * {1} = {2}".format(x, y, s)


if __name__ == "__main__":
   app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)