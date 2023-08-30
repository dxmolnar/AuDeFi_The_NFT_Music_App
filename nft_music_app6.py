import streamlit as st
import boto3

# Streamlit UI
st.title("AuDeFi NFT Music App")

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

    # Upload to Amazon S3
    s3 = boto3.client('s3')
    bucket_name = 'audefi-music-nft'
    file_name = uploaded_file.name
    s3.upload_fileobj(uploaded_file, bucket_name, file_name)
    
    st.write(f"File uploaded to Amazon S3: {bucket_name}/{file_name}")
