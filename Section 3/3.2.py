'''

Funzioni con parametri

Esempio 1
'''

def mia_somma(x,y):

    somma = x+y

    return somma


# attenzione all'indentatura, poiché se indentato come le altre istruzioni
# della function precedente il codice verrà inserito nel corpo della function.

risultato = mia_somma(5,4)

print(risultato)

    
'''
Esempio 2

Immaginiamo di dover svillupare un sito web
eabbiamo una function che definisca il font, il background, la grnadezza

'''

def website(font,background_color,font_size,font_color):

    print('font:', font)
    print('background:', background_color)
    print('font size:',font_size)
    print('font color:',font_color)

website('TNR','white','11','black')

print('') # giusto per separare i due output della stessa function

# in questo modo perà potremmo sbagliare ad inserire in ordine i
# valori dei parametri per la nostra function
# Soluzione 1:

website(font_size = '11',
        background_color = 'white',
        font = 'TNR',
        font_color = 'black')

# In questo caso però, se mancassimo anche solo un parametro
# l'interprete ci darebbe errore
# quindi potremmo invece optare per questa seconda soluzione,
# ovvero definire dall'inizio dei valori di default della function
# ed andare a modificare poi solo quello ci viene richiesto di modificare
# come spesso accada in un sito wordpress

print('') 

def website_v2( font_size = '11',
                background_color = 'white',
                font = 'TNR',
                font_color = 'black'):

    print('font:', font)
    print('background:', background_color)
    print('font size:',font_size)
    print('font color:',font_color)

# supponiamo che vogliamo cambiare solo il colore dello sfondo
website_v2(background_color = 'red')
print('')
#oppure voglia cambiare più di un parametro

website_v2(font_color = 'blue', font_size = 24)

    


    
