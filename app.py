from flask import Flask, render_template, request, redirect, url_for
import slope_of_bone_calculator
import converter
from flask_frozen import Freezer 
import sys, os

app = Flask(__name__)
freezer = Freezer(app)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/Analysis/", methods = ["POST"])
def Analysis():
    uploaded_file = request.files['file']

    if uploaded_file.filename != "":
        text = request.form['text']
        print("1")
        converter.converter(uploaded_file.filename, text)
        print("2")
        converted = text + ".jpg"
        print("3")
        angle = slope_of_bone_calculator.run_code(converted)
        print("4")
        return "<p>{x} from file {y} </p>".format(x = angle, y = converted)

    else:
        return render_template('index.html')
    


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        print("x")
        freezer.freeze()
    else:
        app.run()