print("🚀 wordcloud.py 已启动")
import os
import jieba
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# =========================
# 路径配置（自动适配项目）
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)


def load_text():
    file_path = os.path.join(PROJECT_ROOT, "data", "danmaku.csv")

    df = pd.read_csv(file_path)

    text_col = df.columns[0]
    texts = df[text_col].dropna().astype(str).tolist()

    return texts


def load_stopwords():
    path = os.path.join(PROJECT_ROOT, "stopwords.txt")

    if not os.path.exists(path):
        return set()

    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f)


def cut_words(texts, stopwords):
    words = []

    for text in texts:
        for w in jieba.cut(text):
            w = w.strip()

            if not w:
                continue
            if w in stopwords:
                continue
            if len(w) == 1:
                continue

            words.append(w)

    return words


def generate_wordcloud(words):
    text = " ".join(words)

    font_path = "C:/Windows/Fonts/simhei.ttf"  # 中文字体（Windows通用）

    wc = WordCloud(
        font_path=font_path,
        background_color="white",
        width=1000,
        height=600,
        max_words=200
    ).generate(text)

    output_path = os.path.join(PROJECT_ROOT, "output", "wordcloud.png")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    wc.to_file(output_path)

    print(f"☁️ 词云已保存：{output_path}")

    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def main():
    print("🚀 开始生成词云")

    texts = load_text()
    stopwords = load_stopwords()

    words = cut_words(texts, stopwords)

    print(f"🔤 有效词数：{len(words)}")

    generate_wordcloud(words)

    print("✅ 完成")


if __name__ == "__main__":
    main()
print("🔥 进入main函数")