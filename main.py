import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

app = Flask(__name__)


# Home Page route
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/enternew")
def enternew():
    return render_template("add.html")


@app.route("/results")
def results():
    return render_template("result.html")


@app.route("/addrec", methods=['POST', 'GET'])
def addrec():
    pass_list = []
    for char in range(nr_letters):
        pass_list.append(random.choice(letters))

    for char in range(nr_symbols):
        pass_list += random.choice(symbols)

    for char in range(nr_numbers):
        pass_list += random.choice(numbers)

    random.shuffle(pass_list)

    password1 = ""
    for char in pass_list:
        password1 += char

    print(f"Your password is: {password1}")
    # Data will be available from POST submitted by the form
    if request.method == 'POST':
        nm = request.form['nm']
        if len(nm) == 0:
            print("Enter something")
            return render_template("add.html")
        with sqlite3.connect('passSaver1.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO password_tbl (name, password) VALUES (?,?)", (nm, password1))
            print("it was a success")
            con.commit()
            return render_template('result.html', msg1=nm, passw=password1)


if __name__ == "__main__":
    app.run(debug=True)
