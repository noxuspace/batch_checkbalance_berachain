from web3 import Web3
from prettytable import PrettyTable
import time

file_path = './wallet.txt'
rpc_bera = 'https://bartio.rpc.berachain.com/'

balance_bera = []

def read_file_to_list(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Strip newline characters from each line
        lines = [line.strip() for line in lines]
    return lines

def get_balance(address):
    balance_wei = w3.eth.get_balance(address)
    balance_eth = balance_wei / 10**18
    return balance_eth

start_time = time.perf_counter()
w3 = Web3(Web3.HTTPProvider(rpc_bera))
with open(file_path, 'r') as file:
    addresses = file.readlines()
for address in addresses:
    address = address.strip()
    if address:
        balance = get_balance(address)
        balance_bera.append(balance)

address = read_file_to_list(file_path)

table = PrettyTable()
table.add_column("address",address)
table.add_column('Balance Bera',balance_bera)
table.align = "r"
finish_time = time.perf_counter()

print(table)
print(f'Total BERA for all wallet : {sum(balance_bera)} BERA')
print(f'Task done in {round(finish_time-start_time,2)} seconds')
