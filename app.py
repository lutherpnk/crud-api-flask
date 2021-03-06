from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    age = db.Column(db.Integer)

    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

db.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'email', 'age')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Create new user
@app.route("/user", methods=['POST'])
def add_user():
    username = request.json['username']
    email = request.json['email']
    age = request.json['age']
    new_user = User(username, email, age)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


# Show all users
@app.route('/user', methods=['GET'])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


# Get user detail by ID
@app.route('/user/<id>', methods=['GET'])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# Update user
@app.route('/user/<id>', methods=['PUT'])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']
    user.email = email
    user.username = username
    db.session.commit()
    return user_schema.jsonify(user)


# Delete user by ID
@app.route('/user/<id>', methods=['DELETE'])
def user_delete_by_id(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
