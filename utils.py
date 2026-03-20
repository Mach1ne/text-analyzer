def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Файл не найден")
        return ""


def get_words(text):
    text = text.lower()
    text = text.replace("-", " ")
    to_replace = "!?.,"
    for sym in to_replace:
        text = text.replace(sym, "")
    words = text.split()
    words = [word for word in words if word]
    return words


def count_words(words):
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def top_word(freq):
    max_count = 0
    top_list = []

    for word, count in freq.items():
        if count > max_count:
            max_count = count
            top_list = [word]
        elif count == max_count:
            top_list.append(word)

    return top_list, max_count


def average_length(words):
    if len(words) == 0:
        return 0

    total = 0
    for word in words:
        total += len(word)

    return total / len(words)


def top_n_words(freq, n):
    items = list(freq.items())
    items = sorted(items, key=lambda x: (-x[1], x[0]))
    
    return items[:n]

def build_report(words, freq, top_list, max_count, avg_len, top_n, n):
    top_lines = []
    for i, (word, count) in enumerate(top_n, 1):
        top_lines.append(f"{i}. {word} — {count}")

    top_text = "\n".join(top_lines)
    freq_lines = []
    for word, count in sorted(freq.items()):
        freq_lines.append(f"{word}: {count}")

    freq_text = "\n".join(freq_lines)
    return f"""Топ {n} слов:
{top_text}

Всего слов: {len(words)}
Уникальных слов: {len(freq)}
Частота:
{freq_text}
Топ слова: {top_list}
Максимальная частота: {max_count}
Средняя длина слова: {round(avg_len, 2)}
"""