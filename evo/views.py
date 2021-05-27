from django.http import HttpResponse
from django.shortcuts import render
from web3 import Web3
from solc import compile_standard
import os
import json

# compiled_sol = compile_standard({
#      "language": "Solidity",
#      "sources": {
#          "Voting.sol": {
#              "content": '''
#                     pragma solidity ^0.8.3;

#                     contract Voting {

                    
#                     mapping (bytes32 => uint256) public votesReceived;
                    

#                     bytes32[] public candidateList;

#                     constructor(bytes32[] memory candidateNames) public {
#                         candidateList = candidateNames;
#                     }


#                     function totalVotesFor(bytes32 candidate) view public returns (uint256) {
#                         require(validCandidate(candidate));
#                         return votesReceived[candidate];
#                     }


#                     function voteForCandidate(bytes32 candidate) public {
#                         require(validCandidate(candidate));
#                         votesReceived[candidate] += 1;
#                     }

#                     function validCandidate(bytes32 candidate) view public returns (bool) {
#                         for(uint i = 0; i < candidateList.length; i++) {
#                         if (candidateList[i] == candidate) {
#                             return true;
#                         }
#                         }
#                         return false;
#                     }
#                     }
#                '''
#          }
#      },
#      "settings":
#          {
#              "outputSelection": {
#                  "*": {
#                      "*": [
#                          "metadata", "evm.bytecode"
#                          , "evm.bytecode.sourceMap"
#                      ]
#                  }
#              }
#          }
#  })
# web3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))
# web3.eth.default_account = web3.eth.accounts[0]
# bytecode = compiled_sol['contracts']['Voting.sol']['Voting']['evm']['bytecode']['object']
# abi = json.loads(compiled_sol['contracts']['Voting.sol']['Voting']['metadata'])['output']['abi']
# contract = web3.eth.contract(abi=abi, bytecode=bytecode)

# # PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
# # contract_path = PROJECT_ROOT + '/evo/contracts/Voting.sol'
# # abi = json.loads('[{"inputs":[{"internalType":"bytes32[]","name":"candidateNames","type":"bytes32[]"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"candidateList","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"candidate","type":"bytes32"}],"name":"totalVotesFor","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"candidate","type":"bytes32"}],"name":"validCandidate","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"candidate","type":"bytes32"}],"name":"voteForCandidate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"name":"votesReceived","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
# # bytecode = '608060405234801561001057600080fd5b50600436106100575760003560e01c80632f265cf71461005c578063392e66781461008c5780637021939f146100bc578063b13c744b146100ec578063cc9ab2671461011c575b600080fd5b61007660048036038101906100719190610294565b610138565b6040516100839190610349565b60405180910390f35b6100a660048036038101906100a19190610294565b610166565b6040516100b39190610313565b60405180910390f35b6100d660048036038101906100d19190610294565b6101ef565b6040516100e39190610349565b60405180910390f35b610106600480360381019061010191906102bd565b610207565b604051610113919061032e565b60405180910390f35b61013660048036038101906101319190610294565b61022b565b005b600061014382610166565b61014c57600080fd5b600080838152602001908152602001600020549050919050565b600080600090505b6001805490508110156101e45782600182815481106101b6577f4e487b7100000000000000000000000000000000000000000000000000000000600052603260045260246000fd5b906000526020600020015414156101d15760019150506101ea565b80806101dc906103da565b91505061016e565b50600090505b919050565b60006020528060005260406000206000915090505481565b6001818154811061021757600080fd5b906000526020600020016000915090505481565b61023481610166565b61023d57600080fd5b600160008083815260200190815260200160002060008282546102609190610364565b9250508190555050565b60008135905061027981610452565b92915050565b60008135905061028e81610469565b92915050565b6000602082840312156102a657600080fd5b60006102b48482850161026a565b91505092915050565b6000602082840312156102cf57600080fd5b60006102dd8482850161027f565b91505092915050565b6102ef816103ba565b82525050565b6102fe816103c6565b82525050565b61030d816103d0565b82525050565b600060208201905061032860008301846102e6565b92915050565b600060208201905061034360008301846102f5565b92915050565b600060208201905061035e6000830184610304565b92915050565b600061036f826103d0565b915061037a836103d0565b9250827fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff038211156103af576103ae610423565b5b828201905092915050565b60008115159050919050565b6000819050919050565b6000819050919050565b60006103e5826103d0565b91507fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff82141561041857610417610423565b5b600182019050919050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b61045b816103c6565b811461046657600080fd5b50565b610472816103d0565b811461047d57600080fd5b5056fea264697066735822122090d37ac1d2cb9d3ad58a1cbfdd3f45b3b0f8bd2b32e5b7ef594dca8c11ed0b1a64736f6c63430008030033'
# # contract = web3.eth.contract(abi=abi, bytecode=bytecode)
# candidatelist = ['candidate1', 'candidate2', 'candidate3']
# candidatelist = list(map(lambda x:x.encode('utf-8').hex(), candidatelist))
# print(candidatelist)
# tx_hash = contract.constructor(candidatelist).transact()
# # contractName, contract_interface = compile_contract(contract)
# # con = web3.eth.contract(abi=contract_interface['abi'],bytecode=contract_interface['bin']);


def homepage(request):
    # return render(request, 'index.html', {'candidate':candidatelist})
    return render(request, 'base_layout.html')

def vote(request):
    return render(request, 'index.html')
