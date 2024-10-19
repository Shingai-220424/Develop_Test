import pandas as pd

# 入力CSVファイルの読み込み
input_file = 'input_19.csv'
data = pd.read_csv(input_file)

# 各教科のインデックスに対する名前の対応付け
subjects = ['国語', '数学', '理科', '社会', '英語']

# 結果を格納するためのリスト
results = []

for index, row in data.iterrows():
    # 各教科の点数を取得
    scores = [row[subject] for subject in subjects]
    
    # 平均点を計算
    average_score = round(sum(scores) / len(scores), 1)
    
    # 順位を計算（平均点で順位付け）
    rank = data[subjects].mean(axis=1).rank(ascending=False, method='min')[index]
    
    # 成績の判定
    if rank == 1:
        grade = 'A'
    elif rank in [2, 3]:
        grade = 'B'
    elif rank in range(4, 8):
        grade = 'C'
    elif rank in range(8, 10):
        grade = 'D'
    else:
        grade = 'E'
    
    # 判定の計算
    re_test = '合格' if grade in ['A', 'B', 'C'] else '再テスト' if grade == 'D' else '不合格'
    
    # 再テスト判定の調整
    if (scores.count(30) >= 3) or (any(score < 10 for score in scores)):
        re_test = '再テスト' if grade != '不合格' else '不合格'
    
    # 各教科の結果をリストに追加
    for i, subject in enumerate(subjects):
        results.append([subject, average_score, rank, grade, re_test])

# 結果をデータフレームに変換
results_df = pd.DataFrame(results, columns=['教科', '平均点', '順位', '成績', '判定'])

# 各生徒の通知簿CSVを出力
for i in range(10):
    output_file = f'生徒19-{i+1}.csv'
    subject_results = results_df.copy()
    
    # 各ファイルの生徒名を追加
    subject_results.insert(0, '生徒名', [f'生徒19-{i+1}'] * len(subjects))
    
    subject_results.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"出力ファイル '{output_file}' が作成されました。")
