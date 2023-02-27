from Model.DTO.AluguelDTO import AluguelDTO
from Model.DAO.AluguelDAO import AluguelDAO

class AluguelCTR:
    # recebe parâmetros relacionados a um aluguel de veículo e cria um objeto "AluguelDTO" com essas informações.
    # ele instancia um objeto "AluguelDAO" e chama o método "CadastrarAluguel", passando o objeto "AluguelDTO" como argumento.
    # Esse método é responsável por persistir as informações sobre um novo aluguel no banco de dados.
    def CadastrarAluguel(DataAluguel, DataPrazo, DataDevolucao, ValorAluguel,
                      ValorMulta, KmEntrada, KmSaida, CodigoCli, CodigoVeic):
        aluguelDTO = AluguelDTO
        aluguelDTO.DataAluguel = DataAluguel
        aluguelDTO.DataPrazo = DataPrazo
        aluguelDTO.DataDevolucao = DataDevolucao
        aluguelDTO.ValorAluguel = ValorAluguel
        aluguelDTO.ValorMulta = ValorMulta
        aluguelDTO.KmEntrada = KmEntrada
        aluguelDTO.KmSaida = KmSaida
        aluguelDTO.CodigoCli = CodigoCli
        aluguelDTO.CodigoVeic = CodigoVeic

        aluguelDAO = AluguelDAO
        aluguelDAO.CadastrarAluguel(aluguelDTO)

    # instancia um objeto "AluguelDAO" e chama o método "PesquisarTodosAluguel".
    #  O método retorna uma query com todos os alugueis armazenados no banco de dados.
    def PesquisarTodosAluguel():
        aluguelDAO = AluguelDAO
        query = aluguelDAO.PesquisarTodosAluguel()

        return query

    # instancia um objeto "AluguelDAO" e chama o método "PesquisarAluguel", passando dois argumentos; valor e tipo.
    # ele retorna uma query com os alugueis que correspondem aos critérios de pesquisa especificados.
    def PesquisarAluguel(valor, tipo):
        aluguelDAO = AluguelDAO
        query = aluguelDAO.PesquisarAluguel(valor, tipo)

        return query

    # recebe vários parâmetros relacionados a devolução de um veículo alugado e cria um objeto "AluguelDTO" com essas informações.
    def DevolverVeiculo(codigoAlug, dataDevol, valorMulta, kmSaida):
        aluguelDTO = AluguelDTO

        aluguelDTO.DataDevolucao = dataDevol
        aluguelDTO.ValorMulta = valorMulta
        aluguelDTO.KmSaida = kmSaida

        aluguelDAO = AluguelDAO
        aluguelDAO.DevolverVeiculo(codigoAlug, aluguelDTO)