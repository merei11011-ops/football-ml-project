Football Team Strength Prediction

Data Analysis & Machine Learning Final Project

📌 Project Overview

Бұл жоба футбол командаларының тактикалық көрсеткіштері негізінде
олардың күш деңгейін (әлсіз, орташа, күшті) болжауға арналған.

Жоба барысында деректерді талдаудың толық циклі орындалды:

деректерді зерттеу (EDA),

тазалау және алдын ала өңдеу,

feature engineering,

машиналық оқыту модельдерін құру,

нәтижелерді интерпретациялау.

Жобаның негізгі мақсаты — деректерге негізделген футбол аналитикасын
машиналық оқыту әдістері арқылы көрсету.

🎯 Problem Statement

Мәселе:
Футбол командаларының тактикалық параметрлеріне қарап,
олардың жалпы күш деңгейін автоматты түрде болжауға бола ма?

Тапсырма түрі:
🔹 Классификация (3 класс: Weak / Medium / Strong)

📂 Dataset Information

Датасет атауы: Team_Attributes.csv

Дерек көзі: Kaggle (European Soccer Database)

Жазбалар саны: 1458

Белгілер саны: 25+

Негізгі белгілер:

buildUpPlaySpeed

buildUpPlayPassing

chanceCreationPassing

chanceCreationCrossing

chanceCreationShooting

defencePressure

defenceAggression

defenceTeamWidth

🧠 Feature Engineering

Датасетте дайын overall рейтинг болмағандықтан,
жаңа агрегатталған белгілер жасалды:

attack_score – шабуыл сапасы

defence_score – қорғаныс сапасы

overall_custom – команданың жалпы деңгейі

Target айнымалысы:

team_strength (0 – Weak, 1 – Medium, 2 – Strong)

📊 Exploratory Data Analysis (EDA)

EDA барысында:

сипаттамалық статистикалар есептелді,

таралулар визуализацияланды,

белгілер арасындағы корреляциялар зерттелді.

Негізгі инсайттар:

Шабуыл және қорғаныс көрсеткіштері арасында оң байланыс бар

Қорғаныс параметрлері команданың тұрақтылығына қатты әсер етеді

Класстарды ажырату классификация үшін қолайлы

🧹 Data Preprocessing

Preprocessing кезеңінде:

пропущенные значения медиана арқылы толтырылды

выброс-тар IQR әдісімен өңделді

категориялық белгілер кодталды

деректерді жоймай тазалау стратегиясы қолданылды

🤖 Machine Learning Models

Үш түрлі модель салыстырылды:

Model	Accuracy
Logistic Regression	1.00
Decision Tree	0.71
Random Forest	0.90

🔹 Финалдық модель: Random Forest
🔹 Себебі: тұрақтылық, жалпылау қабілеті және интерпретация мүмкіндігі

📈 Model Evaluation

Финалдық модель бағаланды:

Accuracy

Precision

Recall

F1-score

Confusion Matrix

Feature Importance

Random Forest моделі барлық класстар бойынша
балансталған және сенімді нәтиже көрсетті.

📌 Results & Interpretation

Қорғаныс және шабуыл көрсеткіштері шешуші рөл атқарады

Модель футбол логикасына сәйкес нәтиже береді

Практикалық қолдануға жарамды

⚠️ Limitations

Матч нәтижелері мен ойыншылар статистикасы ескерілмеді

Уақыттық динамика (маусымдық өзгеріс) қосылмаған

Target айнымалысы feature engineering арқылы жасалды

🚀 Future Improvements

Match нәтижелерін қосу

Time-series модельдер қолдану

XGBoost / Neural Networks пайдалану

Кросс-валидацияны кеңейту

🛠️ Technologies Used

Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

Jupyter Notebook