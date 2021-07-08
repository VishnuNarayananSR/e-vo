import os
import brownie.project as project
from brownie import network, accounts


def main(MEDIA_ROOT):
    network.connect('gui')
    EthereumProject = project.load('ethereum')
    contract = EthereumProject.Voting
    address = contract.deploy({'from':accounts[0]})
    if not os.path.exists(MEDIA_ROOT):
        os.mkdir(MEDIA_ROOT)
    filepath = os.path.join(MEDIA_ROOT, 'deploymentAddress.txt')
    with open(filepath, 'w') as f:
        f.write(str(address))