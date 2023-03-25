from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.jobs import Jobs
from flask import request, jsonify


def abort_if_news_not_found(jobs_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(jobs_id)
    if not job:
        abort(404, message=f"Jobs {jobs_id} not found")


class NewsResource(Resource):
    def get(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(jobs_id)
        return jsonify({'jobs': job.to_dict(
            only=('team_leader', 'job', 'id', 'is_published'))})

    def delete(self, jobs_id):
        abort_if_news_not_found(jobs_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(jobs_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

class NewsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        job = session.query(Jobs).all()
        print("asdasd")
        return jsonify({'news': [item.to_dict(
            only=('id', 'team_leader','job', 'work_size', 'collaborators', 'is_finished')) for item in job]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        news = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_published=args['is_published']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})



parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True)
parser.add_argument('collaborators', required=True, type=int)
parser.add_argument('is_finished', required=True, type=bool)


