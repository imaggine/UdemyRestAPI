from flask_restful import Resource, reqparse
from models.hotel import HotelModel

class Hoteis(Resource):
  def get(self):
    return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]}

class Hotel(Resource):
  argumentos = reqparse.RequestParser()
  argumentos.add_argument('nome', type=str, required=True, help="Field nome required")
  argumentos.add_argument('estrelas')
  argumentos.add_argument('diaria')
  argumentos.add_argument('cidade', type=str, required=True, help="Field nome required")
  
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
    try:
      hotel.save_hotel()
    except:
      return {'message' : 'Error trying to save hotel'}, 500
    return hotel.json()

  def put(self, hotel_id):

    dados = Hotel.argumentos.parse_args()
    #novo_hotel = hotel_objeto.json()
    #novo_hotel = { 'hotel_id' : hotel_id, **dados }
    hotel_encontrado = HotelModel.find_hotel(hotel_id)
    if hotel_encontrado:
      hotel_encontrado.update_hotel(**dados)
      try:
        hotel_encontrado.save_hotel()
      except:
        return {'message': 'Error trying to save hotel'}, 500
      return hotel_encontrado.json(), 200 # Ok
    hotel = HotelModel(hotel_id, **dados)
    try:
      hotel.save_hotel()
    except:
      return {'message' : 'Error trying to save hotel'}, 500
    return hotel.json(), 201

  def delete(self, hotel_id):
    hotel = HotelModel.find_hotel(hotel_id)
    if hotel:
      try:
        hotel.delete_hotel()
      except:
        return {'message': 'Error trying to delete hotel'}, 500
      return {'message': 'Hotel deleted'}
    return {'message':'hotel not found'}, 404

    #global hoteis
    #hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
