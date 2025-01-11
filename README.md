# Python project - Maxime Altrichter

# Project description 

## Project overview
The **python203** package is designed to create a tokenized reward system that **remunerates** users for submitting **profitable** financial backtests. The reward mechanism evaluates backtests based on two key performance metrics: **Sharpe Ratio** (representing risk-adjusted returns) and **Maximum Drawdown** (representing risk exposure). Users are rewarded with **cryptocurrency tokens** proportional to the quality of their backtesting results.

To demonstrate this reward system, I developed a **volume-based** backtesting strategy as an example of a user-submitted strategy. This strategy uses trading signals derived from volume patterns to showcase how backtests are evaluated and rewarded. By integrating blockchain technology into the framework, the package ensures seamless reward distribution, transparency, and accountability.

The Python203 package leverages:

- Pybacktestchain for advanced backtesting capabilities,
- ERC-20 token contracts for blockchain-based rewards,
- A streamlined process to evaluate user-submitted strategies and distribute rewards securely.

This system bridges traditional financial research and modern blockchain technology, creating an incentive for users to collaborate and innovate in the field of financial strategy development.

## Explanation of volumebacktest
The VolumeBacktest Strategy serves as a demonstration of how an end-user's trading strategy might be integrated into the reward system. This strategy leverages trading volume patterns to generate buy or sell signals, a common approach in technical analysis used by financial professionals and retail traders alike. The premise of this strategy is that significant deviations in trading volume, relative to historical averages, can signal potential market opportunities. For instance, unusually high trading volume may indicate heightened interest in a stock and serve as a buy signal, while low trading volume could suggest reduced liquidity or declining interest, triggering a sell signal.

This example is used purely for **demonstration purposes**, showcasing how the python203 package evaluates strategies based on their performance metrics (e.g., Sharpe Ratio and Maximum Drawdown) and rewards users accordingly. By including this volume-based strategy, the package demonstrates its flexibility in adapting to user-submitted backtests.

## Explanation of backtestevaluator
The *backtestevaluator* class plays a crucial role in the python203 package by evaluating user-submitted backtests based on two performance metrics: Sharpe Ratio and Maximum Drawdown. These metrics are designed to objectively assess both the profitability and risk of a strategy.

To ensure a **balanced grading system**, the Sharpe Ratio contributes 75% of the final score, reflecting its importance in measuring risk-adjusted returns, while Maximum Drawdown accounts for 25%, highlighting its role in managing risk exposure. This weighted approach ensures that strategies with high returns and controlled risks are rewarded appropriately.

The BacktestEvaluator’s decisions emphasize fairness and precision, aligning rewards with strategies that demonstrate both profitability and sound risk management. By doing so, it sets the foundation for transparent and meaningful tokenized incentives.

## Reward mechanism overview
### Smart contract on Sepolia testnet
The reward system uses an **ERC-20 smart contract** deployed on the **Sepolia** testnet. Named RewardToken, the contract mints a **fixed supply** of 203 tokens to the deployer during deployment. Key features include:
- ERC-20 Standard: Ensures compatibility with wallets and tools.
- Fixed Supply: Guarantees a transparent and finite reward pool.
- Purpose: Automates and secures reward distribution for backtesting performance.

Using a smart contract ensures transparency, automation, and trust by leveraging blockchain’s immutable and decentralized nature. 
I used the Sepolia testnet to safely develop and test the reward mechanism in a realistic Ethereum environment without incurring real-world costs or risks.

I used the Google Cloud Sepolia Faucet (https://cloud.google.com/application/web3/faucet/ethereum/sepolia) to acquire free Sepolia ETH, which is essential for paying gas fees required to execute transactions on the Sepolia testnet.

### Why I used Hardhat ? 
I used Hardhat which is a development framework for Ethereum used to streamline smart contract writing, testing, and deployment. 
It offers:
- Easy Deployment: Simplified scripts like the provided deploy.js.
- Powerful Features: Local blockchain simulation, debugging, and gas estimation.
- Integration: Compatibility with OpenZeppelin and Ethereum libraries.

### Why I used Infura ?
I used Infura as it provides reliable access to the Ethereum network without running a local node. 
I choosed Inufura mainly for:
- Ease of Use: Quick connection to Sepolia via an API.
- Reliability: Stable network access for transactions and interactions.
- Scalability: Handles high request volumes seamlessly.

### Key Token features
The RewardToken is an ERC-20 token deployed on the Sepolia testnet with a total fixed supply of 203 tokens. I chose a fixed supply of 203 tokens and disabled additional minting to **preserve the token's value** and prevent devaluation, ensuring a fair and stable reward system.

It is named **Master203token** and uses the symbol **203T**. The token is designed to **incentivize** users for **profitable** backtesting results. The contract is deployed at 0xA0f0a2D53b3476c50F2Cf24307F8a1Cd3c758254 and can be view using Sepolia Etherscan at https://sepolia.etherscan.io/token/0xA0f0a2D53b3476c50F2Cf24307F8a1Cd3c758254
