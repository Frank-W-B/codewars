
def divisible_count(x,y,k):
    return y // k - (x - 1)//k    

if __name__ == '__main__':
    x = 2
    y = 12
    k = 3 
    nums = range(x, y+1)
    div_k = [i % k == 0 for i in nums]
    cnt = sum(div_k)
    cnt2 = divisible_count(x, y, k)
    cnt3 = divisible_count(101, 9999999999999999999999999999999999999999999, 11)