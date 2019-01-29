# # 不用collections模块的例子
# def sock_merchant(s):
#     s_dic = {}
#     for i in s:
#         # 获得值，如果没有，默认为0；循环加1
#         # 因为是以列表元素作为键，因此相同元素相同下标，会查回原有值，在原有值基础上循环加1
#         s_dic[i] = s_dic.get(i, 0) + 1
#
#     res = 0
#     for v in s_dic.values():
#         res += v // 2
#
#     return res
#
#
# if __name__ == '__main__':
#     s = input("请输入每一只袜子：")
#     # 去除右空白，分割，转变为列表，映射为int类型，再转为列表类型
#     s = list(map(int, s.rstrip().split()))
#     # 调用函数
#     result = sock_merchant(s)
#     print("共有 %d 对袜子。" % result)

from collections import Counter


def sock_merchant(s):
        # 将相同的元素计数，并转化为字典
    res = 0
    for k in s:
        # 每个值向下取整后相加
        res += s[k]//2
    return res


if __name__ == '__main__':
    s = input("请输入每只袜子型号：")
    # 转换为已统计好数量的字典类型
    s = Counter(map(int, (s.rstrip().split())))
    res = sock_merchant(s)
    print("袜子有%d对。" % res)