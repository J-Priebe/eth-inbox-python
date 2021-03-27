import solcx
from os import path
import pdb
# this might be useless because brownie has compilation tools...?
# perhaps only for dev and we still want to compile/deploy with solc/web3 directly
def compile_inbox():
    contract_path = path.join(
        path.dirname(__file__), 
        '..', 
        'contracts', 
        'Inbox.sol'
    )
    # install runs once?
    # solcx.install_solc('0.7.4')
    res = list(solcx.compile_files(
        contract_path,
        output_values=["abi", "bin-runtime"],
        solc_version='0.7.4',
    ).values())[0]
    return res['abi'], res['bin-runtime']


if __name__ == '__main__':
    print(compile_contracts)

'''
{'contracts/Inbox.sol:Inbox': {'abi':
 [{'inputs': [{'internalType': 'string', 'name': 
 'initialMessage', 'type': 'string'}], 
 'stateMutability': 'nonpayable', 'type': 'constructor'},
  {'inputs': [], 'name': 'message', 'outputs':
   [{'internalType': 'string', 'name': '', 'type': 'string'}], 
   'stateMutability': 'view', 'type': 'function'}, 
   {'inputs': [{'internalType': 'string', 'name': 'newMessage', 'type': 'string'}], 'name': 'setMessage', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}],
    'bin-runtime': 'LONG_BIN_HERE'}}

'''