def squads(n):
    res = []
    for i in range(n):
        res.append(i ** 2)
    return res


if __name__ == "__main__":
    n = 10
    result = squads(n)

    print(result)