from Transicao import Transicao

class Maquina():
    def __str__(self):
        out = ""
        out += ("FITA 1 [REGRAS]:\n" + str(self.fita1) + "\n\nFITA 2 [ESTADO_ATUAL]:\n" + str(self.fita2) 
            + "\n\nFITA 3 [PALAVRA]:\n" + str(self.fita3) + "\n\n")
        return out

    def __init__(self, regras, palavra):
        self.fita1 = regras 	  
        self.fita2 = "1"		  
        self.fita3 = palavra      
        self.lista_transicoes = [Transicao(tran) for tran in regras]		
        self.cabesss_maquina = 0  										
        self.D = "1"              
        self.E = "11"
        self.REJEITA = "\nPalavra rejeitada\n" 
        self.ACEITA = "\nPalavra aceita\n"
        self.ultima_transicao = []             