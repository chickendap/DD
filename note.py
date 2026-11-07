from flask import Flask, request, redirect, render_template_string
import sqlite3
app = Flask(__name__)
def home():
    return render_template("notes.html")
def add_note():
    return render_template("add_note.html")
