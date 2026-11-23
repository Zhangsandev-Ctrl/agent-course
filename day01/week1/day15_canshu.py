# 默认参数示例
def calc_total(items, tax=0.06):
    total = sum(items)
    tax_money = total * tax
    return total, tax_money

nums = [200,150,50]
res1 = calc_total(nums)          # 不填税率，用默认0.06
res2 = calc_total(nums, tax=0.13)# 关键字传参，指定税率
print(res1, res2)
