## DIY WiFi Catfeeder
Uw katten op afstand voer toedienen <br>

<img src="https://github.com/pappavis/Easylab4kids_lessen/blob/master/lesmateriaal/082_ESP8266_kattenvoerder/plaatjes/kattenvoerder_anim.gif?raw=true" width="30%" height="30%">

# Waarom?
Omdat het kan. Omdat het moeilijk is. Je kunt ook in een winkel kopen. Weet ik. 

# Hoe werkt het
Een computerprogramma doseert kattenvoer op vaste intervals. 

# Ervaring vereist
 - Niveau 1. "Ikea-niveau.. je moet , instructies kunnen lezen, en ze opvolgen.
 - Niveau 2. Gamma bouwmarkt doe-het-zelfer. Je heb de basisplan, nu gaat je zelf klussen.

Wij gaan aan de slag met (virtuele) gereedschap.  
Heb je dit nooit eerder gedaan, dan adviseer ik je de Ikea-niveau ;)

# Benodigheden
Uiteraard, voor je beginnen zorg ervoor dat je deze in huis heb.

## Randapparatuur
 - 1x ESP8266 zoals Wemos D1 Mini  €5,00
 - 1x Raspberry Pi zero W 1.3  €12,00
 - 1x SG90 microservo.
 - 1x Lege colaflesje 500ml, of 1L.
 - 1x schaar.

## Software benodigd
 - 8Gb SD card met <a href="http://www.sensorsiot.org/diet-pi-supporting-material-videos-126-and-128/" target="_blank">dietpi image</a> van Andreas Spiess.
 - Micropython gedeploy op de ESP8266.

Een ESP-01 werkt ook, maar wegens tekort aan output pinnen niet geschikt.

 # Stappenplan
  - Zet de Micropython over op ESP8266
  - Maak jumper van D0 naar RST op Wemos d1 mini.
  - Deploy de node-red flow naar dietpi.
  - Gebruik je mobiele telefoon op http://dietpi:1880/ui/#/1
  
## TODO: volledig documentatie maken.
 
# Credits
 Ontwikkeld door Michiel Erasmus
 
<img src="https://github.com/pappavis/Easylab4kids_lessen/raw/master/plaatjes/Easy_Lab_logo_kleur.png?raw=true" width="20%" height="20%">
<br>
