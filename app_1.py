import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="Valentine Card 💖", layout="wide")

# ---------- Add Custom CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #FFB6C1, #FFC0CB);
    margin: 0;
    padding: 0;
}

.card-container {
    text-align: center;
    position: relative;
    z-index: 2;
    width: 100%;
    display: inline-block;
}

.card-image {
    max-width: 100%;
    height: auto;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    display: block;
    width: 100%;
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
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    # Load card image and add text to it
    card_image = Image.open("card.png").convert("RGBA")
    
    # Create a copy to write text on
    card_with_text = card_image.copy()
    draw = ImageDraw.Draw(card_with_text)
    
    # Define text lines with emojis (using simpler emojis that render properly)
    text_lines = [
        "On behalf of all Learners,",
        "",
        "Dear Arihanth Sir,",
        "",
        "You are not just a Mentor, but",
        "the guiding light of our journey.",
        "",
        "Like a torch in the darkness,",
        "you illuminate the path of our careers.",
        "",
        "Your wisdom and patience light our",
        "present and shape our future.",
        "",
        "Twinkle, Twinkle Little Star —",
        "Arihanth Sir, Our Super Star!",
        "",
        "Forever grateful for your guidance",
        "and inspiration."
    ]
    
    # Try to use a nice font, fall back to default if not available
    try:
        text_font = ImageFont.truetype("arial.ttf", 25)
    except:
        text_font = ImageFont.load_default()
    
    # Add text to image (centered, with dark red/maroon color)
    text_color = (139, 0, 0)  # Dark red
    img_width, img_height = card_with_text.size
    
    # Position text in the middle white space of the card
    # Adjust these values based on your card's white space area
    x_position = img_width // 2
    y_start = img_height // 3  # Start from roughly 1/3 down the card
    line_spacing = 25
    
    # Draw each line of text
    for i, line in enumerate(text_lines):
        y_position = y_start + (i * line_spacing)
        draw.text((x_position, y_position), line, fill=text_color, font=text_font, anchor="mm", align="center")
    
    # Display the card with text overlaid
    st.image(card_with_text, use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

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


