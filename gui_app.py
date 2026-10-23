## modèle pour chaque UI
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import Slot
from gui_MainWindow import Ui_MainWindow
from text_analyser import Cleaner, Counter

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(600, 400)
        self.setupUi(self)

        # gestion d'évènement: attacher une fonction à un évènement d'un widget
        # plus besoin si on utilise un Slot()
        # self.okBtn.clicked.connect(self.on_okBtn_clicked)

    # en décorant le gestionnaire avec Slot()
    # et nommant le gestionnaire intelligemment : on_<widget>_<event>
    @Slot()
    def on_okBtn_clicked(self):
        """
        gestionnaire d'évènement: eventHandler
        ici on ajoute la logique métier
        """
        self.listWidget.clear()

        # données d'entrées
        text = self.textEdit.toPlainText()
        word_length = self.signWords.value()
        nb_crop = self.results.value()

        cleaner = Cleaner(text)
        counter = Counter(cleaner, word_length)
        occurences = counter.count(nb_crop=nb_crop)
        
        for key, occurence in occurences.items():
            line = f"{key}: {occurence}"
            self.listWidget.addItem(line)
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
