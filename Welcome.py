from PyQt4 import QtGui, QtCore
import subprocess


print("Executando tela de boas vindas...")


class Welcome(QtGui.QMainWindow):
    def __init__(self):
        super(Welcome, self).__init__()
        self.initUI()
        self.fadeIn()
        
    def startNewProcess(self):
        # inicia um novo processo para executar o arquivo novo_arquivo.py
        subprocess.Popen(['python', 'Main.py'])
        # apagar ao clicar em iniciar
        self.hide()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)

        # label com a imagem
        self.label = QtGui.QLabel(self)
        self.pixmap1 = QtGui.QPixmap('Imagens/BGImg2.png')
        self.pixmap2 = QtGui.QPixmap('Imagens/BGImg1.png')
        self.current_pixmap = self.pixmap1
        self.label.setPixmap(self.current_pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # nome do programa
        self.labelNome = QtGui.QLabel('Sistema de Aluguel de Veículos v1.1.2', self)
        self.labelNome.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNome.setStyleSheet('font-weight: bold;')

        # botões "Iniciar" e "Sobre"
        self.btnIniciar = QtGui.QPushButton('Iniciar', self)
        self.btnSobre = QtGui.QPushButton('Sobre', self)

        # botão de sair
        self.btnSair = QtGui.QPushButton('Sair', self)

        # layout vertical e adiciona os elementos
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.labelNome)
        vbox.addWidget(self.btnIniciar)
        vbox.addWidget(self.btnSobre)
        vbox.addWidget(self.btnSair)

        # criar um widget central e adiciona o layout vertical
        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        # definir tamanho e título da janela
        self.resize(700, 500)
        self.setWindowTitle('Aluguel de Veículos 1.1.2')

        # conectar o sinal clicked do botão "Iniciar" ao slot que inicia o novo processo
        self.btnIniciar.clicked.connect(self.startNewProcess)

        # conectar o sinal clicked do botão "Sobre" ao slot que exibe a caixa de diálogo
        self.btnSobre.clicked.connect(self.showDialog)

        # conectar o sinal clicked do botão "Sair" ao slot que fecha a janela
        self.btnSair.clicked.connect(self.fadeOut)

        # estilo da janela com bordas arredondadas
        self.setStyleSheet('''
            QMainWindow {
                background-color: white;
                border-radius: 10px;
            }
            QPushButton {
                background-color: black;
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #5f5f5f;
            }
        ''')
  
  
        # centralizar a janela no centro da tela do computador após um curto intervalo
        QtCore.QTimer.singleShot(10, self.center)      
        
    def fadeOut(self):
        # animação de fade out
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000) # duração da animação em milissegundos
        self.animation.setStartValue(1) # valor de opacidade inicial
        self.animation.setEndValue(0) # valor de opacidade final
        self.animation.finished.connect(self.close) # conectar o sinal de término da animação ao slot de fechar a janela
        self.animation.start()
        print("Saindo do programa...")
        
    def fadeIn(self):
        # animação de fade in
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000) # duração da animação em milissegundos
        self.animation.setStartValue(0) # valor de opacidade inicial
        self.animation.setEndValue(1) # valor de opacidade final
        self.animation.start()


    def center(self):
        # centraliza a janela no centro da tela do pc
        self.move(QtGui.QDesktopWidget().screenGeometry().center() - self.rect().center())


    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            if self.label.geometry().contains(event.pos()):
                if self.current_pixmap == self.pixmap1:
                    self.current_pixmap = self.pixmap2
                else:
                    self.current_pixmap = self.pixmap1
                self.label.setPixmap(self.current_pixmap)

    def showDialog(self):
        # cria uma nova caixa de diálogo
        dialog = QtGui.QDialog(self)
        dialog.setWindowTitle('Sobre')
        
        # icone
        icon = QtGui.QIcon('Imagens/interrogacao.png')
        dialog.setWindowIcon(icon)

        # cria uma label com a imagem
        label = QtGui.QLabel(dialog)
        pixmap = QtGui.QPixmap('Imagens/dev.png')
        pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)

        # criar um botão de voltar
        btnSair = QtGui.QPushButton('Voltar', dialog)
        btnSair.clicked.connect(dialog.close)

        # cria uma label com as informações do usuário
        labelUser = QtGui.QLabel(dialog)
        labelUser.setText('Equipe de Desenvolvimento:\nRaimundo Gonçalves de Sousa Júnior\n')
        # labelUser.setStyleSheet('font-weight: bold;')

        # adicionar a label, o botão e a label de usuário ao layout vertical
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(labelUser)
        vbox.addWidget(btnSair)
        dialog.setLayout(vbox)

        # exibir a caixa de diálogo
        dialog.exec_()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    welcome = Welcome()
    welcome.show()
    sys.exit(app.exec_())