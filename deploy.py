import os
import brownie.project as project
from brownie import network, accounts
from ethereum.scripts.deploy import main

MEDIA_ROOT = "./media"

main(MEDIA_ROOT)

