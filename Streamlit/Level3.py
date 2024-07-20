"""
Displaying   Images , audio and video as Input
"""

import streamlit as st
import asyncio

async def main():
    st.title("Displaying Media in Streamlit")

    # Image
    st.header("Displaying an Image")
    image_url = "https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png"
    st.image(image_url, caption="Streamlit Logo", use_column_width=True)
    
    # You can also display local images
    st.image("/Users/eshantdas/Desktop/India.png", caption="Local Image")

    st.markdown("<br>", unsafe_allow_html=True)

    # Audio
    st.audio("/Users/eshantdas/Downloads/wind-chimes-37762.mp3")
    
    # You can also play audio from a URL
    # audio_url = "https://example.com/audio.mp3"
    # st.audio(audio_url)

    st.markdown("<br>", unsafe_allow_html=True)

    # Video
    st.header("Playing Video")
    video_file = open("/Users/eshantdas/Downloads/Eren & Zeke vs Reiner, Porco and Pieck FULL FIGHT _ [Attack on Titan] 2022.mp4", "rb")
    st.video(video_file)
    
    # You can also play videos from a URL
    # video_url = "https://example.com/video.mp4"
    # st.video(video_url)

if __name__ == "__main__":
    asyncio.run(main())

