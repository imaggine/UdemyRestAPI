from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
  {
    'hotel_id': 'avenida',
    'nome': 'Hotel Avenida',
    'estrelas': 4.2,
    'diaria': 80.00,
    'cidade': "Santa Rita do Sapucai"
  },
  {
    'hotel_id': 'lidia',
    'nome': 'Hotel Lidia',
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
  argumentos = reqparse.RequestParser()
  argumentos.add_argument('nome')
  argumentos.add_argument('estrelas')
  argumentos.add_argument('diaria')
  argumentos.add_argument('cidade')
  
  def get(self, hotel_id):
    hotel = HotelModel.find_hotel(hotel_id)
    if hotel:
      return hotel.json()
    return {'message' : 'hotel not found'}, 404 # Not found

  def post(self, hotel_id):
    if HotelModel.find_hotel(hotel_id):
      return {"message" : "Hotel id '{}' already exists".format(hotel_id)}, 403 # Already Exists
    
    dados = Hotel.argumentos.parse_args()
    hotel = HotelModel(hotel_id, **dados)
    #novo_hotel = hotel_objeto.json()
    #novo_hotel = { 'hotel_id' : hotel_id, **dados }
    #hoteis.append(novo_hotel)
    #return novo_hotel
    hotel.save_hotel()
    return hotel.json()

  def put(self, hotel_id):

    dados = Hotel.argumentos.parse_args()
    hotel_objeto = HotelModel(hotel_id, **dados)
    novo_hotel = hotel_objeto.json()
    #novo_hotel = { 'hotel_id' : hotel_id, **dados }
    hotel = Hotel.find_hotel(hotel_id)
    if hotel['hotel_id'] == hotel_id:
      hotel.update(novo_hotel)
      return novo_hotel, 200 # Ok
    hoteis.append(novo_hotel)
    return novo_hotel

  def delete(self, hotel_id):
    global hoteis
    hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
    return {'message': 'Hotel deleted'}
