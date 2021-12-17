# -*- coding: utf-8 -*-
"""
@author: Gunhee LEE (gunheecs.lee@samsung.com)
@date: initially created on 2021/12/17.
"""
from decimal import *
import yaml

class Market:
    pass

class Actor:
    pass

class Turn:
    def __init__(self, startTurn, endTurn):
        self.startTurn = startTurn
        self.endTurn = endTurn
        self.currentTurn = startTurn
        self.turnIncrements = 1
    def proceedTurn(self):
        print("-- Current turn", self.currentTurn, "starts. --")
        if self.currentTurn < self.endTurn:
            self.currentTurn += self.turnIncrements
            return True
        else:
            print("  Reached end of turn", self.endTurn, ".")
            return False

class Bank:
    pass

class Treasury:
    pass
    


def loadConfigYaml():
    print("Loading default config.yaml file...")
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config
    
def main():
    print("Abstract market simulator v0.1")
    config = loadConfigYaml()
    print(config)
    print(config["startTurn"])
    
if __name__ == "__main__":
    main()