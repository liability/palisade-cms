import sys,os,codecs

from flask import Flask,g,request,render_template
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.restless import APIManager
#from restless import APIManager


"""
mysql -u 'root' -p
DROP DATABASE a2;
CREATE DATABASE a2;
GRANT ALL PRIVILEGES ON a2.* TO 'a2'@'localhost' IDENTIFIED BY 'a2'; FLUSH PRIVILEGES;
exit
"""



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s.sqlite' % __name__
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://a2:a2@localhost/a2'
app.secret_key="sdjk2j3ofod"
app.template_folder='../templates'
app.static_folder='../static'
db = SQLAlchemy(app)
#app.project_path=get_project_path()

from palisade.models import *
from palisade.views import *

db.create_all()

#p=Preference(keyname="Test",value="Test2")
#db.session.add(p)
#db.session.commit()


@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return ""

"""
@app.route('/edit/<path:path>', methods=['GET','POST'])
def edit(path):
    c={}
    c['path']=path
    c['content']=codecs.open(path,'r','utf-8').read()
    print c['content']
    return render_template('edit.html', **c)
"""
