def counter(start=0):
    count = [start]
    def incr():
        count[0] += 1
        return count[0]
    return incr

def counter2(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr


