#coding utf-8

from tkinter import *
import tkinter.simpledialog as sr
import tkinter.messagebox as xx

root = Tk()
a = Label(root,text = "��ʲô��Ϸ���أ�")
a.pack()
xx.showinfo("����С����","Ȼ������㣬��ӭ����������ҫ��Ϸ��Ӫ��")

id = 821            				 #���ñ�����ֵ
num = 10            				 #����ѭ������
for i in range(1,num + 1):                       #for��ѭ����ÿ�ζ���iֵ����������û����ڵĴ���
	output = ("�ܹ�10�λ��ᣬ�������ǵ�" + str(i) + "�λ���")
	xx.showinfo("���棬bibo",output)
	while True:                                                      #��whileֵ����Ϊtrue��һֱִ��while��䣬ֱ������
		try:                                                     #���û������ֵ�����жϣ�����û���������������ִ��except
			user = sr.askinteger('������Ϸ��������Դ���',"����������Ϊ��ȷ��ֵ(�����ޣ�)")
			break
		except values:
			output = ("�����������֣���ͺú��䣡����")
			xx.showinfo("���棡",output)
	if user == id:                                               #����ֵ�뱻�����ֽ��бȽϣ�Ȼ�������Ӧ�Ľ��
		output = ("��Ӵι���������ô����Ȼ�����ˣ���ϧû�н�������")
		xx.showinfo("��ϲ",output)
		break
	elif user > id:
		output = ("�������ֵ̫big_big_big�ˣ������䣡")
		xx.showinfo("����",output)
	else:
		output = ("�������ֵ̫С�ˣ������䣡")
		xx.showinfo("����",output)
output = ("��Ϸ����")
xx.showinfo("bibo��",output)
