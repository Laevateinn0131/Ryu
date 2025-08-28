import streamlit as st
import sympy
from sympy import symbols, expand, factor
import random

x, y = symbols('x y')

# --- 展開・因数分解（easy） ---
def easy_expansion():
    a, b = random.randint(1, 5), random.randint(-5, 5)
    c, d = random.randint(1, 5), random.randint(-5, 5)
    expr = (a * x + b) * (c * x + d)
    return expr.expand(), f"次の式を展開しなさい：({a}x + {b})({c}x + {d})"

def easy_factor():
    form = random.choice(["simple", "common_factor"])
    if form == "simple":
        while True:
            a, b, c = 1, random.randint(-10, 10), random.randint(-10, 10)
            expr = a * x**2 + b * x + c
            factored = sympy.factor(expr)
            if expr != factored:
                return expr, f"次の式を因数分解しなさい：{sympy.pretty(expr)}"
    else:
        a = random.randint(2, 5)
        b = random.randint(1, 5)
        c = random.randint(-5, 5)
        expr = a * x * (x + b) + a * c
        return expr, f"次の式を因数分解しなさい：{sympy.pretty(expr)}"

# --- 展開・因数分解（hard） ---
def hard_expansion():
    a, b, c = random.randint(1, 3), random.randint(-5, 5), random.randint(-5, 5)
    d = random.randint(1, 5)
    expr = (a * x**2 + b * x + c) * (d * x + random.randint(-5, 5))
    return expr.expand(), f"次の式を展開しなさい：({a}x² + {b}x + {c})({d}x + ...)"

def hard_factor():
    while True:
        a, b, c = random.randint(1, 6), random.randint(-20, 20), random.randint(-10, 10)
        expr = a * x**2 + b * x + c
        factored = sympy.factor(expr)
        if expr != factored:
            return expr, f"次の式を因数分解しなさい：{sympy.pretty(expr)}"

# --- 類似式（恒等式活用）問題 ---
def identity_problem():
    problems = [
        (x**2 + y**2, "(x + y)^2 - 2xy を使って表しなさい", (x + y)**2 - 2*x*y),
        ((x - y)**2, "式を展開しなさい", expand((x - y)**2)),
        (x**2 - y**2, "因数分解しなさい", factor(x**2 - y**2)),
        (x**2 + y**2 + 2*x*y, "因数分解しなさい", factor(x**2 + y**2 + 2*x*y)),
    ]
    expr, q, ans = random.choice(problems)
    return expr, q, ans

# --- 問題作成 ---
def generate_problem(level, index):
    # 類似式問題を2問ほど混ぜる（3問目と6問目）
    if index in [2, 5]:
        expr, question, answer = identity_problem()
        return "類似式の変形", question, expr, answer

    if level == "easy":
        if random.choice(["expand", "factor"]) == "expand":
            ans, q = easy_expansion()
            return "展開", q, None, ans
        else:
            expr, q = easy_factor()
            return "因数分解", q, expr, sympy.factor(expr)

    elif level == "hard":
        if random.choice(["expand", "factor"]) == "expand":
            ans, q = hard_expansion()
            return "展開", q, None, ans
        else:
            expr, q = hard_factor()
            return "因数分解", q, expr, sympy.factor(expr)

    else:
        return None, None, None, None

# --- Streamlit UI ---
def main():
    st.title("高校1年生レベル：展開・因数分解・類似式問題ジェネレーター")

    level = st.radio("難易度を選んでください", ("easy（定期テストレベル）", "hard（全国模試レベル）"))
    level_key = "easy" if level.startswith("easy") else "hard"

    # セッションステートで問題番号管理
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0

    if st.button("次の問題"):
        st.session_state.q_index += 1
        if st.session_state.q_index > 6:
            st.session_state.q_index = 0

    idx = st.session_state.q_index

    q_type, question, expr, answer = generate_problem(level_key, idx)

    if q_type is None:
        st.error("難易度を選択してください")
        return

    st.markdown(f"### 問題 {idx + 1} : {q_type}")
    st.write(question)
    if expr is not None:
        st.latex(sympy.latex(expr))

    if st.button("答えを見る"):
        if answer is not None:
            st.latex(sympy.latex(answer))
        else:
            st.write("答えがありません。")

if __name__ == "__main__":
    main()
