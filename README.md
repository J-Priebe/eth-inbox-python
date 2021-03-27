# Setup

globally install ganache-cli. this is a node library but we never interact with it directly. brownie will manage it for us.

npm install -g ganache-cli

-globally install brownie
- run brownie init
- setup venv: virtualenv venv
- source venv/bin/activate 
- pip3 install -r requirements.txt


# Testing
`brownie test`

# Deployment
IMPORTANT: When deploying non-locally, to a testnet or otherwise, you must use a real account that has an ETH balance on the network being deployed to.

https://eth-brownie.readthedocs.io/en/latest/account-management.html

Either generate a new account 
```
brownie accounts generate deployment_test
```
Or add an existing account (you will need to input the account's private key) :
```
brownie accounts new deployment_from_my_existing_account
```


`brownie run deploy.py --network rinkeby`
When you run via `brownie run` your contracts are automagically modularized
and can be imported. I.e., `Inbox.deploy..`

You also need an Infura account:
https://eth-brownie.readthedocs.io/en/latest/network-management.html

Create an infura account and a new project. export your project id.

Then run the deploy command and check out the transaction in etherscan. ezpz

Also cool: brownie maintains map of live-deployed contracts and remembers them so they can be interacted with. so we can find a deployed contract and read from it, set a new message, etc.