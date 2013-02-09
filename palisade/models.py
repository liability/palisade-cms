#encoding:utf8

from palisade import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(150))

    def __init__(self, keyname, value):
        self.keyname=keyname
        self.value=value

    def __repr__(self):
        return "<User('%s', '%s')>" % (self.username, self.password)



class Preference(db.Model):
    __tablename__ = 'preference'

    id = db.Column(db.Integer, primary_key=True)
    keyname = db.Column(db.String(50))
    value = db.Column(db.String(150))

    def __init__(self, keyname, value):
        self.keyname=keyname
        self.value=value

    def __repr__(self):
        return "<Preference('%s', '%s')>" % (self.keyname, self.value)


class Item(db.Model):
    __tablename__ = 'item'
    __mapper_args__ = {'order_by':'item_index'}

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    index = db.Column(db.Integer())
    title = db.Column(db.String(100))
    slug = db.Column(db.String(250))
    published = db.Column(db.Boolean)
    content = db.Column(db.Text)
    images = db.relationship("Image", cascade="all", backref=db.backref("item", remote_side='Item.id'))

    def __init__(self, **kw):
        for k,v in kw.items():
            if hasattr(self,k):
                setattr(self,k,v)


class Image(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    itype = db.Column(db.String(50)) # png, jpg
    text = db.Column(db.String(250))
    alt = db.Column(db.String(50))
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    filesize = db.Column(db.Integer)
    filename = db.Column(db.String(100))
    original = db.Column(db.Boolean) # original images are new used directly
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))

    def __init__(self, **kw):
        for k,v in kw.items():
            if hasattr(self,k):
                setattr(self,k,v)


