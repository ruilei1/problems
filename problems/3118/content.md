给定一个有N个点（编号0,1,…,N-1）的树，每条边都有一个权值（不超过1000）。

树上两个节点x与y之间的路径长度就是路径上各条边的权值之和。

求长度不超过K的路径有多少条。

#### 输入格式

输入包含多组测试用例。

每组测试用例的第一行包含两个整数N和K。

接下来N-1行，每行包含三个整数u,v,l，表示节点u与v之间存在一条边，且边的权值为l。

当输入用例N=0，K=0时，表示输入终止，且该用例无需处理。

#### 输出格式

每个测试用例输出一个结果。

每个结果占一行。

#### 数据范围

$N \le 10000$

#### 输入样例：

```
5 4
0 1 3
0 2 1
0 3 2
2 4 1
0 0
```

#### 输出样例：

```
8
```

## 来源 
- 《算法竞赛进阶指南》
- [acwing](https://www.acwing.com/problem/content/254/) 可能含有视频讲解