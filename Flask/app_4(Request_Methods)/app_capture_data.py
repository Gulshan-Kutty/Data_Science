from flask import Flask, render_template, request

app = Flask(__name__)

###############################################


@app.route('/', methods=['GET','POST'])
def fun_1():
    if request.method == 'POST':
        email = request.form['in_1'] # the data stored in 'in_1' will be now stored in variable 'email'
        return 'Welcome {}'.format(email)
    return render_template('index.html')

###############################################

if __name__ == '__main__':
    app.run(debug=True)