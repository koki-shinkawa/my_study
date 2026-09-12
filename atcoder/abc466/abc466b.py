n,m = map(int,input().split())
#print(n)
#print(m)
ball={}
for _ in range(n): #変数は使わない
    c,s = map(int,input().split())
    if c not in ball: #ballに色cがなかったらその大きさsと一緒に辞書に追加
        ball[c] = s
    else:             #ballに色cがあったら、sを比べて大きい方を登録
        if ball[c] < s:
            ball[c] = s
#print(ball) {1: 7, 2: 10, 4: 9}

ans = []
for i in range(1,m+1):
    if i in ball: #ballにi(1,2,...,m+1)というkeyがあったら、対応するvalueをansに入れる
        ans.append(ball[i])
    else:
        ans.append(-1)
print(*ans)

