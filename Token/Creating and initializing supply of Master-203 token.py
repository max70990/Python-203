from web3 import Web3
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO)

# Replace with your Infura project ID
INFURA_PROJECT_ID = "f6b751d1f86b42f2bd23af09b4547634"  # Your Infura project ID
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

# Contract address (replace with your deployed contract's address)
CONTRACT_ADDRESS = "0x48f752Da1eaC771A7250D726d73EE1b1Cd8b7A24"  

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

# Initialize the contract
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

# Replace with your deployer's private key
DEPLOYER_PRIVATE_KEY = "3a078e0c831b014a8ff42a99b0e58718eecd856abf4ca040eaada338b9c33077"  # Replace with your private key
DEPLOYER_ADDRESS = "0x0390cF896B4a7D984017e6C9D3d17b5A6287a874"  # Replace with your deployer address

# Mint 203 tokens
try:
    recipient_address = "0x0390cF896B4a7D984017e6C9D3d17b5A6287a874"  # Replace with the recipient's address
    mint_amount = web3.to_wei(203, 'ether')  # Convert 203 tokens to Wei (assuming 18 decimals)

    # Build the transaction
    nonce = web3.eth.get_transaction_count(DEPLOYER_ADDRESS)
    transaction = contract.functions.mint(recipient_address, mint_amount).build_transaction({
        'from': DEPLOYER_ADDRESS,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': web3.to_wei('20', 'gwei'),
    })

    # Sign the transaction
    signed_transaction = web3.eth.account.sign_transaction(transaction, DEPLOYER_PRIVATE_KEY)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    logging.info(f"Minted 203 tokens to {recipient_address}. Transaction hash: {web3.to_hex(tx_hash)}")

except Exception as e:
    logging.error(f"Error minting tokens: {e}")

# Test interaction with the contract
try:
    token_name = contract.functions.name().call()
    token_symbol = contract.functions.symbol().call()
    total_supply = contract.functions.totalSupply().call()

    logging.info(f"Token Name: {token_name}")
    logging.info(f"Token Symbol: {token_symbol}")
    logging.info(f"Total Supply: {web3.from_wei(total_supply, 'ether')} tokens")
except Exception as e:
    logging.error(f"Error interacting with the contract: {e}")

