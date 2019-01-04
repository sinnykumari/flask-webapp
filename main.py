from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

@app.route("/")
def index():
    user_details = []
    if os.path.exists('user_details.json'):
        with open("user_details.json", "r") as read_file:
              user_details = json.load(read_file)
    return render_template("index.html", user_details=user_details)

@app.route("/about")
def about():
    return render_template("about.html")

# Use POST method to get details from register form
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        _username = request.form['username']
        _fullname = request.form['inputName']
        _email = request.form['inputEmail']
        _dob = request.form['dob']
        # Add information in our json file
        user_detail = {'username': _username,
                       'fullname': _fullname,
                       'email':_email,
                        'dob': _dob}
        user_details = []
        if os.path.exists('user_details.json'):
            with open("user_details.json", "r") as read_file:
                user_details = json.load(read_file)
                read_file.close()
        with open("user_details.json", "w") as write_file:
            user_details.append(user_detail)
            json.dump(user_details, write_file, indent=4)
            write_file.close()
        return render_template("success.html")
    if request.method == 'GET':
        return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
