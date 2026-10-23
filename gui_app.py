## modèle pour chaque UI
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from gui_MainWindow import Ui_MainWindow
from text_analyser import Cleaner, Counter

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(600, 400)
        self.setupUi(self)

        # gestion d'évènement: attacher une fonction à un évènement d'un widget
        self.okBtn.clicked.connect(self.on_okBtn_clicked)

    def on_okBtn_clicked(self):
        """
        gestionnaire d'évènement: eventHandler
        ici on ajoute la logique métier
        """
        text = self.textEdit.toPlainText()
        cleaner = Cleaner(text)
        counter = Counter(cleaner)
        occurences = counter.count()
        for key, occurence in occurences.items():
            line = f"{key}: {occurence}"
            self.listWidget.addItem(line)
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
