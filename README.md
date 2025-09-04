import random
import streamlit as st

# 定期テストレベルの単語と意味
easy_vocabulary = {
    "basic": "fundamental or simple",
    "bizarre": "very strange or unusual",
    "precise": "exact and accurate",
    "loyal": "showing strong support",
    "generous": "willing to give and share",
}

# 全国模試レベルの単語と意味
hard_vocabulary = {
    "aberration": "a deviation from what is normal",
    "sagacious": "wise or shrewd",
    "perspicacious": "having a ready insight into and understanding of things",
    "recalcitrant": "stubbornly resisting authority",
    "obfuscate": "to confuse or make unclear",
}

# 定期テストレベルの文脈問題
easy_contextual_vocabulary = {
    "She is very __ and always helps her classmates.": ["generous", "recalcitrant", "sagacious", "perspicacious"],
    "The detective was very __, quickly solving the case.": ["sagacious", "bizarre", "precise", "basic"],
}

# 全国模試レベルの文脈問題
hard_contextual_vocabulary = {
    "The student's __ behavior caused problems in the class.": ["recalcitrant", "loyal", "generous", "basic"],
    "The witness tried to __ the truth, but the detective could still tell what happened.": ["obfuscate", "precise", "loyal", "bizarre"],
}

# 単語の意味を選ぶ問題（難易度別）
def vocabulary_quiz(vocab):
    # ランダムに単語を選ぶ
    word, correct_meaning = random.choice(list(vocab.items()))
    
    # 意味の候補をランダムにシャッフル
    meanings = list(vocab.values())
    random.shuffle(meanings)
    
    # 正しい意味を選択肢に加える
    if correct_meaning not in meanings:
        meanings[0] = correct_meaning
    
    # ユーザーに問題を出題
    st.write(f"**Question: What is the meaning of '{word}'?**")
    choices = [f"{idx}. {meaning}" for idx, meaning in enumerate(meanings, 1)]
    user_answer = st.radio("Choose your answer", choices)
    
    # ユーザーの回答をチェック
    if user_answer:
        selected_meaning = meanings[int(user_answer[0])-1]
        if selected_meaning == correct_meaning:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is: {correct_meaning}")
    
# 文脈に適した単語を選ぶ問題（難易度別）
def contextual_quiz(contextual_vocab):
    # ランダムに文脈と選択肢を選ぶ
    sentence, choices = random.choice(list(contextual_vocab.items()))
    
    # ユーザーに問題を出題
    st.write(f"**Question: {sentence}**")
    user_answer = st.radio("Choose your answer", choices)
    
    # ユーザーの回答をチェック
    if user_answer:
        correct_answer = choices[0]  # 0番目が正解と仮定
        if user_answer == correct_answer:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is: {correct_answer}")

# 難易度に応じて問題を出題する関数
def start_quiz():
    st.title("Vocabulary Quiz")
    
    st.write("### Choose a difficulty level:")
    level = st.radio("Select level", ("定期テストレベル", "全国模試レベル"))
    
    if level == "定期テストレベル":
        st.write("\n--- 定期テストレベルの問題 ---")
        vocabulary_quiz(easy_vocabulary)
        contextual_quiz(easy_contextual_vocabulary)
        
    elif level == "全国模試レベル":
        st.write("\n--- 全国模試レベルの問題 ---")
        vocabulary_quiz(hard_vocabulary)
        contextual_quiz(hard_contextual_vocabulary)

# クイズを実行
if __name__ == "__main__":
    start_quiz()


