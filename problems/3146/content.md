“多边形游戏”是一款单人益智游戏。

游戏开始时，给定玩家一个具有N个顶点N条边（编号1-N）的多边形，如图1所示，其中N = 4。

每个顶点上写有一个整数，每个边上标有一个运算符+（加号）或运算符\*（乘号）。

![1179_1.jpg](/media/article/image/2019/01/25/19_5bc58b2420-1179_1.jpg)

第一步，玩家选择一条边，将它删除。

接下来在进行N-1步，在每一步中，玩家选择一条边，把这条边以及该边连接的两个顶点用一个新的顶点代替，新顶点上的整数值等于删去的两个顶点上的数按照删去的边上标有的符号进行计算得到的结果。

下面是用图1给出的四边形进行游戏的全过程。

![1179_2.jpg](/media/article/image/2019/01/25/19_579cb74c20-1179_2.jpg)

最终，游戏仅剩一个顶点，顶点上的数值就是玩家的得分，上图玩家得分为0。

请计算对于给定的N边形，玩家最高能获得多少分，以及第一步有哪些策略可以使玩家获得最高得分。

#### 输入格式

输入包含两行，第一行为整数N。

第二行用来描述多边形所有边上的符号以及所有顶点上的整数，从编号为1的边开始，边、点、边…按顺序描述。

其中描述顶点即为输入顶点上的整数，描述边即为输入边上的符号，其中加号用“t”表示，乘号用“x”表示。

#### 输出格式

输出包含两行，第一行输出最高分数。

在第二行，将满足得到最高分数的情况下，所有的可以在第一步删除的边的编号从小到大输出，数据之间用空格隔开。

#### 数据范围

$3 \le N \le 50$,  
数据保证无论玩家如何操作，顶点上的数值均在\[-32768,32767\]之内。

#### 输入样例：

```
4
t -7 t 4 x 2 x 5
```

#### 输出样例：

```
33
1 2
```

## 来源 
- 《算法竞赛进阶指南》
- [acwing](https://www.acwing.com/problem/content/285/) 可能含有视频讲解