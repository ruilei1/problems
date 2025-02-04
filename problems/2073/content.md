## 题目描述

大小为 3 的棋盘游戏里有 3 个白色棋子,3 个黑色棋子,和一个有 7 个格子一线排开的木盒子.3 个白棋子被放在一头,3 个黑棋子被放在另一头,中间的格子空着.

 - 初始状态: WWW_BBB
 - 目标状态: BBB_WWW

在这个游戏里有两种移动方法是允许的:

 - 1. 你可以把一个棋子移到与它相邻的空格；
 - 2. 你可以把一个棋子跳过一个(仅一个)与它不同色的棋子到达空格.

大小为 N 的棋盘游戏包括 N 个白棋子,N 个黑棋子,还有有 2N+1 个格子的木盒子.

这里是 3-棋盘游戏的解,包括初始状态,中间状态和目标状态:

```
WWW BBB
WW WBBB
WWBW BB
WWBWB B
WWB BWB
W BWBWB
 WBWBWB
BW WBWB
BWBW WB
BWBWBW
BWBWB W
BWB BWW
B BWBWW
BB WBWW
BBBW WW
BBB WWW
```

请编一个程序解大小为 N 的棋盘游戏(1 <= N <= 12).要求用最少的移动步数实现.

## INPUT FORMAT

一个整数 N.

## SAMPLE INPUT (file shuttle.in)
```
3
```
## OUTPUT FORMAT

用空格在棋盘的位置(位置从左到右依次为 1, 2, ..., 2N+1)表示棋盘的状态.输出棋盘的状态变换序列,每行 20 个数(除了最后一行).

输出的解还应当有最小的字典顺序(即如果有多组移动步数最小的解,输出第一个数最小的解；如果还有多组,输出第二个数最小的解；...).

## SAMPLE OUTPUT (file shuttle.out)

```
3 5 6 4 2 1 3 5 7 6 4 2 3 5 4 
```
