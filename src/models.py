from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Primera(db.Model):
    __tablename__ = "primera"
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    lastname = db.Column(db.String(250), unique=False, nullable=False)
    age = db.Column(db.String(250), unique=False, nullable=False)
    segunda = db.relationship('Segunda',backref='owner_primera', lazy=True)

    def __repr__(self):
        return '<Primera %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "segunda": list(map(lambda x: x.serialize(), self.segunda)),
          
        }


class Segunda(db.Model):
    __tablename__ = 'segunda'
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    lastname = db.Column(db.String(250), unique=False, nullable=False)
    age = db.Column(db.String(250), unique=False, nullable=False)
    primera = db.Column(db.Integer, db.ForeignKey('primera.id'))
    tercera = db.relationship('Tercera',backref='owner_segunda', lazy=True)


    def __repr__(self):
        return '<Segunda %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "primera": self.primera,  
            "tercera": list(map(lambda x: x.serialize(), self.tercera)),     
            # do not serialize the password, its a security breach
        }

class Tercera(db.Model):
    __tablename__ = "tercera"
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=False, nullable=False)
    lastname = db.Column(db.String(250), unique=False, nullable=False)
    age = db.Column(db.String(250), unique=False, nullable=False)
    segunda = db.Column(db.Integer, db.ForeignKey('segunda.id'))

    def __repr__(self):
        return '<Tercera %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "age": self.age,
            "segunda": self.segunda, 
            
        }