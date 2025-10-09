import streamlit as st

st.subheader("Image :")
# If you have a local file named 'kid.jpg' it will be used; otherwise a web image is shown.
local_path = "kid.jpg"
fallback_url = "https://images.unsplash.com/photo-1544005313-94ddf0286df2?q=80&w=1200&auto=format&fit=crop"
try:
    st.image(local_path)
except Exception:
    st.image(fallback_url)

st.subheader("Audio :")
# Local 'audio.mp3' if present, else a sample URL
audio_local = "audio.mp3"
audio_url = "https://file-examples.com/storage/fe7f2b6049a4f2b2a3a6d88/2017/11/file_example_MP3_700KB.mp3"
try:
    st.audio(audio_local)
except Exception:
    st.audio(audio_url)

st.subheader("Video :")
# Local 'video.mp4' if present, else a sample URL
video_local = "video.mp4"
video_url = "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4"
try:
    st.video(video_local)
except Exception:
    st.video(video_url)
