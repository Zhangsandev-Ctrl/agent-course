#新增学习：`isdigit()`（字符串方法）:只判断**纯正数字字符串**；负数、小数返回 False;只能字符串调用，数字变量不能用 `.isdigit()`
text='123'
print(text.isdigit())
text1='12a3'
print(text1.isdigit())
text2='78.5'
print(text2.isdigit())
text3='-100'
print(text3.isdigit())
text4='99.0'
print(text4.isdigit())
#1. `isdigit()` **只认全部是 0-9 的字符串**，才返回 True
#2. 只要里面有 `.` 小数点、`-` 负号、字母，一律返回 False
#3. 它只适合校验**正整数输入**，小数、负数它判断不了
#4. 必须是字符串（带引号）才能调用，int 数字直接调用会报错