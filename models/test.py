from . import db

class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(30), nullable= False)

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return [{
            'id': self.id,
            'name': self.name
        }]