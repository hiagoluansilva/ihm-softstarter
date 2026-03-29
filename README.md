🇧🇷 Português | 🇺🇸 [English](#english)

# ihm-softstarter

Interface HMI em Python/Kivy para controle do Soft Starter STM32 via porta serial.

## Requisitos

```bash
pip install kivy pyserial
python ihm_softstarter.py
```

## Configuração serial

```python
serial.Serial('COM3', 9600)  # Windows
```

## Hardware relacionado

[stm32-softstarter](https://github.com/hiagoluansilva/stm32-softstarter)
Centro Tecnológico Liberato — Novo Hamburgo/RS

---

<a name="english"></a>
🇧🇷 [Português](#) | 🇺🇸 English

# ihm-softstarter

Python/Kivy HMI application for STM32 Soft Starter control via serial port.

## Requirements

```bash
pip install kivy pyserial
python ihm_softstarter.py
```

## Serial configuration

```python
serial.Serial('COM3', 9600)  # Windows
# or /dev/ttyUSB0 on Linux
```

## Related hardware

[stm32-softstarter](https://github.com/hiagoluansilva/stm32-softstarter)
Centro Tecnológico Liberato — Novo Hamburgo/RS, Brazil
