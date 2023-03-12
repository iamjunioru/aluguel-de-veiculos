# O método "CadastrarVeiculo" recebe como parâmetros várias informações sobre o veículo que está sendo cadastrado (modelo, marca, ano de modelo, placa, etc.) e as armazena em um objeto "VeiculoDTO". Em seguida, o método invoca o método "CadastrarVeiculo" da classe "VeiculoDAO" e passa o objeto "VeiculoDTO" como parâmetro, 
# para que os dados do veículo possam ser persistidos em um banco de dados.
# Os métodos "AtualizarVeiculo", "PesquisarVeiculosDisponiveis", "PesquisarTodosVeiculos" e "PesquisarVeiculo" funcionam de maneira semelhante, mas oferecem funcionalidades diferentes. O método "AtualizarVeiculo" recebe um código de veículo e as novas informações para atualizar, enquanto os métodos de pesquisa retornam resultados de consulta ao banco de dados. 
# O método "ExcluirVeiculo" recebe um código de veículo e remove o registro correspondente do banco de dados.

from Model.DTO.VeiculoDTO import VeiculoDTO
from Model.DAO.VeiculoDAO import VeiculoDAO

class VeiculoCTR:
    def CadastrarVeiculo(modelo, marca, anoModelo, placa, alugado, batido,
                         kmAtual, valorDiaria, descricao, tipoVeiculo):
        veiculoDTO = VeiculoDTO
        veiculoDTO.Modelo = modelo
        veiculoDTO.Marca = marca
        veiculoDTO.AnoModelo = anoModelo
        veiculoDTO.Placa = placa
        veiculoDTO.Alugado = alugado
        veiculoDTO.Batido = batido
        veiculoDTO.KmAtual = kmAtual
        veiculoDTO.ValorDiaria = valorDiaria
        veiculoDTO.Descricao = descricao
        veiculoDTO.TipoVeiculo = tipoVeiculo

        veiculoDAO = VeiculoDAO
        veiculoDAO.CadastrarVeiculo(veiculoDTO)

    def AtualizarVeiculo(codigoVeic, modelo, marca, anoModelo, placa, alugado,
                         batido, kmAtual, valorDiaria, descricao, tipoVeiculo):
        veiculoDTO = VeiculoDTO
        veiculoDTO.Modelo = modelo
        veiculoDTO.Marca = marca
        veiculoDTO.AnoModelo = anoModelo
        veiculoDTO.Placa = placa
        veiculoDTO.Alugado = alugado
        veiculoDTO.Batido = batido
        veiculoDTO.KmAtual = kmAtual
        veiculoDTO.ValorDiaria = valorDiaria
        veiculoDTO.Descricao = descricao
        veiculoDTO.TipoVeiculo = tipoVeiculo

        veiculoDAO = VeiculoDAO
        veiculoDAO.AtualizarVeiculo(codigoVeic, veiculoDTO)

    def PesquisarVeiculosDisponiveis():
        veiculoDAO = VeiculoDAO
        query = veiculoDAO.PesquisarVeiculosDisponiveis()

        return query

    def PesquisarTodosVeiculos():
        veiculoDAO = VeiculoDAO
        query = veiculoDAO.PesquisarTodosVeiculos()

        return query

    def PesquisarVeiculo(valor, tipo):
        veiculoDAO = VeiculoDAO
        query = veiculoDAO.PesquisarVeiculo(valor, tipo)

        return query

    def ExcluirVeiculo(codigoVeic):
        veiculoDAO = VeiculoDAO
        veiculoDAO.ExcluirVeiculo(codigoVeic)