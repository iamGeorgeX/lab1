import requests 

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


while True:

    url = input('url:\t')     
    if url == '': break     
    if not url.startswith('http'):         
        url = 'http://'+ url     
    try:         
        with requests.get(url) as response:             
            
            print("RESPONSE HEADER")             
            for key, value in response.headers.items():                
                print("{:30s} {}".format(key, value))   


    except:         
        print('error opening', url) 
