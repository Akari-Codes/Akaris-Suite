import os
import webview
import subPrograms.fc as fc
from pathlib import Path
import subPrograms.fb as fb
from subPrograms.cachy_sub import Cachy
from subPrograms.logger import log
from subPrograms.logger import init as loginit
cache = Cachy()
import py7zr

appName = "Manga Reader"

cache.__init__()
loginit(mode=1,appName=appName)

mangaFolder = os.getcwd() + "/bin/manga/"
Path(mangaFolder).mkdir(exist_ok=True,parents=True)
uiFolder = os.getcwd() + "/bin/ui/"
Path(uiFolder).mkdir(exist_ok=True,parents=True)
assetsFolder = os.getcwd() + "/bin/assets/"
Path(assetsFolder).mkdir(exist_ok=True,parents=True)

def getUI(name):
    data = fc.open(path = uiFolder + name + ".ui")
    return data

def listMangas():
    mangas = os.listdir(Path(mangaFolder))
    return mangas

class Api:
    def ui(self,name):
        window.load_html(getUI(name))
        return

    def loadManga(self):
        log("Loading Manga...")
        mangaList = listMangas()
        htmlContent = ""
        numContent = 0
        for x in mangaList:
            htmlContent = htmlContent + "<option value='" + numContent + "'>" + x + "</option>"
        window.run_js("""document.getElementById("mangaList").innerHTML = """ + htmlContent + """;""")

    def loadMangas(self):
        self.ui("mangaReader")
        log("Loading Mangas...")
        mangaList = listMangas()
        num = int(window.dom.get_element('#mangaList').value)
        pages = os.listdir(Path(mangaFolder + mangaList[num] + "/"))
        window.dom.get_element('#mangaTitle').text = mangaList[num]
        pageCount = len(pages) - 1
        currentPage = 1
        cache.deposit(data=pageCount, id="pageCount")
        cache.deposit(data=currentPage, id="currentPage")
        cache.deposit(data=mangaList[num], id="mangaName")
        window.run_js("""document.getElementById("mangaList").src = './bin/manga/""" + mangaList[num] + """/""" + currentPage + """.manga';""")

    def nextPage(self):
        mangaName = cache.withdraw(id="mangaName")
        pageCount = int(cache.withdraw(id="pageCount"))
        currentPage = int(cache.withdraw(id="currentPage"))
        if currentPage == 1:
            window.dom.get_element('#prevBtn').style["display"] = "none"
        else:
            window.dom.get_element('#prevBtn').style["display"] = "inline-block"
        

    def prevPage(self):
        mangaName = cache.withdraw(id="mangaName")
        pageCount = int(cache.withdraw(id="pageCount"))
        currentPage = int(cache.withdraw(id="currentPage"))
        if currentPage == 1:
            window.dom.get_element('#nextBtn').style["display"] = "inline-block"
        else:
            window.dom.get_element('#nextBtn').style["display"] = "none"

    def __init__(self):
        self.loadManga()

if __name__ == "__main__":
    api = Api()
    window = webview.create_window(title=appName, html=getUI(name="home"), js_api=api)
    webview.start()