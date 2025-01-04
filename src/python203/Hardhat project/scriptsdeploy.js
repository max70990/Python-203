const hre = require("hardhat");

async function main() {
    // Get the deployer's address (signer)
    const [deployer] = await hre.ethers.getSigners();

    console.log("Deploying contract with the account:", deployer.address);

    // Get the contract factory
    const RewardToken = await hre.ethers.getContractFactory("RewardToken");

    // Deploy the contract, passing the deployer's address as the initial owner
    const rewardToken = await RewardToken.deploy(deployer.address);

    // Wait for deployment to finish
    await rewardToken.deployed();

    console.log("RewardToken deployed to:", rewardToken.address);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
