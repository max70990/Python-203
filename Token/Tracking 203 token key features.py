from web3 import Web3
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO)

# Infura project ID
INFURA_PROJECT_ID = "f6b751d1f86b42f2bd23af09b4547634"
INFURA_URL = f"https://sepolia.infura.io/v3/{INFURA_PROJECT_ID}"

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check connection
if web3.is_connected():
    logging.info("Connected to the Sepolia testnet via Infura.")
    logging.info(f"Current block number: {web3.eth.block_number}")
else:
    logging.error("Failed to connect to the Sepolia testnet.")
    exit()

# Contract address 
CONTRACT_ADDRESS = "0xA0f0a2D53b3476c50F2Cf24307F8a1Cd3c758254"  

# Contract ABI
CONTRACT_ABI = json.loads('''
[
    {
        "inputs": [{"internalType": "address","name": "initialOwner","type": "address"}],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [{"internalType": "address","name": "to","type": "address"},{"internalType": "uint256","name": "amount","type": "uint256"}],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "address","name": "account","type": "address"}],
        "name": "balanceOf",
        "outputs": [{"internalType": "uint256","name": "","type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string","name": "","type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string","name": "","type": "string"}],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"internalType": "uint256","name": "","type": "uint256"}],
        "stateMutability": "view",
        "type": "function"
    }
]
''')

# Initialize contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Fetch and print key elements of the token
try:
    # Get token details
    token_name = contract.functions.name().call()
    token_symbol = contract.functions.symbol().call()
    total_supply = contract.functions.totalSupply().call()
    deployer_balance = contract.functions.balanceOf("0x0390cF896B4a7D984017e6C9D3d17b5A6287a874").call()

    # Print token information
    logging.info(f"Token Address: {CONTRACT_ADDRESS}")
    logging.info(f"Token Name: {token_name}")
    logging.info(f"Token Symbol: {token_symbol}")
    logging.info(f"Total Supply: {web3.from_wei(total_supply, 'ether')} tokens")
    logging.info(f"Deployer's Balance: {web3.from_wei(deployer_balance, 'ether')} tokens")

except Exception as e:
    logging.error(f"Error fetching token details: {e}")
