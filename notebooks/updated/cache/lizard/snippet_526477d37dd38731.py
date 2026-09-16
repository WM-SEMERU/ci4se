def iso_date_to_datetime(string):
    nums = DATE_TIMESPLIT.split(string)
    if nums[-1] == '':
        nums = nums[:-1]
    if len(nums) == 7:
        nums[6] = nums[6][:6]
        nums[6] += PAD_MICRO[len(nums[6]):]
    the_datetime = datetime.datetime(*(int(num) for num in nums))
    return the_datetime