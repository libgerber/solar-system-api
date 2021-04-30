from app import db
# from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET", "POST"])
def handle_planets():
    return "hello"


# def handle_books():
#     if request.method == "GET":
#         books = Book.query.all()
#         books_response = []
#         for book in books:
#             books_response.append({
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             })
#         return jsonify(books_response)
#     elif request.method == "POST":
#         request_body = request.get_json()
#         new_book = Book(title=request_body["title"],
#                         description=request_body["description"])

#         db.session.add(new_book)
#         db.session.commit()

#         return make_response(f"Book {new_book.title} successfully created", 201)


# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = Book.query.get(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#     }
