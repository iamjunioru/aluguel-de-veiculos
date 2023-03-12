from View.FrmPrincipal import *
import sys

if __name__ == "__main__":
    print("Executando o programa principal...")
    app = QtGui.QApplication(sys.argv)
    FrmPrincipal = QtGui.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    # fix p que seja fechada corretamente

    sys.exit(app.exec_())
