#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
#import pdb
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/item/new', methods=["GET", "POST"])
def new_item():
    #pdb.set_trace()
    if request.method == "POST":
        # Process the form data
        print("Form data:")
        print("Title: {}, Description: {}".format(
            request.form.get("title"), request.form.get("description")
        ))
        # Redirect to home page
        return redirect(url_for("home"))

    return render_template("new_item.html")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)