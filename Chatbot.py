def saudacao(nome)
    import random

    
    frases = ["Bom dia! Meu nome é" +nome+".Como vai você?", "Olá","Oi, tudo bem?"]
    print(frases[random.random.randint(0,2)])


def recebeTexto():
    texto = "Cliente:" + input("Cliente:")
    palavraProibida = ["bocó"]
    for p in palavraProibida
       if p in texto:
        print ("Não vem não me respeite! Me respeite!")
        return recebeTexto
    return texto

def buscaResposta(nome,texto):
    with open("BaseDeConhecimento.txt", "a+", enconding="utf-8") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente:", "") == "Tchau":
                    print(nome+ ": volte sempre!")   
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline() 
                    if "Chatbot: "  in proximalinha:
                        return proximalinha
            else:
                print("Me desculpe, não sei oque falar") 
                conhecimento.write("\n" + texto)
                resposta_user = input("O que esperava?\n")
                conhecimento.write("\n" + "Chatbot:" + resposta_user)
                return "Hum..."           