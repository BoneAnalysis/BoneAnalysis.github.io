from flask import Flask, render_template, request, redirect, url_for
import slope_of_bone_calculator


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/Analysis/", methods = ["POST"])
def Analysis():
    print("ANALYSIS POOPING?")
    uploaded_file = request.files['filename']
    print("CAN YOU SEE THIS?")

    if uploaded_file.filename != "":
        print("FILE UPLOADED")
        uploaded_file.save("THIS IS A TEST")

    angle = slope_of_bone_calculator.run_code()
    print(angle)
    return "<p>{x}</p>".format(x = angle)


if __name__ == "__main__":
    app.run()