usage: hue_inverter.py [-h] -m M -x X -i IMAGE

Inverter Faixas Hue

options:
  -h, --help            show this help message and exit      
  -m M, --m M           Valor do hue (int entre 0-359)       
  -x X, --x X           Tamanho da faixa (int entre 0-179)   
  -i IMAGE, --image IMAGE
                        Caminho da imagem (string)
                        
Exemplos:
  > python hue_inverter.py -m 30 -x 60 -i disco_hue.png
  > python hue_inverter.py -m 354 -x 25 -i carro_vermelho.jpg
  > python hue_inverter.py -m 200 -x 20 -i carro_azul.png