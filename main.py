"https://github.com/Valeysy/EvalR3.09"

"Pour démarrer sur mac, faire : python3 main.py"


from PyQt6.QtWidgets import QApplication
from gui import ApplicationServeur
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = ApplicationServeur()
    fenetre.show()
    sys.exit(app.exec())
