from flask import request, jsonify
from config import app, db
from models import Post


@app.route("/posts", methods=['GET'])
def get_posts():
  posts = Post.query.all()
  result = [post.to_json() for post in posts]
  return jsonify({"posts": result})

@app.route("/posts", methods=['POST'])
def create_post():
  data = request.json

  title = data.get("title")
  author = data.get("author")
  description = data.get("description")
  imgUrl = data.get("imgUrl")

  if not author or not description or not title:
    return (
      jsonify({"Message": "You must include a title, author, and description"})
    )
  
  new_post = Post(title=title, author=author, description=description, img_url=imgUrl)
  try:
    db.session.add(new_post)
    db.session.commit()
  except Exception as e:
        return jsonify({"message": str(e)}), 400

  return jsonify({"message": "post created successfully"}), 201

@app.route("/posts/<int:id>", methods=['DELETE'])
def delete_post(id):
  post = Post.query.get(id)
  if not post:
    return jsonify({"message": "post not found"}), 404
  
  db.session.delete(post)
  db.session.commit()
  return jsonify({"message": "post deleted successfully"}), 200


if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)