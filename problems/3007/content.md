从 1~n 这 n 个整数中随机选出 m 个，输出所有可能的选择方案。

#### 输入格式

两个整数 $n, m$ ,在同一行用空格隔开。

#### 输出格式

按照从小到大的顺序输出所有方案，每行1个。

首先，同一行内的数升序排列，相邻两个数用一个空格隔开。

其次，对于两个不同的行，对应下标的数一一比较，字典序较小的排在前面（例如1 3 5 7排在1 3 6 8前面）。

#### 数据范围

$ n>0 $ ,  
$ 0 \le m \le n$ ,  
$ n+(n-m) \le 25 $

#### 输入样例：

```
5 3
```

#### 输出样例：

```
1 2 3 
1 2 4 
1 2 5 
1 3 4 
1 3 5 
1 4 5 
2 3 4 
2 3 5 
2 4 5 
3 4 5 
```

**思考题**：如果要求使用非递归方法，该怎么做呢？

## 来源 
- 《算法竞赛进阶指南》
- [acwing](https://www.acwing.com/problem/content/95/) 可能含有视频讲解