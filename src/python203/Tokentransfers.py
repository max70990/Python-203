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
        "name": "transfer",
        "outputs": [{"internalType": "bool","name": "","type": "bool"}],
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

class TokenTransfer:
    def __init__(self, private_key: str, sender_address: str):
        """
        Initialize the TokenTransfer class.

        Args:
            private_key (str): The private key of the sender's wallet.
            sender_address (str): The sender's wallet address.
        """
        self.private_key = private_key
        self.sender_address = sender_address

    def get_balance(self, address: str):
        """
        Get the token balance of a given address.

        Args:
            address (str): The wallet address.

        Returns:
            float: The token balance in ether units.
        """
        balance = contract.functions.balanceOf(address).call()
        return web3.from_wei(balance, 'ether')

    def transfer_tokens_from_rating(self, user_address: str, rating: float):
        try:
            # Convert the rating to token units
            token_amount = web3.to_wei(rating, 'ether')

            # Get balances before the transaction
            sender_balance_before = contract.functions.balanceOf(self.sender_address).call()
            recipient_balance_before = contract.functions.balanceOf(user_address).call()
            total_supply_before = contract.functions.totalSupply().call()

            logging.info(f"Sender Balance Before: {web3.from_wei(sender_balance_before, 'ether')} tokens")
            logging.info(f"Recipient Balance Before: {web3.from_wei(recipient_balance_before, 'ether')} tokens")
            logging.info(f"Total Supply Before: {web3.from_wei(total_supply_before, 'ether')} tokens")

            # Create the transaction
            transaction = contract.functions.transfer(user_address, token_amount).build_transaction({
                'from': self.sender_address,
                'nonce': web3.eth.get_transaction_count(self.sender_address),
                'gas': 200000,
                'gasPrice': web3.to_wei('20', 'gwei'),  # Adjust gas price as needed
            })

            # Sign and send the transaction
            signed_transaction = web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

            logging.info(f"Transaction sent. TX hash: {web3.to_hex(tx_hash)}")

            # Wait for the transaction receipt
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            logging.info(f"Transaction confirmed. Receipt: {receipt}")

        except Exception as e:
            logging.error(f"Error transferring tokens: {e}")
            raise