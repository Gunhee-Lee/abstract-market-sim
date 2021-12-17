# -*- coding: utf-8 -*-
"""
@author: Gunhee LEE (gunheecs.lee@samsung.com)
@date: initially created on 2021/12/17.
"""
from decimal import *
import yaml

class Market:
    def __init__(self, config):
        self.turn = Turn(config["startTurn"], config["endTurn"])
        self.bank = Bank(config["initialMoney"])
    def StartSimulation(self):
        while self.turn.ProceedTurn() == True:
            print("  Do something in this turn -- still implementing.")
        return
    
class Actor:
    pass

class Turn:
    def __init__(self, startTurn, endTurn):
        self.startTurn = startTurn
        self.endTurn = endTurn
        self.currentTurn = startTurn
        self.turnIncrements = 1
    def ProceedTurn(self):
        if self.currentTurn <= self.endTurn:
            print("-- Current turn", self.currentTurn, "starts. --")
            self.currentTurn += self.turnIncrements
            return True
        else:
            print("  Reached endTurn", self.endTurn, ".")
            return False
                 
class Bank:
    def __init__(self, initialMoney):
        self.initialMoney = Decimal(initialMoney)   # is Decimal() idempotent?

class Treasury:
    def PrintMoney(self, amount):
        return
    
class Product:
    pass    

class Service:
    pass

def LoadConfigYaml():
    print("Loading default config.yaml file...")
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config
    
def Main():
    print("Abstract market simulator v0.1")
    config = LoadConfigYaml()
    print(config)
    market = Market(config)
    market.StartSimulation()
    
if __name__ == "__main__":
    Main()