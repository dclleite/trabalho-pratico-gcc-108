class Transicao(): 
    def __init__(self, transicao: str) -> None:
        self.estado_inicial, self.simbolo_entrada, self.estado_destino, self.simbolo_escrita, self.direcao = map(str, transicao.split('0'))

    def __str__(self) -> str:
        traducao_estado = lambda s: "q" + str(len(s) - 1)

        direcao = {
            "1": "R",
            "11": "L"
        }

        saida = ""
        saida += traducao_estado(self.estado_inicial) + ", " + self.simbolo_entrada + "] ->  "
        saida += "[" + traducao_estado(self.estado_destino) + ", " + self.simbolo_escrita + ", " + direcao[self.direcao] + "]\n"
