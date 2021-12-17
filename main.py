# -*- coding: utf-8 -*-
"""
@author: Gunhee LEE (gunheecs.lee@samsung.com)
@date: initially created on 2021/12/17.
"""
import yaml

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