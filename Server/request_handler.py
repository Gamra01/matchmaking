import socket 
import threading 
from player import Player
from game import Game
import json

server ="" 
port =  4000

class Server(object):
    PLAYERS = 1

    def __init__(self):
        self.connections_queue = []
        self.game_id = 0

    # def player_thread(self, conn, player):

    #     while True:
    #         try:
    #             #
    #             pass
    #             try: 
    #                 data = conn.rect(1024)
    #                 data = json.loads(data.decode())
    #                 print("[LOG] Received data:", data)
    #             except Exception as e:
    #                 break

    #             # Player ne fait pas partie du jeu 
    #             keys = [int(key) for key in data.keys()]
    #             send_smg = {key:[] for key in keys}    
