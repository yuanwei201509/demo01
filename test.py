# 1. 商品信息
dict_commodity_info = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 显示所有商品信息
# 2. 创建订单
result_prices=0
list_orders = []
while True:
    key_board=input("请输入１键购买或２键结算:")
    if key_board=="1":
        for cid, dict_infos in dict_commodity_info.items():
            print("商品编号：" + str(cid) + ",商品名称：" + dict_infos["name"] + ",商品单价：" + str(dict_infos["price"]))
        commodity_id=int(input("请输入商品编号:"))
        buy_count=int(input("请输入商品数量:"))
        commodity_price=dict_commodity_info[commodity_id]["price"] * buy_count  #商品的价格
        result_prices+=commodity_price
        list_orders.append({"cid":commodity_id,"count":buy_count})
        print(list_orders)     #购物车

    elif key_board == "2":        #结算
        print("总消费金额为:"+str(result_prices))
        while True:
            accounts=float(input("请输入金额:"))
            if accounts<result_prices:
                print("重新获取金额")
            else:
                print("购买成功,清空购物车!")
                break
        break
    else:
        print("输入错误,晴重新输入！")