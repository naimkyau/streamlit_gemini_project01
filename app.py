from PIL import Image
import streamlit as st
from api_call import note_generator, audio_transcription, quiz_generator


# Title
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate summary and Quizzas")
st.divider()


# Sidebar
with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the photo of you note", 
        type=['jpg','jpeg','png'], 
        accept_multiple_files=True
        )

    pil_image = []

    for i in images:
        tmp = Image.open(i)
        pil_image.append(tmp)

    if images:
        # st.image(images)
        if len(images) > 3:
            print("Upload at max 3 images.")
        else:
            st.subheader("Image uploaded!")
            col = st.columns(len(images))

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)


    # Difficulty
    selected = st.selectbox("Enter difficulty of your quiz", ('Easy', 'Medium', 'Hard'), index= None)

 
    pressed = st.button("Click the button to initiate AI", type="primary")


if pressed:
    if not images:
        st.error("You must upload 1 image")
    if not selected:
        st.error("You must select a difficulty")

    if images and selected:
        #Note
        with st.container(border=True):
            st.subheader("Your Note")
            with st.spinner("AI is writing note for you"):
                gen_txt = note_generator(pil_image)
                st.markdown(gen_txt)

        st.divider()

        #audio
        with st.container(border=True):
            st.subheader("Audio Transcription")
            with st.spinner("AI is writing note for you"):
                audio_script = audio_transcription(gen_txt)
                st.audio(audio_script)
        
        # st.divider()
        
        #quiz
        with st.container(border=True):
            st.subheader(f"Quiz ({selected}) Difficult")
            with st.spinner("AI is writing note for you"):
                quizz = quiz_generator(pil_image, selected)
                st.markdown(quizz)


        
