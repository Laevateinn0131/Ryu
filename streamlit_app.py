import streamlit as st
import random
import math
import time

def generate_pythagorean_problem():
    """暗算で解ける三平方の定理の問題を生成"""
    # 有名なピタゴラス数のペアを使用
    pythagorean_triples = [
        (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
        (6, 8, 10), (9, 12, 15), (12, 16, 20), (15, 20, 25)
    ]
    
    a, b, c = random.choice(pythagorean_triples)
    
    # どの辺を求めるかランダムに決定
    problem_type = random.choice(['hypotenuse', 'leg'])
    
    if problem_type == 'hypotenuse':
        # 斜辺を求める問題
        problem = f"直角三角形で、直角を挟む2辺の長さがそれぞれ {a}cm、{b}cm のとき、斜辺の長さを求めなさい。"
        answer = c
        solution = f"三平方の定理により: {a}² + {b}² = c²\n{a**2} + {b**2} = c²\n{c**2} = c²\nよって c = {c}cm"
    else:
        # 一つの辺を求める問題
        problem = f"直角三角形で、斜辺の長さが {c}cm、直角を挟む一辺の長さが {a}cm のとき、もう一辺の長さを求めなさい。"
        answer = b
        solution = f"三平方の定理により: {a}² + b² = {c}²\n{a**2} + b² = {c**2}\nb² = {c**2} - {a**2}\nb² = {b**2}\nよって b = {b}cm"
    
    return problem, answer, solution

def generate_quadratic_completion_problem():
    """暗算で解ける平方完成の問題を生成"""
    # 完全平方式になるように係数を選択
    # (x + p)² = x² + 2px + p² の形
    p_values = [-4, -3, -2, -1, 1, 2, 3, 4, 5]
    p = random.choice(p_values)
    
    # x² + 2px + ? = (x + p)² の形で問題を作成
    linear_coeff = 2 * p
    constant_needed = p * p
    
    problem_type = random.choice(['complete', 'factor'])
    
    if problem_type == 'complete':
        # 平方完成の問題
        if linear_coeff >= 0:
            problem = f"x² + {linear_coeff}x + ？ が完全平方式になるとき、？に入る数を求めなさい。"
        else:
            problem = f"x² {linear_coeff}x + ？ が完全平方式になるとき、？に入る数を求めなさい。"
        answer = constant_needed
        if p >= 0:
            solution = f"完全平方式 (x + {p})² = x² + {2*p}x + {p**2} と比較すると、？ = {constant_needed}"
        else:
            solution = f"完全平方式 (x {p})² = x² + {2*p}x + {p**2} と比較すると、？ = {constant_needed}"
    else:
        # 因数分解の問題
        if linear_coeff >= 0:
            problem = f"x² + {linear_coeff}x + {constant_needed} を因数分解しなさい。"
        else:
            problem = f"x² {linear_coeff}x + {constant_needed} を因数分解しなさい。"
        if p >= 0:
            answer = f"(x + {p})²"
        else:
            answer = f"(x {p})²"
        solution = f"x² + {linear_coeff}x + {constant_needed} = (x + {p})²"
    
    return problem, answer, solution

def main():
    st.title("数学問題生成器 (時間制限付き)")
    st.write("暗算で解ける三平方の定理と平方完成の問題を生成します")
    
    # サイドバーで問題の種類を選択
    problem_type = st.sidebar.selectbox(
        "問題の種類を選択してください",
        ["三平方の定理", "平方完成"]
    )
    
    # 制限時間の設定
    time_limit = 30 if problem_type == "三平方の定理" else 15
    
    # セッション状態の初期化
    if 'timer_started' not in st.session_state:
        st.session_state.timer_started = False
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
    if 'time_up' not in st.session_state:
        st.session_state.time_up = False
    
    # 問題生成ボタン
    if st.button("新しい問題を生成"):
        if problem_type == "三平方の定理":
            problem, answer, solution = generate_pythagorean_problem()
        else:
            problem, answer, solution = generate_quadratic_completion_problem()
        
        # セッション状態に保存
        st.session_state.current_problem = problem
        st.session_state.current_answer = answer
        st.session_state.current_solution = solution
        st.session_state.current_problem_type = problem_type
        st.session_state.show_answer = False
        st.session_state.timer_started = True
        st.session_state.start_time = time.time()
        st.session_state.time_up = False
    
    # 現在の問題を表示
    if hasattr(st.session_state, 'current_problem'):
        st.subheader("問題")
        st.write(st.session_state.current_problem)
        
        # タイマー表示
        if st.session_state.timer_started and not st.session_state.show_answer:
            current_time = time.time()
            elapsed_time = current_time - st.session_state.start_time
            remaining_time = max(0, time_limit - elapsed_time)
            
            if remaining_time > 0:
                # 残り時間を表示
                minutes = int(remaining_time // 60)
                seconds = int(remaining_time % 60)
                
                # 残り時間が5秒以下の場合は赤色で表示
                if remaining_time <= 5:
                    st.markdown(f"<h2 style='color: red;'>残り時間: {minutes:02d}:{seconds:02d}</h2>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<h2 style='color: blue;'>残り時間: {minutes:02d}:{seconds:02d}</h2>", unsafe_allow_html=True)
                
                # 1秒ごとに自動更新
                time.sleep(0.1)
                st.rerun()
            else:
                # 時間切れ
                st.session_state.time_up = True
                st.session_state.timer_started = False
                st.markdown("<h2 style='color: red;'>⏰ 時間切れ！</h2>", unsafe_allow_html=True)
        
        # 解答入力（時間内の場合のみ）
        if not st.session_state.time_up and not getattr(st.session_state, 'show_answer', False):
            st.subheader("解答入力")
            
            if st.session_state.current_problem_type == "平方完成" and "因数分解" in st.session_state.current_problem:
                user_answer = st.text_input("答えを入力してください (例: (x+2)² )", key="answer_input")
            else:
                user_answer = st.number_input("答えを入力してください", step=1, key="answer_input")
            
            if st.button("答えをチェック"):
                st.session_state.user_answer = user_answer
                st.session_state.show_answer = True
                st.session_state.timer_started = False
        
        # 解答表示ボタン（時間切れまたは答えをチェック後）
        elif not getattr(st.session_state, 'show_answer', False):
            if st.button("解答を表示"):
                st.session_state.show_answer = True
        
        # 解答と解説を表示
        if getattr(st.session_state, 'show_answer', False):
            st.subheader("解答")
            st.write(f"**正解: {st.session_state.current_answer}**")
            
            # ユーザーの答えとの比較
            if hasattr(st.session_state, 'user_answer'):
                if str(st.session_state.user_answer) == str(st.session_state.current_answer):
                    st.success("🎉 正解です！")
                else:
                    st.error(f"❌ 不正解です。あなたの答え: {st.session_state.user_answer}")
            
            st.subheader("解説")
            st.write(st.session_state.current_solution)
            
            # 時間結果の表示
            if hasattr(st.session_state, 'start_time') and st.session_state.start_time:
                if st.session_state.time_up:
                    st.warning(f"⏱️ 制限時間 {time_limit} 秒を超過しました")
                else:
                    elapsed = time.time() - st.session_state.start_time
                    if elapsed <= time_limit:
                        st.success(f"⏱️ 解答時間: {elapsed:.1f} 秒 (制限時間内)")
                    else:
                        st.warning(f"⏱️ 解答時間: {elapsed:.1f} 秒 (制限時間超過)")
    
    # 使い方の説明
    st.sidebar.markdown("## 使い方")
    st.sidebar.markdown("""
    1. 問題の種類を選択
    2. 「新しい問題を生成」をクリック
    3. 制限時間内に問題を解く
    4. 答えを入力して「答えをチェック」
    5. 解答と解説を確認
    """)
    
    st.sidebar.markdown("## 制限時間")
    st.sidebar.markdown("""
    - **三平方の定理**: 30秒
    - **平方完成**: 15秒
    """)
    
    st.sidebar.markdown("## 問題の特徴")
    st.sidebar.markdown("""
    **三平方の定理:**
    - 有名なピタゴラス数を使用
    - 暗算で計算可能
    
    **平方完成:**
    - 簡単な整数係数
    - 完全平方式の問題
    """)

if __name__ == "__main__":
    main()