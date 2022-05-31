# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:04:28 2022

@author: HP
"""
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to The application"

@app.route('/user/<username>')
def user_function(username):
    return "Welcome %s" %username

@app.route('/logout')
def logout_function():
    return "Thank you"

if __name__=='__main__':
    app.run()

