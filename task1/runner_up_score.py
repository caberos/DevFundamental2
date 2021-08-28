def runner(numbers):
    arr = map(int, numbers)
    return sorted(set(arr))[-2]

if __name__ == "__main__":

    x = [2, 3, 6, 6, 5]

    print(runner(x))
