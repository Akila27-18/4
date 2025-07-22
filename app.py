from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy credentials
DUMMY_EMAIL = "user@example.com"
DUMMY_PASSWORD = "password123"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == DUMMY_EMAIL and form.password.data == DUMMY_PASSWORD:
            flash("Login successful", "success")
            return redirect(url_for('login'))
        else:
            flash("Invalid credentials", "danger")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
