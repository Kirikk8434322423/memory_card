from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QGroupBox, QHBoxLayout,QRadioButton, QPushButton, QLabel, QButtonGroup)
#привязка элементов к вертикальной линии
from random import shuffle
from random import randint
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question('Фамилия Маши', ' Татаринова','Пушкина','Алгоритмиковна' ,'class Question'))
question_list.append(Question('Как зовут Машу', 'Мария','Евгений','Антон','Кирилл'))
question_list.append(Question('Корень из 169', '13','644','6' ,'11'))
question_list.append(Question('Площадь параллелограмма', 'S = a·h','S = P· h','d=B^2-4AC','все стороны перемножить на основание'))
question_list.append(Question('Во скольких странах работает Алгоритмика', 'в более 90 странах','в более 20 странах','в более 100 странах','В Тюмени только'))
app = QApplication([] )#Конструктор,создающий объект типа 'Приложение'
#обработка событий

main_win = QWidget()#Конструктор,создающий объект типа 'окно'
main_win.setWindowTitle('Memo Card')#сделать надпись для окна
main_win.move(40, 20) #координаты появления экрана
#запуск приложения
main_win.resize(40,150) #размер экрана
text = QLabel('Во скольких странах работает Алгоритмика')#Надпись

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('в 20 странах')
rbtn_2 = QRadioButton('в более 30 странах')
rbtn_3 = QRadioButton('в более 90 странах')
rbtn_4 = QRadioButton('в более 130 странах')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
button = QPushButton('Ответить')

AnsGroupBox = QGroupBox('результат теста')
result = QLabel('Правильно/Неправильно')
itog = QLabel('Правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(itog)
AnsGroupBox.setLayout(layout_res)


AnsGroupBox.hide
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line2.addWidget(RadioGroupBox, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
line3.addWidget(button)
glav = QVBoxLayout()
glav.addLayout(line1)
glav.addLayout(line2)
glav.addLayout(line3)
main_win.setLayout(glav)
AnsGroupBox.hide()
line2.addWidget(AnsGroupBox)

def show_result(): 
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


        
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text.setText(q.question)#вопрос
    itog.setText(q.right_answer)
    show_question()#функции с панелью

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика: \n Всего вопросов:' , main_win.total, '\n Правильных ответов:', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total * 100), '%')
    else:   

        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг: ', (main_win.score/main_win.total * 100), '%')
def next_question():
    main_win.total += 1
    print('Статистика: \n Всего вопросов:' , main_win.total, '\n Правильных ответов:', main_win.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q) #cпросили

# ask(q)

def click_ok():
    if button.text()=='Ответить':
        check_answer()
    else:
        next_question()

button.clicked.connect(click_ok)
main_win.score = 0

main_win.total = 0
next_question()
main_win.show() #сделать окно видимым(по умолчанию скрыто)

main_win.cur_question = -1 #создали номер вопрорса
app.exec_()





 #оставлять окно открытым.пока не буде нажата кнопка выхода.
