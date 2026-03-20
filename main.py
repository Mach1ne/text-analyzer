import argparse
from utils import (
    read_file,
    get_words,
    count_words,
    top_word,
    average_length,
    top_n_words,
    build_report,
)

parser = argparse.ArgumentParser(description="Анализатор текста")
parser.add_argument("-r", "--read", help="читать текст из файла")
parser.add_argument("-n", "--top", type=int, default=3, help="сколько топ слов показать")
parser.add_argument("-o", "--output", help="сохранить результат в файл")

args = parser.parse_args()

if args.read:
    text = read_file(args.read)
else:
    text = input("Введите текст: ")

words = get_words(text)
freq = count_words(words)
top_list, max_count = top_word(freq)
avg_len = average_length(words)
top_n = top_n_words(freq, args.top)

result = build_report(words, freq, top_list, max_count, avg_len, top_n, args.top)

if args.output:
    with open(args.output, "w", encoding="utf-8") as file:
        file.write(result)
    print(f"Результат сохранён в {args.output}")
else:
    print(result)