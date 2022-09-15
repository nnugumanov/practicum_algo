# hashes = 0 97 97098 97226 225227 225076 74077 76437 436420
def compute_powers(maxn, k, mod):
    _pows = [int] * (maxn + 1)
    _pows[0] = 1

    for i in range(1, maxn + 1):
        _pows[i] = _pows[i - 1] * k % mod

    return _pows


def compute_prefix_hashes(maxn, s, k, mod) -> [int]:
    prefixes = [int] * (maxn + 1)
    h = 0
    prefixes[0] = 0
    for i in range(1, len(s) + 1):
        h = (h * k + s[i - 1]) % mod
        prefixes[i] = h
    return prefixes


def calc_hash(s):

    k = 1000
    mod = 123987123

    pows = compute_powers(len(s), k, mod)
    prefix_hashes = compute_prefix_hashes(len(s), s, k, mod)

    return(prefix_hashes[-1])

def main():


    s1 = bytearray("dd", encoding='utf-8')
    h1 = calc_hash(s1)
    cur_value = h1
    found = False
    while not found:
        cur_value = cur_value + 123987123
        t = cur_value

        found = True
        while t > 0:
            x = t % 1000
            if not(97 <= x <= 122):
                found = False
                break
            t = t // 1000
    return cur_value

if __name__ == "__main__":
    print(main())

