import win32com.client

speaker = win32com.client.Dispatch('SAPI.SpVoice')

def say(text):
    speaker.Speak(text)