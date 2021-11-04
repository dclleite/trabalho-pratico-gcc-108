from Maquina import Maquina
import sys

ENTRADAINVALIDA = "\nEntrada invalida"

if __name__ == '__main__':

    try:
        arquivo = open(sys.argv[1], 'r', encoding='utf8')
    except:
        print('Arquivo não encontrado')
        sys.exit()

    rMw = arquivo.read() 

    rMw = rMw[3:]
    finalLeitura = rMw.find("000")

    rM = rMw[:finalLeitura]
    rM = rM.split("00") 

    if len( rM ) == 1: 
        print( ENTRADAINVALIDA )
        exit(0)

    w = rMw[finalLeitura+3:] 

    terOcorrencia = w.find("000") 

    if terOcorrencia == -1: 
        print ( ENTRADAINVALIDA )
        exit(0)
    else:
        w = w[:len(w)-4]
        w = w.split('0')
        
        w.append('111')

        Maquina( rM , w ).executarMaquina()
