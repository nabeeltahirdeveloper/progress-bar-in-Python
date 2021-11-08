# IMPORTS
import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *



  
#IMPORT PYSIDE2EXTN WIDGET YOU USED IN THE QTDESIGNER FOR DESIGNING.
from PySide2extn.RoundProgressBar import roundProgressBar
  
#UI FILE CONVERTED FROM .ui to python file ui_main.py
from ui_main import Ui_MainWindow
  
# GLOBAL VALUES
progress_1_val = 0
progress_2_val = 0
progress_3_val = 0
progress_4_val = 0
progress_5_val = 0
progress_6_val = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # PART 1: CIRCULAR PROGRESSBARS;
        # We have THREE progressbars 
        # progress_1
        # progress_2
        # progress_3

        #SETTING THE RANGE : 
        self.ui.progress_1.rpb_setMaximum(420) 
        self.ui.progress_2.rpb_setRange(0, 720)
        self.ui.progress_3.rpb_setRange(0, 1000)
        
        #SETTING THE VALUE
        self.ui.progress_1.rpb_setValue(300)
        self.ui.progress_2.rpb_setValue(456)
        self.ui.progress_3.rpb_setValue(890)

        #CHANGING STYLE
        # Style_Name: 
        # Donet (Default)
        # Line
        # Pie
        # Pizza
        # Pie
        # Hybrid1
        # Hybrid2
        self.ui.progress_1.rpb_setBarStyle('Pie')
        self.ui.progress_2.rpb_setBarStyle('Pizza')
        self.ui.progress_3.rpb_setBarStyle('Hybrid1')

        #CHANGING COLOR
        #Line:
        self.ui.progress_1.rpb_setLineColor((255, 255, 255)) #ARGUMENT RGB AS A TUPLE
        self.ui.progress_2.rpb_setLineColor((255, 255, 255)) #ARGUMENT RGB AS A TUPLE
        self.ui.progress_3.rpb_setLineColor((255, 255, 255)) #ARGUMENT RGB AS A TUPLE

        #Path:
        self.ui.progress_1.rpb_setPathColor((0, 0, 0)) #ARGUMENT RGB AS A TUPLE
        self.ui.progress_2.rpb_setPathColor((255, 235, 59)) #ARGUMENT RGB AS A TUPLE
        self.ui.progress_3.rpb_setPathColor((156, 39, 176)) #ARGUMENT RGB AS A TUPLE

        #Text:
        self.ui.progress_1.rpb_setTextColor((0, 0, 0)) #ARGUMENT RGB AS A TUPLE
        self.ui.progress_2.rpb_setTextColor((255, 255, 255)) #ARGUMENT RGB AS A TUPLE
        self.ui.progress_3.rpb_setTextColor((255, 255, 255)) #ARGUMENT RGB AS A TUPLE

        #Circle:
        self.ui.progress_2.rpb_setCircleColor((205, 220, 57)) #ARGUMENT RGB AS A TUPLE
        self.ui.progress_3.rpb_setCircleColor((156, 39, 176)) #ARGUMENT RGB AS A TUPLE

        #Pie:
        self.ui.progress_1.rpb_setPieColor((255, 193, 7)) #ARGUMENT RGB AS A TUPLE

        # Sample colors =  (255, 193, 7)(255, 87, 34) (205, 220, 57)(255, 235, 59) (156, 39, 176)(233, 30, 99)
        

        # STARTING POSITION
        # North, East, West, South
        self.ui.progress_1.rpb_setInitialPos('West') #WEST AS STARTING POSITION.
        self.ui.progress_2.rpb_setInitialPos('East') #EAST AS STARTING POSITION.
        self.ui.progress_3.rpb_setInitialPos('South') #SOUTH AS STARTING POSITION.

        # PROGRESS DIRECTION
        # Clockwise, AntiClockwise
        self.ui.progress_1.rpb_setDirection('AntiClockwise')
        self.ui.progress_2.rpb_setDirection('Clockwise')
        self.ui.progress_3.rpb_setDirection('AntiClockwise')
        # Effect only visible when progress changes

        #CHANGING THE TEXT TYPE : VALUE OR PERCENTAGE
        # Value, Percentage
        self.ui.progress_1.rpb_setTextFormat('Value')
        self.ui.progress_2.rpb_setTextFormat('Percentage')
        self.ui.progress_3.rpb_setTextFormat('Value')


        #CHANGING THE TEXT SIZE
        self.ui.progress_1.rpb_setTextRatio(3)   #1/3 OF SIZE OF THE PROGRESSBAR
        self.ui.progress_2.rpb_setTextRatio(6)   #1/3 OF SIZE OF THE PROGRESSBAR
        self.ui.progress_3.rpb_setTextRatio(9)   #1/9 OF SIZE OF PROGRESS BAR

        #CHANGING THE FONT
        self.ui.progress_1.rpb_setTextFont('Arial')
        self.ui.progress_3.rpb_setTextFont('Times New Roman')

        #TEXT HIDDEN
        self.ui.progress_1.rpb_enableText(False) 


        #LINE WIDTH 
        self.ui.progress_3.rpb_setLineWidth(10)

        #LINE CAP
        self.ui.progress_2.rpb_setLineCap('SquareCap')
        self.ui.progress_3.rpb_setLineCap('RoundCap')

        #LINE STYLE
        self.ui.progress_2.rpb_setLineStyle('DotLine')
        self.ui.progress_3.rpb_setLineStyle('DashLine')

        #PATH WIDTH
        self.ui.progress_2.rpb_setPathWidth(5)
        self.ui.progress_3.rpb_setPathWidth(10)

        #CHANGING THE PATH COLOR
        self.ui.progress_2.rpb_setPathColor((255, 235, 59))
        self.ui.progress_3.rpb_setPathColor((233, 30, 99))











        # LETS ADD TIMER TO CHANGE PROGRESSES
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(60)

        # Change all progresses to zero on start
        QtCore.QTimer.singleShot(0, lambda: self.ui.progress_1.rpb_setValue(0))
        QtCore.QTimer.singleShot(0, lambda: self.ui.progress_2.rpb_setValue(0))
        QtCore.QTimer.singleShot(0, lambda: self.ui.progress_3.rpb_setValue(0))

        # END PART ONE;









        # PART 2: SPIRAL PROGRESSBARS;
        # We have THREE progressbars 
        # progress_4
        # progress_5
        # progress_6

        #SETTING THE MINIMUM VALUE
        self.ui.progress_4.spb_setMinimum((0, 0, 0)) 
        self.ui.progress_5.spb_setMinimum((0, 0, 0)) 
        self.ui.progress_6.spb_setMinimum((0, 0, 0)) 

        #SETTING THE MAXIMUM VALUE    
        self.ui.progress_4.spb_setMaximum((360, 360, 360)) 
        self.ui.progress_5.spb_setMaximum((720, 720, 720)) 
        self.ui.progress_6.spb_setMaximum((1000, 1000, 1000)) 

        # SETTING CURRENT VALUE
        self.ui.progress_4.spb_setValue((100, 350, 250))
        self.ui.progress_5.spb_setValue((400, 350, 150))
        self.ui.progress_6.spb_setValue((370, 50, 550))

        #SETTING COLOR (R,G,B)
        # Method 1
        # Sample colors =  (255, 193, 7)(255, 87, 34) (205, 220, 57)(255, 235, 59) (156, 39, 176)(233, 30, 99)

        self.ui.progress_4.spb_lineColor(((233, 30, 99), (255, 193, 7), (0, 255, 0))) 

        self.ui.progress_5.spb_lineColor(((156, 39, 176), (255, 193, 7), (0, 255, 0))) 

        self.ui.progress_6.spb_lineColor(((156, 39, 176), (255, 87, 34), (0, 255, 0)))  


        #LINE COLOR (Method 2)
        colorTuple = ((0, 125, 125), (125, 0, 125), (125, 255, 0))
        self.ui.progress_4.spb_lineColor(colorTuple)
         

        #SETING THE INITIAL POSITION OF THE PROGRESS BAR: FROM OUTER->INWARDS
        self.ui.progress_4.spb_setInitialPos(('North', 'South', 'East'))
        self.ui.progress_4.spb_setInitialPos(('South', 'East', 'West'))
        self.ui.progress_4.spb_setInitialPos(('West', 'North', 'East'))

        #SETING THE DIRECTION OF PROGRESS OF THE PROGRESS BAR: FROM OUTER-INWARDS
        # Visible only when progress changes
        self.ui.progress_4.spb_setDirection(('Clockwise', 'AntiClockwise', 'Clockwise'))
        self.ui.progress_5.spb_setDirection(('AntiClockwise', 'Clockwise', 'AntiClockwise'))
        self.ui.progress_6.spb_setDirection(('Clockwise', 'AntiClockwise', 'Clockwise'))

        #LINE WIDTH
        self.ui.progress_4.spb_lineWidth(15)
        self.ui.progress_5.spb_lineWidth(10)
        self.ui.progress_6.spb_lineWidth(5)

        #LINE GAP
        self.ui.progress_4.spb_setGap(17)
        self.ui.progress_5.spb_setGap(7)
        self.ui.progress_6.spb_setGap(10)

        #LINE STYLE
        self.ui.progress_4.spb_lineStyle(('SolidLine', 'DotLine', 'DashLine'))

        #LINE CAP
        self.ui.progress_4.spb_lineCap(('SquareCap', 'RoundCap', 'RoundCap'))
        self.ui.progress_5.spb_lineCap(('SquareCap', 'RoundCap', 'RoundCap'))

        #VARIABLE WIDTH AND WIDTH INCREMENT
        self.ui.progress_6.variableWidth(True)
        self.ui.progress_6.spb_widthIncrement(5)

        #HIDE THE PATH
        self.ui.progress_6.spb_setPathHidden(True)


        # ANIMATE THE PROGRESS USING QTIMER
        # Change all progresses to zero on start
        QtCore.QTimer.singleShot(0, lambda: self.ui.progress_4.spb_setValue((0, 0, 0)))
        QtCore.QTimer.singleShot(0, lambda: self.ui.progress_5.spb_setValue((0, 0, 0)))
        QtCore.QTimer.singleShot(0, lambda: self.ui.progress_6.spb_setValue((0, 0, 0)))















        self.show()




    def progress(self):
        # Get global values
        global progress_1_val, progress_2_val, progress_3_val, progress_4_val, progress_5_val, progress_6_val
        
        # Set progress values
        self.ui.progress_1.rpb_setValue(progress_1_val)
        self.ui.progress_2.rpb_setValue(progress_2_val)
        self.ui.progress_3.rpb_setValue(progress_3_val)

        self.ui.progress_4.spb_setValue((progress_4_val, progress_4_val, progress_4_val))
        self.ui.progress_5.spb_setValue((progress_5_val, progress_5_val, progress_5_val))
        self.ui.progress_6.spb_setValue((progress_6_val, progress_6_val, progress_6_val))

        # Reset progresses if the maximum value is reached
        # Circular
        if progress_1_val > 420:
            progress_1_val = 0;

        if progress_2_val > 720:
            progress_2_val = 0;

        if progress_3_val > 1000:
            progress_3_val = 0;

        # Spiral
        if progress_4_val > 420:
            progress_4_val = 0;

        if progress_5_val > 720:
            progress_5_val = 0;

        if progress_6_val > 1000:
            progress_6_val = 0;
            

        # Increase values
        progress_1_val+=1
        progress_2_val+=1
        progress_3_val+=1

        progress_4_val+=1
        progress_5_val+=1
        progress_6_val+=1





  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
else:
    print(__name__, "hh")

# Press CTRL+B in sublime text to run