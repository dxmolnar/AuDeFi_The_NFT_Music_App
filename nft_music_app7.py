import streamlit as st
import boto3
from web3 import Web3

# Set page configuration
st.set_page_config(
    page_title="AuDeFi NFT Music App",
    page_icon="🎵",
    layout="wide",
)

# Adding custom CSS
st.markdown(
    f"""
    <style>
        .reportview-container {{
            background: url('./Images/audefibackg.png'); 
            background-size: cover;
        }}
        .sidebar {{
            background-color: rgba(0,0,0,0.1);
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Left side: Royalties and Staking
# st.sidebar.text(" ")  # Adds spacing

# Loading and displaying the "Broken Record.png" image
broken_record_image = "./images/Broken Record.png" 
st.sidebar.image(broken_record_image, width=100, caption="Broken Record")

# Displaying total royalties and time remaining staking
your_total_royalties = 15.25
your_time_remaining_staking = " 5 days" 

st.sidebar.write("Your total royalties:", your_total_royalties, "Eth")
st.sidebar.write("Your time remaining staking:", your_time_remaining_staking)

# Right side: Artist Profiles
st.sidebar.title("Artist Profiles")
st.sidebar.markdown("Select a song from the list:")

# Left side: Minting NFT
# st.markdown("## Mint, Buy & Sell Your Favorite Tunes!")
st.text(" \n")

# Right side: Artist Profiles
st.sidebar.title("Artist Profiles")
st.sidebar.markdown("Select a song from the list:")

# Mock artist profiles data
artist_profiles = {
    "DJ Brigitte": {
        "logo": "Images/DJ Brigitte.png",
        "songs": ["Soulseeker", "With Me", "Stay Another Night"],
    },
    "Josh Cruseiro": {
        "logo": "Images/Josh Cruseiro.png",
        "songs": ["Asta La Vista", "Baby", "I'll Be Back"],
    },
    "Yael Amari": {
        "logo": "Images/Yael Amari.png",
        "songs": ["Feelings of Love", "Darling Spotlight", "Passionate Angel"],
    },
    "Rachel Naomi": {
        "logo": "Images/Rachel Naomi.png",
        "songs": ["Time for One More Time", "Frozen Words", "10/10"],
    },
}

# Display artist profiles
for artist_name, artist_data in artist_profiles.items():
    st.sidebar.image(artist_data["logo"], width=200)
    st.sidebar.write("Artist:", artist_name)
    st.sidebar.write("Songs:")
    for song in artist_data["songs"]:
        st.sidebar.write(f"- {song}")
    st.sidebar.text(" \n")
    
###### Daniel #######    
# Initialize Web3
# ganache_url = "http://127.0.0.1:7545" 
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
# transaction_count = web3.eth.getTransactionCount('0xB4C19D6735dc5F3beB3b5045284DabB4352e5d54')

# Contract address and ABI
contract_address = "0xf8e81D47203A594245E36C48e151709F0C19fBe8" 
contract_abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "approved",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Approval",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"indexed": False,
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "ApprovalForAll",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"anonymous": False,
		"inputs": [
			{
				"indexed": True,
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"indexed": True,
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "Transfer",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "approve",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"name": "balanceOf",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "getApproved",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			}
		],
		"name": "isApprovedForAll",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_ipfsHash",
				"type": "string"
			}
		],
		"name": "mint",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "name",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "ownerOf",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "renounceOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			},
			{
				"internalType": "bytes",
				"name": "data",
				"type": "bytes"
			}
		],
		"name": "safeTransferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "operator",
				"type": "address"
			},
			{
				"internalType": "bool",
				"name": "approved",
				"type": "bool"
			}
		],
		"name": "setApprovalForAll",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "songs",
		"outputs": [
			{
				"internalType": "string",
				"name": "ipfsHash",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes4",
				"name": "interfaceId",
				"type": "bytes4"
			}
		],
		"name": "supportsInterface",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "symbol",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "tokenByIndex",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "index",
				"type": "uint256"
			}
		],
		"name": "tokenOfOwnerByIndex",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "tokenURI",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "totalSupply",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "from",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "to",
				"type": "address"
			},
			{
				"internalType": "uint256",
				"name": "tokenId",
				"type": "uint256"
			}
		],
		"name": "transferFrom",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

# Contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

###### Kevin #######

# Streamlit UI
st.title("AuDeFi NFT Music App")
st.markdown("## Mint, Buy & Sell Your Favorite Tunes!")
st.text(" \n")

# File uploader
uploaded_file = st.file_uploader("Choose an .mp3 music file", type="mp3")

if uploaded_file:
    st.audio(uploaded_file, format='audio/mp3')
    
    # Display file details
    st.write("Uploaded File Details:")
    st.write(f"File Name: {uploaded_file.name}")
    st.write(f"File Type: {uploaded_file.type}")
    st.write(f"File Size: {uploaded_file.size} bytes")

    # Create a mock NFT representation
    nft_name = st.text_input("Enter NFT Name")
    nft_description = st.text_area("Enter NFT Description")

    # Generate a mock NFT ID
    nft_id = hash(f"{nft_name}{nft_description}")

    # Display NFT details
    st.write("Generated NFT Details:")
    st.write(f"NFT Name: {nft_name}")
    st.write(f"NFT Description: {nft_description}")
    st.write(f"NFT ID: {nft_id}")
	
####### Daniel #######

    # Upload to Amazon S3
    s3 = boto3.client('s3')
    bucket_name = 'audefi-music-nft-app'
    file_name = uploaded_file.name
    s3.upload_fileobj(uploaded_file, bucket_name, file_name)
    
    st.write(f"File uploaded to Amazon S3: {bucket_name}/{file_name}")

    # Mint NFT by calling the mint function in the smart contract
    def mint_nft(ipfs_hash):
        user_account = web3.eth.accounts[0] 
        nonce = web3.eth.get_transaction_count(user_account)
        gas_price = web3.to_wei('1', 'gwei')
        tx = contract.functions.mint(ipfs_hash).build_transaction({
            'chainId': 1337,  # Update with your Ganache chain ID
            'gas': 2000000,
            'gasPrice': gas_price,
            'nonce': nonce,
        })
        signed_tx = web3.eth.account.sign_transaction(tx, private_key='0x173e6cbd6c65d7fab716cc85489cd0c73cff7a4f1901734461aa3cbd1cd66e34')
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3.eth.waitForTransaction_receipt(tx_hash)
        return receipt

    # Mint NFT on Ethereum (Ganache)
    if st.button("Mint this NFT", key="mint_button"):
        ipfs_cid = f"ipfs://{bucket_name}/{file_name}"
        mint_receipt = mint_nft(ipfs_cid)
        st.write("NFT Minted Successfully!")
        st.write("Transaction Hash:", mint_receipt['transactionHash'].hex())
        
st.markdown(
    """
    <style>
    	.reportview-container {{
           	background: url('./Images/audefibackg.png');  /* Adjust the path to your image file */
           	background-size: cover;
    	}}
    	.sidebar {{
           	background-color: rgba(0,0,0,0.5);
    	}}
    	#mint_button {{
           	background-color: #fffd80;
           	color: white;
           	border: none;
           	padding: 10px 20px;
           	text-align: center;
           	text-decoration: none;
           	display: inline-block;
           	font-size: 16px;
           	border-radius: 5px;
           	cursor: pointer;
    	}}
    	#mint_button:hover {{
           	background-color: #ff2b2b;
    	}}
	</style>
	""",
    unsafe_allow_html=True,
)

###### Kevin #####

# Validate NFT section
st.text(" \n")
st.markdown("## Validate NFT")

# Address input field
nft_address = st.text_input("Enter NFT Address")

# Validate button
if st.button("Validate"):
    if nft_address:
        # Here you can implement your validation logic
        st.write(f"Validating NFT at address: {nft_address}")
    else:
        st.warning("Please enter an NFT address to validate")



