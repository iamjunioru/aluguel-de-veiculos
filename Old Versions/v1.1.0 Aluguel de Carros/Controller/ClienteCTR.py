from Model.DTO.ClienteDTO import ClienteDTO
from Model.DAO.ClienteDAO import ClienteDAO

class ClienteCTR:
    # a função recebe as informações do cliente como argumentos, incluindo nome, CPF, endereço, email e telefone.
    # em seguida, instância a classe "ClienteDTO", atribui cada informação de argumento ao respectivo atributo da classe DTO e,
    # por fim, instância a classe "ClienteDAO" e chama a função "CadastrarCliente",
    def CadastrarCliente(nome, CPF, endereco, email, telefone):
        clienteDTO = ClienteDTO
        clienteDTO.Nome = nome
        clienteDTO.CPF = CPF
        clienteDTO.Endereco = endereco
        clienteDTO.Email = email
        clienteDTO.Telefone = telefone

        clienteDAO = ClienteDAO
        clienteDAO.CadastrarCliente(clienteDTO)

    # aqui funciona da mesma forma que a função "CadastrarCliente".
    # com a diferença de que também recebe o código do cliente como argumento.
    #  Além disso, ao invés de chamar a função "CadastrarCliente", a classe "ClienteDAO" é chamada com a função "AtualizarCliente".
    def AtualizarCliente(codigoCli, nome, CPF, endereco, email, telefone):
        clienteDTO = ClienteDTO
        clienteDTO.Nome = nome
        clienteDTO.CPF = CPF
        clienteDTO.Endereco = endereco
        clienteDTO.Email = email
        clienteDTO.Telefone = telefone

        clienteDAO = ClienteDAO
        clienteDAO.AtualizarCliente(codigoCli, clienteDTO)

    # instancia a classe "ClienteDAO" e chama a função "PesquisarTodosClientes", retornando o resultado da query.
    def PesquisarTodosClientes():
        clienteDAO = ClienteDAO
        query = clienteDAO.PesquisarTodosClientes()

        return query

    # funciona da mesma forma que a função "PesquisarTodosClientes".
    def PesquisarCliente(valor, tipo):
        clienteDAO = ClienteDAO
        query = clienteDAO.PesquisarCliente(valor, tipo)

        return query

    # instancia a classe "ClienteDAO" e chama a função "ExcluirCliente".
    def ExcluirCliente(codigoCli):
        clienteDAO = ClienteDAO
        clienteDAO.ExcluirCliente(codigoCli)