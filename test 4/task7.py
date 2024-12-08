# 7: 3Sum Problem

def defthree_sum(numbers):
    result = []

    for i in numbers:
        for k in numbers:
            for j in numbers:
                if i + j + k == 0:
                    result.append([i,k,j])
    return result

print(defthree_sum([-1, 0, 1, 2, -1, -4]))




# assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
# assert three_sum([0, 0, 0]) == [[0, 0, 0]]
# assert three_sum([1, 2, -2, -1]) == []
