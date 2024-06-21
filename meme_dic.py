meme_dic = {"XD":"algo demaciado gracioso tanto que te puedes ahogar si lo escribes con mayusculas",
            "POSER":"fingir algo que no es un fan por moda pues",
            "CHAMBA":"trabajar",
            "CRINGE":"pena ajena mucha",
            "FANBOY":"ser fanatico a muerte de algo como yo con el bayverse"
            }
for i in range(5):
    word = input("Que deseas saber").upper()
    if word in meme_dic.keys():
        print(meme_dic[word])
    else:
        print("falta agregar elementos al diccionario")
