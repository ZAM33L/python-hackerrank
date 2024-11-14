def average(array):
    # your code goes here
    distinct_heights = set(array)
    avg_heights = sum(distinct_heights) / len(distinct_heights)
    return round(avg_heights, 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)