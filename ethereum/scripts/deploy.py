import os
from django.conf import settings
import brownie.project as project
from brownie import network, accounts


def main():
    network.connect('gui')
    EthereumProject = project.load('ethereum')
    contract = EthereumProject.Voting
    address = contract.deploy({'from':accounts[0]})
    if not os.path.exists(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)
    filepath = os.path.join(settings.MEDIA_ROOT, 'deploymentAddress.txt')
    with open(filepath, 'w') as f:
        f.write(str(address))
