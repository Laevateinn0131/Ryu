import random
import streamlit as st

# 定期テストレベルの単語と意味
easy_vocabulary = {
    "basic": "fundamental or simple",
    "bizarre": "very strange or unusual",
    "precise": "exact and accurate",
    "loyal": "showing strong support",
    "generous": "willing to give and share",
    "obvious": "easily understood or seen",
    "complex": "consisting of many different parts",
    "humble": "having a modest opinion of oneself",
    "curious": "eager to know or learn something",
    "gentle": "kind and mild in manner"
}

# 全国模試レベルの単語と意味
hard_vocabulary = {
    "aberration": "a deviation from what is normal",
    "sagacious": "wise or shrewd",
    "perspicacious": "having a ready insight into and understanding of things",
    "recalcitrant": "stubbornly resisting authority",
    "obfuscate": "to confuse or make unclear",
    "ubiquitous": "present everywhere at the same time",
    "ephemeral": "lasting for a very short time",
    "fastidious": "very attentive to accuracy and detail",
    "mendacious": "given to lying or being dishonest",
    "sanguine": "optimistic or confident about the future"
}

# 定期テストレベルの文脈問題（正解は最初の選択肢）
easy_contextual_vocabulary = {
    "She is very __ and always helps her classmates without expecting anything in return.": 
        {
            "choices": ["generous", "recalcitrant", "sagacious", "perspicacious"],
            "explanation": "「generous」は「寛大な、気前の良い」という意味で、見返りを期待せず助ける行為を表します。"
        },
    "The detective was very __ and quickly solved the complicated case.": 
        {
            "choices": ["sagacious", "bizarre", "precise", "basic"],
            "explanation": "「sagacious」は「賢明な、洞察力のある」という意味で、複雑な事件を解決する能力を表します。"
        },
    "His instructions were so __ that everyone understood exactly what to do.": 
        {
            "choices": ["precise", "bizarre", "complex", "humble"],
            "explanation": "「precise」は「正確な、明確な」という意味で、理解しやすい指示を表します。"
        },
    "The magician's __ performance left the audience completely amazed.": 
        {
            "choices": ["bizarre", "basic", "obvious", "gentle"],
            "explanation": "「bizarre」は「奇妙な、異様な」という意味で、驚くようなマジックパフォーマンスを表します。"
        },
    "Despite his great achievements, he remained __ and never boasted about his success.": 
        {
            "choices": ["humble", "curious", "complex", "loyal"],
            "explanation": "「humble」は「謙虚な」という意味で、成功しても自慢しない態度を表します。"
        },
    "The __ answer to the math problem was right in front of us.": 
        {
            "choices": ["obvious", "complex", "bizarre", "humble"],
            "explanation": "「obvious」は「明らかな、当然の」という意味で、すぐに分かる答えを表します。"
        },
    "She spoke in a __ voice so as not to wake the baby.": 
        {
            "choices": ["gentle", "complex", "obvious", "curious"],
            "explanation": "「gentle」は「優しい、穏やかな」という意味で、赤ちゃんを起こさない声のトーンを表します。"
        },
    "The child was __ about everything and asked many questions.": 
        {
            "choices": ["curious", "loyal", "humble", "basic"],
            "explanation": "「curious」は「好奇心旺盛な」という意味で、多くの質問をする姿勢を表します。"
        }
}

# 全国模試レベルの文脈問題（正解は最初の選択肢）
hard_contextual_vocabulary = {
    "その生徒の__な行動は、規則に従うことを頑固に拒んだため、クラスで問題を引き起こした。": 
        {
            "choices": ["recalcitrant", "loyal", "generous", "sanguine"],
            "explanation": "「recalcitrant」は「反抗的な、言うことを聞かない」という意味で、権威に従わない態度を表します。"
        },
    "その証人は真実を__しようとしたが、探偵はそれでも何が起こったかを推理できた。": 
        {
            "choices": ["obfuscate", "precise", "loyal", "bizarre"],
            "explanation": "「obfuscate」は「曖昧にする、分からなくする」という意味で、真実を隠そうとする行為を表します。"
        },
    "彼女の__な性格により、机の整理の仕方にとても細かくこだわった。": 
        {
            "choices": ["fastidious", "ephemeral", "ubiquitous", "mendacious"],
            "explanation": "「fastidious」は「細かいことにうるさい、完璧主義の」という意味で、詳細にこだわる性格を表します。"
        },
    "桜の__な美しさは、人生の儚い瞬間を大切にすることを思い出させてくれる。": 
        {
            "choices": ["ephemeral", "ubiquitous", "fastidious", "sanguine"],
            "explanation": "「ephemeral」は「短命な、儚い」という意味で、桜のように短い期間しか続かない美しさを表します。"
        },
    "スマートフォンは現代社会で__となり、ほぼ全てのポケットに入っている。": 
        {
            "choices": ["ubiquitous", "ephemeral", "mendacious", "aberration"],
            "explanation": "「ubiquitous」は「どこにでもある、遍在する」という意味で、広く普及している状態を表します。"
        },
    "その__な政治家の嘘は、最終的に調査ジャーナリストによって暴露された。": 
        {
            "choices": ["mendacious", "sanguine", "sagacious", "perspicacious"],
            "explanation": "「mendacious」は「嘘つきの、不正直な」という意味で、虚偽の発言をする人を表します。"
        },
    "経済危機にも関わらず、彼女は会社の将来の見通しについて__だった。": 
        {
            "choices": ["sanguine", "recalcitrant", "mendacious", "fastidious"],
            "explanation": "「sanguine」は「楽観的な、前向きな」という意味で、困難な状況でも希望を持つ態度を表します。"
        },
    "彼の市場動向に対する__な分析は、すべての投資家を感銘させた。": 
        {
            "choices": ["perspicacious", "recalcitrant", "ephemeral", "aberration"],
            "explanation": "「perspicacious」は「洞察力のある、鋭い」という意味で、市場を深く理解する能力を表します。"
        },
    "突然の雷雨は、それまで完璧だった天候パターンの__だった。": 
        {
            "choices": ["aberration", "ubiquitous", "sanguine", "perspicacious"],
            "explanation": "「aberration」は「異常、逸脱」という意味で、通常のパターンから外れた現象を表します。"
        }
}

# スコア管理用のセッション状態初期化
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'answered' not in st.session_state:
    st.session_state.answered = False

# 単語の意味を選ぶ問題（難易度別）
def vocabulary_quiz(vocab, quiz_type="meaning"):
    if 'current_vocab_question' not in st.session_state:
        word, correct_meaning = random.choice(list(vocab.items()))
        other_meanings = [meaning for w, meaning in vocab.items() if w != word]
        wrong_choices = random.sample(other_meanings, min(3, len(other_meanings)))
        all_choices = [correct_meaning] + wrong_choices
        random.shuffle(all_choices)

        st.session_state.current_vocab_question = {
            "word": word,
            "correct_meaning": correct_meaning,
            "choices": all_choices
        }

    question_data = st.session_state.current_vocab_question
    word = question_data["word"]
    correct_meaning = question_data["correct_meaning"]
    choices = question_data["choices"]

    st.write(f"**Question: What is the meaning of '{word}'?**")

    key = f"vocab_{quiz_type}_{word}"
    user_answer = st.radio("Choose your answer:", choices, key=key)

    if st.button("Submit Answer", key=f"submit_{key}"):
        st.session_state.total_questions += 1
        if user_answer == correct_meaning:
            st.session_state.score += 1
            st.success("🎉 Correct!")
        else:
            st.error(f"❌ Wrong! The correct answer is: **{correct_meaning}**")

        st.info(f"Current Score: {st.session_state.score}/{st.session_state.total_questions}")

        # 次の問題に備えて保存された問題を削除
        del st.session_state.current_vocab_question

# 文脈に適した単語を選ぶ問題（難易度別）
def contextual_quiz(contextual_vocab, quiz_type="context"):
    if 'current_context_question' not in st.session_state:
        sentence, data = random.choice(list(contextual_vocab.items()))
        choices = data["choices"]
        explanation = data["explanation"]
        correct_answer = choices[0]
        shuffled_choices = choices.copy()
        random.shuffle(shuffled_choices)

        st.session_state.current_context_question = {
            "sentence": sentence,
            "choices": shuffled_choices,
            "correct": correct_answer,
            "explanation": explanation
        }

    q = st.session_state.current_context_question
    sentence = q["sentence"]
    choices = q["choices"]
    correct_answer = q["correct"]
    explanation = q["explanation"]

    st.write("**Question: Choose the word that best fits the blank:**")
    st.write(sentence.replace("__", "______"))

    key = f"context_{quiz_type}_{random.randint(1000, 9999)}"
    user_answer = st.radio("Choose your answer:", choices, key=key)

    if st.button("Submit Answer", key=f"submit_{key}"):
        st.session_state.total_questions += 1
        if user_answer == correct_answer:
            st.session_state.score += 1
            st.success("🎉 Correct!")
            st.info(f"💡 {explanation}")
        else:
            st.error(f"❌ Wrong! The correct answer is: **{correct_answer}**")
            st.info(f"💡 {explanation}")

        st.info(f"Current Score: {st.session_state.score}/{st.session_state.total_questions}")

        # 次の問題に備えてセッションの問題を削除
        del st.session_state.current_context_question

# スコアリセット機能
def reset_score():
    st.session_state.score = 0
    st.session_state.total_questions = 0
    st.success("スコアがリセットされました！")

# 難易度に応じて問題を出題する関数
def start_quiz():
    st.title("📚 英単語学習クイズ")
    
    # サイドバーにスコア表示
    with st.sidebar:
        st.header("📊 学習進捗")
        if st.session_state.total_questions > 0:
            accuracy = (st.session_state.score / st.session_state.total_questions) * 100
            st.metric("スコア", f"{st.session_state.score}/{st.session_state.total_questions}")
            st.metric("正答率", f"{accuracy:.1f}%")
            
            # 成績に応じたコメント
            if accuracy >= 90:
                st.success("🌟 素晴らしい成績です！")
            elif accuracy >= 80:
                st.info("😊 良い調子です！")
            elif accuracy >= 70:
                st.warning("📚 もう少し頑張りましょう！")
            else:
                st.error("💪 復習が必要です！")
        else:
            st.write("まだ問題に答えていません")
        
        if st.button("スコアをリセット"):
            reset_score()
    
    st.write("### 🎯 難易度を選択してください:")
    level = st.selectbox("難易度:", ("定期テストレベル", "全国模試レベル"))
    
    st.write("### 📝 問題形式を選択してください:")
    quiz_type = st.selectbox("問題形式:", ("単語の意味", "文脈問題", "ミックス"))
    
    st.write("---")
    
    if level == "定期テストレベル":
        st.write("### 📖 定期テストレベルの問題")
        
        if quiz_type == "単語の意味":
            vocabulary_quiz(easy_vocabulary, "easy_vocab")
        elif quiz_type == "文脈問題":
            contextual_quiz(easy_contextual_vocabulary, "easy_context")
        else:  # ミックス
            if random.choice([True, False]):
                st.write("**単語問題:**")
                vocabulary_quiz(easy_vocabulary, "easy_vocab_mix")
            else:
                st.write("**文脈問題:**")
                contextual_quiz(easy_contextual_vocabulary, "easy_context_mix")
    
    elif level == "全国模試レベル":
        st.write("### 🎓 全国模試レベルの問題")
        
        if quiz_type == "単語の意味":
            vocabulary_quiz(hard_vocabulary, "hard_vocab")
        elif quiz_type == "文脈問題":
            contextual_quiz(hard_contextual_vocabulary, "hard_context")
        else:  # ミックス
            if random.choice([True, False]):
                st.write("**単語問題:**")
                vocabulary_quiz(hard_vocabulary, "hard_vocab_mix")
            else:
                st.write("**文脈問題:**")
                contextual_quiz(hard_contextual_vocabulary, "hard_context_mix")
    
    # 新しい問題を生成するボタン
    st.write("---")
    if st.button("🔄 新しい問題を出題"):
        st.rerun()

# 単語集表示機能
def show_vocabulary():
    st.title("📖 単語集")
    
    tab1, tab2 = st.tabs(["定期テストレベル", "全国模試レベル"])
    
    with tab1:
        st.write("### 📚 定期テストレベル単語集")
        st.write("基本的な英単語です。まずはこれらの単語をしっかりと覚えましょう。")
        st.write("---")
        for i, (word, meaning) in enumerate(easy_vocabulary.items(), 1):
            st.write(f"**{i}. {word}**: {meaning}")
    
    with tab2:
        st.write("### 🎓 全国模試レベル単語集")
        st.write("より高度な英単語です。大学受験や英語検定などで出題されることがあります。")
        st.write("---")
        for i, (word, meaning) in enumerate(hard_vocabulary.items(), 1):
            st.write(f"**{i}. {word}**: {meaning}")

# メイン実行部分
if __name__ == "__main__":
    # ナビゲーション
    page = st.sidebar.selectbox("ページ選択:", ["クイズ", "単語集"])
    
    if page == "クイズ":
        start_quiz()
    else:
        show_vocabulary()