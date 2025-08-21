import React, { useState, useEffect } from 'react';
import { CheckCircle, XCircle, RotateCcw, BookOpen } from 'lucide-react';

const PythagoreanQuiz = () => {
  const [currentProblem, setCurrentProblem] = useState(null);
  const [userAnswer, setUserAnswer] = useState('');
  const [showAnswer, setShowAnswer] = useState(false);
  const [score, setScore] = useState({ correct: 0, total: 0 });
  const [feedback, setFeedback] = useState('');
  const [timeLeft, setTimeLeft] = useState(30);
  const [isTimerActive, setIsTimerActive] = useState(false);

  // 暗算で解ける三平方の定理の問題セット
  const problems = [
    {
      type: 'hypotenuse',
      a: 3, b: 4, answer: 5,
      question: '直角をはさむ2辺が 3cm と 4cm のとき、斜辺の長さは？',
      hint: '3² + 4² = 9 + 16 = 25 = 5²'
    },
    {
      type: 'hypotenuse',
      a: 6, b: 8, answer: 10,
      question: '直角をはさむ2辺が 6cm と 8cm のとき、斜辺の長さは？',
      hint: '3-4-5の2倍です'
    },
    {
      type: 'hypotenuse',
      a: 5, b: 12, answer: 13,
      question: '直角をはさむ2辺が 5cm と 12cm のとき、斜辺の長さは？',
      hint: '5² + 12² = 25 + 144 = 169 = 13²'
    },
    {
      type: 'leg',
      hypotenuse: 5, knownLeg: 3, answer: 4,
      question: '斜辺が 5cm、一辺が 3cm のとき、もう一辺の長さは？',
      hint: '5² - 3² = 25 - 9 = 16 = 4²'
    },
    {
      type: 'leg',
      hypotenuse: 5, knownLeg: 4, answer: 3,
      question: '斜辺が 5cm、一辺が 4cm のとき、もう一辺の長さは？',
      hint: '5² - 4² = 25 - 16 = 9 = 3²'
    },
    {
      type: 'leg',
      hypotenuse: 10, knownLeg: 6, answer: 8,
      question: '斜辺が 10cm、一辺が 6cm のとき、もう一辺の長さは？',
      hint: '10² - 6² = 100 - 36 = 64 = 8²'
    },
    {
      type: 'hypotenuse',
      a: 9, b: 12, answer: 15,
      question: '直角をはさむ2辺が 9cm と 12cm のとき、斜辺の長さは？',
      hint: '3-4-5の3倍です'
    },
    {
      type: 'leg',
      hypotenuse: 13, knownLeg: 5, answer: 12,
      question: '斜辺が 13cm、一辺が 5cm のとき、もう一辺の長さは？',
      hint: '13² - 5² = 169 - 25 = 144 = 12²'
    },
    {
      type: 'hypotenuse',
      a: 8, b: 15, answer: 17,
      question: '直角をはさむ2辺が 8cm と 15cm のとき、斜辺の長さは？',
      hint: '8² + 15² = 64 + 225 = 289 = 17²'
    },
    {
      type: 'leg',
      hypotenuse: 17, knownLeg: 8, answer: 15,
      question: '斜辺が 17cm、一辺が 8cm のとき、もう一辺の長さは？',
      hint: '17² - 8² = 289 - 64 = 225 = 15²'
    },
    {
      type: 'leg',
      hypotenuse: 17, knownLeg: 15, answer: 8,
      question: '斜辺が 17cm、一辺が 15cm のとき、もう一辺の長さは？',
      hint: '17² - 15² = 289 - 225 = 64 = 8²'
    },
    {
      type: 'hypotenuse',
      a: 7, b: 24, answer: 25,
      question: '直角をはさむ2辺が 7cm と 24cm のとき、斜辺の長さは？',
      hint: '7² + 24² = 49 + 576 = 625 = 25²'
    },
    {
      type: 'leg',
      hypotenuse: 25, knownLeg: 7, answer: 24,
      question: '斜辺が 25cm、一辺が 7cm のとき、もう一辺の長さは？',
      hint: '25² - 7² = 625 - 49 = 576 = 24²'
    },
    {
      type: 'leg',
      hypotenuse: 25, knownLeg: 24, answer: 7,
      question: '斜辺が 25cm、一辺が 24cm のとき、もう一辺の長さは？',
      hint: '25² - 24² = 625 - 576 = 49 = 7²'
    }
  ];

  const generateProblem = () => {
    const randomIndex = Math.floor(Math.random() * problems.length);
    setCurrentProblem(problems[randomIndex]);
    setUserAnswer('');
    setShowAnswer(false);
    setFeedback('');
    setTimeLeft(30);
    setIsTimerActive(true);
  };

  const checkAnswer = () => {
    setIsTimerActive(false);
    const answer = parseFloat(userAnswer);
    const isCorrect = Math.abs(answer - currentProblem.answer) < 0.01;
    
    setScore(prev => ({
      correct: prev.correct + (isCorrect ? 1 : 0),
      total: prev.total + 1
    }));
    
    if (isCorrect) {
      setFeedback('正解！');
    } else {
      setFeedback(`不正解。正解は ${currentProblem.answer}cm です。`);
    }
    
    setShowAnswer(true);
  };

  const handleTimeUp = () => {
    setIsTimerActive(false);
    setScore(prev => ({
      correct: prev.correct,
      total: prev.total + 1
    }));
    setFeedback(`時間切れ！正解は ${currentProblem.answer}cm です。`);
    setShowAnswer(true);
  };

  const reset = () => {
    setScore({ correct: 0, total: 0 });
    setIsTimerActive(false);
    generateProblem();
  };

  // タイマーのuseEffect
  useEffect(() => {
    let interval;
    if (isTimerActive && timeLeft > 0) {
      interval = setInterval(() => {
        setTimeLeft(prev => {
          if (prev <= 1) {
            handleTimeUp();
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }
    return () => clearInterval(interval);
  }, [isTimerActive, timeLeft]);

  useEffect(() => {
    generateProblem();
  }, []);

  if (!currentProblem) return <div>読み込み中...</div>;

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-lg shadow-lg">
      <div className="text-center mb-6">
        <h1 className="text-3xl font-bold text-blue-600 mb-2 flex items-center justify-center gap-2">
          <BookOpen className="w-8 h-8" />
          三平方の定理 練習問題
        </h1>
        <div className="text-lg text-gray-600">
          正解数: {score.correct}/{score.total}
          {score.total > 0 && (
            <span className="ml-2 text-blue-500">
              ({Math.round(score.correct / score.total * 100)}%)
            </span>
          )}
        </div>
        
        {/* タイマー表示 */}
        <div className="mt-4">
          <div className={`text-2xl font-bold ${
            timeLeft <= 5 ? 'text-red-500' : timeLeft <= 10 ? 'text-orange-500' : 'text-green-500'
          }`}>
            残り時間: {timeLeft}秒
          </div>
          <div className="w-full bg-gray-200 rounded-full h-2 mt-2">
            <div 
              className={`h-2 rounded-full transition-all duration-1000 ${
                timeLeft <= 5 ? 'bg-red-500' : timeLeft <= 10 ? 'bg-orange-500' : 'bg-green-500'
              }`}
              style={{ width: `${(timeLeft / 30) * 100}%` }}
            />
          </div>
        </div>
      </div>

      <div className="bg-blue-50 p-6 rounded-lg mb-6">
        <div className="text-lg font-medium mb-4 text-gray-800">
          {currentProblem.question}
        </div>
        
        {currentProblem.type === 'hypotenuse' ? (
          <div className="text-sm text-gray-600 mb-4">
            公式: c² = a² + b² → c = √(a² + b²)
          </div>
        ) : (
          <div className="text-sm text-gray-600 mb-4">
            公式: a² = c² - b² → a = √(c² - b²)
          </div>
        )}

        <div className="flex items-center gap-4">
          <input
            type="number"
            value={userAnswer}
            onChange={(e) => setUserAnswer(e.target.value)}
            placeholder="答えを入力"
            className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            disabled={showAnswer}
          />
          <span className="text-gray-600">cm</span>
        </div>

        <div className="mt-4 flex gap-2">
          <button
            onClick={checkAnswer}
            disabled={!userAnswer || showAnswer || !isTimerActive}
            className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:bg-gray-300 disabled:cursor-not-allowed"
          >
            答え合わせ
          </button>
          
          <button
            onClick={generateProblem}
            className="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600"
          >
            次の問題
          </button>
        </div>
      </div>

      {feedback && (
        <div className={`p-4 rounded-lg mb-4 flex items-center gap-2 ${
          feedback.includes('正解') 
            ? 'bg-green-100 text-green-800' 
            : feedback.includes('時間切れ')
            ? 'bg-orange-100 text-orange-800'
            : 'bg-red-100 text-red-800'
        }`}>
          {feedback.includes('正解') ? (
            <CheckCircle className="w-5 h-5" />
          ) : (
            <XCircle className="w-5 h-5" />
          )}
          {feedback}
        </div>
      )}

      {showAnswer && (
        <div className="bg-gray-50 p-4 rounded-lg mb-4">
          <div className="font-medium text-gray-800 mb-2">解説:</div>
          <div className="text-gray-600 text-sm">
            {currentProblem.hint}
          </div>
        </div>
      )}

      <div className="flex justify-center">
        <button
          onClick={reset}
          className="flex items-center gap-2 px-4 py-2 text-gray-600 hover:text-gray-800"
        >
          <RotateCcw className="w-4 h-4" />
          スコアリセット
        </button>
      </div>

      <div className="mt-6 p-4 bg-yellow-50 rounded-lg">
        <div className="text-sm text-gray-700">
          <strong>覚えておくと便利な直角三角形:</strong>
          <ul className="mt-2 space-y-1">
            <li>• 3-4-5の三角形（とその倍数：6-8-10, 9-12-15など）</li>
            <li>• 5-12-13の三角形</li>
            <li>• 8-15-17の三角形</li>
            <li>• 7-24-25の三角形</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default PythagoreanQuiz;