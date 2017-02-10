from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'password'

@app.route('/')
def  index():
    return render_template("index.html")

@app.route('/process', methods=['post'])
def results():
    errors = False
    if len(request.form['name'])< 1:
        errors = True
        flash("name can't be blank.")
    if len(request.form['comment'])< 1:
        errors = True
        flash("comments can't be blank.")
    if len(request.form['comment'])> 120:
        errors = True
        flash("comments can't be longer than 120 characetrs.")
    if errors:
        return redirect('/')

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite'] = request.form['favorite']
    session['comment'] = request.form['comment']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('results.html')



app.run(debug=True)
