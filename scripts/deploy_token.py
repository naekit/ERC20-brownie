from scripts.helpful_scripts import get_account
from brownie import MyToken, network, config
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")


def deploy_token():
    account = get_account()
    token = MyToken.deploy(initial_supply, 
    {"from": account})
    print(token)


def main():
    deploy_token()