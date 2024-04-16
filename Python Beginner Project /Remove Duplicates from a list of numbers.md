## Removing duplicate number on list

#### Sample code:

        def remove_duplicates(nums):
          unique_nums = []
          for num in nums:
            if num not in unique_nums:
              unique_nums.append(num)
          return unique_nums

        nums = [22, 44, 44, 13, 82, 2, 82]
        unique_nums = remove_duplicates(nums)
        print(unique_nums)
              
