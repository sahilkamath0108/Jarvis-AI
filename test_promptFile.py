# import win32com.client
# speaker = win32com.client.Dispatch('SAPI.SpVoice')

# voices = speaker.GetVoices()

# selected_voice = voices.Item(0)

# speaker.Voice = selected_voice

# speaker.Speak("Hello")



import pyttsx3

engine = pyttsx3.init()

# Set properties such as voice and rate (if desired)
voices = engine.getProperty('voices')  # Uncomment to see available voices
engine.setProperty('voice', voices[2].id)  # Set the voice (index might vary)

# Say something
engine.say("Hello, I'm using a different TTS engine now.")
engine.runAndWait()

for i, voice in enumerate(voices):
    print(f"Voice {i}: {voices}")
