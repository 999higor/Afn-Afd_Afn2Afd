import json
import sys
    
def afd_function(afd_dados, palavra):
    estado_atual = afd_dados['initial']
    for simbolo in palavra:
            if simbolo in afd_dados['transitions'][estado_atual]:
                estado_atual = afd_dados['transitions'][estado_atual][simbolo]
            else:
                return 'no'
    if estado_atual in afd_dados['final']:
        return 'yes'
    else:
        return 'no'

def afn_function(afn_dados, palavra):
    estado_atuais = afn_dados['initials']
    for simbolo in palavra:
        novos_estados_atuais = []
        for estado in estado_atuais:
            if simbolo in afn_dados['transitions'][estado]:
                estado_destino = afn_dados['transitions'][estado][simbolo]
                novos_estados_atuais.extend(estado_destino)

        estado_atuais = novos_estados_atuais
    for estado in estado_atuais:
        if estado in afn_dados['final']:
            return 'yes'
    return 'no'

  



def main():

    option = sys.argv[1]

    if option == 1:

        afd_json = open(sys.argv[2]).read()
        dados = json.loads(afd_json)

        afd_palavra = open(sys.argv[3], "r")
        txt = afd_palavra.read()
        palavras = txt.split("\n")

        for i in palavras:
            q = afd_function(dados, i)
            print(q)

        afd_palavra.close()

    elif option == 2:
    
        afd_json = open(sys.argv[2]).read()
        dados = json.loads(afd_json)

        afd_palavra = open(sys.argv[3], "r")
        txt = afd_palavra.read()
        palavras = txt.split("\n")

        for i in palavras:
            q = afn_function(dados, i)
            print(q)

        afd_palavra.close()
    

main()