from ctypes.wintypes import tagMSG
import math

from numpy import indices

ram = [0] * (2**16) # cria um vetor de 2 elevado a 16 posicaoes



# cria a cache com a configuracao passada
def criarCache(entradasDaCache,tamanhoBloco,mapeamento):
    cache = []       
    x = {
            "valido": 0,
            "offsetByte": 0,
            "offsetBloco": 0,
            "indice": 0,
            "tag": 0,
        }
    
    for i in range(0, entradasDaCache):
        cache.append(x)
    return cache

cache = criarCache(8,4,2)


def decodificarDiretamenteMapeado(endereco,tamanhoBloco,tamanhoCache):

    #acha a quantidade de bits para o indice e offset do bloco
    bitsOffsetBloco = int(math.log(tamanhoBloco,2))
    bitsIndice = int(math.log(tamanhoCache,2))

    #separa os bits de offset , indice , tag do endereco , e operacao (read or write)
    offsetBloco = endereco[ (18-bitsOffsetBloco) : 18]
    indice = endereco[(18-bitsOffsetBloco-bitsIndice) : (18-bitsOffsetBloco)]
    tag = endereco[2 : (18-bitsOffsetBloco-bitsIndice)]
    operacao = endereco[0]

    return {"offsetBloco": offsetBloco,
        "indice": indice,
        "tag": tag,
        "operacao": operacao,
        }



def buscarRam(offsetbloco,endereco):
    if offsetbloco == "":
        return ram[int(endereco,2)]



def buscarCache(offsetBloco,indice,tag):

    #caso que o tamanho do bloco é igual a 1, entao, bloco  = um endereco
    if offsetBloco == "":

        #busca o bloco na cache pelo seu indice
        bloco = cache[int(indice,2)]

        #checa se o bloco que esta na cache é valido e possuim a mesma tag
        if bloco.valido == 1  and  bloco.tag == tag :
            return "hit"
        else:
            return "miss"


def processador(mapeamento,tamanhoBloco,tamanhoCache):


    #abre os arquivos
    trace1 = open("trace1.txt","r")
    trace2 = open("trace1.txt","r")
    trace3 = open("trace1.txt","r")

    trace1 = trace1.readlines()
    trace2 = trace2.readlines()
    trace3 = trace3.readlines()




    # mapeamento direto
    if mapeamento == 0:
        for endereco in trace1:
            enderecoDecodificado = decodificarDiretamenteMapeado(endereco,tamanhoBloco,tamanhoCache)



    elif mapeamento == 1:
        return
    else:
        return 

    return

