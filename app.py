"""Flask app for Cupcakes"""
from flask import Flask, render_template, request, redirect, flash, jsonify, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SECRET_KEY'] = "SECRET!"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


with app.app_context():
    db.create_all()

app.app_context().push()


@app.route('/api/cupcakes', methods=["GET"])
def get_all_cupcakes():
    """ Get data about all cupcakes."""

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)



@app.route('/api/cupcakes/<int:id>')
def get_single_cupcake(id):
    """ Get data about one cupcake."""

    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake = cupcake.serialize())



@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """ Create new cupcake. """

    cupcake = Cupcake(
                            flavor = request.json['flavor'],
                            size = request.json['size'],
                            rating = request.json['rating'],
                            image = request.json['image'] or None)
    db.session.add(cupcake)
    db.session.commit()
    response_json = jsonify(cupcake = cupcake.serialize())
    return (response_json, 201)



@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """ Update existing cupcake. """

    cupcake = Cupcake.query.get_or_404(id)
    request.json
    cupcake.flavor = request.json.get('flavor')
    cupcake.size = request.json.get('size')
    cupcake.rating = request.json.get('rating')
    cupcake.image = request.json.get('image')
    db.session.commit()
    return jsonify(cupcake = cupcake.serialize())



@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """ Delete a cupcake. """

    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")



@app.route('/')
def show_form():
    """ Show form to submit new cupcake."""

    return render_template('index.html')