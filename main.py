meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL",
            "PILETA": "PILETA su significado es piscina >:("            
}

user=input("QUE PALABRA NO ENTIENDES(Utiliza Mayuscula si no, no entiende)")



if user in meme_dict.keys():
    print(meme_dict[user])
else:
    print("Todavía no tenemos esta palabra... Pero estamos trabajando en ella.")
