def make_judge(grade, points):
    """判定を行う関数

    Args:
        grade (str): 成績（'A'～'E'）
        points (list of int): 点数のリスト（0～100の整数）

    Returns:
        int: 判定結果 (1: 合格, 2: 再テスト, 3: 不合格)
    """
    result = None
    is_failure = any(data < 10 for data in points)
    is_retest = sum(data <= 30 for data in points) >= 3

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
    print(make_judge('A', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 出力は 3（不合格）
