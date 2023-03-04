# this is valid only for 3 numbers of the password
password = "985"
lent = 10
isTrue = 0
index1, index2, index3 = 0, 0, 0
n_isEnd, j_isEnd = False, False
for i in range(lent):
    if int(password[0]) == i:
        index1 = password[0]
        if j_isEnd: break
    for j in range(lent):
        if int(password[1]) == j:
            index2 = password[1]
            if n_isEnd:
                j_isEnd = True
                break
            for n in range(lent):
                if int(password[2]) == n:
                    index3 = password[2]
                    n_isEnd = True
                    break

tackerPassword = str(index1) + str(index2) + str(index3)
print('tracked password is : ', tackerPassword)
