def leng (s):
    start= -1
    dic = {
    }
    max = 0
    for i in range(len(s)):
        print(dic)
        if s[i] in dic and start<dic[s[i]]:
            start = dic[s[i]]
            print("start"+str(start)+"ddd"+str(i))

            dic[s[i]] = i
        else :
            dic[s[i]] = i
            if i-start>max:
                max = i-start
                print(max)
    return max

print(leng("hellohellohehepp"))