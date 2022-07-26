from re import L
from flask import Flask, make_response, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from main.model.pack import Pack, PackEncoder
from main.model.player import Player, PlayerEncoder
from main.model.lobby import Lobby, LobbyEncoder
from uuid import uuid4
from main.model.game import Game
import json
import jsonpickle

app = Flask(__name__)
# TODO figure this out, seems to be related to access control
CORS(app)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument("player_name")
parser.add_argument("lobby_name")

players = []
lobbies = []
games = []

pack_fields = {'cards': []}
class PackAPI(Resource):
    def get(self):
        p = Pack()
        p.generate_pack()
      
        returndata= json.dumps(p, cls=PackEncoder)
        resp = make_response(returndata, 200)
        return resp

        

class GameAPI(Resource):
    def get(self):
        return json.dumps(games)

    def post(self):
        args = parser.parse_args()
        game = Game(None)
        games.append(game)
        return game.gameid

class PlayerAPI(Resource):
    def get(self):
        return json.dumps(players, cls=PlayerEncoder)
    
    def put(self):
        args = parser.parse_args()
        player = Player(str(uuid4()), args['player_name'])
        players.append(player)

class LobbyAPI(Resource):
    def get(self):
        return json.dumps(lobbies, cls=LobbyEncoder)

    def put(self):
        args = parser.parse_args()
        name = args['lobby_name']
        lobby = Lobby(name)
        lobbies.append(lobby)

class LobbyInfoAPI(Resource):
    def post(self):
        args = parser.parse_args()
        lobby_name = args['lobby_name']
        lobby = None
        for l in lobbies:
            if l.name == lobby_name:
                lobby = l
                break
        return json.dumps(lobby, cls=LobbyEncoder)
    
class JoinLobbyAPI(Resource):
    def post(self):
        args = parser.parse_args()
        lobby_name = args['lobby_name']
        player = args['player_name']
        player_obj = None

        # find the player
        for p in players:
            if p.name == player:
                player_obj = p
                break

        # find the lobby
        for l in lobbies:
            if l.name == lobby_name:
                l.AddPlayer(player_obj)
                break

class StartGameAPI(Resource):
    def post(self):
        args = parser.parse_args()
        lobby_name = args['lobby_name']
        
        for l in lobbies:
            if l.name == lobby_name:
                g = Game(l.name, l.players)
                games.append(g)
                break

class PackInGameAPI(Resource):
    def post(self):
        args = parser.parse_args()
        lobby_name = args['lobby_name']
        player_name = args['player_name']

        for g in games:
            if g.name == lobby_name:
                for idx, p in enumerate(g.players):
                    if p.name == player_name:
                        return json.dumps(g.packs[idx], cls=PackEncoder)
                        

        

api.add_resource(PackAPI, "/")
api.add_resource(GameAPI, "/game")
api.add_resource(PlayerAPI, "/player")
api.add_resource(LobbyAPI, "/lobby")
api.add_resource(JoinLobbyAPI, "/joinlobby")
api.add_resource(LobbyInfoAPI, "/lobbyinfo")
api.add_resource(StartGameAPI, "/startgame")
api.add_resource(PackInGameAPI, "/packingame")

if __name__ == '__main__':
    app.run(port=5000,  debug=True)