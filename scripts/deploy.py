import os
from brownie import Inbox, accounts

# Must have an Infura account and configured project ID 
# to deploy to a non-local network
# e.g.,
# brownie run deploy.py --network rinkeby
def main():
    acct = accounts.load(os.getenv('TESTNET_DEPLOYMENT_ACCOUNT_NAME'))
    inbox = Inbox.deploy('My first message', {'from': acct})
