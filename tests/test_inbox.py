import pdb

from compiler.compiler import compile_inbox

# brownie automatically generates fixtures for your contracts
def test_deploy(Inbox, accounts):
    # instantiate an Inbox contract with 1 arg 
    # (constructor initialMessage param)
    inbox = Inbox.deploy(
        "wololo", 
        {
            'from': accounts[0], 
            'gas': '1000000',  # gas limit (max gas this txn can use)
            'gasPrice': '50000' # price in wei
        }
    )
    assert inbox.address
    assert inbox.message() == 'wololo'
    assert accounts[0].gas_used > 0
    # all accounts have the same opening balance we use account[1] 
    # as a comparison
    assert accounts[0].balance() == accounts[1].balance() - accounts[0].gas_used * 50000


def test_set_message(Inbox, accounts):
    inbox = Inbox.deploy(
        "foo", 
        {'from': accounts[0], 'gas': '1000000'}
    )

    tx = inbox.setMessage('bar')
    assert inbox.message() == 'bar'
