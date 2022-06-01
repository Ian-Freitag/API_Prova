from flask_restplus import fields
from src.config.restplus import api


jobhistory_request = api.model('JobHistory Request', {
    'employee_id': fields.Integer(required=True, description='jobhistory employee ID '),
    'title': fields.String(required=True, description='text title'),
    'startDate' : fields.String(required=True, description='date startDate'),
    'endDate' : fields.String(required=True, description='date endDate'),
    'salary' : fields.Float(required=True, description='salary'),
    'job' : fields.String(required=True, description='job description')

})

jobhistory_result = api.model('JobHistory Result', {
    'id': fields.Integer(required=True, description='JobHistory Id'),
    'title': fields.String(required=True, description='text title'),
    'employee_id': fields.Integer(required=True, description='jobhistory employee ID '),
    'startDate' : fields.String(required=True, description='date startDate'),
    'endDate' : fields.String(required=True, description='date endDate'),
    'salary' : fields.Float(required=True, description='salary'),
    'job' : fields.String(required=True, description='job description')

})
