题目描述
----

`小K`是一个海港的海关工作人员，每天都有许多船只到达海港，船上通常有很多来自不同国家的乘客。

`小K`对这些到达海港的船只非常感兴趣，他按照时间记录下了到达海港的每一艘船只情况；对于第i艘到达的船，他记录了这艘船到达的时间ti (单位：秒)，船上的乘 客数$k\_i$，以及每名乘客的国籍 $x\_{i,1}, x\_{i,2},…,x\_{i,k}$。

`小K`统计了$n$艘船的信息，希望你帮忙计算出以每一艘船到达时间为止的$24$小时($24$小时=$86400$秒）内所有乘船到达的乘客来自多少个不同的国家。

形式化地讲，你需要计算$n$条信息。对于输出的第$i$条信息，你需要统计满足$ t\_i-86400

输入输出格式
------

**输入格式：**  

第一行输入一个正整数$n$，表示`小K`统计了$n$艘船的信息。

接下来$n$行，每行描述一艘船的信息：前两个整数$t\_i$和$k\_i$分别表示这艘船到达海港的时间和船上的乘客数量，接下来$k\_i$个整数$x\_{i,j}$表示船上乘客的国籍。

保证输入的$t\_i$是递增的，单位是秒；表示从`小K`第一次上班开始计时，这艘船在第$t\_i$秒到达海港。

保证 $1 \\le n \\le 10^5$，$\\sum{ki} \\le 3\*10^5 $ ，$1\\le x(i,j) \\le 10^5$， $1 \\le t(i-1)\\le ti \\le 10^9$。

其中$\\sum{ki}$表示所有的$k\_i$的和。

**输出格式：**  

输出$n$行，第$i$行输出一个整数表示第$i$艘船到达后的统计信息。

输入输出样例
------

**输入样例#1：** 复制

3
1 4 4 1 2 2
2 2 2 3
10 1 3

**输出样例#1：** 复制

3
4
4

**输入样例#2：** 复制

4
1 4 1 2 2 3
3 2 2 3
86401 2 3 4
86402 1 5

**输出样例#2：** 复制

3
3
3
4

说明
--

【样例解释1】

第一艘船在第$1$秒到达海港，最近$24$小时到达的船是第一艘船，共有$4$个乘客， 分别是来自国家$4,1,2,2$，共来自$3$个不同的国家；

第二艘船在第$2$秒到达海港，最近$24$小时到达的船是第一艘船和第二艘船，共有$ 4 + 2 = 6$个乘客，分别是来自国家$4,1,2,2,2,3$，共来自$4$个不同的国家；

第三艘船在第$10$秒到达海港，最近$24$小时到达的船是第一艘船、第二艘船和第 三艘船，共有$4+ 2+1=7$个乘客，分别是来自国家$4,1,2,2,2,3,3$，共来自4$$个不同 的国家。

【样例解释2】

第一艘船在第$1$秒到达海港，最近$24$小时到达的船是第一艘船，共有$4$个乘客，分别是来自国家$1,2,2,3$，共来自$3$个不同的国家。

第二艘船在第$3$秒到达海港，最近$24$小时到达的船是第一艘船和第二艘船，共有$4+2=6$个乘客，分别是来自国家$1,2,2,3,2,3$，共来自$3$个不同的国家。

第三艘船在第$86401$秒到达海港，最近$24$小时到达的船是第二艘船和第三艘船，共有$2+2=4$个乘客，分别是来自国家$2,3,3,4$，共来自$3$个不同的国家。

第四艘船在第$86402$秒到达海港，最近$24$小时到达的船是第二艘船、第三艘船和第四艘船，共有$2+2+1=5$个乘客，分别是来自国家$2,3,3,4,5$，共来自$4$个不同的国家。

【数据范围】

![](https://cdn.luogu.org/upload/pic/3455.png)