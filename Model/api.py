#!/usr/bin/python
from flask import Flask
from flask_restplus import Api, Resource, fields
import joblib
from Model_Price import predict_price

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Car Price Prediction',
    description='Get car price based on its description')

ns = api.namespace('predict', 
     description='Price Prediction')
   
parser = api.parser()

parser.add_argument(
    'Year', 
    type=int, 
    required=True, 
    help="car's Year", 
    location='args')

parser.add_argument(
    'Mileage', 
    type=int, 
    required=True, 
    help="car's Mileage", 
    location='args')

parser.add_argument(
    'State', 
    type=str, 
    required=True, 
    help="car's State", 
    location='args')

parser.add_argument(
    'Make', 
    type=str, 
    required=True, 
    help="car's maker", 
    location='args')

parser.add_argument(
    'Model', 
    type=str, 
    required=True, 
    help="car's model", 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PriceApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_price(args)
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)
