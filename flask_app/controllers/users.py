from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.user import User

@app.route('/')                 
def index():
    return redirect('/users')

@app.route('/users')         
def users():
    return render_template('users.html', users=User.get_all(), title='Users')

@app.route('/users/new')
def new_user():
    return render_template('new_user.html', title='New User')

@app.route('/user/create', methods=['POST'])
def create():
    # print(request.form,"request.form")
    User.save(request.form)
    return redirect('/users')

# new routing begins here

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id':id
    }
    return render_template('edit_user.html', title='edit', user=User.get_one(data))

@app.route('/user/print/<int:id>')
def print(id):
    data= {
        'id':id
    }
    return render_template("print_user.html", title='print', user=User.get_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/users')