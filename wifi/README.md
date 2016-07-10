# ESP8266サンプル


Wi-FiモジュールのESP8266を使ったATコマンドサンプルです。  
秋月電子通商のESP-WROOM-02(DIP化キット)で試しています。  

ピンの接続は以下のとおりです。  
(Pyboard --> ESP-WROOM-02)  
3V3 --> 3V3  
3V3 --> 抵抗10kΩ --> EN  
3V3 --> 抵抗10kΩ --> IO2  
3V3 --> 抵抗10kΩ --> IO0  
GND --> GND(※３箇所)  
GND --> 抵抗10kΩ --> IO15  
Y1 --> RXD  
Y2 --> TXD  

##コマンド実行例
```
from esp8266 import ESP8266
e = ESP8266()
e.write('AT+RST¥r¥n')
e.write('AT¥r¥n')
e.write('AT+GMR¥r¥n')
```
