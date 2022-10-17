
from socket import *
from web3 import Web3
from eth_utils import *
from eth_typing import *

#根据题目描述所获取的各类信息
uuid ='xxxx'     						#唯一标识符
URL = 'http://127.0.0.1:8545' + uuid    #远程节点url
privatekey = 'xxxx'      				#私钥
contract = 'xxxx'   					#合约地址


#在Remix里compile，获取到Setup.sol中合约Setup的abi
config = {
'abi':
[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "isSolved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "random",
		"outputs": [
			{
				"internalType": "contract Random",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
}


#Random.sol中合约Random的abi
config1 ={
	'abi':
	[
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "guess",
				"type": "uint256"
			}
		],
		"name": "solve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "solved",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
}
web3 = Web3(Web3.HTTPProvider(URL))       							#连接到指定的节点
contract2 = web3.eth.contract(address=contract,abi=config['abi'])	#合约实例化，获取返回的合约地址，得到当前Setup实例
result = contract2.functions.isSolved().call()
print(result)
randomAddress = contract2.functions.random().call()					#获取其中random实例的合约地址
print(randomAddress)

contract1 = web3.eth.contract(address= randomAddress,abi=config1['abi']) #合约实例化，获取返回的合约地址，得到当前Random实例
result = contract1.functions.solve(4).transact()						 #调用random.solve(4)
print(result)

