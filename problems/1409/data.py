#!/usr/bin/env python

from cyaron import * # 引入CYaRon的库

for i in range(1,11):
    io = IO(file_prefix="problem", data_id=i) # test3.in, test3.out

    a = randint(1,105)
    b = randint(a,105)
    io.input_write(a,b)
    io.output_gen("../std")
