def make_judge(grade, points):
    """判定を行う関数

    Args:
        grade (str): 成績（'A'～'E'）
        points (list of int): 点数のリスト（0～100の整数）

    Returns:
        int: 判定結果 (1: 合格, 2: 再テスト, 3: 不合格)
    """
    result = None
    is_failure = any(data < 10 for data in points) # 点数リストの中に10天未満の点数が1つでもあればTrue
    is_retest = sum(data <= 30 for data in points) >= 3 # 30点以下の点数が3つ以上あるかどうかをカウントし、3以上であればTrue

    if is_failure or grade == 'E':
        result = 3  # 不合格
    elif is_retest or grade == 'D':
        result = 2  # 再テスト
    elif grade in ('A', 'B', 'C'):
        result = 1  # 合格
    else:
        raise ValueError("Invalid grade. Must be A, B, C, D, or E.")

    return result


if __name__ == '__main__':
    # テスト例
    print(make_judge("A", [65, 70, 75, 80, 90, 85, 95, 100, 95, 80]))  # 合格: 1
    print(make_judge("D", [60, 20, 50, 40, 30, 10, 90, 100, 85, 75]))  # 再テスト: 2
    print(make_judge("E", [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]))  # 不合格: 3
    print(make_judge("C", [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]))  # 不合格: 3