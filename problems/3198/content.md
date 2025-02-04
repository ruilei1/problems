给定一张 N 个点 M 条边的有向无环图，点的编号从 0 到 N - 1，每条边都有一个长度。

给定一个起点 S 和一个终点 T。

若从 S 到 T 的每条路径都经过某条边，则称这条边是有向图的必经边或桥。

北大 ACM 队要从 S 点到 T 点。

他们在路上可以搭乘两次车。

每次可以从任意位置（甚至是一条边上的任意位置）上车，从任意位置下车，但连续乘坐的长度不能超过 q 米。

除去这两次乘车外，剩下的路段步行。

定义从 S 到 T 的路径的危险程度等于步行经过的桥上路段的长度之和。

求从 S 到 T 的最小危险程度是多少。

#### 输入格式

第一行包含整数 L，表示共有 L 组测试数据。

每组测试数据，第一行包含五个整数 N,M,S,T,q 。

接下来 M 行，每行包含三个整数u,v,w，表示点 u 到点 v 存在一条边，长度为 w。

#### 输出格式

每组数据输出一个结果，每个结果占一行。

若没有从 S 到 T 的路径，则输出 -1。

#### 数据范围

$1 \le L \le 5$,  
$1 \le N \le 10^5$,  
$1 \le M \le 2\*10^5$,  
$0 \le S,T < N, S \neq T$,  
$1 \le q \le 10^9$,  
$1 \le w \le 1000$

#### 输入样例：

```
1
8 9 0 7 7
0 4 1
0 1 10
1 2 9
4 2 2
2 5 8
4 3 3
5 6 6
5 6 7
6 7 5
```

#### 输出样例：

```
1
```

## 来源 
- 《算法竞赛进阶指南》
- [acwing](https://www.acwing.com/problem/content/371/) 可能含有视频讲解