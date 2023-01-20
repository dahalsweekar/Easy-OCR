# Easy-OCR

Implementing EasyOCR

EasyOCR is another Optical Character Recognition tool that is used to recognize the characters in the image. Like KerasOCR, this tool also allows user to use the pre built trained model or to create their own model. For the purpose of testing, I am using prebuilt trained model. This OCR supports 80 different languages including Nepali and Newari. 
Easy OCR implements ResNet, LSTM and greedy decoder inorder to recognize the characters in the image. 

https://github.com/JaidedAI/EasyOCR

  

Like before, I have used data as images of backside of the citizenship card.But due to lack of High defination images, the accuracy of recognizing individual character is still poor. Nonetheless, the accuracy of recognizing and detecting the text outperforms Tesseract. 

Similar to Keras-OCR, EasyOCR makes spelling mistake here and there.

 Output:

![Screenshot from 2023-01-20 12-45-36](https://user-images.githubusercontent.com/99968233/213639442-0fdad2c2-6909-46fd-9330-ac922b5ffa80.png)

Government of Nepal has Issued Ihls Cltizenship Cerlilicate wuth followtng details
Citizenship Ccrtificate No.
31-1-76-03422
Ser Mtalc
Full Namc
SUBASH KHATRI
Datc of Birtb (ADJ:
Year 2001
Month APR
Day 14
Birth
District Makawanpur
Municipality
Thaha
Ward No 7
Pcrmancal Address
District Makawanpur
Mlunicipality
Thaha
Ward
a9aanATTT (7 308} ahfaa xt A1or (AN4T fes0a€ |
TNRaa FTAA *6
91"9t
"Znna&7t0TT
(@h
33atun
aru
5TTt 57 7ratF xdra
377dd
Aa 4174Taatt
Zh Dnaa
Matff
7oU5' e}te
TAnu
T7T
Tnoh7TZ+a) {Zrt1 (TIt 4T4T4rT AT Fet #ai473Fs6377"
racc
So:
179
66 &1 _
sfyad
3047
[

Output:

![cleaner](https://user-images.githubusercontent.com/99968233/213639428-ef1dce9e-1dcd-4585-ac84-c3cbb3ebd332.png)

Govemment of Nepal has issued tlis Citizenship Certificate with following details
Citizenship Certificatc No::
3517/3812
Sex: Male
Full Name:
PHANINDRA BADI
Date of Birth (AD):
Year:1983
Month:MAY
Day:16
Birth Place:
District: Dailekh
VDC
Dullu
Ward No:: 1
Permanent Address:
District: Dailekh
VDC
Dullu
Ward Noa:1
Aaaa T?o63 qhifjH 41 T0RoballomuTsuat 5
TMaafaRTH; @riG
fAa ?olgk-o4-?&
4AT Q dropd1 TRda
salfeify f4* afeapra
@y:.14*14
(44)
T;e HeRq
culf:wg fodl 3eemi
TRddi:
MHI4 MT
#Radl
T R;Zar vldici
vulf :qofoje3ro
TfAfa: Roeo_o?-or
41
[zIa +u 91-UAT #fojopar] feril WRIRTA <1fa4r a1e +rfa4H grrgeldt
FofaRiaf 4€ K]
