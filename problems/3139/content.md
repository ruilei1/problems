在 N\*M 的矩阵中，每个格子有一个权值，要求寻找一个包含 K 个格子的凸连通块（连通块中间没有空缺，并且轮廓是凸的），使这个连通块中的格子的权值和最大。

**注意**：凸连通块是指：连续的若干行，每行的左端点列号先递减、后递增，右端点列号先递增、后递减。

求出这个最大的权值和，并给出连通块的具体方案，输出任意一种方案即可。

#### 输入格式

第一行包含三个整数N,M和K。

接下来N行每行M个整数，表示N\*M的矩阵上每个格子的权值（均不超过1000）。

#### 输出格式

第一行输出“Oil : X”，其中X为最大权值和。

接下来K行每行两个整数$x\_i$和$y\_i$，用来描述所有格子的具体位置，每个格子位于第$x\_i$行，第$y\_i$列。

#### 数据范围

$1 \le N,M \le 15$,  
$0 \le K \le N\*M$

#### 输入样例：

```
2 3 4 
10 20 30 
40 2 3
```

#### 输出样例：

```
Oil : 100 
1 1 
1 2 
1 3 
2 1
```

## 来源 
- 《算法竞赛进阶指南》
- [acwing](https://www.acwing.com/problem/content/278/) 可能含有视频讲解