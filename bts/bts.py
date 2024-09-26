class BTSSolutions:
    def first_match_in_arr(self, arr: [int], target: int) -> int:
        left, right = 0, len(arr) - 1
        found_index = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                if arr[mid] == target:
                    found_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return found_index

    def peak_of_mtn(self, arr: [int]) -> int:
        left, right = 0, len(arr) - 1
        boundary = -1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] >= arr[mid - 1]:
                boundary = mid
                left = mid + 1
            else:
                right = mid - 1

        return boundary


    def sqrt_estimate(self, n: int) -> int:
        if n == 0:
            return 0
        left = 1
        right = n
        res = -1
        while left < right:
            mid = (left + right) // 2
            sqrt = mid ** mid
            if sqrt == n:
                return mid
            elif sqrt > n:
                right = mid - 1
            else:
                res = mid
                left = mid + 1
        return res