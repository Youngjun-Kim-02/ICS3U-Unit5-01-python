#!/usr/bin/env python3

# created by Youngjun Kim
# created on May 2021
# This program uses user defined functions


def fahrenheit():
    # this function convert celcius to fahrenheit
    
    # input
    Celsius = int(input("Enter the temperature in celsius: "))
    
    # process
    Fahrenheit = (Celsius * 9/5) + 32
    
    # output
    print("{0} degree Celsius is equal to {1} degree Fahrenheit.".format
    (Celsius, Fahrenheit))

def main():
    # this function just calls other functions
    
    # call functions
    fahrenheit()


if __name__ == "__main__":
    main()
