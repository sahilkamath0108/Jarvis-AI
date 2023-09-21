import speech_recognition as sr
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        try:
            audio = r.listen(source, timeout=20)  # Wait for up to 10 seconds for input
            query = r.recognize_google(audio, language='en-in')
            print(query)
            return query
        except sr.WaitTimeoutError:
            print('timeout')
            return 'error'
        except Exception as e:
            print('malf')
            return 'malf'