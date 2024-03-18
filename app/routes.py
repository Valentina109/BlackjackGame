
from app import app
from flask import render_template, Flask, request, flash, url_for,redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from flask_login import LoginManager, UserMixin,login_user,login_required,current_user

from app.forms import LoginForm, RegistrationForm
import random
from flask import render_template, jsonify

# Initialize game statistics variables
total_games = 0
total_wins = 0

# Function to calculate win percentage
def calculate_win_percentage():
    return (total_wins / total_games) * 100 if total_games > 0 else 0

# Define your Flask routes
@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/leaderboard')
def leaderboard():
    return render_template('statistics.html', title='Leaderboard')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('registration.html', title='register',form=form)




# API Endpoint for statistics
@app.route('/statistics', methods=['GET'])
def get_statistics():
    stats = {
        "total_games": total_games,
        "total_wins": total_wins,
        "win_percentage": calculate_win_percentage()
    }
    return jsonify(stats)

@app.route('/playgame', methods=['POST', 'GET'])
def play_game_route():
    return render_template('playgame.html', title='playgame')