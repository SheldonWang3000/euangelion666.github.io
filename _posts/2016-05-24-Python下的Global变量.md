---
layout:     post
title:	    Python下的Global变量
date:       2016-05-24 10:17:02
summary:    Global变量的基本用法
categories: jekyll
thumbnail: jekyll
tags:
 - Python
---
Python中的变量分为局部变量和全局变量两种

    def func():
        a = 1
        a = a * 8
        print(a)
    a = 100
    func()

这里`a = 1`表示的是局部变量，而`a = 100`表示的是全局变量，这里与普通的C程序是一样的

Python中需要注意的一点是在于全局变量的使用

    def func():
        a = a * 8
        print(a)
    a = 100
    func()

上面代码如果运行，则会出现报错`UnboundLocalError: local variable 'a' referenced before assignment`原因是在局部域内虽然可以直接调用全局变量，但如果需要修改全局变量，需要添加`global a`的语句进行标记

正确的代码应该为

    def func():
        global a
        a = a * 8
        print(a)
    a = 100
    func()
    
这样就可以正常运行了
