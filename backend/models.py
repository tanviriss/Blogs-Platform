from config import db

class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(100), nullable=False)
  author = db.Column(db.String(20), unique=False, nullable=False)
  description = db.Column(db.String(500), nullable=False)
  img_url = db.Column(db.String(200), unique=False, nullable=True)

  def to_json(self):
    return {
      "id": self.id,
      "title" : self.title,
      "author": self.author,
      "description": self.description,
      "imgUrl" : self.img_url,
    }