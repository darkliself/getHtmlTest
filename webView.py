from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
#from PyQt5.QtCore import QUrl
import os


# testing webView
# self.textBrowser = QtWidgets.QTextBrowser(self.aceTab)
# self.textBrowser.setObjectName("textBrowser")
# self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)

# self.webView = QWebView()
# self.webView.setHtml(testText)
# self.gridLayout_2.addWidget(self.webView, 0, 0, 1, 1)

class editableView(QWebEngineView):
    def __init__(self):
        super().__init__()
        page = self.page()


# end of testing webView
class AceWebView:
    def __init__(self, layout):
        testText = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=9">
    <title>Ace Winforms</title>
    <style type="text/css" media="screen">
        #editor {
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
        }
    </style>
    <script src="https://code.jquery.com/jquery-3.4.0.min.js" integrity="sha256-BJeo0qm959uMBGb65z40ejJYGSgR7REI4+CW1fNKwOg=" crossorigin="anonymous"></script>
</head>
<body>
    <div id="editor">
        some text here
    </div>
    <div id="commandline" style="position: absolute; bottom: 10px; height: 20px; width: 800px;"></div>
    <!--<script src="http://cdn.jsdelivr.net/ace/1.1.01/min/ace.js" type="text/javascript" charset="utf-8"></script>-->

    <script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.3.3/ace.js" type="text/javascript" charset="utf-8"></script>

    <script>
       var editor = ace.edit("editor");
    editor.setTheme("ace/theme/ambiance");
    editor.getSession().setMode("ace/mode/csharp");
    </script>
    <div id="tested"></div>
</body>
</html>
                   """
        self.browserView = QWebEngineView()
        layout.addWidget(self.browserView, 0, 0, 1, 1)
        ##file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ace_page.html"))
        ##self.someTest.load(QUrl.fromLocalFile(file_path))
        self.browserView.setHtml(testText)
        somez = self.browserView.page().runJavaScript("""
                    //alert('its wotking')
                """)

        def write_html_to_file(html):
            test = html
            print(test)

        self.browserView.page().toHtml(write_html_to_file)

        # print(testText)



        #somez2 = self.someTest.page().toHtml()



        # self.someTest.QWebEnginePage.triggerAction(9)

# test.triggerPageAction(9)
# <script src="http://d1n0x3qji82z53.cloudfront.net/src-min-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>