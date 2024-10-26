from judge_maker import make_judge

def test_make_judge_no1():
    """マトリックスNo1
    10点より下の点数がある場合
    """
    gradeList = ['A', 'B', 'C', 'D', 'E']
    pointsList = [
        [9, 100, 100, 100, 100, 100, 100, 100, 100, 100],
        [11, 21, 15, 100, 100, 100, 100, 100, 100, 100],
        [20, 100, 10, 100, 100, 100, 100, 100, 100, 100],
        [20, 100, 100, 90, 80, 20, 100, 100, 100, 100],
        [20, 100, 100, 100, 100, 100, 100, 100, 100, 30]
    ]
    resultList = [3, 2, 1, 2, 3]
    
    for index, grade in enumerate(gradeList):
        result = make_judge(grade, pointsList[index])
        assert result == resultList[index]