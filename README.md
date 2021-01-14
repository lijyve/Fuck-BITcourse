# Fuck-BITcourse
新的选课系统上线了，不来fuck一下吗？

| 参数              | 获取方法                                                     |
| ----------------- | ------------------------------------------------------------ |
| token             | 登录后在浏览器的地址栏可以找到                               |
| Cookie            | 按F12，换到Network，随便点击选一门课，可以在Request Headers中看到 |
| studentCode       | 你的学号                                                     |
| electiveBatchCode | 按F12，换到Network，随便点击选一门课，可以在Headers中的Form Data里看到 |
| teachingClassId   | 找到你要选的课程，按F12，换到Network，在网页上点击要选课的教学班详情，从http://xk.bit.edu.cn/xsxkapp/sys/xsxkapp/publicinfo/queryjxb.do?返回的Response中可以找到 |
| teachingClassType | 课程类型：TJKC 系统推荐课程 FANKC 方案内课程 XGXK 校公选课 TYKC 体育课程 |



## 2021.1.14  1.1beta
1. 更新了FormData的内容
2. 测试脚本，仍然正常运行

## 2020.9.19  1.0 beta
第一版功能  
1. 一次只能抢一门课
2. 学习的选课系统的token似乎有时限，大概不到20分钟就会失效  