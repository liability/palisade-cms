#import sys,datetime,os,imp,json,threading,time,os

import flask
from flask import Flask, request, redirect, session, render_template, flash, Markup, stream_with_context, Response

#from werkzeug.routing import Map, Rule, RequestRedirect, BuildError
#from werkzeug.exceptions import HTTPException, NotFound

from palisade import db, app
from palisade import User, Preference, Item, Image

#from sqlalchemy import event

@app.route('/', methods=['GET'])
def dashboard():
    c={}
    c['files']=[1,2,3]
    return render_template('index.html', **c)
