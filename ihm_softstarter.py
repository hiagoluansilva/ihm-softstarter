from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from random import *
import serial

send1=''
send2=''
send3=''
valor=''
rel=''
    
class Menu(Screen):
    pass

class Config(Screen):
    temp_sub = ObjectProperty(None)
    temp_desc = ObjectProperty(None)

    def soma(self):
        self.temp_sub.text = str(int(self.temp_sub.text)+1)
        if (int(self.temp_sub.text)>55):
            self.temp_sub.text =str(55)

    def subtrai(self):
        self.temp_sub.text = str(int(self.temp_sub.text)-1)
        if (int(self.temp_sub.text)<3):
            self.temp_sub.text =str(3)

    def soma1(self):
        self.temp_desc.text = str(int(self.temp_desc.text)+1)
        if (int(self.temp_desc.text)>55):
            self.temp_desc.text =str(55)

    def subtrai1(self):
        self.temp_desc.text = str(int(self.temp_desc.text)-1)
        if (int(self.temp_desc.text)<3):
            self.temp_desc.text =str(3)

class First(Screen):
    pass

class Exerc2_1(Screen):
    tensao = ObjectProperty(None)   
    def dois_1(self):
        global send1
        global send2
        global send3
        send1 = '2'
        send2 = '1'
        val = self.tensao.text
        val.replace(" ", "");
        send3= val
        self.tensao.text=''

class Exerc3_1(Screen):

    tensao_ADC = ObjectProperty(None)

    def medir_adc(self):
        global send1
        global send2
        global send3
        global valor
        global rel
        ser.write('X'.encode('ASCII'))
        valor = ser.read(4).decode('ASCII')
        valor += 'V'
        send1 = '3'
        send2 = '1'
        send3 = valor
        self.tensao_ADC.text=valor
        print(valor)
        valor=''

class IHM_Softstarter(App):

    master = ScreenManager()
    exerc1 = ["exerc1_1", "exerc1_2", "exerc1_3", "exerc1_4", "exerc1_5"]
    suffle= randint(0,4)

    start = 'Y'
    stop = 'W'
    
    def build(self):
        IHM_Softstarter.master.add_widget(Menu(name="menu"))
        IHM_Softstarter.master.add_widget(Config(name="config"))
        IHM_Softstarter.master.add_widget(First(name="first"))
        return IHM_Softstarter.master
    
    def envia(self):
        global send1
        global send2
        global send3
        ser.write(IHM_Softstarter().start.encode('ASCII'))
        ser.write(send1.encode('ASCII'))
        ser.write(send2.encode('ASCII'))
        ser.write(send3.encode('ASCII'))
        ser.write(IHM_Softstarter.stop.encode('ASCII'))



if __name__ == '__main__':
    try:
        ser = serial.Serial('COM3', 9600, timeout=0)
    except:
        print ("Falha na Conexão")
       
    IHM_Softstarter().run()

    ser.close()
