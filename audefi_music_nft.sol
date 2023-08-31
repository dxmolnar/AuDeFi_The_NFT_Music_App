// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract AudioNFT is ERC721Enumerable, Ownable {
    using Strings for uint256;

    struct Song {
        string ipfsHash;
    }

    Song[] public songs;

    constructor() ERC721("AudioNFT", "ANFT") {}

    function mint(string memory _ipfsHash) public {
        Song memory newSong = Song({
            ipfsHash: _ipfsHash
        });
        songs.push(newSong);
        uint256 newSongId = songs.length - 1;
        _mint(msg.sender, newSongId);
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(tokenId < songs.length, "Token ID out of range");
        string memory ipfsHash = songs[tokenId].ipfsHash;
        return string(abi.encodePacked("https://ipfs.io/ipfs/", ipfsHash));
    }

    // Implement totalSupply() function from IERC721Enumerable
    function totalSupply() public view override returns (uint256) {
        return songs.length;
    }
}
