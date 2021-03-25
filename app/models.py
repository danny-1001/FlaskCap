from app import db 


class User(db.Model):
    user_id = db.Column (db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, default=f'{first_name}{last_name}@codingtemple.com')
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User: {self.email}>'