import random
import streamlit as st
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0

# 基礎レベルの単語（高校1年生向け）
basic_vocabulary = {
    "achieve": "to successfully complete or accomplish something",
    "analyze": "to examine something in detail",
    "approach": "to come near or closer to something",
    "benefit": "an advantage or profit gained from something",
    "challenge": "a difficult task or problem",
    "communicate": "to share or exchange information",
    "create": "to bring something into existence",
    "develop": "to grow or come into existence gradually",
    "environment": "the natural world or surroundings",
    "experience": "knowledge or skill gained over time",
    "generate": "to produce or create something",
    "identify": "to recognize or establish who someone is",
    "individual": "a single person or thing",
    "influence": "the power to affect someone or something",
    "maintain": "to keep something in good condition",
    "opportunity": "a chance to do something",
    "participate": "to take part in something",
    "require": "to need something",
    "significant": "important or meaningful",
    "technology": "the use of science to solve problems"
}

# 中級レベルの単語（高校2年生向け）
intermediate_vocabulary = {
    "acknowledge": "to accept or admit the existence of something",
    "acquire": "to obtain or gain possession of something",
    "adapt": "to change to suit new conditions",
    "advocate": "to publicly support or recommend",
    "anticipate": "to expect or predict something",
    "coincide": "to occur at the same time",
    "comprehensive": "including everything that is necessary",
    "constitute": "to form or make up something",
    "controversy": "public disagreement or debate",
    "derive": "to obtain something from a source",
    "diverse": "showing variety or differences",
    "eliminate": "to remove completely",
    "emphasize": "to give special importance to something",
    "enhance": "to improve the quality or value",
    "exploit": "to make full use of something",
    "facilitate": "to make something easier",
    "implement": "to put a plan or decision into effect",
    "inevitable": "certain to happen",
    "legitimate": "acceptable according to law or rules",
    "predominant": "most common or noticeable"
}

# 上級レベルの単語（高校3年生・受験向け）
advanced_vocabulary = {
    "aberration": "a deviation from what is normal or expected",
    "alleviate": "to make something less severe",
    "ambiguous": "having more than one possible meaning",
    "coherent": "logical and consistent",
    "compel": "to force someone to do something",
    "contemplate": "to think about something carefully",
    "discrepancy": "a difference between things that should be the same",
    "elaborate": "developed in great detail",
    "fluctuate": "to change irregularly",
    "inevitable": "certain to happen and unable to be avoided",
    "intrinsic": "belonging naturally to something",
    "meticulous": "showing great attention to detail",
    "prevalent": "widespread in a particular area",
    "scrutinize": "to examine something very carefully",
    "substantial": "of considerable importance or size",
    "tangible": "able to be touched or perceived clearly",
    "unprecedented": "never done or known before",
    "viable": "capable of working successfully",
    "volatile": "liable to change rapidly and unpredictably",
    "vulnerable": "exposed to the possibility of attack or harm"
}

# 文法問題データベース
grammar_questions = {
    "時制": {
        "basic": [
            {
                "question": "I __ to school every day.",
                "choices": ["go", "goes", "going", "went"],
                "correct": 0,
                "explanation": "現在の習慣を表すときは現在形を使います。主語が I なので go を使います。"
            },
            {
                "question": "She __ her homework yesterday.",
                "choices": ["finish", "finished", "finishing", "finishes"],
                "correct": 1,
                "explanation": "yesterday があるので過去形 finished を使います。"
            },
            {
                "question": "We __ studying English for three years.",
                "choices": ["are", "have been", "were", "will be"],
                "correct": 1,
                "explanation": "for three years という期間を表す語句があるので現在完了進行形を使います。"
            }
        ],
        "intermediate": [
            {
                "question": "By the time you arrive, I __ my work.",
                "choices": ["finish", "will finish", "will have finished", "finished"],
                "correct": 2,
                "explanation": "未来完了形: 未来のある時点までに完了している動作を表します。"
            },
            {
                "question": "If I __ rich, I would travel around the world.",
                "choices": ["am", "was", "were", "will be"],
                "correct": 2,
                "explanation": "仮定法過去: 現在の事実に反する仮定を表すときは were を使います。"
            },
            {
                "question": "He said he __ to the party the next day.",
                "choices": ["will go", "would go", "goes", "went"],
                "correct": 1,
                "explanation": "時制の一致: 主節が過去形なので従属節も過去形系列になります。"
            }
        ],
        "advanced": [
            {
                "question": "I wish I __ more attention in class yesterday.",
                "choices": ["pay", "paid", "had paid", "would pay"],
                "correct": 2,
                "explanation": "I wish + 過去完了: 過去の事実に対する後悔を表します。"
            },
            {
                "question": "Not until I arrived home __ that I had lost my keys.",
                "choices": ["I realized", "did I realize", "I did realize", "realized I"],
                "correct": 1,
                "explanation": "倒置: Not until が文頭に来ると主節は疑問文語順になります。"
            }
        ]
    },
    "受動態": {
        "basic": [
            {
                "question": "This book __ by many students.",
                "choices": ["reads", "is read", "read", "reading"],
                "correct": 1,
                "explanation": "受動態の現在形: be動詞 + 過去分詞の形を使います。"
            },
            {
                "question": "The window __ by the wind last night.",
                "choices": ["broke", "was broken", "is broken", "break"],
                "correct": 1,
                "explanation": "受動態の過去形: was/were + 過去分詞を使います。"
            }
        ],
        "intermediate": [
            {
                "question": "The new bridge __ next year.",
                "choices": ["will complete", "will be completed", "completes", "is completed"],
                "correct": 1,
                "explanation": "未来の受動態: will be + 過去分詞を使います。"
            },
            {
                "question": "She is said __ very talented.",
                "choices": ["be", "to be", "being", "been"],
                "correct": 1,
                "explanation": "It is said that... = 主語 + be said + to不定詞の書き換えです。"
            }
        ],
        "advanced": [
            {
                "question": "Having been __ by the teacher, he felt embarrassed.",
                "choices": ["criticize", "criticized", "criticizing", "to criticize"],
                "correct": 1,
                "explanation": "完了受動分詞: Having been + 過去分詞で「〜されてしまって」を表します。"
            }
        ]
    },
    "不定詞・動名詞": {
        "basic": [
            {
                "question": "I want __ English well.",
                "choices": ["speak", "to speak", "speaking", "spoke"],
                "correct": 1,
                "explanation": "want は to不定詞を目的語に取る動詞です。"
            },
            {
                "question": "He enjoys __ music.",
                "choices": ["listen", "to listen", "listening", "listened"],
                "correct": 2,
                "explanation": "enjoy は動名詞を目的語に取る動詞です。"
            }
        ],
        "intermediate": [
            {
                "question": "I remember __ him at the party.",
                "choices": ["meet", "to meet", "meeting", "met"],
                "correct": 2,
                "explanation": "remember + 動名詞: 過去にしたことを覚えている"
            },
            {
                "question": "Don't forget __ the door when you leave.",
                "choices": ["lock", "to lock", "locking", "locked"],
                "correct": 1,
                "explanation": "forget + to不定詞: これからすることを忘れる"
            }
        ],
        "advanced": [
            {
                "question": "The problem is too difficult for me __.",
                "choices": ["solve", "to solve", "solving", "solved"],
                "correct": 1,
                "explanation": "too...for A to不定詞: Aが〜するには...すぎる"
            }
        ]
    },
    "関係詞": {
        "basic": [
            {
                "question": "The book __ I bought yesterday is interesting.",
                "choices": ["who", "which", "where", "when"],
                "correct": 1,
                "explanation": "先行詞が物（book）で、関係詞が目的格なので which を使います。"
            }
        ],
        "intermediate": [
            {
                "question": "This is the house __ I was born.",
                "choices": ["which", "that", "where", "when"],
                "correct": 2,
                "explanation": "先行詞が場所で、関係副詞として使うので where を使います。"
            },
            {
                "question": "He has two sons, both of __ are doctors.",
                "choices": ["who", "whom", "which", "that"],
                "correct": 1,
                "explanation": "非制限用法で、前置詞の後なので whom を使います。"
            }
        ],
        "advanced": [
            {
                "question": "__ is often the case, he was late again.",
                "choices": ["Which", "What", "As", "That"],
                "correct": 2,
                "explanation": "As is often the case: よくあることだが（関係代名詞の非制限用法）"
            }
        ]
    },
    "仮定法": {
        "intermediate": [
            {
                "question": "If it __ tomorrow, we will cancel the picnic.",
                "choices": ["rain", "rains", "rained", "would rain"],
                "correct": 1,
                "explanation": "未来のことでも条件節では現在形を使います。"
            },
            {
                "question": "If I __ a bird, I could fly anywhere.",
                "choices": ["am", "was", "were", "will be"],
                "correct": 2,
                "explanation": "仮定法過去: 現在の事実に反する仮定。be動詞は were を使います。"
            }
        ],
        "advanced": [
            {
                "question": "If you __ harder last year, you would have passed the exam.",
                "choices": ["study", "studied", "had studied", "would study"],
                "correct": 2,
                "explanation": "仮定法過去完了: 過去の事実に反する仮定で had + 過去分詞を使います。"
            },
            {
                "question": "__ for your help, I couldn't have finished the project.",
                "choices": ["If it were not", "Were it not", "Had it not been", "If it had not been"],
                "correct": 2,
                "explanation": "仮定法の倒置: Had it not been for... = If it had not been for..."
            }
        ]
    }
}

# 文脈問題（レベル別）
contextual_questions = {
    "basic": {
        "My sister is very __ and always helps others without expecting anything back.": {
            "choices": ["generous", "selfish", "lazy", "angry"],
            "explanation": "見返りを期待せず他人を助けるのは「generous（寛大な）」です。"
        },
        "The math problem was so __ that even the best students couldn't solve it.": {
            "choices": ["difficult", "easy", "simple", "clear"],
            "explanation": "最優秀生徒でも解けないのは「difficult（難しい）」問題です。"
        },
        "Please speak more __. I can't hear you clearly.": {
            "choices": ["loudly", "quietly", "slowly", "quickly"],
            "explanation": "はっきり聞こえないので「loudly（大きく）」話してほしいです。"
        }
    },
    "intermediate": {
        "The company decided to __ the new policy to improve employee satisfaction.": {
            "choices": ["implement", "ignore", "reject", "postpone"],
            "explanation": "従業員満足度向上のため新方針を「implement（実施する）」しました。"
        },
        "His argument was so __ that everyone was convinced by his presentation.": {
            "choices": ["compelling", "boring", "confusing", "irrelevant"],
            "explanation": "みんなが納得したということは議論が「compelling（説得力のある）」でした。"
        },
        "The research team needs to __ more data before drawing any conclusions.": {
            "choices": ["analyze", "ignore", "destroy", "hide"],
            "explanation": "結論を出す前にデータを「analyze（分析する）」必要があります。"
        }
    },
    "advanced": {
        "The politician's __ remarks during the debate sparked controversy among voters.": {
            "choices": ["inflammatory", "diplomatic", "cautious", "neutral"],
            "explanation": "論争を引き起こしたということは「inflammatory（扇動的な）」発言でした。"
        },
        "Despite the __ evidence, the jury remained skeptical about the defendant's guilt.": {
            "choices": ["circumstantial", "conclusive", "overwhelming", "definitive"],
            "explanation": "陪審員が懐疑的だったということは証拠が「circumstantial（状況的な）」でした。"
        },
        "The CEO's decision to restructure was __ by the company's declining profits.": {
            "choices": ["precipitated", "prevented", "delayed", "ignored"],
            "explanation": "利益減少がリストラの決定を「precipitated（引き起こした）」しました。"
        }
    }
}

# セッション状態の初期化
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total_questions' not in st.session_state:
    st.session_state.total_questions = 0
if 'grammar_score' not in st.session_state:
    st.session_state.grammar_score = 0
if 'grammar_total' not in st.session_state:
    st.session_state.grammar_total = 0

def vocabulary_quiz(vocab_dict, level_name):
    # 問題番号をセッションで持つ
    if 'vocab_current_question' not in st.session_state:
        st.session_state.vocab_current_question = 0

    # 問題一覧
    items = list(vocab_dict.items())
    idx = st.session_state.vocab_current_question % len(items)
    word, correct_meaning = items[idx]
    
    other_meanings = [meaning for w, meaning in vocab_dict.items() if w != word]
    wrong_choices = random.sample(other_meanings, min(3, len(other_meanings)))
    all_choices = [correct_meaning] + wrong_choices
    random.shuffle(all_choices)
    
    st.write(f"### 📚 {level_name} 単語クイズ")
    st.write(f"**単語の意味を選んでください: '{word}'**")
    
    # radio の key は固定
    radio_key = f"vocab_radio_{level_name}_{idx}"
    user_answer = st.radio("選択肢:", all_choices, key=radio_key)
    
    # submit ボタンも key を固定
    submit_key = f"vocab_submit_{level_name}_{idx}"
    if st.button("回答する", key=submit_key):
        st.session_state.total_questions += 1
        if user_answer == correct_meaning:
            st.session_state.score += 1
            st.success("🎉 正解です！")
        else:
            st.error(f"❌ 不正解です。正解は: **{correct_meaning}**")
        
        st.info(f"単語スコア: {st.session_state.score}/{st.session_state.total_questions}")
        
        # ここで問題番号を進める（回答したときのみ）
        st.session_state.vocab_current_question += 1

def grammar_quiz(grammar_type, level):
    if 'grammar_current_question' not in st.session_state:
        st.session_state.grammar_current_question = 0

    if grammar_type not in grammar_questions or level not in grammar_questions[grammar_type]:
        st.warning("この組み合わせの問題はまだ準備中です。")
        return

    questions = grammar_questions[grammar_type][level]
    question_data = questions[st.session_state.grammar_current_question % len(questions)]

    # 問題表示など
    st.write(f"**適切な語句を選んでください:**")
    st.write(f"```{question_data['question']}```")

    key = f"grammar_{grammar_type}_{level}_{st.session_state.grammar_current_question}"
    user_choice = st.radio("選択肢:", question_data['choices'], key=key)

    if st.button("回答する", key=f"submit_{key}"):
        st.session_state.grammar_total += 1
        if user_choice == question_data['choices'][question_data['correct']]:
            st.session_state.grammar_score += 1
            st.success("🎉 正解です！")
        else:
            correct_answer = question_data['choices'][question_data['correct']]
            st.error(f"❌ 不正解です。正解は: **{correct_answer}**")

        st.info(f"💡 **解説**: {question_data['explanation']}")

        # 次の問題へ
        st.session_state.grammar_current_question += 1

        st.info(f"文法スコア: {st.session_state.grammar_score}/{st.session_state.grammar_total}")

def contextual_quiz(level):
    if 'context_current_question' not in st.session_state:
        st.session_state.context_current_question = 0

    items = list(contextual_questions[level].items())
    sentence, data = items[st.session_state.context_current_question % len(items)]

    choices = data['choices']
    explanation = data['explanation']

    correct_answer = choices[0]
    shuffled_choices = choices.copy()
    random.shuffle(shuffled_choices)

    st.write("**文脈に最も適した語句を選んでください:**")
    st.write(sentence.replace("__", "______"))

    key = f"context_{level}_{st.session_state.context_current_question}"
    user_answer = st.radio("選択肢:", shuffled_choices, key=key)

    if st.button("回答する", key=f"submit_{key}"):
        st.session_state.total_questions += 1
        if user_answer == correct_answer:
            st.session_state.score += 1
            st.success("🎉 正解です！")
        else:
            st.error(f"❌ 不正解です。正解は: **{correct_answer}**")

        st.info(f"💡 **解説**: {explanation}")

        # 次の問題へ
        st.session_state.context_current_question += 1

        st.info(f"文脈スコア: {st.session_state.score}/{st.session_state.total_questions}")


def show_reference():
    """参考資料ページ"""
    st.title("📚 学習参考資料")
    
    tab1, tab2, tab3 = st.tabs(["単語集", "文法解説", "学習のコツ"])
    
    with tab1:
        st.header("📖 レベル別単語集")
        
        vocab_tab1, vocab_tab2, vocab_tab3 = st.tabs(["基礎レベル", "中級レベル", "上級レベル"])
        
        with vocab_tab1:
            st.write("### 基礎レベル（高校1年生向け）")
            for i, (word, meaning) in enumerate(basic_vocabulary.items(), 1):
                st.write(f"**{i:2d}. {word}** - {meaning}")
        
        with vocab_tab2:
            st.write("### 中級レベル（高校2年生向け）")
            for i, (word, meaning) in enumerate(intermediate_vocabulary.items(), 1):
                st.write(f"**{i:2d}. {word}** - {meaning}")
        
        with vocab_tab3:
            st.write("### 上級レベル（高校3年生・受験向け）")
            for i, (word, meaning) in enumerate(advanced_vocabulary.items(), 1):
                st.write(f"**{i:2d}. {word}** - {meaning}")
    
    with tab2:
        st.header("📝 文法項目解説")
        
        for grammar_type in grammar_questions.keys():
            with st.expander(f"📖 {grammar_type}"):
                if grammar_type == "時制":
                    st.write("""
                    **時制の基本:**         
                    - 現在形: 習慣・真理を表す
                    - 過去形: 過去の一時点の動作・状態
                    - 現在完了形: 過去から現在への継続・完了・経験
                    - 未来完了形: 未来のある時点までの完了
                    - 仮定法: 事実に反する仮定
                    """)                                  
            
def show_progress_tracker():
    """学習進捗追跡ページ"""
    st.title("📈 学習進捗トラッカー")
    
    # 今日の学習目標設定
    st.header("🎯 今日の学習目標")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        daily_vocab_goal = st.number_input("単語問題目標数", min_value=0, max_value=100, value=10)
    with col2:
        daily_grammar_goal = st.number_input("文法問題目標数", min_value=0, max_value=100, value=5)
    with col3:
        daily_context_goal = st.number_input("文脈問題目標数", min_value=0, max_value=100, value=5)
    
    # 今日の進捗表示
    st.header("📊 今日の進捗")
    
    # 進捗バー表示
    vocab_progress = min(st.session_state.total_questions / daily_vocab_goal * 100, 100) if daily_vocab_goal > 0 else 0
    grammar_progress = min(st.session_state.grammar_total / daily_grammar_goal * 100, 100) if daily_grammar_goal > 0 else 0
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("単語・文脈問題", f"{st.session_state.total_questions}/{daily_vocab_goal}")
        st.progress(vocab_progress / 100)
    
    with col2:
        st.metric("文法問題", f"{st.session_state.grammar_total}/{daily_grammar_goal}")
        st.progress(grammar_progress / 100)
    
    # 学習アドバイス
    st.header("💡 学習アドバイス")
    
    total_answered = st.session_state.total_questions + st.session_state.grammar_total
    total_correct = st.session_state.score + st.session_state.grammar_score
    
    if total_answered > 0:
        overall_accuracy = (total_correct / total_answered) * 100
        
        if overall_accuracy >= 90:
            st.success("🌟 素晴らしい成績です！この調子で続けましょう。")
            st.info("💡 より高難度の問題にチャレンジしてみましょう。")
        elif overall_accuracy >= 80:
            st.info("😊 良い成績です！安定した学習ができています。")
            st.info("💡 間違えた分野を重点的に復習しましょう。")
        elif overall_accuracy >= 70:
            st.warning("📚 もう少し頑張りましょう！基礎を固めることが大切です。")
            st.info("💡 基礎レベルの問題を多めに解いて自信をつけましょう。")
        else:
            st.error("💪 復習が必要です！焦らず基礎から取り組みましょう。")
            st.info("💡 参考資料を読んでから問題に取り組むことをお勧めします。")
    
    # 弱点分析
    if st.session_state.total_questions > 0 and st.session_state.grammar_total > 0:
        st.header("🎯 分野別分析")
        
        vocab_accuracy = (st.session_state.score / st.session_state.total_questions) * 100
        grammar_accuracy = (st.session_state.grammar_score / st.session_state.grammar_total) * 100
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📚 単語・文脈")
            st.metric("正答率", f"{vocab_accuracy:.1f}%")
            if vocab_accuracy < 75:
                st.warning("💡 単語力強化が必要です")
        
        with col2:
            st.subheader("✍️ 文法")
            st.metric("正答率", f"{grammar_accuracy:.1f}%")
            if grammar_accuracy < 75:
                st.warning("💡 文法の基礎固めが必要です")

# メイン実行部分
if __name__ == "__main__":
    # ページナビゲーション
    page = st.sidebar.radio(
        "📍 ページ選択",
        ["🎯 クイズ", "📚 参考資料", "📈 進捗管理"]
    )
    
    if page == "🎯 クイズ":
        main_quiz()
    elif page == "📚 参考資料":
        show_reference()
    else:
        show_progress_tracker()
        grammar_type = st.selectbox(
    "文法項目を選択してください：",
    ["受動態", "不定詞・動名詞", "関係詞", "仮定法"]
)

    if grammar_type == "受動態":
        st.write("""
        **受動態の基本:**
        - 基本形: be動詞 + 過去分詞
        - 時制に応じてbe動詞を変化
        st.write("- by + 行為者(省略可能)")
        """)
    elif grammar_type == "不定詞・動名詞":
        st.write("""
        **不定詞と動名詞:**
        - 不定詞: to + 動詞の原形
        st.write("- 動名詞: 動詞のing形(名詞的用法)")
        - 動詞によって取る形が決まる
        """)
    elif grammar_type == "関係詞":
        st.write("""
        **関係詞の基本:**
        - who/whom: 人が先行詞
        - which: 物が先行詞
        - that: 人・物両方可能
        - where/when: 関係副詞
        """)
    elif grammar_type == "仮定法":
        st.write("""
        **仮定法:**
        - 仮定法過去: 現在の事実に反する仮定
        - 仮定法過去完了: 過去の事実に反する仮定
        - 混合仮定法: 時制が異なる仮定
        """)
    
    with tab3:
        st.header("💡 効果的な学習方法")
        
        st.write("""
        ### 🎯 単語学習のコツ
        1. **文脈で覚える**: 単語を文章の中で理解する
        2. **反復練習**: 定期的に復習して記憶を定着させる
        3. **関連語をまとめて**: 同義語・反義語・派生語を一緒に覚える
        4. **実際に使う**: 作文や会話で積極的に使用する
        
        ### 📚 文法学習のコツ
        1. **基本から応用へ**: 基礎をしっかり固めてから発展問題へ
        2. **例文で理解**: 文法規則を例文で確認する
        3. **間違いから学ぶ**: 間違えた問題は解説をよく読む
        4. **パターン認識**: 似た構文をまとめて整理する
        
        ### 🏆 効果的な復習方法
        st.write("- 間違えた問題は翌日、1週間後、1ヶ月後に再確認")
        - 正答率が90%以上になるまで繰り返す
        - 定期的に総復習テストを実施
        - 学習記録をつけて進捗を可視化
        """)