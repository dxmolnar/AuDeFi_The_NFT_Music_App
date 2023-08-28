import streamlit as st
from web3 import Web3

st.title("Digitize Your Songs!")

# Connect to Metamask
w3 = Web3(Web3.HTTPProvider('<http://127.0.0.1:7545>'))
connected = w3.is_connected()

if connected:
    st.write("Connected to Ethereum")
else:
    st.write("Not connected to Ethereum. Please check your connection.")

# Upload music file
uploaded_file = st.file_uploader("Upload your song")

if uploaded_file:
    # TODO: Store the music file on a cloud (e.g., IPFS, S3) 
    # and retrieve the URI/link for the song
    song_uri = upload_to_cloud(uploaded_file)

    # Mint the NFT using the URI/link
    if st.button("Mint NFT"):
        # TODO: Use Web3.py to call the mint function of your contract
        mint_nft(song_uri)
        st.write("NFT minted!")
