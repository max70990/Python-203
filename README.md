# Python project - Maxime Altrichter

# Project description 

## Project overview
The Python203 package is designed to create a tokenized reward system that remunerates users for submitting profitable financial backtests. The reward mechanism evaluates backtests based on two key performance metrics: Sharpe Ratio (representing risk-adjusted returns) and Maximum Drawdown (representing risk exposure). Users are rewarded with cryptocurrency tokens proportional to the quality of their backtesting results.

To demonstrate this reward system, I developed a volume-based backtesting strategy as an example of a user-submitted strategy. This strategy uses trading signals derived from volume patterns to showcase how backtests are evaluated and rewarded. By integrating blockchain technology into the framework, the package ensures seamless reward distribution, transparency, and accountability.

The Python203 package leverages:

- Pybacktestchain for advanced backtesting capabilities,
- ERC-20 token contracts for blockchain-based rewards,
- A streamlined process to evaluate user-submitted strategies and distribute rewards securely.

This system bridges traditional financial research and modern blockchain technology, creating an incentive for users to collaborate and innovate in the field of financial strategy development.

## Integration of pybacktestchain
As part of the project, I will utilize the pybacktestchain library to enhance the backtesting capabilities. This library will serve as the foundation for running and validating backtesting strategies. I will extend its functionality to incorporate blockchain-based rewards, ensuring that backtesting outputs can seamlessly connect to the tokenized reward system.

## Cryptocurrency implementation
The core of the project is the implementation of an ERC-20 token on an Ethereum-compatible blockchain. This cryptocurrency will serve as the reward mechanism, allowing users to earn tokens for their contributions. The token will include essential functionalities such as transferring tokens, minting new tokens, and approving transactions. I will write the smart contract for the token in Solidity, deploy it on Ethereum testnets for testing, and integrate it with Python using web3.py.

## Reward mechanism
I will define criteria for distributing tokens through the reward system. Users will earn rewards for:
- Developing profitable backtesting strategies using pybacktestchain.
- Contributing innovative or efficient approaches to the framework.
- Validating and adding new blocks to the blockchain.
The reward system will be automated to ensure that tokens are distributed based on predefined rules and user performance metrics.

## Blockchain integration with Python
Using web3.py, I will enable seamless interaction with the deployed blockchain. This integration will allow the Python-based application to manage token transactions, monitor the blockchain for new blocks, and execute smart contract functions. The blockchain connection will be established through an Ethereum node provider like Infura or Alchemy, ensuring reliable and secure interactions.

