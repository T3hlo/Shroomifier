![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg) ![License](https://img.shields.io/github/license/<username>/<repository>.svg)![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi%20Pico-blue.svg)![Python](https://img.shields.io/badge/python-MicroPython%201.20+-brightgreen.svg)![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)![Made with Love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red.svg)

# Shroomifier 🍄💨

*A Humidifier for the Budding Mushroom Enthusiast*

So, you've recently found yourself mesmerized by the world of gourmet mushrooms—welcome to the club! If you're anything like me, you started innocently enough, perhaps dreaming of a shiitake or lion's mane pasta, but soon found yourself surrounded by substrate, spores, and... a tent?

Enter **Shroomifier**, a Raspberry Pi Pico-powered humidifier system designed to keep your mushroom growing tent in tip-top shape. Whether you're nurturing delicate enoki or regal king oysters, this gadget ensures your fungi friends stay cozy with perfect humidity levels.

## Features 🚀

- **Precise Humidity Control**: Powered by the SHT31 sensor, it monitors and maintains optimal humidity levels for mushroom growth.

- **Compact and Modular Design**: Built for the Raspberry Pi Pico, making it affordable and adaptable.

- **Customizable Settings**: Fine-tune your humidity thresholds with ease using the `config.json` file.

- **Real-time Display**: Includes TM1637 display support for showing live data like humidity and temperature.

- **Open-Source Goodness**: Fully hackable! Add features, tweak settings, or just marvel at the code.

## Getting Started

### Hardware Requirements

- **Raspberry Pi Pico**
- **SHT31 Humidity and Temperature Sensor**
- **TM1637 4-Digit Display Module**
- A power supply, cables, and a mushroom tent full of potential.

### Software Setup

1. Clone this repository to your local machine:

   ```bash
   bash
   
   
   Copy code
   git clone <repository-url>  
   ```

2. Flash your Raspberry Pi Pico with MicroPython (if not already done).

3. Copy the following files to your Pico:

   - `main.py`
   - `sht31.py`
   - `tm1637.py`
   - `config.json`

4. Adjust the `config.json` file to your preferred humidity and temperature settings:

   ```json
   jsonCopy code{  
       "humidity_target": 85,  
       "humidity_tolerance": 5  
   }  
   ```

5. Power up your Pico, place it in your mushroom tent, and watch the magic happen!

### Pin Connections

| Raspberry Pi Pico Pin | Module | Description |
| --------------------- | ------ | ----------- |
| GPIO X                | SHT31  | Data line   |
| GPIO Y                | TM1637 | Clock       |
| GPIO Z                | TM1637 | Data        |

> Replace X, Y, and Z with the actual GPIO pins you're using.

## Contributions

Have an idea to make this even cooler? Pull requests are welcome! Whether it's adding support for new sensors, improving the UI, or sharing your own mushroom tales, this project thrives on collaboration.

## Attribution

This project uses the following third-party modules:

- **`tm1637.py`**: MicroPython TM1637 quad 7-segment LED display driver, created by Mike Causer. Licensed under the MIT License.
  - [GitHub Repository](https://github.com/mcauser/micropython-tm1637)

- **`sht31.py`**: MicroPython SHT31 temperature and humidity sensor driver, created by Kai Fricke. Licensed under the MIT License.
  - [GitHub Repository](https://github.com/kfricke/micropython-sht31)

The MIT License details for both `tm1637.py` and `sht31.py` are included in this repository to comply with the license terms.

## License

This project is licensed under the MIT License.

------

------

Go forth and grow gourmet mushrooms with ease—and may your tent always be humid, but your spirits dry. 🌱
