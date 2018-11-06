#coding utf-8

from tkinter import *
import tkinter.simpledialog as sr
import tkinter.messagebox as xx

root = Tk()
a = Label(root,text = "叫什么游戏好呢？")
a.pack()
xx.showinfo("弹个小窗口","然后告诉你，欢迎来到王者荣耀游戏大本营！")

id = 821            				 #设置被猜数值
num = 10            				 #程序循环次数
for i in range(1,num + 1):                       #for的循环，每次都将i值输出，告诉用户现在的次数
	output = ("总共10次机会，你现在是第" + str(i) + "次机会")
	xx.showinfo("警告，bibo",output)
	while True:                                                      #将while值设置为true，一直执行while语句，直到跳出
		try:                                                     #对用户输入的值进行判断，如果用户输入数非整数则执行except
			user = sr.askinteger('这是游戏，请认真对待。',"请输入你认为正确的值(整数噢！)")
			break
		except values:
			output = ("叫你输入数字，你就好好输！！！")
			xx.showinfo("警告！",output)
	if user == id:                                               #输入值与被猜数字进行比较，然后输出相应的结果
		output = ("哎哟喂。你是天才么，居然猜中了，可惜没有奖励哈！")
		xx.showinfo("恭喜",output)
		break
	elif user > id:
		output = ("你输入的值太big_big_big了，请重输！")
		xx.showinfo("呆子",output)
	else:
		output = ("你输入的值太小了，请重输！")
		xx.showinfo("呆子",output)
output = ("游戏结束")
xx.showinfo("bibo！",output)
