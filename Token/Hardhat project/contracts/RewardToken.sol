// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract RewardToken is ERC20 {
    constructor(address initialOwner) ERC20("Master203token", "203T") {
        // Mint a constant supply of 203 tokens to the initial owner
        _mint(initialOwner, 203 * 10**decimals());
    }
}
