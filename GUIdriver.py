import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic

qtCreatorFile = "design.ui"  # Path to your .ui file
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):  # Changed to QtWidgets.QMainWindow
    def __init__(self):
        super(MyApp, self).__init__()
        self.setupUi(self)
        self.browse.clicked.connect(self.Test)
        self.close.clicked.connect(self.Close)

    def Test(self):
        options = QtWidgets.QFileDialog.Options()  # Correctly use QtWidgets.QFileDialog
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        ImageFile, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Image To Process", "", "All Files (*);;Image Files (*.jpg *.gif)", options=options)
        exec(open('main.py').read())

    def Close(self):
        self.close()  # Gracefully close the window

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Use QtWidgets.QApplication
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
