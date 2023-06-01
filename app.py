import streamlit as st
import speech_recognition as sr


def main():
    st.title("Real-time Voice Transcription App")
    st.write("Click the microphone button and start speaking for real-time transcription.")

    # Create a button to start/stop the microphone recording
    button_text = "Start Recording"
    button_action = st.button(button_text)

    # Initialize the speech recognizer
    recognizer = sr.Recognizer()

    if button_action:
        # Start recording the microphone input
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)

        # Perform speech recognition
        try:
            text = recognizer.recognize_google(audio)
            st.write("Transcription:")
            st.write(text)
        except sr.UnknownValueError:
            st.write("Unable to transcribe the speech.")
        except sr.RequestError:
            st.write("Could not connect to the speech recognition service.")

if __name__ == "__main__":
    main()
