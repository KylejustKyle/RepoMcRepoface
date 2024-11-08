import time

def linear_search1(seq, val):
    answer = None
    for i in range(len(seq)):
        if seq[i] == val:
            answer = i
    return answer

def linear_search2(seq, val):
    for i in range(len(seq)):
        if seq[i] == val:
            return i
    return None

def linear_search3(seq, val):
    n = len(seq) - 1
    last = seq[n]
    seq[n] = val
    i = 0
    while seq[i] != val:
        i += 1
    seq[n] = last
    if i < n or seq[n] == val:
        return i
    else:
        return None

if __name__ == "__main__":
    seq = []
    for i in range(0, 1000000):
        seq.append(i)
    val = 700000

    start = time.time_ns()
    result = linear_search1(seq, val)
    end = time.time_ns()
    print(f"Algm 1 1 Iter Result {result} Time {end-start} nanos")
    start = time.time_ns()
    for i in range(0, 1000):
        result = linear_search1(seq, val)
    end = time.time_ns()
    print(f"Algm 1 1000 Iter Result {result} Time {end-start} nanos")
    
    start = time.time_ns()
    result = linear_search2(seq, val)
    end = time.time_ns()
    print(f"Algm 2 1 Iter Result {result} Time {end-start} nanos")
    start = time.time_ns()
    for i in range(0, 1000):
        result = linear_search2(seq, val)
    end = time.time_ns()
    print(f"Algm 2 1000 Iter Result {result} Time {end-start} nanos")

    start = time.time_ns()
    result = linear_search3(seq, val)
    end = time.time_ns()
    print(f"Algm 3 1 Iter Result {result} Time {end-start} nanos")
    start = time.time_ns()
    for i in range(0, 1000):
        result = linear_search3(seq, val)
    end = time.time_ns()
    print(f"Algm 3 1000 Iter Result {result} Time {end-start} nanos")