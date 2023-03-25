from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.users import User
from flask import request, jsonify


def abort_if_news_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    print(user)
    if not user:
        abort(404, message=f"Jobs {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        job = session.query(User).get(user_id)
        return jsonify({'users': job.to_dict(
            only=('surname', 'name','age', 'position', 'speciality', 'address', 'email'))})

    def delete(self, user_id):
        print(user_id)
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        job = session.query(User).get(user_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('surname', 'name','age', 'position', 'speciality', 'address', 'email')) for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['ps']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})



parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True, type=bool)
parser.add_argument('address', required=True, type=bool)
parser.add_argument('email', required=True, type=bool)

