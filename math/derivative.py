# f(x) = x^2 の導関数を数値微分で確認する
def f(x):
    return x ** 2

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

print(derivative(f, 3))  # 理論値は 2*3 = 6 に近い値が出るはず