#!/usr/bin/env python

from cyaron import * # 引入CYaRon的库

for i in range(1,11):
    io = IO(file_prefix="problem", data_id=i) # test3.in, test3.out

    a = randint(1,1000000)
    b = randint(1,1000000)
    c = randint(1,1000000)
    io.input_write(a,b,c)
    io.output_gen("../std")
