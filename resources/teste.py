from flask_restful import Resource, reqparse

hoteis = [
  {
    'hotel_id': 'avenida',
    'hotel_name': 'Hotel Avenida',
    'estrelas': 4.2,
    'diaria': 80.00,
    'cidade': "Santa Rita do Sapucai"
  },
  {
    'hotel_id': 'lidia',
    'hotel_name': 'Hotel Lidia',
    'estrelas': 2.3,
    'diaria': 30.00,
    'cidade': "Pouso Alegre"
  },
  {
    'hotel_id': 'cidade',
    'hotel_name': 'Hotel Cidade',
    'estrelas': 3.5,
    'diaria': 60.00,
    'cidade': "Alfenas"
  }
]

class Hoteis(Resource):
  def get(self):
    return {'hoteis': hoteis}

class Hotel(Resource):
  def get(self, hotel_id):
    for hotel in hoteis:
      if hotel['hotel_id'] == hotel_id:
        return hotel
    return {'message' : 'hotel not found'}, 404 # Not found

  def post(self, hotel_id):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('hotel_name')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')

    dados = argumentos.parse_args()

    novo_hotel = {
        'hotel_id' : hotel_id,
        'hotel_name': dados['hotel_name'],
        'estrelas' : dados['estrelas'],
        'diaria' : dados['diaria'],
        'cidade' : dados['cidade']
    }

    hoteis.append(novo_hotel)
    return novo_hotel

  def put(self, hotel_id):
    pass

  def delete(self, hotel_id):
    pass
