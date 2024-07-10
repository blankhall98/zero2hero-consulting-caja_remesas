from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#register
@auth.route('/register')
def register():
    return render_template('auth/register.html')


#documentation
@auth.route('/documentation')
def documentation():
    return render_template('auth/documentation.html')