
class IndexedDocuments:
    """ self._index = {word: {document_number: word appearance count in document} }"""
    def __init__(self, n: int, documents: [str]):
        self._n = n
        self._index = {}
        for i in range(self._n):
            for word in documents[i].split():
                document_number = i + 1
                word_in_document_counts = self._index.setdefault(word, {})
                self._index[word][document_number] = word_in_document_counts.get(document_number, 0) + 1

    def search_relevant_docs(self, line: str) -> [int]:
        # document_relevance = { document_number: sum(words count) }
        document_relevance = {}

        uniq_words = {}
        for word in line.split():
            if word in uniq_words:
                continue
            uniq_words[word] = 1

            if word in self._index:
                for document_number, count in self._index[word].items():
                    document_relevance[document_number] = document_relevance.get(document_number, 0) + count

        # weight2doc = { relevance1 : [doc5, doc7...], relevance2: [doc1, doc2],..}
        weight2doc = [ [] for _ in range(self._n + 1) ]
        for document_number, relevance in document_relevance.items():
            weight2doc[relevance] += [document_number]

        top_five_docs = []
        for i in range(self._n, 0, -1):
            if weight2doc[i]:
                for doc in sorted(weight2doc[i]):
                    if len(top_five_docs) < 5:
                        top_five_docs.append(doc)
                    else:
                        return top_five_docs

        return top_five_docs


def main():
    n = int(input())
    docs = []
    for _ in range(n):
        docs.append(input())

    index_data = IndexedDocuments(n, docs)

    m = int(input())
    for _ in range(m):
        print(*index_data.search_relevant_docs(input()))

def test():
    docs = """i love coffee
coffee with milk and sugar
free tea for everyone"""

    search_lines = """i like black coffee without milk
everyone loves new year
mary likes black coffee without milk""".split("\n")

    index_data = IndexedDocuments(3, docs.split("\n"))

    assert (index_data.search_relevant_docs(search_lines[0]) == [1, 2])
    assert (index_data.search_relevant_docs(search_lines[1]) == [3])
    assert (index_data.search_relevant_docs(search_lines[2]) == [2, 1])

    docs = """buy flat in moscow
rent flat in moscow
sell flat in moscow
want flat in moscow like crazy
clean flat in moscow on weekends
renovate flat in moscow"""

    search_lines = "flat in moscow for crazy weekends"

    index_data = IndexedDocuments(6, docs.split("\n"))
    assert(index_data.search_relevant_docs(search_lines) == [4, 5, 1, 2, 3])

    docs = """i like dfs and bfs
i like dfs dfs
i like bfs with bfs and bfs"""

    search_lines = """dfs dfs dfs dfs bfs"""

    index_data = IndexedDocuments(3, docs.split("\n"))
    result = index_data.search_relevant_docs(search_lines)
    assert (result == [3, 1, 2])

    docs = """tjegerxbyk pdvmj wulmqfrx
pndygsm dvjihmxr tcdtqsmfe
txamzxqzeq dxkxwq aua
hsciljsrdo fipazun kngi
xtkomk aua wulmqfrx ydkbncmzee
pndygsm cqvffye pyrhcxbcef
szyc uffqhayg ccktodig
ntr wpvlifrgjg htywpe
kngi tjegerxbyk zsnfd
tqilkkd gq qc fipazun"""

    search_lines = """dxkxwq htywpe
aua tjegerxbyk
xtkomk tjegerxbyk
szyc fipazun
xtkomk tjegerxbyk""".split("\n")

    index_data = IndexedDocuments(10, docs.split("\n"))
    result = index_data.search_relevant_docs(search_lines[0])
    assert (result == [3, 8])

    result = index_data.search_relevant_docs(search_lines[1])
    assert (result == [1, 3, 5, 9])

    result = index_data.search_relevant_docs(search_lines[2])
    assert (result == [1, 5, 9])

    result = index_data.search_relevant_docs(search_lines[3])
    assert (result == [4, 7, 10])

    result = index_data.search_relevant_docs(search_lines[4])
    assert (result == [1, 5, 9])


if __name__ == "__main__":
    # main()

    test()
