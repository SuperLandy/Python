pro_list = [
    ('iphone',6000),
    ('apple',100),
    ('book',1000),
    ('mac book',880),
]
print(pro_list[1])
shopping_list = []
gongzi = input('请输入你的钱：')
if gongzi.isdigit():#判断工资是否是整数！
    gongzi = int(gongzi)
    while True:
        for index,item in enumerate(pro_list):#打印商品列表
            print(index,item)
        user_choice = input('请输入购买商品编号：')
        if user_choice.isdigit():#判断商品编号是否为整数
            user_choice = int(user_choice)
            if user_choice < len(pro_list) and user_choice > -1:#判断商品编号是否存在
                p_item = pro_list[user_choice]
                if p_item[1] <= gongzi: #判断能否能买的起
                    shopping_list.append(p_item)
                    gongzi -= p_item[1]
                    print('你已成功把%s加入购物车，钱包余额%s'%(p_item,gongzi))
                else:
                    print('你钱不够！剩余[%s]'%gongzi)
            else:
                print('你选择的[%s]商品不存在！'% user_choice)
        elif user_choice == 'q':
            print('------购买商品列表-----')
            for p in shopping_list:
                print(p)
            print('余额还剩下%s'%gongzi)
            exit()
        else:
            print('请输入正确的商品编号！！')
else:
    print('退出！')
