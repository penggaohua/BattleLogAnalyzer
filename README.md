# BattleLogAnalyzer
情景：测试过程中少不了查看日志，从中得到数据进行分析和测试，之前都是把log拷过来再搜索关键信息进行分析，不是很方便，所以用python tkinter 结合正在表达式做了个工具。
效果：
![图片描述](https://testerhome.com/uploads/photo/2021/9af80c98-d712-45ba-ba2f-43a503494dc2.png!large)
先在游戏项目对应的代码中插入打印，格式是这样   “ 攻击者=***    ...... 受击者=****  ....  最终伤害 ”

1.如果我想看 c_tujiu （秃鹫）的属性变化，只需要输入
![图片描述](https://testerhome.com/uploads/photo/2021/dfbca728-1edd-484a-bf23-7e42268a6f16.png!large）

![](/uploads/photo/2021/1c2c2001-e996-4c33-8a7c-b949d62b745e.png!large)
2.如果我想看这个怪物或英雄受击的情况只需要在下面输入对应的名字
![](/uploads/photo/2021/8e9cd50b-50dd-4d2f-9298-196add63ef4e.png!large)、
![](/uploads/photo/2021/dad5414c-f4af-4837-b01a-942b7430b980.png!large)

3.如果我想看A攻击B的具体情况，只需要上面输入A的名字下面输入B的名字（比如秃鹫攻击亡灵塔）
![](/uploads/photo/2021/f5fc8fda-1d08-4f27-a523-0e3d3ed277bb.png!large)

4.如果觉得属性太多太长，勾选“仅显示攻击者/受击者名称”就可以只显示名字方便查阅
![](/uploads/photo/2021/2c215bd9-12de-4407-bb7d-e656acf93616.png!large)

5.对比池其实就是一个复制粘贴的区域，用来对比分析。比如戴个装备前搜索数据后复制到这里，再戴装备后再复制就可以轻松对比属性变化。
![](/uploads/photo/2021/6142a742-c2ab-4c3b-b13b-86c11a03ae42.png!large)

6.这个搜索框可以直接输入想要查询的内容支持正则表达式，不仅仅是战斗日志的相关内容，只要是在Editor.log中的日志都可以搜索查询。
![](/uploads/photo/2021/d41e06c7-8257-4b3c-9037-c82b4b09d737.png!large)
比如想搜索所有的Lua报错，输入关键字查询即可
![](/uploads/photo/2021/f2272668-bc87-427d-807d-2529f14fb1c2.png!large)
再比如想看所有的前后端消息 ，输入send msg|receive msg
![](/uploads/photo/2021/f5ac2118-c76b-4362-b084-42df38138c99.png!large)


有了这个工具，属性的变化分析、伤害的计算核对、技能释放序列、装备的实际效果测试都很方便。




