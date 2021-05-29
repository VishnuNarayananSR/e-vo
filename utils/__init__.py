from io import open_code
from web3 import Web3
import json
from django.conf import settings
import os

def get_abi():
    with open('ethereum/build/contracts/Voting.json') as f:
        file = json.load(f)
        abi = file['abi']
        return abi

def get_contract_address():
    filepath = os.path.join(settings.MEDIA_ROOT, 'deploymentAddress.txt')

    with open(filepath) as f:
        address = f.read()
        return address
