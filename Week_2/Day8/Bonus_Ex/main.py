from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/skillio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Sport(db.Model):
	__tablename__ = 'sports'
	id = db.Column(db.Integer, primary_key=True)
	sport_name = db.Column(db.String(100), nullable=False)
	sport_desc = db.Column(db.String(255), nullable=False)
	example_player = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		return f"Sport: {self.sport_name}"
	
def add_sport(sport_name, sport_desc, example_player):
	new_sport = Sport(
		sport_name=sport_name,
		sport_desc=sport_desc,
		example_player=example_player
	)
	db.session.add(new_sport)
	db.session.commit()

def get_all_sports():
	sports_list = Sport.query.all()
	sports = [{'id': sport.id, 'sport_name': sport.sport_name, 'sport_desc': sport.sport_desc, 'example_player': sport.example_player} for sport in sports_list]
	return jsonify({'sports': sports})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sports', methods=['GET', 'POST'])
def handle_sports():
	if request.method == 'GET':
		return get_all_sports()

	elif request.method == 'POST':
		data = request.json
		add_sport(sport_name=data['sport_name'], sport_desc=data['sport_description'], example_player=data['example_player'])
		return jsonify({'message': 'Sport added successfully'})
	
if __name__ == "__main__":
	app.run(debug=True)