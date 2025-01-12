#!/bin/env python3
from web3 import Web3
from eth_account import Account

web3 = Web3(Web3.HTTPProvider('http://10.150.0.71:8545'))

# Sender's private key 
key = '20aec3a7207fcda31bdef03001d9caf89179954879e595d9a190d6ac8204e498'
sender = Account.from_key(key)

recipient = Web3.toChecksumAddress('0xCBF1e330F0abD5c1ac979CF2B2B874cfD4902E24')
tx = {
  'chainId':  1337, 
  'nonce':    web3.eth.getTransactionCount(sender.address),
  'from':     sender.address,
  'to':       recipient,
  'value':    Web3.toWei("9", 'ether'),
  'gas':      200000,
  'maxFeePerGas':         Web3.toWei('4', 'gwei'),
  'maxPriorityFeePerGas': Web3.toWei('3', 'gwei'),
  'data':     ''
}

# Sign the transaction and send it out
signed_tx  = web3.eth.account.sign_transaction(tx, sender.key)
tx_hash    = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# Wait for the transaction to appear on the blockchain
print("Transaction sent, waiting for receipt ...")
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction Receipt: {}".format(tx_receipt))
