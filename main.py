import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QProgressBar
from PyQt6.QtGui import QIcon
from functionsFood import LogInRefresh
from functionsFood import lookforfood

class MyApp(QWidget):
    #make the app like make it exist
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TooGoodToGUI")
        
        #make a layout
        layout = QVBoxLayout()
        
        #output text (where text goes)
    
        self.output= QTextEdit("Message field")
        self.output.setReadOnly(True)
    
        #buttons activate progress bar and activate the browser

        self.input = QTextEdit("frishcoco@gmail.com")

        self.buttonLogIn = QPushButton("Log in!?")
        self.buttonLookForFood = QPushButton("Look for food")

        #give the button functions

        self.buttonLogIn.clicked.connect(lambda:superLogIn())
        self.buttonLookForFood.clicked.connect(lambda:superlookforfood())
        self.output.setText("hi")
        
        #SET SIZES

        #we have multiple layers so add a hoz layer and hozlayer2 here

        layout.addWidget(self.input)
        layout.addWidget(self.buttonLogIn)
        layout.addWidget(self.buttonLookForFood)
        layout.addWidget(self.output)

        #set layout
        self.setLayout(layout)

        def superlookforfood():
            g = lookforfood()
            if g != None:
                g = "\n".join(g)
                self.output.setText(g)
            else:
                self.output.setText("Nothing found sorry")

        def superLogIn():
            g = self.input.toPlainText()
            
            try:
                self.output.setText("check email and click confirm")
                LogInRefresh(g)
            except Exception as e:
                self.output.setText(f"ERROR: {e}")


app = QApplication(sys.argv)

window = MyApp()
window.show()

app.exec()

