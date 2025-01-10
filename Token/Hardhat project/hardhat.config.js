require("@nomiclabs/hardhat-ethers");

module.exports = {
    solidity: "0.8.20",  // Make sure the Solidity version matches your contract
    networks: {
        sepolia: {
            // Correct string interpolation for the Infura URL
            url: `https://sepolia.infura.io/v3/f6b751d1f86b42f2bd23af09b4547634`,  // Use backticks for string interpolation
            accounts: ["3a078e0c831b014a8ff42a99b0e58718eecd856abf4ca040eaada338b9c33077"]
        },
    },
};
