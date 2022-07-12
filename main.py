import random
import time


# File name: New_Eng.py
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

"""

# Getting data from file
filename='./eng, summary, temp.txt'
s = open(filename).read()
lines = [line.strip() for line in open(filename)]

print(lines)

num=[]
column1=[]
column2=[]
column3=[]
column4=[]
column5=[]
word_list=[]
word_meaning=[]
example_list=[]
example_meaning=[]
real_example=[]


for i in range (0,len(lines)):
    num.append(i)
    line=lines[i].split(chr(9))
    column1.append(line[1])
    column2.append(line[0])
    column3.append(line[3])
    column4.append(line[2])
    column5.append(line[4])

word_list=column4
word_meaning=column3
example_list=column1
example_meaning=column2
real_example=column5

"""


word_list=[]
word_meaning=[]
example_list=[]
example_meaning=[]
real_example=[]
word_list = ['уму непостижимо', 'журнальная/ багажная полка', 'мучиться от боли/чувства вины и т. д.', 'ломать себе голову', 'раздобыть, добиться, наделать', 'вешалка для полотенец', 'полка для верхней одежды', 'яма для барбекю', 'дурное предчувствие', 'приспособление', 'мед. учреждение', 'возвращаться к чему-либо ', 'изменение порядка, возвращение к прежнему состоянию', 'размалывать кофе', 'измельчитель кофе', 'точильный камень ', 'скрежетать зубами', 'мучить, изводить', 'ежедневная изнурительная работа', 'смять сигаретный окурок в перелнице', 'застопориться / остановиться', 'переходить к делу/ к сути', 'в полнейшем беспорядке', 'товар', 'Его признали невиновным (на суде)', 'Он/она взмолилась', 'молить о пощаде/ жалости / сострадании', 'ссылаться не неосведомленность', 'защищать кого-либо/чьи-либо интересы в суде', 'показать/ проявить смелость в сложной ситуации', 'перед лицом сложной ситуации', 'тележка в супермаркете', 'тележка для багажа', 'трамвай', 'не в себе, помешанный, спятивший', 'совершенно безумный', 'колокольня', 'глупая идея', 'коллектив', 'харизма, притягательная сила', 'харизматический, притягательный', 'пятна краски', 'прилежный / усердный сдудент', 'раскаиваться', 'быть искреннее раскаявшимся', 'промокать (тряпочкой, промокашкой)', 'стирать / вычеркивать из памяти воспоминания', 'заслонять солнце', 'чернильные пятна', 'пятно на репутации', 'еда на вынос', 'обновлять / подписывать / брать в аренду', 'аренда ч-л', 'подписать 3-х годичный контракт об аренде', 'возродить надежду, возвратить жизненные силы', 'взять в аренду офисное пространство', 'предоставить землю в аренду ', 'киль', 'падать (в обморок)', 'водопроводчик', 'водопровод', 'существует огромное кол-во слухов / слухи множатся', 'после 2-х лет застоя', 'фондовый рынок находится в состоянии застоя', 'хандрить', 'полагаться на себя, заботиться о себе', 'смочь отбиться от нападающих / грабителей', 'парировать вопросы', 'крыло автомобиля', 'удариться головой о дверь', 'налетать на что-либо', 'налетать на дерево', 'Не ударься / не ушиби голову!', 'трястись (в транспорте)', 'трястись по грязной дороге', 'наткнуться на старого школьного друга', 'прибить / грохнуть жену', 'налететь на ухаб', 'выступ / ухаб на дороге', 'шишка на голове', 'услышать глухой удар', 'передний/ задний трафик', 'быть таким же мертвым, как додо', 'принижать, умалять (заслуги, достоинство)', 'делать уничижительные / пренебрежительные комментарии / замечание', 'теленок', 'икра (ноги)', 'садиться к к-л на колени', 'круг беговой дорожки', 'клевер', 'бросать игральный кубик', 'наслаждатьсясооей ролью в качестве', 'наслаждаться вниманием с ч-л стороны', 'всовывать письмо в руку', 'навязывать отцовство к-л', 'заскулить от боли', 'запутанный аргумент история', 'длинные, запутанные выражения', 'право на бесплатное медицинское обслуживание', 'подчиняться инструкциям', 'в соотвествиии с нормами', 'не подчиняться закону', 'соответствие закону', 'оценить результаты', 'оценка новых хирургических методов', 'оценка психического состояния', 'оценочный вопрос', 'результаты исследования будут подтверждены', 'утверждение, подтверждение', 'встречаться по мере необходимости', 'комитет, собираюзийся по мере необходимости', 'группа студентов', 'Группами/ партиями', 'букет цветов', 'множество мест', 'задавать к-л кучу вопросов', 'быть лучшим из группы', 'недомогание', 'расцеплять, разъединять', 'приманка', 'перестать хвастаться ч-л', 'хвастать тем, что', '', 'предположение', 'вошь', 'отопление, вентиляция и кондиционирование воздуха', 'не предвидеть никаких проблем', 'Он представляет себе Америку где…', 'военный летчик']
word_meaning = ['the mind boggles / it boggles the mind', 'a magazine/luggage rack', 'to be racked with pain/guilt, etc', 'to rack your brain/brains', 'to rack up sth', '? towel ? rail / rack', 'a coat rack', 'a barbecue pit', 'a sense of foreboding', 'facility', 'medical facility', 'to revert to sth/doing sth', 'reversion', 'to grind coffee', 'a coffee grinder', 'a stone for grinding knives and scissors', 'to grind your teeth', 'to grind sb down', 'the daily grind', 'to grind a cigarette butt into the ashtray', 'to grind to a halt', 'to cut to the chase', 'in complete disarray', 'commodity', 'He pleaded not guilty to', 'he/she pleaded (with)', 'to plead for mercy', 'to plead ignorance', "to plead sb's case/cause", 'to show courage in adversity', 'in the face of adversity', 'a supermarket trolley', 'a luggage trolley', 'trolley', 'off your trolley', 'as mad as a hatter', 'belfry', 'daft idea', "collective [k?'lekt?v], group, body", 'сharisma / k??r?zm? /', 'charismatic', 'flecks of paint', 'a diligent student', 'repent', 'to be sincerely repentant', 'blot', 'to blot out memories of', 'blots out the sun', 'ink blots', 'blot on reputation', 'takeaway', 'renew / sign / take a lease', 'a lease of / on sth', 'to sign a three-year lease', 'give sb/sth a new lease of life', 'to lease some office space', 'to lease the land to a local company', 'keel', 'keel over', 'plumber', 'plumbing', 'rumours abound about …', 'after two years in the doldrums', 'the stock market is in the doldrums', 'in the doldrums / ?d?ldr?mz /', 'fend for yourself', 'to managed to fend off attackers / muggers', 'to fend off questions about', 'fender', 'to bump one’s head on the door', 'bump into/against sth', 'to bump into a tree', 'Don’t bump your head!', 'bump along/over sth', 'to bump along the dirt road', 'to bumped into an old school friend', "to bump off one's wife", 'to hit a bump', 'a bump in the road', 'a bump on the head', 'to hear a bump', 'a front/rear bumper', 'to be (as) dead as a/the dodo', "derogate ['der?uge?t]", 'to make derogatory comments/remarks', 'calf / k??f /, calves / k??vz /', 'calf / k??f /', 'to sit on one’s lap', 'to be two laps behind …', 'clover / ?kl??v? r /', 'Roll the dice', 'to revel in one’s role as', 'to revel in one’s attention', 'to thrust a letter into one’s hand', 'to thrust fatherhood on smb', 'to whimper with pain', 'a convoluted argument/story', 'long convoluted sentences', 'an entitlement to free medical care', 'to comply with instructions', 'in compliance with regulations', 'to fail to comply with the law', 'сompliance with the law', 'to evaluate the results', 'an evaluation of new surgical techniques', 'a psychological evaluation', 'evaluative question', 'the results of the study will be validated by', 'validation', 'to meet on an ad hoc basis', 'an ad hoc committee', 'batch of students', 'in batches', 'a bunch of flowers', 'a whole bunch of places', 'to ask smb. a bunch of questions', 'is the best of the bunch', 'malaise', 'decouple', 'decoy', 'to stop boasting about', 'to boast that', '', 'supposition', 'louse', 'HVAC', "don't envisage any trouble", 'He envisions an America where …', 'airman']
example_list = ['the mind boggles / it boggles the mind', 'rack', 'be racked with pain/guilt, etc', 'rack your brain/brains', 'rack up sth', '? towel ? rail / rack', 'a coat rack', 'pit', 'foreboding', 'facility', 'facility', 'revert to sth/doing sth', 'reversion', 'grind', 'grind', 'grind', 'grind your teeth', 'grind sb down', 'grind', 'grind', 'grind to a halt', 'cut to the chase', 'disarray', 'commodity', 'plead', 'plead', 'plead', 'plead', "plead sb's case/cause", 'adversity', 'adversity', 'trolley', 'trolley', 'trolley', 'off your trolley', 'as mad as a hatter', 'belfry', 'daft', "collective [k?'lekt?v], group, body", 'сharisma / k??r?zm? /', 'charismatic', 'fleck', 'diligence', 'repent', 'repentance', 'blot', 'blot sth out', 'blot', 'blot', 'a blot on sth', 'takeaway', 'renew / sign / take a lease', 'a lease of / on sth', 'lease  / li?s /', 'give sb/sth a new lease of life', 'lease / li?s /', 'lease / li?s /', 'keel', 'keel over', 'plumber', 'plumbing', 'abound', 'in the doldrums / ?d?ldr?mz /', 'in the doldrums / ?d?ldr?mz /', 'in the doldrums / ?d?ldr?mz /', 'fend for yourself', 'fend sb/sth off', 'fended off questions about', 'fender', 'bump', 'bump into/against sth', 'bump into/against sth', 'bump', 'bump along/over sth', 'bump along/over sth', 'bump into sb', 'bump sb off', 'bump', 'bump', 'bump', 'bump', 'bumper', "dodo ['d?ud?u]", "derogate ['der?uge?t]", 'derogatory', 'calf / k??f /, calves / k??vz /', 'calf / k??f /', 'lap / l?p /', 'lap / l?p /', 'clover / ?kl??v? r /', 'dice', 'revel in sth / ?rev ? l /', 'revel in sth / ?rev ? l /', 'thrust sth behind/into/through, etc', 'thrust sth on/upon sb', 'whimper', 'convoluted', 'convoluted', 'entitlement', 'comply', 'compliance', 'comply', 'compliance', 'evaluate', 'evaluation', 'evaluation', '-', 'validate', 'validation', 'ad hoc', 'ad hoc', 'batch', 'batch', 'bunch', 'a bunch of sth', 'a bunch of sth', 'bunch', 'malaise', 'decouple', 'decoy', 'boast', 'boast', 'boast', 'supposition', 'louse', 'HVAC', 'envisage', 'envision', 'airman']
example_meaning = ['the mind boggles / it boggles the mind', 'полка, вешалка, стойка', 'be racked with pain/guilt, etc', 'rack your brain/brains', 'rack up sth', 'вешалка для полотенец', 'полка для верхней одежды', 'яма', 'дурное предчувствие', 'приспособление', 'учреждение', 'возвращаться к чему-либо ', 'изменение порядка, возвращение к прежнему состоянию', 'молоть, размалывать', 'молоть, размалывать', 'точить, оттачивать ', 'скрежетать зубами', 'мучить, изводить', 'изнурительная, однообразная работа', 'молоть, размалывать', 'застопориться / остановиться', 'переходить к делу/ к сути', 'беспорядок', 'товар', '(не) признавать себя виновным (на суде)', 'умолять', 'умолять', 'оправдываться, ссылаться на что-либо', 'защищать кого-либо/чьи-либо интересы в суде', 'трудность, напасть', 'трудность, напасть', 'тележка', 'тележка', 'трамвай', 'не в себе, помешанный, спятивший', 'совершенно безумный', 'колокольня', 'глупый', 'коллектив', 'харизма, притягательная сила', 'харизматический, притягательный', 'пятнышко, крапинка', 'усердие ', 'раскаиваться', 'раскаяние', 'промокать (тряпочкой, промокашкой)', 'стирать, вычеркивать из памяти', 'заслонять', 'пятно, клякса', 'пятно', 'еда на вынос', 'обновлять / подписывать / брать в аренду', 'аренда ч-л', 'контракт об аренде', 'возродить надежду, возвратить жизненные силы', 'сдавать/брать в аренду', 'сдавать/брать в аренду', 'киль', 'падать (в обморок)', 'водопроводчик', 'водопровод', 'существовать в большом количестве', 'период застоя', 'период застоя', 'хандрить', 'полагаться на себя, заботиться о себе', 'отражать, парировать', 'парировать вопросы', 'крыло автомобиля', 'ударять(ся)', 'налетать на что-либо', 'налетать на что-либо', 'ударять(ся)', 'трястись (в транспорте)', 'трястись (в транспорте)', 'натыкаться на к-л', 'убить, грохнуть', 'ухаб', 'ухаб', 'шишка (от удара)', 'глухой удар', 'бампер', 'дронт, додо', 'принижать, умалять (заслуги, достоинство)', 'уничижительный, пренебрежительный', 'теленок', 'икра (ноги)', 'колени (сидящего человека)', 'круг беговой дорожки', 'клевер', 'кубик для игры', 'наслаждаться ч-л', 'наслаждаться ч-л', 'засовывать/всовывать/просовывать что-либо', 'навязывать ч-л к-л', 'хныкать, скулить', 'запутанный', 'запутанный', 'право', 'исполнять, подчиняться', 'согласие', 'исполнять, подчиняться', 'согласие', 'оценивать, определять (качество, количество и т. д.)', 'оценка, определение (качества, количества и т. д.)', 'оценка, определение (качества, количества и т. д.)', '-', 'признавать действительным, подтверждать', 'утверждение, подтверждение', 'по мере необходимости', 'по мере необходимости', 'партия, группа', 'партия, группа', 'связка, пучок, букет', 'множество', 'множество', 'связка, пучок, букет', 'недомогание', 'расцеплять, разъединять', 'приманка', 'хвастаться', 'хвастаться', 'славиться', 'предположение', 'вошь', 'отопление, вентиляция и кондиционирование воздуха', 'представлять себе, предвидеть ', 'представлять себе, предвидеть', 'военный летчик']
real_example = ['The mind boggles at the stupidity of some people. / The paperwork you have to fill out just boggles the mind.', '-', 'Afterwards, he was racked with guilt and shame.', '-', "He's racked up debts of over thirty thousand pounds. / They racked up a nine-game winning streak.", '-', '-', '-', 'We waited for news of the men with a sense of foreboding.', 'This phone has a memory facility.', 'a new medical facility', 'For a while I ate low-fat food but then I reverted to my old eating habits. / For a while I ate low-fat food but then I reverted to my old eating habits.', '-', 'Could you grind some coffee for me?', '-', '-', '-', 'Living alone in London really ground me down.', 'The work has become a grind to them.', 'He paused and ground his cigarette butt into the ashtray.', 'If something grinds to a halt, it stops moving or making progress: Traffic slowly ground to a halt', '-', 'The house was in complete disarray . / papers in disarray on the desk', '-', 'He pleaded not guilty to five felony charges.', '"You must believe me!"" she pleaded. / He pleaded with her to come back."', '-', "You'll just have to plead ignorance (= say you did not know) .", '-', 'She showed a great deal of courage in adversity .', 'We remained hopeful in the face of adversity.', '-', '-', '-', '-', '-', '-', "That's a daft idea .", '-', '-', '-', 'His shirt was covered in flecks of paint. / a black beard with flecks of gray', '-', '-', 'His apology was sincerely repentant.', '-', "I've tried to blot out memories of my relationship with Dieter. / He tried to blot out the memory of that night.", 'If smoke or cloud blots out the sun, it prevents it from being seen / Black clouds blotted out the sun.', '-', 'The financial scandal was a blot on his reputation.', '-', '-', '-', 'We signed a three-year lease when we moved into the house.', 'The operation has given her a new lease of life.', 'We want to lease some office space in the centre of town.', 'The council eventually leased the land to a local company.', '-', 'He said he felt dizzy and then just keeled over. / Rob looked as if he were ready to keel over.', '-', '-', 'Rumours abound about a possible change of leadership.', 'After two years in the doldrums, profits are finally rising.', 'The stock market has been in the doldrums for most of this year.', '-', 'When you go away to college, you have to learn to fend for yourself. / You’ll have to fend for yourself while I’m gone.', 'They managed to fend off their attackers with rocks and sticks. / Mrs. Spector tried to fend off the other mugger', 'She fended off questions about her marriage.', '-', 'I bumped my head on the door.', 'He kept falling over and bumping into things.', 'It was so dark I bumped into a tree.', '-', 'The bus bumped along the country road.', 'We bumped along the dirt road.', 'I bumped into an old school friend in town today. / Guess who I bumped into this morning?', "The film's about a guy who tries to bump off his wife.", 'My bike hit a bump in the road.', '-', 'a nasty bump on the head / a bump on his head', 'I heard a bump upstairs. / The elevator stopped with a bump.', 'bumper-to-bumper traffic is very close together and moving slowly', 'to not be important or\xa0popular any longer (вымершая птица отряда голубеобразных, обитавшая на островах Индийского океана и истреблённая в 17-18 вв. завезёнными туда свиньями)', '-', 'He was constantly making derogatory remarks about women.', '-', '-', "Sit on my lap and I'll read you a story.", "He's two laps behind the leaders.", '-', 'Roll the dice to see who starts the game.', 'He revelled in his role as team manager.', 'Bobby reveled in my undivided attention.', 'She thrust a letter into my hand and told me to read it.', 'Fatherhood had been thrust on him.', 'The dog was whimpering with pain.', '-', 'He tends to use, which make the book difficult for the ordinary reader.', 'an employee’s entitlement to free medical care', 'The pilot complied with instructions to descend.', 'The work was done in compliance with planning regulations.', 'Those who fail to comply with the law will be fined.', 'Compliance with the law is expected of everyone.', 'a chance for students to evaluate teachers / Scientists are evaluating the results of the drug trials.', 'an evaluation of new surgical techniques', 'The child was sent for a psychological evaluation.', '-', 'It is hoped that the results of the study will be validated by future research.', '-', 'We meet on an ad hoc basis .', 'an ad hoc committee', 'She’s just baked another batch of cookies / a fresh batch of pancakes', '-', '-', "There's a whole bunch of places I'd like to visit. / There are a whole bunch of little restaurants by the beach.", 'The doctor asked me a bunch of questions. / a bunch of grapes', 'This beer is the best of the bunch.', "mal·aise [m?'le?z] n. [U] (formal) a feeling of anxiety, and a lack of confidence and satisfaction", '-', '/ ?di?k?? /', 'I wish she would stop boasting about her exam results. / Scott was boasting about winning the game.', '[ + that ] Liam boasted that he owned two sports cars.', 'New York boasts some of the best museums in the world. / if a place boasts something good, the place has it: The new athletic center boasts an Olympic-sized swimming pool.', '/ ?s?p??z?? ? n /', '-', 'HVAC - Heating, Ventilation, and Air Conditioning', "The police don't envisage any trouble at the festival.", 'envisage / ?n?v?z?d? / mainly UK ( mainly US envision / ?n?v?? ? n / ) verb [ T ] / He envisions an America where poor children have just as many opportunities as richer ones.', '-']
num=[]
for i in range(0,len(word_list)):
    num.append(i)


print('word_list = ', word_list)
print('word_meaning = ', word_meaning)
print('example_list = ', example_list)
print('example_meaning = ', example_meaning)
print('real_example = ', real_example)

global rand_num
global secret_num
global right_answers_stat
global wrong_answers_stat

right_answers_stat=0
wrong_answers_stat=0


def choose_combination():
    global rand_num
    global secret_num

    right_combination = False

    
    while right_combination==False:
        four_sample_words = []
        four_sample_meaning = []
        rand_num = random.choices(num, k=4)
        secret_num = random.choices(rand_num, k=1)


        for y in range (0,4):
            four_sample_words.append(word_list[rand_num[y]])
            four_sample_meaning.append(word_meaning[rand_num[y]])

        if len(set(four_sample_words)) == len(set(four_sample_meaning)) == 4:
            right_combination = True

            
    return (rand_num, secret_num)



class New_EngApp(App):
    global rand_num
    global secret_num
    global right_answer
    global real_example



    
    
    def build(self, btn1_txt='Answer 1', btn2_txt='Answer 2', btn3_txt='Answer 3', btn4_txt='Answer 4'):
     
        superBox = BoxLayout(orientation ='vertical') 

        q_label = Label(text = 'What is the right translation of this word?', font_size = 48)

        q_word_label = Label(text = 'WORD', font_size = 60, color = 'orange')

        o_text = TextInput(text='Examples:', readonly='True', foreground_color = 'blue', line_height = 1)

        statistics_label = Label(text= 'Statistics...')


        btn1 = Button(text = btn1_txt,
                    font_size = 72, 
                    size_hint =(1, 1))

        btn2 = Button(text = btn2_txt, 
                    font_size = 72, 
                    size_hint =(1, 1)) 

        btn3 = Button(text = btn3_txt, 
                    font_size = 72, 
                    size_hint =(1, 1)) 

        btn4 = Button(text = btn4_txt, 
                    font_size = 72, 
                    size_hint =(1, 1)) 

        btn_next = Button(text ="NEXT", 
                    font_size = 72, 
                    size_hint =(1, 1),
                    background_color = (0.8, 0.8, 0.8, 0.8))

        def change_text_btn1(btn1):
            btn1.text = '1 was Pressed'

        def change_text_btn2(btn2):
            btn2.text = '2 was Pressed'
            
        def change_text_btn3(btn3):
            btn3.text = '3 was Pressed'

        def change_text_btn4(btn4):
            btn4.text = '4 was Pressed'

        def new_q(self):
            new_question('1','2','3','4')

        def btn1_press(self):
            my_answer = 1
            check_result(my_answer)

        def btn2_press(self):
            my_answer = 2
            check_result(my_answer)

        def btn3_press(self):
            my_answer = 3
            check_result(my_answer)

        def btn4_press(self):
            my_answer = 4
            check_result(my_answer)

        def btn_next_press(self):
            new_question()
            
        btn1.bind(on_press=btn1_press)
        btn2.bind(on_press=btn2_press)
        btn3.bind(on_press=btn3_press)
        btn4.bind(on_press=btn4_press)   
        btn_next.bind(on_press=btn_next_press) 

        superBox.add_widget(q_label)
        superBox.add_widget(q_word_label)
        superBox.add_widget(btn1)
        superBox.add_widget(btn2)
        superBox.add_widget(btn3)
        superBox.add_widget(btn4)
        superBox.add_widget(btn_next)
        superBox.add_widget(o_text)
        superBox.add_widget(statistics_label)

        def new_question( btn1_txt='Answer 1', btn2_txt='Answer 2', btn3_txt='Answer 3', btn4_txt='Answer 4'):
            btn1.disabled = False
            btn2.disabled = False
            btn3.disabled = False
            btn4.disabled = False
            btn1.background_color = (1, 1, 1, 1)
            btn2.background_color = (1, 1, 1, 1)
            btn3.background_color = (1, 1, 1, 1)
            btn4.background_color = (1, 1, 1, 1)
            choose_combination()
            q_word_label.text = word_list[secret_num[0]] 
            btn1.text = word_meaning[rand_num[0]]  
            btn2.text = word_meaning[rand_num[1]] 
            btn3.text = word_meaning[rand_num[2]]  
            btn4.text = word_meaning[rand_num[3]]            
            o_text.text = 'Examples:'
            btn_next.disabled = True

        def show_statistics():
            statistics_label.text = 'Right Answers: ' + str(right_answers_stat) + '   ' + 'Wrong Answers: ' + str(wrong_answers_stat)
        def show_result(my_answer, right_answer):
            if right_answer != -1:
                if my_answer == 1:
                    btn1.background_color = (0, 200/255, 0, 1)
                    btn2.disabled = True
                    btn3.disabled = True
                    btn4.disabled = True
                elif my_answer == 2:
                    btn2.background_color = (0, 200/255, 0, 1)
                    btn1.disabled = True
                    btn3.disabled = True
                    btn4.disabled = True
                elif my_answer == 3:
                    btn3.background_color = (0, 200/255, 0, 1)
                    btn1.disabled = True
                    btn2.disabled = True
                    btn4.disabled = True
                else:
                    btn4.background_color = (0, 200/255, 0, 1)
                    btn1.disabled = True
                    btn2.disabled = True
                    btn3.disabled = True
                o_text.text = 'Examples: \n' + real_example[secret_num[0]]
                btn_next.disabled = False
                show_statistics()
            else:
                if my_answer == 1:
                    btn1.background_color = (1, 0, 0, 1)
                    btn2.disabled = True
                    btn3.disabled = True
                    btn4.disabled = True
                elif my_answer == 2:
                    btn2.background_color = (1, 0, 0, 1)
                    btn1.disabled = True
                    btn3.disabled = True
                    btn4.disabled = True
                elif my_answer == 3:
                    btn3.background_color = (1, 0, 0, 1)
                    btn1.disabled = True
                    btn2.disabled = True
                    btn4.disabled = True
                else:
                    btn4.background_color = (1, 0, 0, 1)
                    btn1.disabled = True
                    btn2.disabled = True
                    btn3.disabled = True
                o_text.text = 'Examples: \n' + real_example[secret_num[0]]
                btn_next.disabled = False
                show_statistics()

        def check_result(my_answer):
            global right_answers_stat
            global wrong_answers_stat
            right_answer = -1
            if rand_num[my_answer-1] == secret_num[0]:
                right_answer=my_answer        
                right_answers_stat += 1
                show_result(my_answer, right_answer)
            else:   
                wrong_answers_stat += 1
                show_result(my_answer, right_answer)
              
        new_question('1','2','3','4')

        return superBox
    
if __name__=="__main__":
    New_EngApp().run()

