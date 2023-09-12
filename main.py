import speech_recognition as sr
import os
import win32com.client
import webbrowser
from youtubesearchpython import VideosSearch
import datetime
import promptFile
import pyperclip
import sentiment

speaker = win32com.client.Dispatch('SAPI.SpVoice')

memory = ''

def say(text):
    speaker.Speak(text)

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
            return 'error'
        
def youtube_video(query):
    query = query.replace("play song", "").strip()
    query = query.replace(" ", "+")
    search_query = query
    videos_search = VideosSearch(search_query, limit=1)
    results = videos_search.result()
    
    if results['result']:
        first_video_url = results['result'][0]['link']
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" 
        webbrowser.get(chrome_path).open(first_video_url, new=2)
    else:
        say("No search results found")
        
def google_search(query):
    query = query.replace("search", "").replace("on Google", "").strip()
    search_url = f"https://www.google.com/search?q={query}"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" 
    webbrowser.get(chrome_path).open(search_url, new=2)
    
def enterPrompt():
    say('Yes sir, go ahead')
    prompt = listen()
    prompt = prompt.lower()
    response = promptFile.return_answer(prompt)
    
    token = response.split()
    if(len(token) > 20):
        say('Answer too large to say')
    else:
        say(response)
    
    if not os.path.exists('prompt_answers'):
        os.mkdir('prompt_answers')
    
    with open(f'prompt_answers/{prompt}', 'w') as f:
        f.write(response)
        
    say('Would you like to copy the answer to clipboard?')
    resp = listen().lower()
    if resp == 'yes':
        pyperclip.copy(response)
        say('Copied')

def chat():
    global memory
    count = 0
    say('What can I help you with?')
    while count != 1:
        query = listen().lower()
        if 'error' in query:
            continue
        if 'jarvis quit chatting' in query:
            count = 1
        memory += f'Sahil : {query}\n Jarvis: '
        response = promptFile.return_answer(memory)
        say(response)
        memory += f'{response}\n'
    return 'Nice talking with you sir!'

def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    say(f'Sir, the time is {time}')
    
if __name__ == '__main__':
    print('hi')
    say('Jarvis activated')
    
    while True:
        print('Listening')
        query = listen()
        query = query.lower()
        if query:
            if 'jarvis play song' in query:
                youtube_video(query)
            elif query.startswith('jarvis search') and query.endswith('on google'):
                google_search(query)
            elif 'jarvis what time is it' in query:
                time()
            elif 'jarvis new prompt' in query:
                enterPrompt()
            elif 'jarvis power off' in query:
                exit()
            elif 'jarvis clear memory' in  query:
                memory = ''
            elif 'jarvis talk to me' in query:
                print('Chatting')
                chat()
