import streamlit as st
import base64
from io import BytesIO
from datetime import datetime
from PIL import Image

def save_to_history(prompt, image):
    buf = BytesIO()
    image.save(buf, format="PNG")

    st.session_state.image_history.insert(0, {
        "prompt": prompt,
        "image": base64.b64encode(buf.getvalue()).decode(),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def render_latest_image():
    if not st.session_state.image_history:
        return

    item = st.session_state.image_history[0]
    img = Image.open(BytesIO(base64.b64decode(item["image"])))

    st.image(img, use_container_width=True)
    
    # Download button at top left
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.download_button(
            label="⬇️ Download",
            data=buf.getvalue(),
            file_name=f"ghibli_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png",
            mime="image/png"
        )
