## 题目描述
如果一个数从左往右读和从右往左读都是一样,那么这个数就叫做“回文数”.例如,12321 就是一
个回文数,而 77778 就不是.当然,回文数的首和尾都应是非零的,因此 0220 就不是回文数.
事实上,有一些数（如 21）,在十进制时不是回文数,但在其它进制（如二进制时为 10101）时就是
回文数. 
编一个程序,从文件读入两个十进制数
```
N (1 <= N <= 15) S (0 < S < 10000)
```
然后找出前 N 个满足大于 S 且在两种以上进制（二进制至十进制）上是回文数的十进制数,输出到
文件上.
本问题的解决方案不需要使用大于 4 字节的整型变量.

## INPUT FORMAT
只有一行,用空格隔开的两个数 N 和 S.

## SAMPLE INPUT (file dualpal.in)
```
3 25
```
## OUTPUT FORMAT
N 行, 每行一个满足上述要求的数,并按从小到大的顺序输出.
## SAMPLE OUTPUT (file dualpal.out)
```
26
27
28
```
