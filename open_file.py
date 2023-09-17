import os

location_map = {
    'desktop': r'C:\Users\Hp\Desktop',
    'code folder': r'C:\Users\Hp\Desktop\Code',
    'college folder': r'C:\Users\Hp\Desktop\College',
    'downloads': r'C:\Users\Hp\Downloads'
}

def location_translate(location):
    return location_map.get(location.lower(), None)

def deal_with_query(query):
    #open name.pdf located on Desktop
    #open name.pdf located in Code folder
    #open name.pdf located in College folder
    #open name.pdf located in downloads
    words = query.split()
    
    for i, word in enumerate(words):
        if word.lower() == "open":
            if i + 1 < len(words):
                file_name = words[i + 1]
                
        if word.lower() == "located" and i + 2 < len(words):
            folder_name = location_translate(' '.join(words[i + 2:]))
        else:
            folder_name = location_translate('desktop')
            
        if file_name and folder_name:
            path = folder_name + f"\{file_name}"
        
        if path:
            if os.path.exists(path):
                os.startfile(path)
            else:
                print(f"File not found: {path}")

    return None

if __name__ == "__main__":
    deal_with_query('open offerletter.pdf located in Code folder')
    
    print("Succesful")