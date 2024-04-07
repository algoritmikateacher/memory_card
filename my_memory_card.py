from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QLabel, QPushButton, QButtonGroup

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])
window = QWidget()
window.setWindowTitle('!MEMORY CARD!')
window.resize(500, 300)

question_label = QLabel('На каком игровом движке был разработан Genshin Impact?')
rbutton1 = QRadioButton('Unreal Engine')
rbutton2 = QRadioButton('Unity')
rbutton3 = QRadioButton('Frostbite')
rbutton4 = QRadioButton('Godot')
answer_button = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')
radio_hline = QHBoxLayout()
radio_hline.addWidget(rbutton1, alignment=Qt.AlignHCenter)
radio_hline.addWidget(rbutton2, alignment=Qt.AlignHCenter)
radio_hline2 = QHBoxLayout()
radio_hline2.addWidget(rbutton3, alignment=Qt.AlignHCenter)
radio_hline2.addWidget(rbutton4, alignment=Qt.AlignHCenter)
radio_vline = QVBoxLayout()
radio_vline.addLayout(radio_hline)
radio_vline.addLayout(radio_hline2)
RadioGroupBox.setLayout(radio_vline)
#RadioGroupBox.hide()

AnsGroupBox = QGroupBox('Результат теста')
rw = QLabel('Правильно/неправильно')
answer_label = QLabel('Здесь будет правильный ответ')
ans_vline = QVBoxLayout()
ans_vline.addWidget(rw, alignment=(Qt.AlignTop | Qt.AlignLeft))
ans_vline.addWidget(answer_label, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(ans_vline)
AnsGroupBox.hide()

vline = QVBoxLayout()
vline.addWidget(question_label, alignment=Qt.AlignCenter)
vline.addStretch(1)
vline.addWidget(RadioGroupBox)
vline.addWidget(AnsGroupBox)
vline.addWidget(answer_button, alignment=Qt.AlignCenter, stretch=3)

stats = QGroupBox('Статистика')
right_label = QLabel('Правильные ответы: 0')
total_label = QLabel('Всего вопросов: 1')
stats_line = QVBoxLayout()
stats_line.addWidget(right_label, alignment=Qt.AlignLeft)
stats_line.addWidget(total_label, alignment=Qt.AlignLeft)
stats.setLayout(stats_line)
vline.addWidget(stats)

window.setLayout(vline)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbutton1)
RadioGroup.addButton(rbutton2)
RadioGroup.addButton(rbutton3)
RadioGroup.addButton(rbutton4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer_button.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    answer_button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbutton1.setChecked(False)
    rbutton2.setChecked(False)
    rbutton3.setChecked(False)
    rbutton4.setChecked(False)
    RadioGroup.setExclusive(True)

from random import shuffle
answers = [rbutton1, rbutton2, rbutton3, rbutton4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_label.setText(q.question)
    answer_label.setText(q.right_answer)
    show_question()

def show_correct(res):
    rw.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика')
        right_label.setText('Правильные ответы: ' + str(window.score))
        total_label.setText('Всего вопросов:' + str(window.total))
        print('Рейтинг:', window.score / window.total * 100, '%')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct('Неправильно!')

from random import randint
def next_question():
    window.total += 1
    print('Статистика')
    right_label.setText('Правильные ответы: ' + str(window.score))
    total_label.setText('Всего вопросов:' + str(window.total))
    print('Рейтинг:', window.score / window.total * 100, '%')
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if answer_button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

question_list = list()
question_list.append(Question('Сколько лет Даничу?', '12 лет', '3 годика', '7 лет', '46 лет'))
question_list.append(Question('Сколько лет Даничу?', '12 лет', '3 годика', '7 лет', '46 лет'))
question_list.append(Question('Сколько лет Даничу?', '12 лет', '3 годика', '7 лет', '46 лет'))
question_list.append(Question('Сколько лет Даничу?', '12 лет', '3 годика', '7 лет', '46 лет'))
question_list.append(Question('Сколько лет Даничу?', '12 лет', '3 годика', '7 лет', '46 лет'))

#window.cur_question = -1
answer_button.clicked.connect(click_OK)
window.total = 1
window.score = 0
window.show()
app.exec_()