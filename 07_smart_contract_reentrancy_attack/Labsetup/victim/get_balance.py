#!/bin/env python3

from web3 import Web3
import SEEDWeb3

def print_balance(_web3, address):
    if address != None:
       caddr = Web3.toChecksumAddress(address)
       print("{}: {}".format(caddr, _web3.eth.get_balance(caddr)))
    else:
       print("Address is None!")

web3 = SEEDWeb3.connect_to_geth_poa('http://10.150.0.71:8545')

# Get the balance of the accounts on the geth node 
print("----------------------------------------------------------")
print("*** Node: 10.150.0.71")
print("*** The following are the accounts on this Ethereum node")
for acct in web3.eth.accounts:
    print_balance(web3, acct)
print("----------------------------------------------------------")


# Get the balances of the victim contract 
# Please use the correct address.
try:
  victim_addr = '0xaf98236bcb084ADc949f43d647eb4045260b31F3'
  print("  Victim: ", end='')
  print_balance(web3, victim_addr)
except:
  print()
  print("Exception captured: Please put the actual address in the code")
