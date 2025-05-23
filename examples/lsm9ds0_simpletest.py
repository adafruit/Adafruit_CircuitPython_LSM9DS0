# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the LSM9DS0 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time

import board
import busio

# import digitalio # Used with SPI
import adafruit_lsm9ds0

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds0.LSM9DS0_I2C(i2c)

# SPI connection:
# from digitalio import DigitalInOut, Direction
# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# gcs = DigitalInOut(board.D5)
# xmcs = DigitalInOut(board.D6)
# sensor = adafruit_lsm9ds0.LSM9DS0_SPI(spi, xmcs, gcs)

# Main loop will read the acceleration, magnetometer, gyroscope, Temperature
# values every second and print them out.
while True:
    # Read acceleration, magnetometer, gyroscope, temperature.
    accel_x, accel_y, accel_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic
    gyro_x, gyro_y, gyro_z = sensor.gyro
    temp = sensor.temperature
    # Print values.
    print(f"Acceleration (m/s^2): ({accel_x:0.3f},{accel_y:0.3f},{accel_z:0.3f})")
    print(f"Magnetometer (gauss): ({mag_x:0.3f},{mag_y:0.3f},{mag_z:0.3f})")
    print(f"Gyroscope (degrees/sec): ({gyro_x:0.3f},{gyro_y:0.3f},{gyro_z:0.3f})")
    print(f"Temperature: {temp:0.3f}C")
    # Delay for a second.
    time.sleep(1.0)
