达达是一名漫画家，她有一个奇特的爱好，就是在纸上画括号。

这一天，刚刚起床的达达画了一排括号序列，其中包含小括号( )、中括号\[ \]和大括号{ }，总长度为N。

这排随意绘制的括号序列显得杂乱无章，于是达达定义了什么样的括号序列是美观的：

(1) 空的括号序列是美观的；

(2) 若括号序列A是美观的，则括号序列 (A)、\[A\]、{A} 也是美观的；

(3) 若括号序列A、B都是美观的，则括号序列AB也是美观的。

例如 `[(){}]()` 是美观的括号序列，而`)({)[}](` 则不是。

现在达达想在她绘制的括号序列中，找出其中连续的一段，满足这段子序列是美观的，并且长度尽量大。

你能帮帮她吗？

#### 输入格式

输入一行由括号组成的字符串。

#### 输出格式

输出一个整数，表示最长的美观的子段的长度。

#### 数据范围

字符串长度不超过100000。

#### 输入样例：

```
({({(({()}})}{())})})[){{{([)()((()]]}])[{)]}{[}{)
```

#### 输出样例：

```
4
```

## 来源 
- 《算法竞赛进阶指南》
- [acwing](https://www.acwing.com/problem/content/152/) 可能含有视频讲解