// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RewardToken is ERC20, Ownable {
    constructor(address initialOwner) ERC20("RewardToken", "RWT") Ownable(initialOwner) {
        // Additional setup can be added here if necessary
    }

    // Mint new tokens (only the owner can call this function)
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
