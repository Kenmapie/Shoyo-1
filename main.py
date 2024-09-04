meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            }
kelime = input("Anlamadığınız bir kelime yazın ): ").upper()

if kelime in meme_dict.keys():
    print(meme_dict[kelime])
else:
    print("Bu kelime listede değil.")
