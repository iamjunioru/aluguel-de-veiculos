from PyQt4.QtSql import QSqlDatabase

class ConexaoSQL:
    # criar banco.
    def getConexao():
        # adicionar banco.
        db = QSqlDatabase.addDatabase('QSQLITE')
        # configurar nome: DataBase/nome.db3
        db.setDatabaseName("DataBase/LocadoraDB.db3")

        # retorna o objeto de conexão com o banco de dados.
        return db