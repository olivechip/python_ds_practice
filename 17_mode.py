def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_set = set(nums)
    num_dict = {num: nums.count(num) for num in num_set}

    most = 0
    highest = 0
    for key in num_dict:
        if num_dict[key] > most:
            most = num_dict[key]
            highest = key
    print(highest)

    # count_nums = []
    # for num in nums:
    #     count_nums.append(nums.count(num))
    # most = 0
    # for count in count_nums:
    #     if count > most:
    #         most = count
    # idx = count_nums.index(most)
    # print(nums[idx])