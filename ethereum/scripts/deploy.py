import os
from brownie import accounts, Voting


def main():
    deployed_contract = Voting.deploy({'from': accounts[0]})
    return deployed_contract
