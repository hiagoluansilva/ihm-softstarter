# ihm-softstarter

Interface Homem-Máquina (IHM) em Python/Kivy para controle e configuração do Soft Starter STM32.

## Descrição

Aplicativo desktop desenvolvido com o framework Kivy que serve como interface de controle para o soft starter embarcado (`stm32-softstarter`). Permite configurar os parâmetros de rampa e enviar comandos via porta serial.

## Funcionalidades

- Tela de menu principal
- Configuração de temperatura de subida (3–55 s)
- Configuração de temperatura de descida (3–55 s)
- Envio de parâmetros via comunicação serial
- Interface com botões de incremento/decremento

## Requisitos

```
Python 3.x
kivy
pyserial
```

Instale as dependências:

```bash
pip install kivy pyserial
```

## Configuração serial

Edite `ihm_softstarter.py` para ajustar a porta serial:

```python
serial.Serial('COM3', 9600)   # Windows
# ou
serial.Serial('/dev/ttyUSB0', 9600)  # Linux
```

## Como executar

```bash
python ihm_softstarter.py
```

## Hardware relacionado

Funciona em conjunto com o projeto [stm32-softstarter](https://github.com/hiagoluansilva/stm32-softstarter).

## Escola

Centro Tecnológico Liberato — Novo Hamburgo/RS
