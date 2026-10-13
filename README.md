# スポーツ練習記録ツール

## 概要

スポーツの練習内容、練習時間、振り返りを記録できるPython製ツールです。

## 主な機能

- 練習日、スポーツ名、練習内容の入力
- 練習時間と振り返りメモの保存
- 過去の練習記録の一覧表示
- 累計練習時間の表示
- CSVファイルによるデータ保存

## 利用したOSS

- Rich\
  [https://github.com/Textualize/rich](https://github.com/Textualize/rich)\
  練習記録を見やすい表形式で表示するために使用しました。

## 動作環境

- Python 3.x
- Rich

## インストール方法

```
python -m pip install rich
```

## 実行方法

```
python main.py
```

## データ保存

練習記録は `practice_log.csv` に保存されます。

## Git運用の工夫

- feature-base ブランチで基本機能を作成しました。
- feature-documentation ブランチでREADMEを作成しました。
- 変更内容ごとにコミットし、ブランチを統合しました。
