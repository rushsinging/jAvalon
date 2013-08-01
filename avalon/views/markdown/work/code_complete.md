# High-Quality Routines 高质量的子程序

## 相关
* 构造子程序的步骤 9.3
* 可以工作的类 6
* 一般设计技术 5
* 软件架构 3.5

## 什么是子程序(routine)
子程序是为实现一个特定的目的而编写的可以被调用的方法或者过程。

子程序分布
e.g.  

* function in C++
* method in Java
* function procedure in VB 
* macro in C/C++
* function in python ...

一些不好的子程序写法：

	# 曾经的新浪微博的自动回复脚本
	def get_mention(): # get_mentions or get_mention_list
		'''
		拉取微博函数
		'''
		...
		return list
		
	# 数据库查询函数命名
	def get():
		pass
	def select():
		pass
	def search():
		pass
	
	# 现在的新浪微博自动回复…
	def add_guokr_question():
		'''
		将问题添加到果壳主张
		'''
		# 还会有拼接回复的代码
		# add_question
		return 
		
	# python code
	def do_something(data):
		# data 是什么类型
		do_something
		return 
		
	＃ 参数冗余,排序混乱
	def do_something(b, d, g, a,):
		return
		
	# C# 过多的函数重载
	int do_something(a, b, c, d, e){}
	int do_something(a, c){}
	int do_something(a, c, d){}
	int do_something(a, e){}
	
	# 应该保持一个最常用的和一个功能最常用的
	int do_something(a, b, c, d, e){}
	int do_something(a, b)

## 创建子程序的正当理由
* **降低复杂度** 更好的确认和发现问题
* **避免代码重复**
* 支持子类化
* 隐藏顺序
* 隐藏指针操作
* 提高可移植性
* **简化复杂的布尔判断**

        def is_something_true():
        	pass
        
        form.validate()
			
* 改善性能,很像降低复杂度这一特性
* 创建类的很多理由同样也是
    * 隔离复杂度
    * 隐藏实现细节
    * 限制变化所带来的影响
    * 隐藏全局数据
    * 形成中央控制点
    * 促成可复用的代码
    * 达成特定的目的

### 似乎过于简单而没有必要写成子程序的操作
写成子程序可以：

* 自我注解 提高可读性
* 简单的操作可能变成复杂的操作

        logger.error(error_msg)
		
开始的时候，日志纪录倒是没有明显的问题，不过随着需要纪录的东西增多，以及代码结构层次的混乱，在读代码和检查BUG时，繁多的日志纪录就会开始阻碍视线，甚至在完成debug后你会发现你不知道需要保留哪一部分日志，所以在末日计划后，我对新浪微博的自动回复脚本重构了一次，尽量减少每个子程序的工作，并用装饰器纪录日志。
	
    @logger


## 在子程序层上设计
内聚性：子程序中各种操作之间联系的紧密程度。  

内聚与耦合，得墨忒耳法则（最少知识法则）@程序员修炼之道：  
对于类内的函数而言，它只会调用4种方法：

1. 它自身的方法
2. 传入该方法的参数
3. 它自己创建的任何对象
4. 任何直接持有的组件

功能的内聚性

被认为不够理想的内聚性的分类：

* 顺序上的内聚性
* 通信上的内聚性
* 临时的内聚性
* 过程上的内聚性
* 逻辑上的内聚性
* 巧合的内聚性

## 好的子程序的名字
* 描述子程序所作的事情
* 避免无意义，模糊或者表述不清的动词
* 不要仅通过数字形成子程序的名字
* 根须需要确定程序名字的长度
* 给函数命名时需要对返回值有所描述
* 准确使用对仗词  
		
		add/remove  
		begin/end  
		created/destroy  
		first/last  
		...  
* 为常用操作确立命名规则

## 子程序可以写多长
一些例子

* 一个函数在10行以内
* basili和Perricone的研究发现 子程序的长度和错误量呈现反比（0-200）
* 子程序的长度和错误量无关，结构复杂度？
* 短小的子程序（<32）与较低的成本和错误率无关。而较长的子程序（>65）使得每行代码的成本下降
* 100-150的代码被修改的几率最低
* 最容易出错的是超过500行的代码
* ...

那么，建议是控制在100-200行，并且考虑到子程序的内聚性，嵌套层次，变量数量，决策点。

## 如何使用子程序参数

* 按照输入－输出－修改的顺序
* 考虑自建IN和OUT关键字（in C/C++）
* 如果几个子程序都用了类似的参数，应该让他们保持顺序一致。
* 使用所有的参数
* 把状态和出错变量放在最后
* 不要把子程序的参数用作工作变量
* 限制在7个以内
* 考虑对参数采用某种输入、修改、输出的命名规则
* 为子程序传递用以维持其接口抽象的变量或者对象
* 使用具名参数

## 使用函数时要特别考虑的问题
### 什么时候使用函数，什么时候使用过程
### 设置函数的返回值

## 宏子程序和内联子程序
* \#define in C风格代码
* inline in C 风格代码

---

# 防御式编程
## 相关
* 5.3 信息隐藏
* 5.3 为改变而设计
* 3.5 软件架构
* 5   软件构建中的设计
* 23  调试

防御式编程的思想：子程序应该不因为传入数据的错误而被破坏，哪怕是其他子程序产生的错误数据。

## 保护程序免遭非法输入数据的破坏

* 检查所有源于外部的数据的值
* 检查子程序所有输入参数的值
* 决定如何处理错误的输入数据

## 断言

断言（assertion），是指在开发期间使用的、让程序在运行时进行自检的代码。

断言可以假定很多程序的运行时条件，我认为其主要作用是帮助程序员确认运行时环境。（程序员在写程序的过程中会做各种各样的架设，这种假设很有必要写进代码中确认）

### 使用断言的指导建议
* 用错误处理代码来处理预期会发生的情况和不应该发生的情况
* 避免把需要执行的代码放到断言中
* 用断言注解并验证验证前条件和后条件
* 对于高健壮性代码，应该先使用断言再处理错误

## 错误处理技术
* 返回中立值
* 换用下一个正确的数据
* 返回和前次相同的数据
* 换用接近的合法值
* 将警告信息纪录到日志文件中
* 返回一个错误码
* 调用错误处理子程序或对象
* 显示出错消息
* 用最妥当的方式再局部处理错误
* 关闭程序

**健壮性与正确性**，根据需要在健壮性和正确性之间取舍。

**高层次设计对错误处理方式的响应**，在高层和底层采取统一的方式处理错误。

### Writing Solid Code 第二章（Assert Yourself）示例

#### 保存两份代码

这种C风格的代码大家可以看一下
	
	/* memcpy -- copy a nonoverlapping memory block. */
	
	void *memcpy(void *pvTo, void *pvfrom, size_t size)
	{
		byte *pbTo = (byte *)pvTo;
		byte *pbFrom = (byte *)pvFrom;
		if (pvTo == NULL || pvFrom == Null)
		{
			fprintf(stderr, 'Bad args in memcpy');
			abort();
		}
		
		while (size-- > 0)
		{
			*pbTo++ *pbFrom++;
		}
		
		return (pvTo);
	}
	
	/* memcpy -- copy a nonoverlapping memory block. */
	/* Add debug copd */
	void *memcpy(void *pvTo, void *pvfrom, size_t size)
	{
		byte *pbTo = (byte *)pvTo;
		byte *pbFrom = (byte *)pvFrom;
		#ifdef DEBUG
		if (pvTo == NULL || pvFrom == Null)
		{
			fprintf(stderr, 'Bad args in memcpy');
			abort();
		}
		#endif
		
		while (size-- > 0)
		{
			*pbTo++ *pbFrom++;
		}
		
		return (pvTo);
	}

#### 使用断言

	/* memcpy -- copy a nonoverlapping memory block. */
	/* Add assert copd */
	void *memcpy(void *pvTo, void *pvfrom, size_t size)
	{
		byte *pbTo = (byte *)pvTo;
		byte *pbFrom = (byte *)pvFrom;
		
		assert(pvTo != NULL && pvFrom != NULL)
		
		while (size-- > 0)
		{
			*pbTo++ *pbFrom++;
		}
		
		return (pvTo);
	}
	
	/* 使用assert宏或者自定义 */
	#ifdef DEBUG
		void _Assert(char *, unsigned);
		
		#define ASSERT(f)		\
			if (f)				\
			{}					\
			else
				_Assert(__FILE__, __LINE__) //调用宏来传递信息
	#else
		#define ASSERT(f)
	#endif
	
	/* _Assert的定义*/
	void _Assert(char *strFile, unsigned uLine)
	{	
		fflush(NULL);
		fprintf(stderr, '\nAssertion failed: %s. line %u', strFile, uLine);
		fflush(stderr);
		abort();
	}
	
#### 去除代码中的未定义行为，或者用断言来捕获

	/* memcpy -- copy a nonoverlapping memory block. */
	/* Add assert copd */
	/* check memeory overlap */
	void *memcpy(void *pvTo, void *pvfrom, size_t size)
	{
		byte *pbTo = (byte *)pvTo;
		byte *pbFrom = (byte *)pvFrom;
		
		assert(pvTo != NULL && pvFrom != NULL)
		assert(pvTo > pbFrom + size && pvFrom > pbTo + size)
		
		while (size-- > 0)
		{
			*pbTo++ *pbFrom++;
		}
		
		return (pvTo);
	}

#### 为不清楚的断言加上说明
	
	/* memcpy -- copy a nonoverlapping memory block. */
	/* Add assert copd */
	/* check memeory overlap */
	void *memcpy(void *pvTo, void *pvfrom, size_t size)
	{
		byte *pbTo = (byte *)pvTo;
		byte *pbFrom = (byte *)pvFrom;
		
		assert(pvTo != NULL && pvFrom != NULL)
		/* Block overlap? Use memmove. */
		assert(pvTo > pbFrom + size && pvFrom > pbTo + size)
		
		while (size-- > 0)
		{
			*pbTo++ *pbFrom++;
		}
		
		return (pvTo);
	}
	
	/* strdup -- allocate a dumplicate of a string */
	char *strdup(char *str)
	{
		char *strNew;
		
		ASSERT(str != NULL);
		
		strNew = (char *)malloc(strlen(str) + 1);
		
		/* Should be replaced with code to handle the error conditon. */
		ASSERT(strNew != Null); 
		
		strcpy(strNew, str);
		
		return (strNew);
	}

#### 要么消除隐式的假设，要么断言它们是合法的。

应用Assert的又一个地方。作者举了个c实现内存设值`memset`的例子，有时为了加快`memset`，会将`byte *`指针转换成`long *`的。但是`byte *`的指针可能是个奇地址，如果转换成`long *`的，在有些系统上会出问题，因为`long *`的指针在这些系统上不能以奇地址开始。作者的方法是判断可否使用奇地址，然后在进行处理。 

	long *longfill(long *pl, long l, size_t size)

	void *memset(void *pv, byte b, size_t size)
	{
		byte *pb = (byte *pv)
		
		#ifdefine MC680x0
		// as long *
		#endif 
		
		while (size-- > 0)
			*pb++ = b;
		
		return (pv)
	}
	
#### 使用断言排除不可能的情况
如果你认为一种情况不会发生，就断言它不会发生。

#### 进行防御式编程时，不要隐藏bug
防御式编程是一种编程风格，主要目的是保护系统不受“非法”输入的破坏，但这样很容易掩盖bugs。*程序死应该死的壮烈一点*

**健壮性与正确性**

核电站温度监控，**局部异常该如何处理，沉默处理或者提交给工作人员**。
（现在的新浪微博回复机器人代码）


#### 使用第二套方法验证结果
#### 不要等着bugs发生，使用启动检查。

## 异常
* 用异常通知程序的其他部分，发生了不可忽略的错误
* 只有在真正例外的情况下才抛出异常
* 不能用异常推卸责任
* 避免在构造函数和析构函数中抛出异常，除非在同一的地方捕获
* 在恰当的抽象层次抛出异常
* 在异常消息中加入关于导致异常发生的全部消息
* **避免使用空的catch语句**
* **了解所用函数库可能抛出的异常**
* 考虑创建一个集中的异常报告机制
* 在项目中对异常的使用标准化
* 考虑异常的替换方案

## 隔离程序，使之包容由错误造成的伤害
隔栏（barricade），隔栏可以将程序安全和不安全的部分分离开来。**隔栏和断言的搭配**

## 辅助调试代码

**不要把产品版的限制强加与开发版上**

**尽早引入辅助调试代码**

**采用进攻式编程**

* 确保断言语句使程序终止运行
* 完全填充分配的内存
* 完全填充所有文件或者流
* 确保每一个switch的分支或者else分支都能产生严重错误
* 删除一个对象前填满垃圾数据
* 让程序发送错误日志文件给你
* ...

**计划移除调试辅助代码**

* 使用类似ant和make这样的版本控制工具和make工具
* 使用内置的预处理器
* 自己编写预处理器
* 使用调试存根

## 确定在产品代码中该保留多少防御式代码
 
* 保留检查重要错误的代码，去掉检查细微错误的代码
* 去掉可以导致程序硬性崩溃的代码
* 保留可以让程序稳妥的崩溃的代码
* 为你的技术支持人员纪录错误信息
* 确认留在代码中的错误信息是友好的

## 对防御式编程采取防御的姿势

## 相关资源
### 断言
* <Writing Solid Code> 第二章
* The C++ Programming Language, 第24章
* Object-Orented Software Construction,关于前条件和候条件的权威论述
###  异常
* Object-Orented Software Construction, 
* The C++ Programming Language, 14章 
* ...