import streamlit as st
from ghibli_image.services.image_generator import GhibliImageGenerator
from ghibli_image.services.history_service import save_to_history

def render_input():
    generator = GhibliImageGenerator()
    st.markdown('<h2 class="section-title">Create Your Artwork</h2>', unsafe_allow_html=True)

    # Preset prompts section
    st.markdown("<p style='color: rgba(255, 255, 255, 0.7); font-size: 1rem; margin-top: 20px; margin-bottom: 10px;'><strong>Select a Model:</strong></p>", unsafe_allow_html=True)

    model_options = [
        "Stable Diffusion v2.1",
        "DALL-E 3",
        "Midjourney",
        "Custom Model"
    ]

    selected_model = st.selectbox(
        "Choose your AI model",
        model_options,
        label_visibility="collapsed",
        key="model_selector"
    )

    st.session_state.selected_model = selected_model

    default_prompt = ""

    user_prompt = st.text_area(
        "Enter Prompt:",
        value=default_prompt,
        placeholder="Describe your Ghibli scene in detail... e.g., 'A magical forest with glowing spirits and ancient trees under moonlight'",
        height=250,
        key="prompt_input",
        help="Be descriptive! Include colors, mood, time of day, and specific Ghibli elements"
    )

    # Generate button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        generate_btn = st.button("✨ Generate Artwork", use_container_width=True)

    # Handle generation
    if generate_btn and user_prompt:
        with st.spinner('Creating your masterpiece...'):
            try:
                # Generate image (replace this with your actual model call)
                generated_image = generator.generate(user_prompt)
                
                # Save to history
                save_to_history(user_prompt, generated_image)
                
                st.success("✅ Your artwork has been created successfully!")
                
            except Exception as e:
                st.error(f"❌ Generation failed: {str(e)}")

    elif generate_btn and not user_prompt:
        st.warning("⚠️ Please enter a prompt first!")