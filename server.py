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

class PackAPI(Resource):
    def get(self):
        p = Pack()
        p.generate_pack()
      
        returndata= json.dumps(p, cls=PackEncoder)
        resp = make_response(returndata, 200)
        return resp

        

class GameAPI(Resource):
    def get(self):
        resp = json.dumps(games)
        return resp

    def post(self):
        args = parser.parse_args()
        game = Game(None)
        games.append(game)
        resp = make_response(game.gameid, 200)
        return resp

class PlayerAPI(Resource):
    def get(self):
        resp = json.dumps(players, cls=PlayerEncoder)
        return resp

    def put(self):
        args = parser.parse_args()
        player = Player(str(uuid4()), args['player_name'])
        players.append(player)
        resp = make_response(200)
        return resp

class LobbyAPI(Resource):
    def get(self):
        resp = make_response(json.dumps(lobbies, cls=LobbyEncoder), 200)
        return resp

    def put(self):
        args = parser.parse_args()
        name = args['lobby_name']
        lobby = Lobby(name)
        lobbies.append(lobby)
        resp = make_response("", 200)
        return resp

class LobbyInfoAPI(Resource):
    def post(self):
        args = parser.parse_args()
        lobby_name = args['lobby_name']
        lobby = None
        for l in lobbies:
            if l.name == lobby_name:
                lobby = l
                break
        resp = make_response(json.dumps(lobby, cls=LobbyEncoder), 200)
        return resp
    
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
        resp = make_response(200)
        return resp

class StartGameAPI(Resource):
    def post(self):
        args = parser.parse_args()
        lobby_name = args['lobby_name']
        
        for l in lobbies:
            if l.name == lobby_name:
                g = Game(l.name, l.players)
                games.append(g)
                break

        resp = make_response(200)
        return resp

class PackInGameAPI(Resource):
    def post(self):
        args = parser.parse_args()
        lobby_name = args['lobby_name']
        player_name = args['player_name']

        for g in games:
            if g.name == lobby_name:
                for idx, p in enumerate(g.players):
                    if p.name == player_name:
                        resp = make_response(json.dumps(g.packs[idx], cls=PackEncoder), 200)
                        return resp
                        

        

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