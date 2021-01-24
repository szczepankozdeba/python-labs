
from xml.dom import minidom

DOMTree = minidom.parse("file.xml")
collection = DOMTree.documentElement

beers = collection.getElementsByTagName("car")

for beer in beers:
    nr = beer.getElementsByTagName("nr")[0]
    marka = beer.getElementsByTagName("marka")[0]
    jakosc = beer.getElementsByTagName("jakosc")[0]
    dostepnosc = beer.getElementsByTagName("dostepnosc")[0]

    print("nr: ", nr.childNodes[0].data)
    print("marka: ", marka.childNodes[0].data)
    print("jakosc : ", jakosc.childNodes[0].data)
    print("dostepnosc: ", dostepnosc.childNodes[0].data)
