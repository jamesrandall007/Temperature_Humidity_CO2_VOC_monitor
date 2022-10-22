Using Adafruit VOC detector:
- SGP30 Air Quality Sensor Breakout - VOC and eCO2
  - https://www.adafruit.com/product/3709
- AHT20 - Temperature & Humidity Sensor
  - https://www.adafruit.com/product/4566


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards: https://github.com/adafruit/circuitpython/releases
* Adafruit’s Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice

*class* adafruit_sgp30.Adafruit_SGP30(*i2c*, *address=88* )[[source]](https://docs.circuitpython.org/projects/sgp30/en/latest/_modules/adafruit_sgp30.html#Adafruit_SGP30)

A driver for the SGP30 gas sensor.

Parameters

* **i2c** ([*I2C*](https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html#busio.I2C)) – The I2C bus the SGP30 is connected to.
* **address** ([*int*](https://docs.python.org/3/library/functions.html#int)) – The I2C address of the device. Defaults to `0x58`

### Get hex address of existing I2C devices:
```bash
$sudo i2cdetect -y 1

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- 38 -- -- -- -- -- -- -- 
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --  
```

**Quickstart: Importing and using the SGP30 temperature sensor**

 Here is one way of importing the [`Adafruit_SGP30`](https://docs.circuitpython.org/projects/sgp30/en/latest/api.html#adafruit_sgp30.Adafruit_SGP30) class so you can use it with the name `sgp30`. First you will need to import the libraries to use the sensor

```python
import busio import board import adafruit_sgp30

```
 Once this is done you can define your [`busio.I2C`](https://docs.circuitpython.org/en/latest/shared-bindings/busio/index.html#busio.I2C) object and define your sensor object

 ```python
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000) 
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)
```

Now you have access to the Carbon Dioxide Equivalent baseline using the [`baseline_eCO2`](https://docs.circuitpython.org/projects/sgp30/en/latest/api.html#adafruit_sgp30.Adafruit_SGP30.baseline_eCO2) attribute and the Total Volatile Organic Compound baseline using the [`baseline_TVOC`](https://docs.circuitpython.org/projects/sgp30/en/latest/api.html#adafruit_sgp30.Adafruit_SGP30.baseline_TVOC)

```python
eCO2 = sgp30.baseline_eCO2 TVOC = sgp30.baseline_TVOC
``` 

*property* Ethanol

Ethanol Raw Signal in ticks

*property* H2

H2 Raw Signal in ticks

*property* TVOC

Total Volatile Organic Compound in parts per billion.

*property* baseline_TVOC

Total Volatile Organic Compound baseline value

*property* baseline_eCO2

Carbon Dioxide Equivalent baseline value

*property* eCO2

Carbon Dioxide Equivalent in parts per million

get_iaq_baseline()[[source]](https://docs.circuitpython.org/projects/sgp30/en/latest/_modules/adafruit_sgp30.html#Adafruit_SGP30.get_iaq_baseline)

Retreive the IAQ algorithm baseline for eCO2 and TVOC

iaq_init()[[source]](https://docs.circuitpython.org/projects/sgp30/en/latest/_modules/adafruit_sgp30.html#Adafruit_SGP30.iaq_init)

Initialize the IAQ algorithm

iaq_measure()[[source]](https://docs.circuitpython.org/projects/sgp30/en/latest/_modules/adafruit_sgp30.html#Adafruit_SGP30.iaq_measure)

Measure the eCO2 and TVOC

raw_measure()[[source]](https://docs.circuitpython.org/projects/sgp30/en/latest/_modules/adafruit_sgp30.html#Adafruit_SGP30.raw_measure)

Measure H2 and Ethanol (Raw Signals)

set_iaq_baseline(*eCO2*, *TVOC* )[[source]](https://docs.circuitpython.org/projects/sgp30/en/latest/_modules/adafruit_sgp30.html#Adafruit_SGP30.set_iaq_baseline)

Set the previously recorded IAQ algorithm baseline for eCO2 and TVOC

set_iaq_humidity(*gramsPM3* )[[source]](https://docs.circuitpython.org/projects/sgp30/en/latest/_modules/adafruit_sgp30.html#Adafruit_SGP30.set_iaq_humidity)

Set the humidity in g/m3 for eCO2 and TVOC compensation algorithm

set_iaq_relative_humidity(*celsius*, *relative_humidity* )[[source]](https://docs.circuitpython.org/projects/sgp30/en/latest/_modules/adafruit_sgp30.html#Adafruit_SGP30.set_iaq_relative_humidity)

Set the humidity in g/m3 for eCo2 and TVOC compensation algorithm. The absolute humidity is calculated from the temperature (Celsius) and relative humidity (as a percentage).

### Temp Humid sensor very easy:
```python
from icecream import ic 
import adafruit_ahtx0

# Create the sensor object using I2C
sensor = adafruit_ahtx0.AHTx0(board.I2C())

temp_sensor = sensor.temperature
humidity_sensor = sensor.relative_humidity

ic(int(temp_sensor), int(humidity_sensor))

```