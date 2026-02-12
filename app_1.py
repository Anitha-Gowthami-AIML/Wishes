import streamlit as st
import base64

st.set_page_config(page_title="Valentine Card 💖", layout="wide")

# ---------- Add Custom CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #FFB6C1, #FFC0CB);
    margin: 0;
    padding: 0;
}

.main-card {
    background: linear-gradient(135deg, #FFB6C1, #FFC0CB);
    padding: 50px;
    border-radius: 25px;
    text-align: center;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    position: relative;
    z-index: 2;
    width: 100%;
}

.title {
    font-size: 48px;
    color: #8B0000;
    font-weight: bold;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.3);
}

.message {
    font-size: 18px;
    color: #A52A2A;
    margin-top: 20px;
    line-height: 1.8;
}

.heart {
    position: fixed;
    bottom: -10px;
    font-size: 48px;
    animation: floatUp 8s linear infinite;
}

@keyframes floatUp {
    0% {
        transform: translateY(0);
        opacity: 1;
    }
    100% {
        transform: translateY(-100vh);
        opacity: 0;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------- Card and Audio Player Aligned at Top ----------
col1, col2 = st.columns([4, 1])

with col1:
    st.markdown("""
    <div class="main-card">
        <div class="title">With Gratitude & Respect 🌟</div>
        <div class="message">
            Dear Arihanth Sir, <br><br>
            You are not just a Mentor, but the guiding light of our journey. 🔥 <br><br>
            Like a torch in the darkness, you illuminate the path of our careers. <br><br>
            Your wisdom and patience are the torch that lights our present and shapes the future we are building under your guidance..💛 <br><br>
            Twinkle, Twinkle Little Star — <br>
            Arihanth Sir, Our Super Star! ✨ <br><br>
            Forever grateful for your guidance and inspiration. 🙏
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.write("")  # Add spacing
    st.write("")  # Add spacing
    audio_file = open("super_star_song.mp3", "rb")  # Add your mp3 file in same folder
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")

# ---------- Floating Hearts & Celebration Elements ----------
import random

party_emojis = ["❤️", "🎈", "🧡", "🎉","💛", "💜", "🤍",  "🎊", "🎀", "✨", "⭐", "🌟", "💫", "🎁", "🎗️", "🎪"]

for i in range(25):
    left = random.randint(0, 100)
    duration = random.randint(5, 10)
    delay = random.randint(0, 5)
    emoji = random.choice(party_emojis)

    st.markdown(f"""
    <div class="heart" 
         style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s;">
         {emoji}
    </div>
    """, unsafe_allow_html=True)

