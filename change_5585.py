change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1] #�Ž��� ��
cnt = 0
for i in coins:
    cnt += change // i
    change %= i

print(cnt)