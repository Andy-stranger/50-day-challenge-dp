def largestNumber(self, nums) -> str:
    num_str = [str(num) for num in nums]
    num_str.sort(key = lambda a : a*10 , reverse = True)
    if num_str[0] == '0':
        return '0'
    return "".join(num_str)