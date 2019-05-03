import json
    
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
    initial_state = afn_dados['initial']
    for simbol in palavra:
        new_initial_state = None
        for afn_dados['transitions'] in initial_state:
            'adicionar estado destino'
            'aos novos estados atuais'
        initial_state = new_initial_state
        for afn_dados['states'] in initial_state:
            if afn_dados['states'] in afn_dados['final']:
                return 'yes'
            else:
                return 'no'

  



def main():
    afd_json = open("afd.json").read()
    dados = json.loads(afd_json)
    #print (dados)
   
    '''print (dados["type"])
    print (dados["alphabet"])
    print (dados["states"])
    print (dados["initial"])
    print (dados["transitions"]["q0"])
    print (dados["final"])'''


    afd_palavra = open("afd-palavras.txt", "r")
    palavra = afd_palavra.read()
    #print(palavra)

    palavras = ['abbbbbba', 'aba', 'aa', 'abbba', 'abba']

    for i in palavras:
        q = afd_function(dados, i)
        print(q)

    afd_palavra.close()

main()