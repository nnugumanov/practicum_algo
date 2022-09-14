"""
-- ПРИНЦИП РАБОТЫ --

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

"""
# hashes = 0 97 97098 97226 225227 225076 74077 76437 436420

def main():
    def compute_powers():
        _pows = [int] * (max_distance + 1)
        _pows[0] = 1

        for i in range(1, max_distance + 1):
            _pows[i] = _pows[i - 1] * k % mod

        return _pows

    def compute_prefix_hashes() -> [int]:
        prefixes = [int] * (max_distance +1)
        h = 0
        prefixes[0] = 0
        for i in range(1, len(s) + 1):
            h = (h * k + s[i - 1]) % mod
            prefixes[i] = h
        return prefixes

    k = int(input())
    mod = int(input())
    s = bytearray(input(), encoding='utf-8')
    t_requests = int(input())

    max_distance = len(s)

    requests = []
    for _ in range(t_requests):
        line = input().split()
        data = [int(line[0]), int(line[1])]
        requests.append(data)

    pows = compute_powers()
    prefix_hashes = compute_prefix_hashes()
    for i, j in requests:

        hb = prefix_hashes[j]
        ha = prefix_hashes[i - 1]

        _subs = hb - ha * pows[j - i + 1]
        if _subs < 0:
            _subs += mod
        result = _subs % mod
        print(result)


if __name__ == "__main__":
    main()
