from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QTextEdit, QGridLayout
from server import GestionServeur

class ApplicationServeur(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Evaluation R3.09 - Vladimir Nechaev")
        self.setMinimumSize(500, 600)
        self.setMaximumSize(500, 600)
        self.label_serveur = QLabel("Serveur")
        self.champ_serveur = QLineEdit("localhost")
        self.label_port = QLabel("Port")
        self.champ_port = QLineEdit("4200")
        self.label_clients = QLabel("Nombre de clients maximum")
        self.champ_clients = QLineEdit("5")
        self.zone_logs = QTextEdit()
        self.zone_logs.setReadOnly(True)
        
        self.bouton_demarrer = QPushButton("Démarrer le serveur")
        self.bouton_quitter = QPushButton("Quitter")
        self.bouton_quitter.setObjectName("bouton_quitter")
        disposition_principale = QGridLayout()
        disposition_principale.addWidget(self.label_serveur)
        disposition_principale.addWidget(self.champ_serveur)
        disposition_principale.addWidget(self.label_port)
        disposition_principale.addWidget(self.champ_port)
        disposition_principale.addWidget(self.label_clients)
        disposition_principale.addWidget(self.champ_clients)
        disposition_principale.addWidget(self.bouton_demarrer)
        disposition_principale.addWidget(self.zone_logs)
        disposition_principale.addWidget(self.bouton_quitter)

        self.setLayout(disposition_principale)
        self.serveur = None
        self.serveur_actif = False
        self.bouton_demarrer.clicked.connect(self.basculer_serveur)
        self.bouton_quitter.clicked.connect(self.close)

    def basculer_serveur(self):
        if not self.serveur_actif:
            hote = self.champ_serveur.text()
            try:
                port = int(self.champ_port.text())
            except ValueError:
                self.zone_logs.append("Et non, le port doit être un nombre.")
                return
            try:
                max_clients = int(self.champ_clients.text())
            except ValueError:
                self.zone_logs.append("Et non, le nombre de clients doit être un nombre.")
                return

            self.serveur = GestionServeur(hote, port, max_clients, self)
            self.serveur.demarrer()
            self.bouton_demarrer.setText("Arrête le serveur")
            self.serveur_actif = True
        else:
            if self.serveur:
                self.serveur.arreter()
            self.bouton_demarrer.setText("Démarrer le serveur")
            self.zone_logs.append("Serveur arrêté.")
            self.serveur_actif = False

    def afficher_message(self, message):
        self.zone_logs.append(message)
        
