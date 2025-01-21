
def binary_search(arr, n):
    lr, r = 0, len(arr) - 1

    while lr <= r:
        mid = (r - lr) // 2 + lr
        item = arr[mid]
        if item > n:
            r = mid - 1
        elif item < n:
            lr = mid + 1
        else:
            return True

    return False


def main():
    input()
    data = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    for num in numbers:
        res = binary_search(data, num)
        if res:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
    