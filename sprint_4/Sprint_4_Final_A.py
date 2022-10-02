# Посылка - 71423632

# Советы шикарнейшие =) Нагенерил кучу данных, посмотрел в профайлере подсвеченные файлы - оказывается более трудоемким
# был подсчет релевантностей текста, а не выборка топ 5 элементов с сортировкой.
# Идея с кешированием была вообще вне поля рассматриваемых подходов, как-то даже не думал что это тут можно использовать =)
# Спасибо большое!!!

# в предыдущий раз ошибочно положил pclprof в архив


"""
-- ПРИНЦИП РАБОТЫ --
    Для полученных документов строим индекс:
        word: [ {document_number:count},..  ], где count - количество вхождений слова в документ.

    Подсчет релевантности документов делаем так:
        В словаре {document_number: relevance} будем хранить релевантность документов запросу.
        Пробегаем по каждому слову в запросе.
            Если оно не встречалось ранее - пропускаем.
            Иначе - берем из индекса список документов для слова word и прибавляем для каждого документа количество вхождений:
                document_relevance[document_number] += index[word][document_number]


        Разреженный список weight2doc нужен был чтобы не сортировать весь document_relevance.
        Если сделать как в https://contest.yandex.ru/contest/24414/run-report/71324078/, то я
        перестаю укладываться в 8.5 секунд. Видимо я как-то не верно понял идею со словарем.

        //одна из первых реализаций была со словарем в явном виде - https://contest.yandex.ru/contest/24414/run-report/71072690/
        //и ее пришлось заменить на list фиксированного размера, чтобы уместиться в лимиты


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

    O(n) - затраты на построение индекса, где n - число документов/предложений (не будем учитывать длину текста)

    Затраты на поиск документа:
        O(m), где m - количество слов в документе

    Итого: O(n+m).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
    Затраты на индекс: n
    Затраты на хранение релевантностей: n

    Итого: O(n)


"""
from collections import Counter
from functools import lru_cache

class IndexedDocuments:
    """ self._index = {word: {document_number: word appearance count in document} }"""
    def __init__(self, n: int, documents: [str]):
        self._n = n
        self._index = {}
        for i in range(self._n):
            for word in documents[i].split():
                _ = self._index.setdefault(word, Counter())
                self._index[word][i + 1] += 1

    @lru_cache(maxsize=16384)
    def search_relevant_docs(self, line: str) -> [int]:
        # document_relevance = { document_number: sum(words count) }
        document_relevance = Counter()
        for word in set(line.split()):
            if word in self._index:
                for document_number, count in self._index[word].items():
                    document_relevance[document_number] += count

        top_five_docs = sorted(document_relevance.items(), key=lambda item: (-item[1], item[0]))[:5]

        return [item for item, _ in top_five_docs]


def main():
    n = int(input())
    docs = [input() for _ in range(n)]

    index_data = IndexedDocuments(n, docs)

    m = int(input())
    for _ in range(m):
        print(*index_data.search_relevant_docs(input()))


if __name__ == "__main__":
    main()
