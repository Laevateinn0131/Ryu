import streamlit as st
import random
import time
import math

# ページ設定
st.set_page_config(
    page_title="三平方の定理 練習問題",
    page_icon="📐",
    layout="centered"
)

# セッションステートの初期化
if 'current_problem' not in st.session_state:
    st.session_state.current_problem = None
if 'score_correct' not in st.session_state:
    st.session_state.score_correct = 0
if 'score_total' not in st.session_state:
    st.session_state.score_total = 0
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None
if 'timer_expired' not in st.session_state:
    st.session_state.timer_expired = False

# 問題セット
problems = [
    {
        'type': 'hypotenuse',
        'question': '直角をはさむ2辺が 3cm と 4cm のとき、斜辺の長さは？',
        'answer': 5,
        'hint': '3² + 4² = 9 + 16 = 25 = 5²'
    },
    {
        'type': 'hypotenuse',
        'question': '直角をはさむ2辺が 6cm と 8cm のとき、斜辺の長さは？',
        'answer': 10,
        'hint': '3-4-5の2倍です'
    },
    {
        'type': 'hypotenuse',
        'question': '直角をはさむ2辺が 5cm と 12cm のとき、斜辺の長さは？',
        'answer': 13,
        'hint': '5² + 12² = 25 + 144 = 169 = 13²'
    },
    {
        'type': 'leg',
        'question': '斜辺が 5cm、一辺が 3cm のとき、もう一辺の長さは？',
        'answer': 4,
        'hint': '5² - 3² = 25 - 9 = 16 = 4²'
    },
    {
        'type': 'leg',
        'question': '斜辺が 5cm、一辺が 4cm のとき、もう一辺の長さは？',
        'answer': 3,
        'hint': '5² - 4² = 25 - 16 = 9 = 3²'
    },
    {
        'type': 'leg',
        'question': '斜辺が 10cm、一辺が 6cm のとき、もう一辺の長さは？',
        'answer': 8,
        'hint': '10² - 6² = 100 - 36 = 64 = 8²'
    },
    {
        'type': 'hypotenuse',
        'question': '直角をはさむ2辺が 9cm と 12cm のとき、斜辺の長さは？',
        'answer': 15,
        'hint': '3-4-5の3倍です'
    },
    {
        'type': 'leg',
        'question': '斜辺が 13cm、一辺が 5cm のとき、もう一辺の長さは？',
        'answer': 12,
        'hint': '13² - 5² = 169 - 25 = 144 = 12²'
    },
    {
        'type': 'hypotenuse',
        'question': '直角をはさむ2辺が 8cm と 15cm のとき、斜辺の長さは？',
        'answer': 17,
        'hint': '8² + 15² = 64 + 225 = 289 = 17²'
    },
    {
        'type': 'leg',
        'question': '斜辺が 17cm、一辺が 8cm のとき、もう一辺の長さは？',
        'answer': 15,
        'hint': '17² - 8² = 289 - 64 = 225 = 15²'
    },
    {
        'type': 'leg',
        'question': '斜辺が 17cm、一辺が 15cm のとき、もう一辺の長さは？',
        'answer': 8,
        'hint': '17² - 15² = 289 - 225 = 64 = 8²'
    },
    {
        'type': 'hypotenuse',
        'question': '直角をはさむ2辺が 7cm と 24cm のとき、斜辺の長さは？',
        'answer': 25,
        'hint': '7² + 24² = 49 + 576 = 625 = 25²'
    },
    {
        'type': 'leg',
        'question': '斜辺が 25cm、一辺が 7cm のとき、もう一辺の長さは？',
        'answer': 24,
        'hint': '25² - 7² = 625 - 49 = 576 = 24²'
    },
    {
        'type': 'leg',
        'question': '斜辺が 25cm、一辺が 24cm のとき、もう一辺の長さは？',
        'answer': 7,
        'hint': '25² - 24² = 625 - 576 = 49 = 7²'
    }
]

def generate_new_problem():
    """新しい問題を生成"""
    st.session_state.current_problem = random.choice(problems)
    st.session_state.feedback = ""
    st.session_state.show_answer = False
    st.session_state.start_time = time.time()
    st.session_state.timer_expired = False

def check_answer(user_answer):
    """答えをチェック"""
    if st.session_state.current_problem is None:
        return
    
    # タイマーチェック
    elapsed_time = time.time() - st.session_state.start_time
    if elapsed_time >= 30:
        st.session_state.timer_expired = True
        st.session_state.score_total += 1
        st.session_state.feedback = f"時間切れ！正解は {st.session_state.current_problem['answer']}cm です。"
        st.session_state.show_answer = True
        return
    
    # 答えの判定
    try:
        answer = float(user_answer)
        is_correct = abs(answer - st.session_state.current_problem['answer']) < 0.01
        
        st.session_state.score_total += 1
        if is_correct:
            st.session_state.score_correct += 1
            st.session_state.feedback = "正解！"
        else:
            st.session_state.feedback = f"不正解。正解は {st.session_state.current_problem['answer']}cm です。"
        
        st.session_state.show_answer = True
        
    except ValueError:
        st.error("数字を入力してください。")

def reset_score():
    """スコアをリセット"""
    st.session_state.score_correct = 0
    st.session_state.score_total = 0
    generate_new_problem()

# メインUI
st.title("📐 三平方の定理 練習問題")

# スコア表示
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("正解数", f"{st.session_state.score_correct}/{st.session_state.score_total}")
with col2:
    if st.session_state.score_total > 0:
        accuracy = round(st.session_state.score_correct / st.session_state.score_total * 100)
        st.metric("正答率", f"{accuracy}%")
with col3:
    # タイマー表示
    if st.session_state.start_time and not st.session_state.show_answer:
        elapsed = time.time() - st.session_state.start_time
        remaining = max(0, 30 - int(elapsed))
        
        if remaining > 10:
            st.metric("⏱️ 残り時間", f"{remaining}秒", delta=None)
        elif remaining > 5:
            st.metric("⏱️ 残り時間", f"{remaining}秒", delta=None, delta_color="off")
        else:
            st.metric("⏱️ 残り時間", f"{remaining}秒", delta="急いで！", delta_color="inverse")
        
        # タイマー切れチェック
        if remaining <= 0 and not st.session_state.timer_expired:
            st.session_state.timer_expired = True
            st.session_state.score_total += 1
            st.session_state.feedback = f"時間切れ！正解は {st.session_state.current_problem['answer']}cm です。"
            st.session_state.show_answer = True
            st.rerun()

# 初回問題生成
if st.session_state.current_problem is None:
    generate_new_problem()

# 問題表示エリア
st.markdown("---")
problem_container = st.container()

with problem_container:
    # 問題文
    st.subheader("問題")
    st.write(st.session_state.current_problem['question'])
    
    # 公式表示
    if st.session_state.current_problem['type'] == 'hypotenuse':
        st.info("公式: c² = a² + b² → c = √(a² + b²)")
    else:
        st.info("公式: a² = c² - b² → a = √(c² - b²)")
    
    # 回答入力
    col1, col2 = st.columns([3, 1])
    with col1:
        user_answer = st.number_input(
            "答えを入力してください", 
            value=None, 
            placeholder="例: 5",
            disabled=st.session_state.show_answer or st.session_state.timer_expired,
            key="answer_input"
        )
    with col2:
        st.write("cm")

# ボタンエリア
button_col1, button_col2, button_col3 = st.columns(3)

with button_col1:
    if st.button("答え合わせ", 
                type="primary",
                disabled=user_answer is None or st.session_state.show_answer or st.session_state.timer_expired):
        check_answer(user_answer)
        st.rerun()

with button_col2:
    if st.button("次の問題", type="secondary"):
        generate_new_problem()
        st.rerun()

with button_col3:
    if st.button("スコアリセット"):
        reset_score()
        st.rerun()

# フィードバック表示
if st.session_state.feedback:
    if "正解" in st.session_state.feedback:
        st.success(f"✅ {st.session_state.feedback}")
    elif "時間切れ" in st.session_state.feedback:
        st.warning(f"⏰ {st.session_state.feedback}")
    else:
        st.error(f"❌ {st.session_state.feedback}")

# 解説表示
if st.session_state.show_answer:
    with st.expander("解説", expanded=True):
        st.write(st.session_state.current_problem['hint'])

# 参考情報
st.markdown("---")
with st.expander("覚えておくと便利な直角三角形"):
    st.markdown("""
    - **3-4-5の三角形**（とその倍数：6-8-10, 9-12-15など）
    - **5-12-13の三角形**
    - **8-15-17の三角形**  
    - **7-24-25の三角形**
    """)

# 自動更新（タイマー用）
if st.session_state.start_time and not st.session_state.show_answer and not st.session_state.timer_expired:
    elapsed = time.time() - st.session_state.start_time
    if elapsed < 30:
        time.sleep(1)
        st.rerun()