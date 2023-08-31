// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract SongNFT is ERC721Enumerable, Ownable {
    using Strings for uint256;

    struct Song {
        string uri;
        address owner;
    }

    Song[] public songs;

    constructor() ERC721("SongNFT", "SNFT") {}

    function mint(string memory _uri) external {
        Song memory newSong = Song({
            uri: _uri,
            owner: msg.sender
        });
        songs.push(newSong);
        uint256 newSongId = songs.length - 1;
        _mint(msg.sender, newSongId);
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        return songs[tokenId].uri;
    }
}
