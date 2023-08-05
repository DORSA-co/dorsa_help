# Help_Viewer

Help-Viewer is a PyQt-based module developed to create a help-viewer object. The module uses a PDF explorer API to load PDF help files.

## Features
    - PDF explorer to load pdf files
    - Exploring, zooming in/out, highlighting, editing, saving and printing pdf file

## Notice
This module is completely PyQt5-based and it's not possible to be used with other non-Qt-based applications at this moment.

## Dependencies
    - PyQt5
    - filetype

## Installation
    1- Install dependencies using pip install
    2- clone Help-Viewer repository

## Documentation
Sphinx documents are not available at this moment.

## Quick Start
To use the Help-Viewer module, follow these steps:

1. Import the module: 
``` python
import help_viewer
```

2. Create a `Help-Viewer` object inside a PyQt QMainWindow object and assign it to a frame object:
``` python
qmainwindow_obj.help_viewer = help_viewer.HelpViewer(pdfjs_root_path=os.path.dirname(sys.argv[0]))
qmainwindow_obj.helpviewer_frame.layout().addWidget(qmainwindow_obj.help_viewer)
```
#### Input parameters:
    - pdfjs_root_path: It is the path to pdfjs folder included with the repo. The pdfjs API is used to build PDF-explorer module

3. Add a PDF file
``` python
res, message = qmainwindow_obj.help_viewer.load_pdf_file(pdf_address=pdf_path)
```
#### Input parameters:
    - pdf_address: Path of the pdf file
    
# Main functions

## Load a PDF file
``` python
res, message = qmainwindow_obj.help_viewer.load_pdf_file(pdf_address=pdf_path)
```
#### Input parameters:
    - pdf_address: Path of the pdf file

## Remove/clear Help-Viewer pdf file
```python
qmainwindow_obj.help_viewer.close_file()
```
















