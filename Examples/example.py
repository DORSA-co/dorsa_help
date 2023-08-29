import sys
import os
from functools import partial
from PyQt5 import QtWidgets, uic, QtCore
import help_viewer



class HelpViewer_UI(QtWidgets.QMainWindow):
    """this class is used to build an example ui window for help-viewer module

    :param QtWidgets: _description_
    """

    def __init__(self, ui_file_path):
        """this function is used to laod ui file and build GUI
        """

        super(HelpViewer_UI, self).__init__()

        # load ui file
        uic.loadUi(ui_file_path, self)
        self.setWindowFlags(QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint))

        self.window_is_open = False
        self._old_pos = None
        
        # help viewer module
        self.help_viewer = help_viewer.HelpViewer()
        self.helpviewer_frame.layout().addWidget(self.help_viewer)

        #
        self.button_connector()
    

    def button_connector(self):
        """this function is used to connect ui buttons to their functions
        """

        self.close_header_pushButton.clicked.connect(partial(self.close_win))
        self.load_pdf_toolbar_pushButton.clicked.connect(partial(self.load_pdf))
        self.clear_pdf_toolbar_pushButton.clicked.connect(partial(self.help_viewer.close_file))
        
        
    def mousePressEvent(self, event):
        """mouse press event for moving window

        :param event: _description_
        """

        # accept event only on top and side bars and on top bar
        if event.button() == QtCore.Qt.LeftButton and not self.isMaximized() and event.pos().y()<=self.header.height():
            self._old_pos = event.globalPos()


    def mouseReleaseEvent(self, event):
        """mouse release event for stop moving window

        :param event: _description_
        """

        if event.button() == QtCore.Qt.LeftButton:
            self._old_pos = None


    def mouseMoveEvent(self, event):
        """mouse move event for moving window

        :param event: _description_
        """

        if self._old_pos is None:
            return

        delta = QtCore.QPoint(event.globalPos() - self._old_pos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self._old_pos = event.globalPos()
    

    def open_win(self):
        """this function is used to show/open window
        """

        if not self.window_is_open:
            self.show()
            self.window_is_open = True


    def close_win(self):
        """
        this function closes the window
        Inputs: None
        Returns: None
        """

        # close app window and exit the program
        self.window_is_open = False
        self.close()
    

    def show_alert_window(self, title, message, need_confirm=False, level=0):
        """This function is used to create a alert/confirm window

        :param title: _description_
        :type title: _type_
        :param message: _description_
        :type message: _type_
        :param need_confirm: _description_, defaults to False
        :type need_confirm: bool, optional
        :param level: _description_, defaults to 0
        :type level: int, optional
        :return: _description_
        :rtype: _type_
        """

        level = 0 if level<0 or level>2 else level

        # create message box
        alert_window = QtWidgets.QMessageBox()

        # icon
        if level==0:
            alert_window.setIcon(QtWidgets.QMessageBox.Information)
        elif level==1:
            alert_window.setIcon(QtWidgets.QMessageBox.Warning)
        elif level==2:
            alert_window.setIcon(QtWidgets.QMessageBox.Critical)

        # message and title
        alert_window.setText(message)
        alert_window.setWindowTitle(title)

        # buttons
        if not need_confirm:
            alert_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
            alert_window.button(QtWidgets.QMessageBox.Ok).setText('OK')
        else:
            alert_window.setStandardButtons(QtWidgets.QMessageBox.Cancel | QtWidgets.QMessageBox.Ok)
            alert_window.button(QtWidgets.QMessageBox.Ok).setText('Confirm')
            alert_window.button(QtWidgets.QMessageBox.Cancel).setText('Cancel')
        
        alert_window.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)

        # show
        returnValue = alert_window.exec()

        if not need_confirm:
            return True if returnValue == QtWidgets.QMessageBox.Ok else True
        else:
            return True if returnValue == QtWidgets.QMessageBox.Ok else False
    
    
    def load_pdf(self):
        """This function is used to load a user selected pdf from directory
        """

        # open dialog to select pdf from directory
        options = QtWidgets.QFileDialog.Options()
        pdf_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Select PDF to Load', directory='./', filter='Image File(*.pdf)', options=options)
        if pdf_path == '':
            return

        # laod pdf with help-viewer
        res, message = self.help_viewer.load_pdf_file(pdf_address=pdf_path)
        if not res:
            self.show_alert_window(title='Error', message='Failed to load help file, please ensure right file format.', need_confirm=False, level=2)
        
    


    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = HelpViewer_UI(ui_file_path='./example_UI.ui')
    window.open_win()
    app.exec_()