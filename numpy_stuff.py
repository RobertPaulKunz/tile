import numpy as np
from tkinter import *
import RPi.GPIO as GPIO
import time
from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

A = np.array([ [0x7C], [0x7E], [0x13], [0x13], [0x7E], [0x7C], [0x00], [0x00] ])
B = np.array([ 0x41, 0x7F, 0x7F, 0x49, 0x49, 0x7F, 0x36, 0x00 ])
C = np.array([ 0x1C, 0x3E, 0x63, 0x41, 0x41, 0x63, 0x22, 0x00 ])
D = np.array([ 0x41, 0x7F, 0x7F, 0x41, 0x63, 0x3E, 0x1C, 0x00 ])

display = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0],
    [0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0],
    [0,0,0,1,1,1,1,1,1,0,0,0,0,1,1,0],
    [0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],])

my_hexdata = 0xFFFF
print(bin(my_hexdata))








