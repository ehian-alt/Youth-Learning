# Youth-Learning
### 刷青年大学习的学习记录

首先这是python实现的，且仅限于江西省青年大学习刷学习记录的方法  
### 刷记录的原理  
* 我们发现在学习青年大学习的时候，只要点进去看就有记录，不管你是看多久，后台都会有记录。  
所以很有可能可以使用一个很简单的post请求实现青年大学习刷记录的方法

* 其次对于旧版青年大学习界面是需要我们去手动选择所属组织的，关系是这样的`系统-->单位-->二级学院-->班级`, 在`姓名/学号/工号`那一栏是随便填的。
这个是旧版青年大学习界面: <http://www.jxqingtuan.cn/html/h5_index.html?>

* 也就是说在除了姓名或者工号之前都有对应编号的，使用开发者工具查看的确是如此。  
接下来只要找到post请求的url, 并通过post的数据编写代码就可以实现刷记录了

* 通过查找，验证post发起请求的数据格式是这样的
> course: 本期青年大学id  
> subOrg: 备注 （新版有备注，为对应的学号）  
> nid:    所属组织对应的编号  
> cardNo: 就是姓名/学号/工号那一栏我们填的  

* 那么每一期的青年大学习id和所属组织编号怎么获得呢？  
所属组织对应的编号可以直接f12用开发者工具找到个人所属组织编号  
而每一期的青年大学习信息都会放在这个链接 `http://www.jxqingtuan.cn/pub/vol/volClass/current?` 内  
备注是选填的，这样data就有了，而post请求的链接被我找到了是这个 `http://www.jxqingtuan.cn/pub/vol/volClass/join?`

###### 现在就可以通过这些来编写一个简单的刷一条记录的python代码了！！

* [第一次的代码](https://github.com/ehian-alt/Youth-Learning/edit/main/code/first_version.py)，只由键盘输入id、编号、姓名之类的
* 通过读取文件 `name_list.txt` 实现批量刷记录，就成为了[第二版的代码](https://github.com/ehian-alt/Youth-Learning/edit/main/code/second_version.py)
