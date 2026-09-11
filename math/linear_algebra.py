import numpy as np

a = np.array([[3,1],
              [2,4,]])

ev = np.linalg.eig(a)

print(ev[0]) #固有値
print()
print(ev[1]) #固有ベクトル

#--------------------------

def cos_sim(vec_1,vec_2): #コサイン類似度
    return np.dot(vec_1,vec_2) / (np.linalg.norm(vec_1) * np.linalg.norm(vec_2))

a = np.array([2,2,2,2])
b = np.array([1,1,1,1]) #aと同じ向き
c = np.array([-1,-1,-1,-1]) #aと反対向き

print(cos_sim(a,b))
print(cos_sim(a,c))

