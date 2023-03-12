from PyQt4 import QtGui, QtCore
import subprocess

class Welcome(QtGui.QMainWindow):
    def __init__(self):
        super(Welcome, self).__init__()
        self.initUI()
        self.fadeIn()
        
    def startNewProcess(self):
        subprocess.Popen(['python', 'Main.py'])
        self.hide()

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)

        self.label = QtGui.QLabel(self)
        self.pixmap1 = QtGui.QPixmap('Imagens/BGImg1.png')
        self.pixmap2 = QtGui.QPixmap('Imagens/BGImg.png')
        self.current_pixmap = self.pixmap1
        self.label.setPixmap(self.current_pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.labelNome = QtGui.QLabel('Sistema de Aluguel de Veículos v1.1.1', self)
        self.labelNome.setAlignment(QtCore.Qt.AlignCenter)
        self.labelNome.setStyleSheet('font-weight: bold;')

        self.btnIniciar = QtGui.QPushButton('Iniciar', self)
        self.btnSobre = QtGui.QPushButton('Sobre', self)

        self.btnSair = QtGui.QPushButton('Sair', self)

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.labelNome)
        vbox.addWidget(self.btnIniciar)
        vbox.addWidget(self.btnSobre)
        vbox.addWidget(self.btnSair)

        widget = QtGui.QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.resize(700, 500)
        self.setWindowTitle('Aluguel de Veículos 1.1.1')

        self.btnIniciar.clicked.connect(self.startNewProcess)

        self.btnSobre.clicked.connect(self.showDialog)

        self.btnSair.clicked.connect(self.fadeOut)

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
  

        QtCore.QTimer.singleShot(10, self.center)      
        
    def fadeOut(self):
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000) # duração da animação em milissegundos
        self.animation.setStartValue(1) # valor de opacidade inicial
        self.animation.setEndValue(0) # valor de opacidade final
        self.animation.finished.connect(self.close) # conectar o sinal de término da animação ao slot de fechar a janela
        self.animation.start()
        
    def fadeIn(self):
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000) # duração da animação em milissegundos
        self.animation.setStartValue(0) # valor de opacidade inicial
        self.animation.setEndValue(1) # valor de opacidade final
        self.animation.start()


    def center(self):
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
        dialog = QtGui.QDialog(self)
        dialog.setWindowTitle('Sobre')

        label = QtGui.QLabel(dialog)
        pixmap = QtGui.QPixmap('Imagens/dev.png')
        pixmap = pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)

        btnSair = QtGui.QPushButton('Sair', dialog)
        btnSair.clicked.connect(dialog.close)

        labelUser = QtGui.QLabel(dialog)
        labelUser.setText('Equipe de Desenvolvimento:\nRaimundo Gonçalves de Sousa Júnior')

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(labelUser)
        vbox.addWidget(btnSair)
        dialog.setLayout(vbox)

        dialog.exec_()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    welcome = Welcome()
    welcome.show()
    sys.exit(app.exec_())