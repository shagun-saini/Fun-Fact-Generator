#Fun Fact Generator

#define the import module 
import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    #screen clear
    clear()

    #put html content
    put_html('<p align="left'>
             '<h2><img src="https://www.shutterstock.com/image-vector/doodle-emoji-face-icon-set-hand-2706111629?'
             'trackingId=b9c5e4a8-303c-41d4-b26f-90cc0b584961&listId=searchResults"  width="7%">Fun Fact Generator</h2>'
             '</p>')
    
 #use the useless text
    url="https://uselessfacts.jsph.pl/random.json?language=en"

# use get request
    response=requests.get(url)

    #data load in json file
    data=json.loads(response.text)

    useless_fact=data['text']

    style(put_text(useless_fact), 'color:red; font-size:30px')

    #use the image
    img_url="https://www.vecteezy.com/vector-art/24237089-big-set-of-yellow-emoji-funny-emoticons-faces-with-facial-expressions"
    img_response=requests.get(img_url)

    put_image(img_response.content)

    #generate the button 
    put_buttons([dict(label='click me', value='outline-success', color='outline-success')],
    onclick=get_fun_fact)

if __name__=='__main__':

        #put the html heading
        put_html('<p align="left'>
             '<h2><img src="https://www.vecteezy.com/vector-art/24237089-big-set-of-yellow-emoji-'
             'funny-emoticons-faces-with-facial-expressions"  width="7%">Fun Fact Generator</h2>'
             '</p>')
        
        put_buttons([dict(label='click me', value='outline-success', color='outline-success')],
    onclick=get_fun_fact)
        
       #hold the session for the long time
        hold()

        






