from logging import addLevelName

from eth_utils import address
from web3 import contract
import brownie.project as project
from brownie import network, accounts


def main():
    network.connect('gui')
    EthereumProject = project.load('ethereum')
    contract = EthereumProject.Voting
    address = contract.deploy({'from':accounts[0]})
    return address, contract
