from io import open_code
import json
from django.conf import settings
import os
from brownie import Contract, network, exceptions, web3

NETWORK_URL = 'http://127.0.0.1:7545'

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

def contract(admin=False):
    web3.connect(NETWORK_URL)
    transaction_details = {'from': web3.eth.accounts[1]}
    if admin:
        transaction_details['from'] = web3.eth.accounts[0]
    contract = Contract('Voting', get_contract_address(), abi=get_abi())
    return contract, transaction_details, exceptions