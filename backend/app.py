from flask import request, jsonify
from config import app, db
from models import Post


@app.route("/posts", methods=['GET'])
def get_posts():
  posts = Post.query.all()
  result = [post.to_json() for post in posts]
  return jsonify({"posts": result})





if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)