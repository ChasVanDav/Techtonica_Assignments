from flask import Flask, render_template, request, redirect

# create instance of app
app = Flask(__name__)

# Establish homepage route linked to html page
@app.route("/")
# function to display html page dynamically
def home():
    return render_template("index.html")

# run the app
if __name__ == '__main__':
    app.run (debug=True)