from flask import Blueprint,render_template, request
views=Blueprint(__name__,'views')
@views.route("/")
def home():
    return render_template('homepage.html')      
@views.route("/announcements")
def announcements():
    return render_template("announcement.html")
@views.route("/events")
def events():
    return render_template("events.html")   
@views.route("/execom2021")
def execom2021():
    return render_template("execom2020.html") 
@views.route("/login")
def login():
    return render_template("login.html")        
