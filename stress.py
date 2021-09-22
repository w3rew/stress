#!/bin/python
import subprocess
import sys
import random

prog_path = sys.argv[2]
ref_path = sys.argv[3]
sampler_path = sys.argv[1]
num = int(sys.argv[4])


for i in range(num):
    sampler = subprocess.Popen([sampler_path], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    prog = subprocess.Popen([prog_path], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    ref = subprocess.Popen([ref_path], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    data = sampler.communicate()[0]
    ref_data = ref.communicate(input = data)[0]
    my_data = prog.communicate(input = data)[0]

    if (my_data != ref_data):
        print("Error!")
        print("Data: ", data.decode())
        print("Ref_answer: ", ref_data.decode())
        print("My_answer: ", my_data.decode())
        break
    else:
        print("OK")
        print("Data: ", data.decode())
        print("Ref_answer: ", ref_data.decode())
        print("My_answer: ", my_data.decode())



