class AluguelDTO:
    def __init__(self):
        self.DataAluguel = None
        self.DataPrazo = None
        self.DataDevolucao = None
        self.ValorAluguel = None
        self.ValorMulta = None
        self.KmEntrada = None
        self.KmSaida = None
        self.CodigoCli = None
        self.CodigoVeic = None

        # as variáveis são inicializadas com o valor None
        # None é um valor especial em python que indica que a variável não possui um valor atribuído.

        # o método __init__ é um método especial que é chamado quando um objeto é criado.
        # essa classe é um exemplo de como os dados relacionados a um aluguel podem ser organizados e estruturados para facilitar sua manipulação e gerenciamento.