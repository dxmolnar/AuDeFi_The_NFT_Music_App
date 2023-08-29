import streamlit as st
from web3 import Web3
import ipfshttpclient

st.set_option('deprecation.showfileUploaderEncoding', False)

# Connect to Ethereum
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
connected = w3.is_connected()

# Connect to IPFS
ipfs_client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')  # Assuming your IPFS daemon is running locally

# Streamlit UI
st.title("NFT Music App")

if connected:
   st.success("Connected to Ethereum")
else:
    st.error("Not connected to Ethereum. Please ensure your node/Ganache is running.")

# File uploader
uploaded_file = st.file_uploader("Choose a music file", type="mp3")

if uploaded_file:
    st.audio(uploaded_file, format='audio/mp3')
    
    # Upload to IPFS
    ipfs_response = ipfs_client.add(uploaded_file)
    song_ipfs_hash = ipfs_response['Hash']
    song_uri = f"https://ipfs.io/ipfs/{song_ipfs_hash}"
    
    # Display the URI or use it in your logic
    st.write(f"Song URI: {song_uri}")

    # ... any additional logic you have
