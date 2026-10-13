import csv
from datetime import datetime
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()
DATA_FILE = Path("practice_log.csv")


def add_record():
    print("\n--- 練習記録の入力 ---")

    date_input = input(
        "日付（YYYY-MM-DD、空欄なら今日）："
    ).strip()

    if date_input == "":
        date = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            date = datetime.strptime(
                date_input, "%Y-%m-%d"
            ).strftime("%Y-%m-%d")
        except ValueError:
            print("日付はYYYY-MM-DD形式で入力してください。")
            return

    sport = input("スポーツ名：").strip()
    practice = input("練習内容：").strip()

    if not sport or not practice:
        print("スポーツ名と練習内容を入力してください。")
        return

    try:
        minutes = int(input("練習時間（分）："))
        if minutes <= 0:
            print("練習時間は1以上で入力してください。")
            return
    except ValueError:
        print("練習時間は数字で入力してください。")
        return

    memo = input("振り返り・メモ：").strip()

    file_exists = DATA_FILE.exists() and DATA_FILE.stat().st_size > 0

    with DATA_FILE.open(
        "a", encoding="utf-8-sig", newline=""
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "date", "sport", "practice", "minutes", "memo"
            ]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "date": date,
            "sport": sport,
            "practice": practice,
            "minutes": minutes,
            "memo": memo
        })

    console.print("\n[green]練習記録を保存しました！[/green]")


def show_records():
    if not DATA_FILE.exists():
        print("まだ練習記録がありません。")
        return

    with DATA_FILE.open(
        "r", encoding="utf-8-sig", newline=""
    ) as file:
        records = list(csv.DictReader(file))

    if not records:
        print("まだ練習記録がありません。")
        return

    table = Table(title="スポーツ練習記録")

    table.add_column("日付")
    table.add_column("スポーツ")
    table.add_column("練習内容")
    table.add_column("時間（分）", justify="right")
    table.add_column("振り返り")

    total_minutes = 0

    for record in records:
        table.add_row(
            record["date"],
            record["sport"],
            record["practice"],
            record["minutes"],
            record["memo"]
        )
        total_minutes += int(record["minutes"])

    console.print(table)
    console.print(
        f"\n[bold cyan]累計練習時間：{total_minutes}分"
        f"（約{total_minutes / 60:.1f}時間）[/bold cyan]"
    )


def main():
    while True:
        print("\n===== スポーツ練習記録ツール =====")
        print("1. 練習記録を追加")
        print("2. 練習記録を一覧表示")
        print("3. 終了")

        choice = input("番号を選んでください：").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            print("終了します。お疲れさまでした！")
            break
        else:
            print("1、2、3のいずれかを入力してください。")


if __name__ == "__main__":
    main()
