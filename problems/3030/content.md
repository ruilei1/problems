这里有n列火车将要进站再出站，但是，每列火车只有1节，那就是车头。

这n列火车按1到n的顺序从东方左转进站，这个车站是南北方向的，它虽然无限长，只可惜是一个死胡同，而且站台只有一条股道，火车只能倒着从西方出去，而且每列火车必须进站，先进后出。

也就是说这个火车站其实就相当于一个栈，每次可以让右侧头火车进栈，或者让栈顶火车出站。

车站示意如图：

```
            出站<——    <——进站
                     |车|
                     |站|
                     |__|
```

现在请你按《字典序》输出前20种可能的出栈方案。

#### 输入格式

输入一个整数n，代表火车数量。

#### 输出格式

按照《字典序》输出前20种答案，每行一种，不要空格。

#### 数据范围

$1 \le n \le 20$

#### 输入样例：

```
3
```

#### 输出样例：

```
123
132
213
231
321
```

## 来源 
- 《算法竞赛进阶指南》
- [acwing](https://www.acwing.com/problem/content/131/) 可能含有视频讲解