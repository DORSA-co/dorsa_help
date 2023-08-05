"""
########################################################
This PyQt-based module is developed to create a help-viewer object.
The module uses a PDF explorer API to load PDF help files

Dependencies:
    This module is based on PyQt5 QtWebEngineWidgets. So, to use this module in your code you must have PyQt5 library installed.
    - PyQt5
    - filetype

Features:
    - PDF explorer to load pdf files
    - Exploring, zooming in/out, highlighting, editing and saving pdf file

Notice:
    This module is completely PyQt5-based and it's not possible to be used with other non-Qt-based applications at this moment.

Designed and developed by Ali Salehi
########################################################
"""


from PyQt5 import QtCore, QtWebEngineWidgets
import filetype



class HelpViewer(QtWebEngineWidgets.QWebEngineView):

    def __init__(self, pdfjs_root_path: str):
        """This class is used to build the Help-Viewer object to show help files

        :param pdfjs_root_path: root path of pdfjs folder
        :type pdfjs_root_path: str
        """

        super(HelpViewer, self).__init__()

        # PDF explorer API path
        self.pdfjs_path = 'file:///%s/pdfjs/web/viewer.html' % (pdfjs_root_path)

        # create PDF explorer module
        self.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
        self.showMaximized()
    

    def load_pdf_file(self, pdf_address: str):
        """This function is used to load a pdf file from path and set to PDF-Viewer

        :param pdf_address: pdf file path
        :type pdf_address: str
        :return: Tuple of Boolean detemining pdf loading is successfull and message
        :rtype: (boolean, str)
        """

        try:
            if not self.is_pdf(pdf_address=pdf_address):
                return False, ''
            
            url = '%s?file=%s' % (self.pdfjs_path, pdf_address)
            pdf_url = QtCore.QUrl(QtCore.QUrl.fromUserInput(self.convert_pdf_address(pdf_address=url)))
            pdf_url.setFragment("page=1")
            self.load(pdf_url)
            self.showMaximized()

            return True, ''
        
        except Exception as e:
            self.close_file()
            return False, e
    

    def close_file(self):
        """This function is used to close current help file
        """

        try:
            self.close()
            return
        
        except:
            return
    
    
    def convert_pdf_address(self, pdf_address: str):
        """This function is used to convert pdf address to form that can be loaded by PDF-Explorer module

        :param address: pdf file path
        :type address: str
        :return: _description_
        :rtype: _type_
        """

        return pdf_address.replace('\\', '/')


    def is_pdf(self, pdf_address: str):
        """This function is used to check if input file is a valid pdf

        :param pdf_address: pdf file path
        :type pdf_address: str
        """

        return filetype.guess(pdf_address).mime == 'application/pdf'
