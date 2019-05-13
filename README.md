# RECOGNIZER
## Apraksts
Sejas atpazīšanas rīks, izmantojot Raspberry Pi 3, OpenCV un VNC.
## Saturs
1. [Instalēšana](#Saturs)
     - [OpenCV](#OpenCV)
     - [Flask](#Flask)
     - [VNC](#VNC)
2. [Lietošana](#Lietošana)
## Instalēšana
### OpenCV
![opencv-logo](https://user-images.githubusercontent.com/48751019/56082316-183b1380-5e20-11e9-975e-72c03db68796.png)
- Vispirms jāveic OpenCV instalēšana Raspberry Pi. Šobrīd šajā projektā tiek izmantota OpenCV 4.0.0 versija. Instalācijas procesu veicu pēc pamācības (https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/), kurā ļoti skaidri tika aprakstīts katrs instalēšanas solis.
### VNC
- Komanda, lai instalētu VNC
```
sudo apt-get update
```
```
sudo apt-get install realvnc-vnc-server
```
- VNC iespējošana
```
sudo raspi-config
```
-> Interfacing Options -> VNC -> Yes
### Flask
![flask](https://user-images.githubusercontent.com/48751019/56082346-913a6b00-5e20-11e9-86e4-e6088dbb00f1.png)
- Šim projektam vajadzīgs arī Flask (*micro web framework*). Lai instalētu un uzstādītu Flask,  es sekoju pamācībām (https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/2 un http://mattrichardson.com/Raspberry-Pi-Flask/).
- Servera palaišanai izmantoju komandas:
```
export FLASK_ENV=development
```
```
FLASK_APP=appname.py flask run --host=0.0.0.0
```
## Lietošana
- Kad veikta VNC instalācija, var iestatīt attālināto displeju, lai redzētu kameras iegūtos attēlus reālā laikā. To izdara ar šīm komandām:
```
vncserver :1 -geometry 1366x600 -depth 16 -pixelformat rgb565
export DISPLAY=:1
```
- Pirmais solis ir datu ievākšana, ko veic Kods face-data.py.
```
python face-data.py
```
- Kods face-trainer.py veic algoritma mācīšan jeb iemāca pirmajā solī iegūtos sejas attēlus.
```
python face-trainer.py
```
- Kods recognizer.py veic sejas atpazīšanu.
```
python recognizer.py
```
