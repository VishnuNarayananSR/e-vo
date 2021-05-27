import brownie.project as project
from brownie import network, accounts


def main():
    network.connect('gui')
    EthereumProject = project.load('ethereum')
    contract = EthereumProject.Voting
    address = contract.deploy({'from':accounts[0]})
    return address
