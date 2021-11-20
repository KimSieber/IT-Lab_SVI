####################################
##### Rätsel IT-Lab vom 19.11.2021
#####
##### Rätsel - Welche 2 Zahlen wollte die Frau durcheinander teilen?
##### Frau K. erledigt eine Abrechnung mit einem 10-stelligen Taschenrechner. 
##### Als sie zwei zweistellige Zahlen durcheinander teilt, wird sie von ihrer 
##### Tochter abgelenkt und tippt deshalb bei einer der beiden Zahlen die Ziffern 
##### in umgekehrter Reihenfolge ein. In der Anzeige des Taschenrechners liest 
##### sie das Ergebnis 1,270270270.
##### »Aber Mutti«, sagt ihre Tochter, »das hättest du doch auch im Kopf ausrechnen 
##### können. Es hätte genau zwei ergeben. Durch deine Zahlendreher hast du einen 
##### periodischen Dezimalbruch erhalten.«
#####
##### Welche beiden Zahlen wollte Frau K. durcheinander teilen?
#####
##### @author    Kim Sieber
##### @create    19.11.2012
####################################

####################
### Vorgehen:
### Alle Zahlen von 10..99 gegeneinander prüfen, bis Ergebnis passt
### Alternative:
### Performanter wäre, nur Zahlen von 10..49 zu prüfen mit ihrem 
### doppelten Wert, da ja diviert durch einander 2 das Ergebnis ist.

def drehenZahl(zahl):
    c_zahl = [int(n) for n in str(zahl)]
    return (c_zahl[1]*10)+c_zahl[0]

for x in range(10,100):
    for y in range(10,100):
        if (x / y) > 1.270270 and (x / y < 1.270271):
            print ("x=",x,            "  y=",y,             "    (x / y)=",(x/y))
            print ("  ",drehenZahl(x),"  y=",y,             "    (x / y)=",(drehenZahl(x)/y))
            print ("  ",x,            "  y=",drehenZahl(y), "    (x / y)=",(x/drehenZahl(y)))
