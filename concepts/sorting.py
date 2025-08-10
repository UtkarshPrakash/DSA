class Sorting:
    def selectionSort(self, nums):
        '''
        For each element, look ahead to find the SMALLEST element and swap
        '''
        print("\nSorting by Selection Sort")
        n = len(nums)

        for i in range(n-1):
            localMin = nums[i]
            indexMin = i 
            for j in range(i+1, n):
                if nums[j] < localMin:
                    indexMin = j
                    localMin = nums[j]
            if indexMin != i:
                nums[i], nums[indexMin] = nums[indexMin], nums[i]
        
        return nums

    def bubbleSort(self, nums):
        '''
        Keep bubbling (swapping) the largest element you see in each iteration to the rightmost.
        In next iteration, you have to just go to one before the rightmost, as rightmost will be the largest.
        '''
        print("\nSorting by Bubble Sort")
        n = len(nums)

        for i in range(n-1):
            curr = nums[i]
            for j in range(1, n-i):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
        return nums

    def insertionSort(self, nums):
        '''
        We keep the left part of current element sorted.
        We keep swapping the current to left element until it falls to its correct place
        '''
        print("\nSorting by Insertion Sort")
        n = len(nums)

        for i in range(1, n):
            ind = i
            temp = nums[ind]
            while ind > 0 and nums[ind - 1] > nums[ind]:
                nums[ind], nums[ind-1] = nums[ind-1], nums[ind]
                ind -= 1
        
    def printWithSpace(self, nums):
        # print()
        for i in nums:
            print(i, end = ' ')



sorter = Sorting()

a = [6, 5, 2, 5, 8, 3, 5, 7]
# a = [4, 1, 5, 2, 3]

sorter.printWithSpace(a)

sorter.insertionSort(a)
# bubble_sort(a)
# insertion_sort(a)

sorter.printWithSpace(a)

# help(Sorting.insertionSort)
