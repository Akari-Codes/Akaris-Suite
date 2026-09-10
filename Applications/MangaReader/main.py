import os
import webview
import subPrograms.fc as fc
from pathlib import Path
import subPrograms.fb as fb
from subPrograms.cachy_sub import Cachy
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import threading
import shutil
from py7zr import pack_7zarchive, unpack_7zarchive
try:
    shutil.register_archive_format('7zip', pack_7zarchive, description='7zip archive')
    shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)
except:
    print('shutil.RegistryError: .7z is already registered for "7zip"')
cache = Cachy()

formating = """
<style>
    body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  color:magenta;
}

body::-webkit-scrollbar {
  display: none;
}

#container-1 {
    color:magenta;
    background: #000000;
    background: linear-gradient(90deg,rgba(0, 0, 0, 1) 0%, rgba(94, 23, 110, 1) 45%, rgba(128, 29, 106, 1) 70%, rgba(255, 0, 195, 1) 100%);
    text-align: center;
}

#bd {
  margin-top: -19px;
  padding-bottom: 200%;
  opacity: 1;
  background-color: black;
  background-image: radial-gradient(circle, purple 2px, transparent 2px);
  background-size: 15px 15px;
  text-align: center;
  align-items: center;
  align-self: center;
  align-content: center;
}

#manga-container {
background-color:rgb(27, 0, 40);
border-color: magenta;
border-style:solid;
border-radius: 10px;
width:400px;
height:610px;
position:absolute;
top: 60%;
left: 50%;
margin-top: -9em;
margin-left: -12em;
}

.manga-text {
    color:magenta;
}
#pp {display:none;}
    </style>
    <html>
        <!DOCTYPE html>
        <head>
            <title>Akaris Manga Reader</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="Akaris Manga Reader">
            <meta name="author" content="Akari Codes">
        </head>
        <div id="container-1">
            <br>
            <h2 id="title">Manga Format</h2>
            <br>
        </div>
        <div id="bd">
            <br><br>
            <button id="back-btn" onclick="pywebview.api.loadManga()">Back</button>
            <div id="manga-container">
                <br>
                <h3>Manga Formatting for Import</h3>
                <p>All images must be named as an integer in the order of the images / pages with the extension of manga instead of whatever image one it has.<br><br>The Cover image must be named the name of the manga then the extension to be cover.<br><br>All Pages / Images including the cover must be placed into a folder with the manga title as the folder name.<br><br>Then the manga archive must extract the folder rather than the folder contents.
                </p>
            </div>
        </div>
"""

def getMangaBooks(mangaBooks):
    mangaCollection = """
<style>
    body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  color:magenta;
}

body::-webkit-scrollbar {
  display: none;
}

#container-1 {
    color:magenta;
    background: #000000;
    background: linear-gradient(90deg,rgba(0, 0, 0, 1) 0%, rgba(94, 23, 110, 1) 45%, rgba(128, 29, 106, 1) 70%, rgba(255, 0, 195, 1) 100%);
    text-align: center;
    height: 180px;
    float:center;
}

#bd {
  margin-top: -19px;
  padding-bottom: 100%;
  opacity: 1;
  background-color: black;
  background-image: radial-gradient(circle, purple 2px, transparent 2px);
  background-size: 15px 15px;
  text-align: center;
  width:100%;
}

#mangaContainer {
    color:magenta;
}

.manga-item {
    font-size: 12px;
    border:5px solid black;
    resize: both;
    background: #ff3eec33;
    border-image: url("data:image/svg+xml;charset=utf-8,%3Csvg width='100' height='100' viewBox='0 0 100 100' fill='none' xmlns='http://www.w3.org/2000/svg'%3E %3Cstyle%3Epath%7Banimation:stroke 5s infinite linear%3B%7D%40keyframes stroke%7Bto%7Bstroke-dashoffset:776%3B%7D%7D%3C/style%3E%3ClinearGradient id='g' x1='0%25' y1='0%25' x2='0%25' y2='100%25'%3E%3Cstop offset='0%25' stop-color='%232d3561' /%3E%3Cstop offset='25%25' stop-color='%23c05c7e' /%3E%3Cstop offset='50%25' stop-color='%23f3826f' /%3E%3Cstop offset='100%25' stop-color='%23ffb961' /%3E%3C/linearGradient%3E %3Cpath d='M1.5 1.5 l97 0l0 97l-97 0 l0 -97' stroke-linecap='square' stroke='url(%23g)' stroke-width='3' stroke-dasharray='388'/%3E %3C/svg%3E") 1;
    display: inline-block;
    height:400px;
    width:200px;
    border-radius: 10px;
    float: none;
    margin-left: 20px;
}

.manga-item p {
color:magenta;}

.open-btn {
    border-style: solid;
    border-width: 3.5px;
    border-radius: 5px;
    border-color: purple;
    animation-name: openBtnAni;
    animation-duration: 5s;
    animation-iteration-count: infinite;
    background-color: rgb(58, 0, 58);
    color:purple
}

@keyframes openBtnAni {
  0%   {border-color: purple;color:gold;}
  25%  {border-color: orange;color:red}
  50%  {border-color: gold;color:purple}
  75%  {border-color: red;color:orange}
  100% {border-color: purple;color:gold;}
}

.btn {
    border-style: inset;
    border-radius: 5px;
    border-width: 4px;
    border-color:magenta;
    background-color: transparent;
    color: magenta;
    font-size: 12px;
    font-weight: 15px;
    padding: 5px 7px 5px 7px;
}

.btn:hover {
    border-color:red;
    color: red;
}

.btn2 {
    border-style: inset;
    border-radius: 5px;
    border-width: 4px;
    border-color:magenta;
    background-color: transparent;
    color: magenta;
    font-size: 12px;
    font-weight: 15px;
    padding: 5px 7px 5px 7px;
}

.btn2:hover {
    border-color: darkred;
    color:red;
}

.btnoption {
    background-color: rgb(72, 0, 0);
    border-color:darkred;
    border-style:solid;
    border-width: 5px;
    color:red;
}
.btnoption:first-of-type {
    border-radius: 0px 0px 5px 5px;
}

.btnoption:last-of-type {
    border-radius: 5px 5px 0px 0px;
}

#addMangaBtn {
    border-style: solid;
    border-width: 3.5px;
    border-radius: 5px;
    border-color: purple;
    animation-name: addMangaBtnAni;
    animation-duration: 5s;
    animation-iteration-count: infinite;
    background-color: rgb(58, 0, 58);
    color:magenta;
    font-weight: bold;
}
#addMangaBtn:hover {
    border-color: magenta;
    color:red;
}
</style>
<html>
    <!DOCTYPE html>
        <head>
            <title>Akaris Manga Reader</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="Akaris Manga Reader">
            <meta name="author" content="Akari Codes">
        </head>
        <div id="container-1">
            <br>
            <h2 id="title">Manga Collection</h2>
            <br>
            <button id="addMangaBtn" onclick='pywebview.api.addManga()'>+ Add Manga</button> <button id="addMangaBtn" onclick="pywebview.api.mangaFormat()">Manga Format</button>
        </div>
        <div id="bd">
        <br><br>
            <div id="mangaCollection">""" + mangaBooks + """</div>
            </div>
        </div>
</html>
"""
    return mangaCollection

def getMangaPages(mangaPages):
    mangaReader = """
    <style>
    body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  color:magenta;
}

body::-webkit-scrollbar {
  display: none;
}

#container-1 {
    color:magenta;
    background: #000000;
    background: linear-gradient(90deg,rgba(0, 0, 0, 1) 0%, rgba(94, 23, 110, 1) 45%, rgba(128, 29, 106, 1) 70%, rgba(255, 0, 195, 1) 100%);
    text-align: center;
}

#bd {
  margin-top: -19px;
  padding-bottom: 100%;
  opacity: 1;
  background-color: black;
  background-image: radial-gradient(circle, purple 2px, transparent 2px);
  background-size: 15px 15px;
  text-align: center;
  align-items: center;
  align-self: center;
  align-content: center;
}

#manga-container {
background-color:rgb(27, 0, 40);
border-color: magenta;
border-style:solid;
border-radius: 10px;
width:400px;
height:610px;
position:absolute;
top: 60%;
left: 50%;
margin-top: -9em;
margin-left: -12em;
}

.manga-text {
    color:magenta;
}
#pp {display:none;}
    </style>
    <html>
        <!DOCTYPE html>
        <head>
            <title>Akaris Manga Reader</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="Akaris Manga Reader">
            <meta name="author" content="Akari Codes">
        </head>
        <div id="container-1">
            <br>
            <h2 id="title">Manga Reader</h2>
            <h5 id="subtitle">Manga Name - <font id="manga-name"></font></h5>
            <br>
        </div>
        <div id="bd">
            <button id="back-btn" onclick="pywebview.api.loadManga()">Back</button>
            <div id="manga-container">
                <br>
                <img id="manga-frame" src="" width="350px" height="500px"></img><br><br>
                <button id="pp" onclick="p()">Previous Page</button> <button id="np" onclick="n()">Next Page</button>
                <p class="manga-text">Page <font id="page-num"></font> / <font id="total-p"></font></p>
            </div>
        </div>
    <script>
    const image_list = [""" + mangaPages + """]
    var tpages = image_list.length
    var currentPage = 1
    document.getElementById('total-p').innerText = tpages.toString()
    document.getElementById('page-num').innerText = currentPage.toString()
    document.getElementById('manga-frame').src = image_list[0]
    function p() {
        currentPage = currentPage - 1
        document.getElementById('page-num').innerText = currentPage.toString()
        document.getElementById('manga-frame').src = image_list[currentPage - 1]
        if(currentPage === 1) {document.getElementById('pp').style.display = "none"} else {document.getElementById('pp').style.display = "inline-block"}
        if(currentPage === tpages) {document.getElementById('np').style.display = "none"} else {document.getElementById('np').style.display = "inline-block"}
    }
    function n() {
        currentPage = currentPage + 1
        document.getElementById('page-num').innerText = currentPage.toString()
        document.getElementById('manga-frame').src = image_list[currentPage - 1]
        if(currentPage === 1) {document.getElementById('pp').style.display = "none"} else {document.getElementById('pp').style.display = "inline-block"}
        if(currentPage === tpages) {document.getElementById('np').style.display = "none"} else {document.getElementById('np').style.display = "inline-block"}
    }
    </script>"""
    return mangaReader
appName = "Manga Reader"

cache.__init__()

mangaFolder = os.getcwd() + "/bin/manga/"
Path(mangaFolder).mkdir(exist_ok=True,parents=True)
uiFolder = os.getcwd() + "/bin/ui/"
Path(uiFolder).mkdir(exist_ok=True,parents=True)
if not Path(uiFolder + "mangaFormat.html").exists():
    Path(uiFolder + "mangaFormat.html").touch(exist_ok=True)
    with open(Path(uiFolder + "mangaFormat.html"),'w') as f:
        f.write(formating)
assetsFolder = os.getcwd() + "/bin/assets/"
Path(assetsFolder).mkdir(exist_ok=True,parents=True)

def getUI(name):
    data = fc.open(path = uiFolder + name + ".html")
    return data

def listMangas():
    mangas = os.listdir(Path(mangaFolder))
    return mangas

class Api:
    def ui(self,name="", mode="file", html=""):
        if mode == "file":
            window.load_html(getUI(name))
            return
        elif mode == "string":
            window.load_html(html)
            return

    def loadManga(self):
        mangaList = listMangas()
        mangaBooks = ""
        for x in mangaList:
            mangaBooks = mangaBooks + """
<div class="manga-item">
    <br>
    <img src='http://127.0.0.1:9999/bin/manga/""" + x + """/poster.cover' width="180" height="275">
    <br>
    <p>""" + x + """</p>
    <button class="open-btn"  onclick="pywebview.api.loadMangas('""" + x + """')">Open</button><br><br>
    <button class="delete-btn" onclick="pywebview.api.deleteManga('""" + x + """')">Delete Manga</button>
</div>
"""
        htmlContent = getMangaBooks(mangaBooks)
        self.ui("mangaReader", mode="string", html=htmlContent)

    def loadMangas(self,name):
        pages = sorted(os.listdir(Path(mangaFolder + name + "/")))
        mangaPages = ""
        for x in pages:
            mangaPages = mangaPages + "'http://127.0.0.1:9999/bin/manga/" + name + "/" + x + "',"
        htmlContent = getMangaPages(mangaPages)
        self.ui("mangaReader", mode="string", html=htmlContent)
        window.dom.get_element('#manga-name').text = name

    def deleteManga(self,name):
        fc.rmdir(path = mangaFolder + name + "/", recursive=True)
        self.loadManga()

    def addManga(self):
        mangaArchive = fb.get(title="Select Manga Archive", fileTypes=[("Manga Book Archive (Book Content)", "*.mangaBook")])
        shutil.unpack_archive(mangaArchive, mangaFolder, "7zip")
        self.loadManga()

    def mangaFormat(self):
        self.ui("mangaFormat")

if __name__ == "__main__":
    server = ThreadingHTTPServer(("localhost", 9999), SimpleHTTPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    api = Api()
    mangaList = listMangas()
    mangaBooks = ""
    for x in mangaList:
        mangaBooks = mangaBooks + """
<div class="manga-item">
    <br>
    <img src='http://127.0.0.1:9999/bin/manga/""" + x + """/poster.cover' width="180" height="275">
    <br>
    <p>""" + x + """</p>
    <button class="open-btn"  onclick="pywebview.api.loadMangas('""" + x + """')">Open</button><br><br>
    <button class="delete-btn" onclick="pywebview.api.deleteManga('""" + x + """')">Delete Manga</button>
</div>
"""
    htmlContent = getMangaBooks(mangaBooks)
    window = webview.create_window(title=appName, html=htmlContent, js_api=api)
    webview.start()
