from io import open_code
# from web3 import Web3
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
    # w3 = Web3(Web3.HTTPProvider(NETWORK_URL))
    web3.connect(NETWORK_URL)
    transaction_details = {'from': web3.eth.accounts[1]}
    if admin:
        transaction_details['from'] = web3.eth.accounts[0]
    # contract = w3.eth.contract(get_contract_address(), abi=get_abi())
    contract = Contract('Voting', get_contract_address(), abi=get_abi())
    return contract, transaction_details, exceptions

contract, tx_details, exceptions = contract()


print(contract.getElectionState())
# # network.connect('gui')
# print(tx_details)
# web3.eth.default_account = web3.eth.accounts[0]
# try:
#     contract.createVoter('name', 2, 'constituency', tx_details)
# except exceptions.VirtualMachineError as e:
#     print(e.revert_msg)
# print(contract.getVotersList())
# print(web3.eth.accounts[1])