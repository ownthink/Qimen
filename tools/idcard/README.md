  # 校验码计算步骤

**(一)18身份证号码的结构**　　

公民身份号码是特征组合码，由十七位数字本体码和一位校验码组成。

排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码。 

**1、地址码** 　　

表示编码对象常住户口所在县(市、旗、区)的行政区域划分代码，按GB/T2260的规定执行。
**2、出生日期码** 　　

表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。 

**3、顺序码** 　　

表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，**顺序码的奇数分配给男性，偶数分配给女性**。 

**4、校验码计算步骤**

**(1)十七位数字本体码加权求和公式**

$S = Sum(A_i * W_i), i = 0, ... , 16 $	先对前17位数字的权求和 
$A_i$:表示第$i$位置上的身份证号码数字值(0~9) 
$W_i  $: 7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2	（表示第i位置上的加权因子）

**(2)计算模** 　　

$Y = mod(S, 11)​$

**(3)根据模，查找得到对应的校验码**

Y: 0 1 2 3 4 5 6 7 8 9 10 

校验码: 1 0 X 9 8 7 6 5 4 3 2



### reference：

百度百科：https://baike.baidu.com/item/%E8%BA%AB%E4%BB%BD%E8%AF%81%E6%A0%A1%E9%AA%8C%E7%A0%81/3800388?fr=aladdin

身份证号码验证算法：https://www.cnblogs.com/xudong-bupt/p/3293838.html



|      |      |
| ---- | ---- |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |
|      |      |