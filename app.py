import requests
import streamlit as st
from PIL import Image
from io import BytesIO


url = "https://instagram-profile-picture-viewer.p.rapidapi.com/"

st.title("Instagram Profile Picture Downloader📸")
insta_id = st.text_input("Instagram ID (without @)")

if insta_id:
	querystring = {"username": insta_id}

	headers = {
		"X-RapidAPI-Key": "07a7eecbbamsh04b5e9dd4dfc3edp1dbe6ajsn56bdbbf5520d",
		"X-RapidAPI-Host": "instagram-profile-picture-viewer.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	data = response.json()
	image_url = data['profile_picture_url']
	response2 = requests.get(image_url)
	image = Image.open(BytesIO(response2.content))
	st.image(image, caption=data['username'])
	temp_file = BytesIO()
	image.save(temp_file, format='JPEG')
	temp_file.seek(0)

	st.download_button("Download Profile Picture", temp_file, file_name=f"{insta_id}_profile_picture.jpg")
	st.title("Bio")
	st.text(data['bio'])
	st.title("Followers")
	st.text(data['followers'])
	st.title("Fullname")
	st.text(data['fullname'])
