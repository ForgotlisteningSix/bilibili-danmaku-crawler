import os
import jieba
import pandas as pd
from collections import Counter

print("🚀 脚本启动")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)


def load_data():
    file_path = os.path.join(PROJECT_ROOT, "data", "danmaku.csv")

    print("📥 CSV路径：", file_path)

    df = pd.read_csv(file_path)

    print("📊 CSV列名：", df.columns.tolist())

    text_col = df.columns[0]

    texts = df[text_col].dropna().astype(str).tolist()

    print(f"📦 数据量：{len(texts)}")

    return texts


def load_stopwords():
    file_path = os.path.join(PROJECT_ROOT, "stopwords.txt")

    if not os.path.exists(file_path):
        return set()

    with open(file_path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f)


def cut_words(texts, stopwords):
    words = []

    for text in texts:
        for w in jieba.cut(text):
            w = w.strip()

            if not w or w in stopwords or len(w) == 1:
                continue

            words.append(w)

    print(f"🔤 分词完成：{len(words)}")

    return words


def main():
    print("🔥 进入main函数")

    texts = load_data()
    stopwords = load_stopwords()

    words = cut_words(texts, stopwords)

    counter = Counter(words)

    print("\n🔥 Top 30 高频词：\n")

    for w, c in counter.most_common(30):
        print(w, c)

    print("\n✅ 完成")


if __name__ == "__main__":
    main()