def check_ggv_params(param1, param2):
    """
    检查ggv参数
    :param param1: 第一个参数
    :param param2: 第二个参数
    :return: 如果参数都符合条件返回True，否则返回False
    """
    if not isinstance(param1, int) or not isinstance(param2, int):
        print("参数必须为整数类型")
        return False
    if param1 < 0 or param2 < 0:
        print("参数必须为非负整数")
        return False
    print("参数符合要求")
    return True


# 示例调用
result = check_ggv_params(5, 10)
print(result)
