# IHM Soft Starter — Interface Gráfica Python/Kivy

🇧🇷 **Português** | 🇺🇸 [English](#english)

---

## Português

Interface Homem-Máquina (IHM) para o soft starter STM32, desenvolvida em Python com Kivy. Comunica via porta serial COM3 a 9600 bps.

### O que faz
- Exibe status do soft starter em tempo real
- Permite configurar parâmetros de rampa (subida/descida)
- Comunica com o STM32 via **serial COM3 a 9600 bps**
- Interface gráfica responsiva construída com **Kivy (Python)**

### Configuração serial
```python
serial.Serial('COM3', 9600)
```

### Requisitos
```
pip install kivy pyserial
```

### Executar
```bash
python ihm_softstarter.py
```

### Plataforma
Python 3.x + Kivy + pyserial — Windows/Linux

---

## English

Human-Machine Interface (HMI) for the STM32 soft starter, built in Python with Kivy. Communicates via serial port COM3 at 9600 bps.

### What it does
- Displays soft starter status in real time
- Allows configuring ramp parameters (up/down)
- Communicates with STM32 via **serial COM3 at 9600 bps**
- Responsive GUI built with **Kivy (Python)**

### Serial configuration
```python
serial.Serial('COM3', 9600)
```

### Requirements
```
pip install kivy pyserial
```

### Run
```bash
python ihm_softstarter.py
```

### Platform
Python 3.x + Kivy + pyserial — Windows/Linux
