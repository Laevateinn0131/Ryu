
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vocabulary Quiz</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            color: #333;
        }
        
        .container {
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        h1 {
            text-align: center;
            color: #4a5568;
            margin-bottom: 30px;
            font-size: 2.5em;
        }
        
        .level-selector {
            margin-bottom: 30px;
            text-align: center;
        }
        
        .level-selector label {
            margin: 0 15px;
            font-size: 1.1em;
        }
        
        .quiz-container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 30px;
        }
        
        .quiz-section {
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            border: 2px solid #e2e8f0;
        }
        
        .quiz-section h3 {
            color: #2d3748;
            margin-bottom: 20px;
            font-size: 1.3em;
        }
        
        .question {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            border-left: 4px solid #667eea;
        }
        
        .question h4 {
            margin: 0 0 15px 0;
            color: #2d3748;
        }
        
        .choices {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        
        .choice {
            padding: 10px 15px;
            border: 2px solid #e2e8f0;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.3s ease;
            background: white;
        }
        
        .choice:hover {
            border-color: #667eea;
            background: #f0f4ff;
        }
        
        .choice.selected {
            border-color: #667eea;
            background: #667eea;
            color: white;
        }
        
        .choice.correct {
            border-color: #48bb78;
            background: #48bb78;
            color: white;
        }
        
        .choice.wrong {
            border-color: #e53e3e;
            background: #e53e3e;
            color: white;
        }
        
        button {
            background: #667eea;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1em;
            margin: 10px 5px;
            transition: background-color 0.3s ease;
        }
        
        button:hover {
            background: #5a67d8;
        }
        
        button:disabled {
            background: #a0aec0;
            cursor: not-allowed;
        }
        
        .result {
            margin: 15px 0;
            padding: 15px;
            border-radius: 6px;
            font-weight: bold;
        }
        
        .result.correct {
            background: #c6f6d5;
            color: #22543d;
            border: 1px solid #9ae6b4;
        }
        
        .result.wrong {
            background: #fed7d7;
            color: #742a2a;
            border: 1px solid #fc8181;
        }
        
        @media (max-width: 768px) {
            .quiz-container {
                grid-template-columns: 1fr;
                gap: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📚 Vocabulary Quiz</h1>
        
        <div class="level-selector">
            <h3>Choose a difficulty level:</h3>
            <label>
                <input type="radio" name="level" value="easy" checked onchange="changeLevel()"> 定期テストレベル
            </label>
            <label>
                <input type="radio" name="level" value="hard" onchange="changeLevel()"> 全国模試レベル
            </label>
        </div>
        
        <div class="quiz-container">
            <div class="quiz-section">
                <h3>単語の意味</h3>
                <div id="vocabularyQuiz"></div>
            </div>
            
            <div class="quiz-section">
                <h3>文脈問題</h3>
                <div id="contextualQuiz"></div>
            </div>
        </div>
    </div>

    <script>
        const easyVocabulary = {
            "generous": "willing to give more of something than is necessary",
            "loyal": "faithful to a person or belief",
            "precise": "exact and accurate",
            "basic": "fundamental or essential",
            "bizarre": "very strange or unusual"
        };

        const hardVocabulary = {
            "aberration": "a deviation from what is normal",
            "sagacious": "wise or shrewd",
            "perspicacious": "having a ready insight into and understanding of things",
            "recalcitrant": "stubbornly resisting authority",
            "obfuscate": "to confuse or make unclear"
        };

        const easyContextual = {
            "She is very __ and always helps her classmates.": ["generous", "recalcitrant", "sagacious", "perspicacious"],
            "The detective was very __, quickly solving the case.": ["sagacious", "bizarre", "precise", "basic"]
        };

        const hardContextual = {
            "The student's __ behavior caused problems in the class.": ["recalcitrant", "loyal", "generous", "basic"],
            "The witness tried to __ the truth, but the detective could still tell what happened.": ["obfuscate", "precise", "loyal", "bizarre"]
        };

        let currentLevel = 'easy';
        let currentVocabQuestion = null;
        let currentContextQuestion = null;

        function getRandomItem(obj) {
            const keys = Object.keys(obj);
            const randomKey = keys[Math.floor(Math.random() * keys.length)];
            return [randomKey, obj[randomKey]];
        }

        function shuffle(array) {
            const newArray = [...array];
            for (let i = newArray.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
            }
            return newArray;
        }

        function generateVocabularyQuiz() {
            const vocab = currentLevel === 'easy' ? easyVocabulary : hardVocabulary;
            const [word, correctMeaning] = getRandomItem(vocab);
            
            const allMeanings = Object.values(vocab);
            const wrongMeanings = allMeanings.filter(m => m !== correctMeaning);
            const choices = shuffle([correctMeaning, ...wrongMeanings.slice(0, 3)]);
            
            currentVocabQuestion = { word, correctMeaning, choices };
            
            const html = `
                <div class="question">
                    <h4>What is the meaning of '${word}'?</h4>
                    <div class="choices">
                        ${choices.map((choice, index) => 
                            `<div class="choice" onclick="selectVocabChoice(${index})" data-index="${index}">${choice}</div>`
                        ).join('')}
                    </div>
                    <button onclick="checkVocabAnswer()" id="checkVocabBtn" disabled>Check Answer</button>
                    <button onclick="generateVocabularyQuiz()" id="nextVocabBtn" style="display:none">Next Question</button>
                    <div id="vocabResult"></div>
                    <div id="vocabExplanation" class="explanation"></div>
                </div>
            `;
            
            document.getElementById('vocabularyQuiz').innerHTML = html;
        }

        function generateContextualQuiz() {
            const contextual = currentLevel === 'easy' ? easyContextual : hardContextual;
            const [sentence, sentenceData] = getRandomItem(contextual);
            const choices = sentenceData.choices;
            const correctAnswer = choices[0];
            const difficulty = sentenceData.difficulty;
            
            currentContextQuestion = { sentence, choices, correctAnswer, difficulty };
            
            const difficultyDisplay = getDifficultyDisplay(difficulty);
            const difficultyClass = getDifficultyClass(difficulty);
            
            const html = `
                <div class="question">
                    <div class="difficulty-badge ${difficultyClass}">Difficulty: ${difficultyDisplay}</div>
                    <h4>${sentence}</h4>
                    <div class="choices">
                        ${choices.map((choice, index) => 
                            `<div class="choice" onclick="selectContextChoice(${index})" data-index="${index}">${choice}</div>`
                        ).join('')}
                    </div>
                    <button onclick="checkContextAnswer()" id="checkContextBtn" disabled>Check Answer</button>
                    <button onclick="generateContextualQuiz()" id="nextContextBtn" style="display:none">Next Question</button>
                    <div id="contextResult"></div>
                </div>
            `;
            
            document.getElementById('contextualQuiz').innerHTML = html;
        }

        function selectVocabChoice(index) {
            document.querySelectorAll('#vocabularyQuiz .choice').forEach((el, i) => {
                el.classList.toggle('selected', i === index);
            });
            document.getElementById('checkVocabBtn').disabled = false;
        }

        function selectContextChoice(index) {
            document.querySelectorAll('#contextualQuiz .choice').forEach((el, i) => {
                el.classList.toggle('selected', i === index);
            });
            document.getElementById('checkContextBtn').disabled = false;
        }

        function checkVocabAnswer() {
            const selectedElement = document.querySelector('#vocabularyQuiz .choice.selected');
            const selectedText = selectedElement.textContent;
            const isCorrect = selectedText === currentVocabQuestion.correctMeaning;
            
            document.querySelectorAll('#vocabularyQuiz .choice').forEach(el => {
                el.onclick = null;
                if (el.textContent === currentVocabQuestion.correctMeaning) {
                    el.classList.add('correct');
                } else if (el.classList.contains('selected') && !isCorrect) {
                    el.classList.add('wrong');
                }
            });
            
            const resultDiv = document.getElementById('vocabResult');
            if (isCorrect) {
                resultDiv.innerHTML = '<div class="result correct">Correct! 🎉</div>';
            } else {
                resultDiv.innerHTML = `<div class="result wrong">Wrong! The correct answer is: ${currentVocabQuestion.correctMeaning}</div>`;
            }
            
            document.getElementById('checkVocabBtn').style.display = 'none';
            document.getElementById('nextVocabBtn').style.display = 'inline-block';
        }

        function checkContextAnswer() {
            const selectedElement = document.querySelector('#contextualQuiz .choice.selected');
            const selectedText = selectedElement.textContent;
            const isCorrect = selectedText === currentContextQuestion.correctAnswer;
            
            document.querySelectorAll('#contextualQuiz .choice').forEach(el => {
                el.onclick = null;
                if (el.textContent === currentContextQuestion.correctAnswer) {
                    el.classList.add('correct');
                } else if (el.classList.contains('selected') && !isCorrect) {
                    el.classList.add('wrong');
                }
            });
            
            const resultDiv = document.getElementById('contextResult');
            if (isCorrect) {
                resultDiv.innerHTML = '<div class="result correct">Correct! 🎉</div>';
            } else {
                resultDiv.innerHTML = `<div class="result wrong">Wrong! The correct answer is: ${currentContextQuestion.correctAnswer}</div>`;
            }
            
            document.getElementById('checkContextBtn').style.display = 'none';
            document.getElementById('nextContextBtn').style.display = 'inline-block';
        }

        function changeLevel() {
            const selectedLevel = document.querySelector('input[name="level"]:checked').value;
            currentLevel = selectedLevel;
            generateVocabularyQuiz();
            generateContextualQuiz();
        }

        // 初期化
        generateVocabularyQuiz();
        generateContextualQuiz();
    </script>
</body>
</html>