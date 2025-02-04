## [题目描述]

在史莱姆大陆上有一群史莱姆在一场碰碰游戏,在一长度为$L\ cm$的细长条擂台上分散的站着一些史莱姆,(这个擂台的宽度只能容下一只史莱姆).初始的时候每只史莱姆都有两个属性:

 - 位置m,表示他距离擂台左边的距离
 - 方向
    - $R$,代表他朝向右边
    - $L$,代表他朝向左边
史莱姆的速度为$1\cm /s$,如果两只史莱姆相互碰撞,他们两就会**立刻**转向.问,在一定的时间后,每只史莱姆的状态.

## [输入格式]

 - 第一行:$L,T,N$,表示擂台的长度,过了$T$秒,共有$N$只史莱姆$N<=10000$
 - 接下来$N$行,一个数字,一个字符,其中第$i$行表示编号为$i-1$的史莱姆的位置和方向.

## [输出格式]

输出$N$数据,每行表示编号为$i$史莱姆的状态

 - 如果他跌落下擂台,直接输出$Down$,注意,在两端不算跌落
 - 如果他和其它的史莱姆在同一个位置,输出`位置 Same`
 - 没有和其它的史莱姆在同一个位置,直接输出`位置 方向`

## [输入样例]

```
10 1 4
1 R
5 R
3 L
10 R
```

## [输出样例]

```
2 Same
6 R
2 Same
Down
```
