import random
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


screen_coeff=Window.size[0]/800


        
"""

# Getting data from file
filename='C:/Users/mkozharov/AppData/Local/Programs/Python/Python38/Scripts/eng/eng-rus-new.txt'
s = open(filename).read()
lines = [line.strip() for line in open(filename)]


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



#word_list = ['уму непостижимо', 'журнальная/ багажная полка', 'мучиться от боли/чувства вины и т. д.', 'ломать себе голову', 'раздобыть, добиться, наделать', 'вешалка для полотенец', 'полка для верхней одежды', 'яма для барбекю', 'дурное предчувствие', 'приспособление', 'мед. учреждение', 'возвращаться к чему-либо ', 'изменение порядка, возвращение к прежнему состоянию', 'размалывать кофе', 'измельчитель кофе', 'точильный камень ', 'скрежетать зубами', 'мучить, изводить', 'ежедневная изнурительная работа', 'смять сигаретный окурок в перелнице', 'застопориться / остановиться', 'переходить к делу/ к сути', 'в полнейшем беспорядке', 'товар', 'Его признали невиновным (на суде)', 'Он/она взмолилась', 'молить о пощаде/ жалости / сострадании', 'ссылаться не неосведомленность', 'защищать кого-либо/чьи-либо интересы в суде', 'показать/ проявить смелость в сложной ситуации', 'перед лицом сложной ситуации', 'тележка в супермаркете', 'тележка для багажа', 'трамвай', 'не в себе, помешанный, спятивший', 'совершенно безумный', 'колокольня', 'глупая идея', 'коллектив', 'харизма, притягательная сила', 'харизматический, притягательный', 'пятна краски', 'прилежный / усердный сдудент', 'раскаиваться', 'быть искреннее раскаявшимся', 'промокать (тряпочкой, промокашкой)', 'стирать / вычеркивать из памяти воспоминания', 'заслонять солнце', 'чернильные пятна', 'пятно на репутации', 'еда на вынос', 'обновлять / подписывать / брать в аренду', 'аренда ч-л', 'подписать 3-х годичный контракт об аренде', 'возродить надежду, возвратить жизненные силы', 'взять в аренду офисное пространство', 'предоставить землю в аренду ', 'киль', 'падать (в обморок)', 'водопроводчик', 'водопровод', 'существует огромное кол-во слухов / слухи множатся', 'после 2-х лет застоя', 'фондовый рынок находится в состоянии застоя', 'хандрить', 'полагаться на себя, заботиться о себе', 'смочь отбиться от нападающих / грабителей', 'парировать вопросы', 'крыло автомобиля', 'удариться головой о дверь', 'налетать на что-либо', 'налетать на дерево', 'Не ударься / не ушиби голову!', 'трястись (в транспорте)', 'трястись по грязной дороге', 'наткнуться на старого школьного друга', 'прибить / грохнуть жену', 'налететь на ухаб', 'выступ / ухаб на дороге', 'шишка на голове', 'услышать глухой удар', 'передний/ задний трафик', 'быть таким же мертвым, как додо', 'принижать, умалять (заслуги, достоинство)', 'делать уничижительные / пренебрежительные комментарии / замечание', 'теленок', 'икра (ноги)', 'садиться к к-л на колени', 'круг беговой дорожки', 'клевер', 'бросать игральный кубик', 'наслаждатьсясооей ролью в качестве', 'наслаждаться вниманием с ч-л стороны', 'всовывать письмо в руку', 'навязывать отцовство к-л', 'заскулить от боли', 'запутанный аргумент история', 'длинные, запутанные выражения', 'право на бесплатное медицинское обслуживание', 'подчиняться инструкциям', 'в соотвествиии с нормами', 'не подчиняться закону', 'соответствие закону', 'оценить результаты', 'оценка новых хирургических методов', 'оценка психического состояния', 'оценочный вопрос', 'результаты исследования будут подтверждены', 'утверждение, подтверждение', 'встречаться по мере необходимости', 'комитет, собираюзийся по мере необходимости', 'группа студентов', 'Группами/ партиями', 'букет цветов', 'множество мест', 'задавать к-л кучу вопросов', 'быть лучшим из группы', 'недомогание', 'расцеплять, разъединять', 'приманка', 'перестать хвастаться ч-л', 'хвастать тем, что', '', 'предположение', 'вошь', 'отопление, вентиляция и кондиционирование воздуха', 'не предвидеть никаких проблем', 'Он представляет себе Америку где…', 'военный летчик']
#word_meaning = ['the mind boggles / it boggles the mind', 'a magazine/luggage rack', 'to be racked with pain/guilt, etc', 'to rack your brain/brains', 'to rack up sth', '? towel ? rail / rack', 'a coat rack', 'a barbecue pit', 'a sense of foreboding', 'facility', 'medical facility', 'to revert to sth/doing sth', 'reversion', 'to grind coffee', 'a coffee grinder', 'a stone for grinding knives and scissors', 'to grind your teeth', 'to grind sb down', 'the daily grind', 'to grind a cigarette butt into the ashtray', 'to grind to a halt', 'to cut to the chase', 'in complete disarray', 'commodity', 'He pleaded not guilty to', 'he/she pleaded (with)', 'to plead for mercy', 'to plead ignorance', "to plead sb's case/cause", 'to show courage in adversity', 'in the face of adversity', 'a supermarket trolley', 'a luggage trolley', 'trolley', 'off your trolley', 'as mad as a hatter', 'belfry', 'daft idea', "collective [k?'lekt?v], group, body", 'сharisma / k??r?zm? /', 'charismatic', 'flecks of paint', 'a diligent student', 'repent', 'to be sincerely repentant', 'blot', 'to blot out memories of', 'blots out the sun', 'ink blots', 'blot on reputation', 'takeaway', 'renew / sign / take a lease', 'a lease of / on sth', 'to sign a three-year lease', 'give sb/sth a new lease of life', 'to lease some office space', 'to lease the land to a local company', 'keel', 'keel over', 'plumber', 'plumbing', 'rumours abound about …', 'after two years in the doldrums', 'the stock market is in the doldrums', 'in the doldrums / ?d?ldr?mz /', 'fend for yourself', 'to managed to fend off attackers / muggers', 'to fend off questions about', 'fender', 'to bump one’s head on the door', 'bump into/against sth', 'to bump into a tree', 'Don’t bump your head!', 'bump along/over sth', 'to bump along the dirt road', 'to bumped into an old school friend', "to bump off one's wife", 'to hit a bump', 'a bump in the road', 'a bump on the head', 'to hear a bump', 'a front/rear bumper', 'to be (as) dead as a/the dodo', "derogate ['der?uge?t]", 'to make derogatory comments/remarks', 'calf / k??f /, calves / k??vz /', 'calf / k??f /', 'to sit on one’s lap', 'to be two laps behind …', 'clover / ?kl??v? r /', 'Roll the dice', 'to revel in one’s role as', 'to revel in one’s attention', 'to thrust a letter into one’s hand', 'to thrust fatherhood on smb', 'to whimper with pain', 'a convoluted argument/story', 'long convoluted sentences', 'an entitlement to free medical care', 'to comply with instructions', 'in compliance with regulations', 'to fail to comply with the law', 'сompliance with the law', 'to evaluate the results', 'an evaluation of new surgical techniques', 'a psychological evaluation', 'evaluative question', 'the results of the study will be validated by', 'validation', 'to meet on an ad hoc basis', 'an ad hoc committee', 'batch of students', 'in batches', 'a bunch of flowers', 'a whole bunch of places', 'to ask smb. a bunch of questions', 'is the best of the bunch', 'malaise', 'decouple', 'decoy', 'to stop boasting about', 'to boast that', '', 'supposition', 'louse', 'HVAC', "don't envisage any trouble", 'He envisions an America where …', 'airman']
#example_list = ['the mind boggles / it boggles the mind', 'rack', 'be racked with pain/guilt, etc', 'rack your brain/brains', 'rack up sth', '? towel ? rail / rack', 'a coat rack', 'pit', 'foreboding', 'facility', 'facility', 'revert to sth/doing sth', 'reversion', 'grind', 'grind', 'grind', 'grind your teeth', 'grind sb down', 'grind', 'grind', 'grind to a halt', 'cut to the chase', 'disarray', 'commodity', 'plead', 'plead', 'plead', 'plead', "plead sb's case/cause", 'adversity', 'adversity', 'trolley', 'trolley', 'trolley', 'off your trolley', 'as mad as a hatter', 'belfry', 'daft', "collective [k?'lekt?v], group, body", 'сharisma / k??r?zm? /', 'charismatic', 'fleck', 'diligence', 'repent', 'repentance', 'blot', 'blot sth out', 'blot', 'blot', 'a blot on sth', 'takeaway', 'renew / sign / take a lease', 'a lease of / on sth', 'lease  / li?s /', 'give sb/sth a new lease of life', 'lease / li?s /', 'lease / li?s /', 'keel', 'keel over', 'plumber', 'plumbing', 'abound', 'in the doldrums / ?d?ldr?mz /', 'in the doldrums / ?d?ldr?mz /', 'in the doldrums / ?d?ldr?mz /', 'fend for yourself', 'fend sb/sth off', 'fended off questions about', 'fender', 'bump', 'bump into/against sth', 'bump into/against sth', 'bump', 'bump along/over sth', 'bump along/over sth', 'bump into sb', 'bump sb off', 'bump', 'bump', 'bump', 'bump', 'bumper', "dodo ['d?ud?u]", "derogate ['der?uge?t]", 'derogatory', 'calf / k??f /, calves / k??vz /', 'calf / k??f /', 'lap / l?p /', 'lap / l?p /', 'clover / ?kl??v? r /', 'dice', 'revel in sth / ?rev ? l /', 'revel in sth / ?rev ? l /', 'thrust sth behind/into/through, etc', 'thrust sth on/upon sb', 'whimper', 'convoluted', 'convoluted', 'entitlement', 'comply', 'compliance', 'comply', 'compliance', 'evaluate', 'evaluation', 'evaluation', '-', 'validate', 'validation', 'ad hoc', 'ad hoc', 'batch', 'batch', 'bunch', 'a bunch of sth', 'a bunch of sth', 'bunch', 'malaise', 'decouple', 'decoy', 'boast', 'boast', 'boast', 'supposition', 'louse', 'HVAC', 'envisage', 'envision', 'airman']
#example_meaning = ['the mind boggles / it boggles the mind', 'полка, вешалка, стойка', 'be racked with pain/guilt, etc', 'rack your brain/brains', 'rack up sth', 'вешалка для полотенец', 'полка для верхней одежды', 'яма', 'дурное предчувствие', 'приспособление', 'учреждение', 'возвращаться к чему-либо ', 'изменение порядка, возвращение к прежнему состоянию', 'молоть, размалывать', 'молоть, размалывать', 'точить, оттачивать ', 'скрежетать зубами', 'мучить, изводить', 'изнурительная, однообразная работа', 'молоть, размалывать', 'застопориться / остановиться', 'переходить к делу/ к сути', 'беспорядок', 'товар', '(не) признавать себя виновным (на суде)', 'умолять', 'умолять', 'оправдываться, ссылаться на что-либо', 'защищать кого-либо/чьи-либо интересы в суде', 'трудность, напасть', 'трудность, напасть', 'тележка', 'тележка', 'трамвай', 'не в себе, помешанный, спятивший', 'совершенно безумный', 'колокольня', 'глупый', 'коллектив', 'харизма, притягательная сила', 'харизматический, притягательный', 'пятнышко, крапинка', 'усердие ', 'раскаиваться', 'раскаяние', 'промокать (тряпочкой, промокашкой)', 'стирать, вычеркивать из памяти', 'заслонять', 'пятно, клякса', 'пятно', 'еда на вынос', 'обновлять / подписывать / брать в аренду', 'аренда ч-л', 'контракт об аренде', 'возродить надежду, возвратить жизненные силы', 'сдавать/брать в аренду', 'сдавать/брать в аренду', 'киль', 'падать (в обморок)', 'водопроводчик', 'водопровод', 'существовать в большом количестве', 'период застоя', 'период застоя', 'хандрить', 'полагаться на себя, заботиться о себе', 'отражать, парировать', 'парировать вопросы', 'крыло автомобиля', 'ударять(ся)', 'налетать на что-либо', 'налетать на что-либо', 'ударять(ся)', 'трястись (в транспорте)', 'трястись (в транспорте)', 'натыкаться на к-л', 'убить, грохнуть', 'ухаб', 'ухаб', 'шишка (от удара)', 'глухой удар', 'бампер', 'дронт, додо', 'принижать, умалять (заслуги, достоинство)', 'уничижительный, пренебрежительный', 'теленок', 'икра (ноги)', 'колени (сидящего человека)', 'круг беговой дорожки', 'клевер', 'кубик для игры', 'наслаждаться ч-л', 'наслаждаться ч-л', 'засовывать/всовывать/просовывать что-либо', 'навязывать ч-л к-л', 'хныкать, скулить', 'запутанный', 'запутанный', 'право', 'исполнять, подчиняться', 'согласие', 'исполнять, подчиняться', 'согласие', 'оценивать, определять (качество, количество и т. д.)', 'оценка, определение (качества, количества и т. д.)', 'оценка, определение (качества, количества и т. д.)', '-', 'признавать действительным, подтверждать', 'утверждение, подтверждение', 'по мере необходимости', 'по мере необходимости', 'партия, группа', 'партия, группа', 'связка, пучок, букет', 'множество', 'множество', 'связка, пучок, букет', 'недомогание', 'расцеплять, разъединять', 'приманка', 'хвастаться', 'хвастаться', 'славиться', 'предположение', 'вошь', 'отопление, вентиляция и кондиционирование воздуха', 'представлять себе, предвидеть ', 'представлять себе, предвидеть', 'военный летчик']
#real_example = ['The mind boggles at the stupidity of some people. / The paperwork you have to fill out just boggles the mind.', '-', 'Afterwards, he was racked with guilt and shame.', '-', "He's racked up debts of over thirty thousand pounds. / They racked up a nine-game winning streak.", '-', '-', '-', 'We waited for news of the men with a sense of foreboding.', 'This phone has a memory facility.', 'a new medical facility', 'For a while I ate low-fat food but then I reverted to my old eating habits. / For a while I ate low-fat food but then I reverted to my old eating habits.', '-', 'Could you grind some coffee for me?', '-', '-', '-', 'Living alone in London really ground me down.', 'The work has become a grind to them.', 'He paused and ground his cigarette butt into the ashtray.', 'If something grinds to a halt, it stops moving or making progress: Traffic slowly ground to a halt', '-', 'The house was in complete disarray . / papers in disarray on the desk', '-', 'He pleaded not guilty to five felony charges.', '"You must believe me!"" she pleaded. / He pleaded with her to come back."', '-', "You'll just have to plead ignorance (= say you did not know) .", '-', 'She showed a great deal of courage in adversity .', 'We remained hopeful in the face of adversity.', '-', '-', '-', '-', '-', '-', "That's a daft idea .", '-', '-', '-', 'His shirt was covered in flecks of paint. / a black beard with flecks of gray', '-', '-', 'His apology was sincerely repentant.', '-', "I've tried to blot out memories of my relationship with Dieter. / He tried to blot out the memory of that night.", 'If smoke or cloud blots out the sun, it prevents it from being seen / Black clouds blotted out the sun.', '-', 'The financial scandal was a blot on his reputation.', '-', '-', '-', 'We signed a three-year lease when we moved into the house.', 'The operation has given her a new lease of life.', 'We want to lease some office space in the centre of town.', 'The council eventually leased the land to a local company.', '-', 'He said he felt dizzy and then just keeled over. / Rob looked as if he were ready to keel over.', '-', '-', 'Rumours abound about a possible change of leadership.', 'After two years in the doldrums, profits are finally rising.', 'The stock market has been in the doldrums for most of this year.', '-', 'When you go away to college, you have to learn to fend for yourself. / You’ll have to fend for yourself while I’m gone.', 'They managed to fend off their attackers with rocks and sticks. / Mrs. Spector tried to fend off the other mugger', 'She fended off questions about her marriage.', '-', 'I bumped my head on the door.', 'He kept falling over and bumping into things.', 'It was so dark I bumped into a tree.', '-', 'The bus bumped along the country road.', 'We bumped along the dirt road.', 'I bumped into an old school friend in town today. / Guess who I bumped into this morning?', "The film's about a guy who tries to bump off his wife.", 'My bike hit a bump in the road.', '-', 'a nasty bump on the head / a bump on his head', 'I heard a bump upstairs. / The elevator stopped with a bump.', 'bumper-to-bumper traffic is very close together and moving slowly', 'to not be important or\xa0popular any longer (вымершая птица отряда голубеобразных, обитавшая на островах Индийского океана и истреблённая в 17-18 вв. завезёнными туда свиньями)', '-', 'He was constantly making derogatory remarks about women.', '-', '-', "Sit on my lap and I'll read you a story.", "He's two laps behind the leaders.", '-', 'Roll the dice to see who starts the game.', 'He revelled in his role as team manager.', 'Bobby reveled in my undivided attention.', 'She thrust a letter into my hand and told me to read it.', 'Fatherhood had been thrust on him.', 'The dog was whimpering with pain.', '-', 'He tends to use, which make the book difficult for the ordinary reader.', 'an employee’s entitlement to free medical care', 'The pilot complied with instructions to descend.', 'The work was done in compliance with planning regulations.', 'Those who fail to comply with the law will be fined.', 'Compliance with the law is expected of everyone.', 'a chance for students to evaluate teachers / Scientists are evaluating the results of the drug trials.', 'an evaluation of new surgical techniques', 'The child was sent for a psychological evaluation.', '-', 'It is hoped that the results of the study will be validated by future research.', '-', 'We meet on an ad hoc basis .', 'an ad hoc committee', 'She’s just baked another batch of cookies / a fresh batch of pancakes', '-', '-', "There's a whole bunch of places I'd like to visit. / There are a whole bunch of little restaurants by the beach.", 'The doctor asked me a bunch of questions. / a bunch of grapes', 'This beer is the best of the bunch.', "mal·aise [m?'le?z] n. [U] (formal) a feeling of anxiety, and a lack of confidence and satisfaction", '-', '/ ?di?k?? /', 'I wish she would stop boasting about her exam results. / Scott was boasting about winning the game.', '[ + that ] Liam boasted that he owned two sports cars.', 'New York boasts some of the best museums in the world. / if a place boasts something good, the place has it: The new athletic center boasts an Olympic-sized swimming pool.', '/ ?s?p??z?? ? n /', '-', 'HVAC - Heating, Ventilation, and Air Conditioning', "The police don't envisage any trouble at the festival.", 'envisage / ?n?v?z?d? / mainly UK ( mainly US envision / ?n?v?? ? n / ) verb [ T ] / He envisions an America where poor children have just as many opportunities as richer ones.', '-']

"""


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

word_list = ['чтобы не, как бы не', 'детям требуется пообрение/ одобрение от родителей', 'фонд на непредвиденные случаи', 'план на непредвиденные случаи', 'быть способным поднять шум', 'быть ответственным за безопасность', 'обдумывать разные вещи', 'разоблачать, развенчивать', 'являться полной неразберихой', 'неумелый / неспособный в социальном плане', 'абсолютно не уметь шутить', 'неумело', 'неумение, неспособность', 'отказаться от своих обещаний', 'безрассудное/ неосторожное вождение', 'безрассудно, неосторожно', 'безрассудство, неосторожность', 'современная трактовка Шекспира', 'быть избегаемым коллегами', 'избегать публичности', 'событие спонсируется/ финансируется', 'финансирование', 'милосердный, сострадательный, полный сочувствия', 'читать Евангелие', 'психически неуравновешенный фанат/ поклонник', 'психически неуравновешенный преступник', 'шлепать детей', 'шлепнуть к-л', 'тянуть к-л за хвост', 'выдернуть шнур/ коннектор', 'снять ботинки', 'подтянуть/ натянуть носки', 'потянуть/ растянуть мышцу', 'выхватывать/ наставить пистолет/ нож на к-л', 'разрывать на куски', 'разносить в пух и прах, критиковать', 'разнимать, разрывать', 'дергать за рукав', 'автобус/ ТС отъезжает', 'кто-то отслупает/ отходит от кого-то', 'снести кинотеатр', 'подъехать к краю дороги', 'успешно завершить крупнейшую сделку', 'машина/ ТС отъехала', 'натянуть джинсы', 'машина выехала', 'подъехать к обочине и остановиться', 'выжить', 'взять себя в руки', 'машина притормозила/ остановилась', 'придвигать стул', 'я боюсь ч-л', 'я боюсь снова его встретить/ увидеть', 'я содрогаюсь при мысли, что могло бы произойти, если бы мы не …', 'превзойти друг друга в ч-л', 'превзойти себя', 'мародёрствовать, грабить, совершать набеги', 'хулиган', 'ему перерезали горло', 'резко снижать цены', 'глубокий порез, глубокая рана', 'косая черта', 'быть бдительным', 'бдительность', 'мусор, хлам', 'дрянь, халтура', 'разгромить (к-л место)', 'благосклонные комментарии', 'произвести очень благоприятное впечатление на к-л', 'благоприятные погодные условия', 'благоприятно', 'сильно/ отчаянно нуждаться в помощи/ питании', 'ситуация не такая серьезная/ ужасная как…', 'находиться в тяжелом/ отчаянном положении', 'спустить туалет', 'смывать, выбрасывать в туалет', 'покраснеть, зардеться', 'выманивать', 'этническая/ политическая/ семейная борьба', '(сходить и) принести очки/ ключ, др.', 'выручать столько-то денег на аукционе', 'быть притянутым за уши/ неправдоподобным', 'мелководье', 'неглубокая тарелка', 'мелководье', 'государственность', 'ситуация мрачная, …', 'будущее выглядит мрачным', 'место мрачное', 'унылый пейзаж', 'будущее выглядит унылым', 'унылый ноябрьский день', 'значительно продвигаться вперед', 'сделать незначительное продвижение в мирных переговорах', 'вертолет', 'быть дразненным одноклассниками', 'дразнить к-л из-за веса', '"опасное вещество; взрывчатый материал"', 'спасение', 'быть безнадежным, неисправимым', 'забеременеть', 'постигать', 'идея романа была задумана', 'достичь нижнего предела', 'их отношения достигли нижнего предела', 'самые низкие цены', 'получить порезы и синяки после падения с велосипеда', 'получить сильные ушибы/синяки', 'получить серьезные ушибы/ кровоподтеки', 'грач, ладья, жулик,\xa0мошенник', 'избалованный щенок', 'проиграть все свои сбережения', 'делать ставку', 'приводить в какое-либо состояние', 'потерять дар речи', 'плата за оказанные услуги', 'авария привела к тому что …', 'вынести справедливый вердикт', 'фанатик', 'НЛО означает / расшифровывается как …', 'партия выступает за …', 'Я этого не потерплю!', 'эти даты являются предварительными', 'человек с ножом', 'обладать большим влиянием', 'громоздкий объект', 'актеры поклонились после представления', 'мы склонили наши головы в молитве', 'уйти из политики', 'выбывать из предвыборной гонки', 'уступать общенственному давлению', 'склониться перед статуей Святой Марии', 'девочка с красным бантов в волосах', 'лук (оружие)', 'смычок', 'выдавать себя за полицейского', 'сделать ч-л изображение', 'пародист Элвиса', 'скольких гостей мы обслуживаем?', 'обслуживать ч-л свадьбу', 'клуб обслуживает детей в возрасте от X до Y', 'законодательство потворствует ч-л', 'газеты обслуживают бизнес-сообщество', 'гусеница', 'много покупателей, снщющих вокруг', 'шум большого города', 'быть полным людей', 'дебаты по вопросу привлекли внимание всей нации', 'нанять секретаря для …', 'участвовать', 'вовлечь к-л в диалог', 'бренчать ключами', 'торговый аппарат', 'ковбойский наряд', 'наряд/ одежда для вечеринки', 'сокращать расходы', 'новые законы по сокращению иммиграции', '"наращивать, расширять; увеличивать"', 'лужа', 'коллективный иммунитет', 'быть отстранным от власти в ходе гос. переворота', 'отстаивать свободу слова', 'туалет', 'избежать попадания в плен', 'уклоняться от уплаты налогов', 'суметь избежать попадания в полицию', 'избегать обсуждения вопроса/ проблемы', 'уклоняться от ответа', 'уклоняться от ответа', 'быть принужденным к подписанию соглашения', 'обвинить полицию в принуждении', 'быть принужденным к сокрытию наркотиков', 'крайние формы принуждения', 'принуждать к-л к женитьбе', 'страшное/ жуткое место/ дом', 'страшный/ жуткий старый дом', 'уголовный кодекс', 'женоненавистничество', 'выказывать/ демонстрировать пренебрежение к к-л / ч-л', 'пренебречь всеми предложениями', 'скрывать свое презрение к к-л', 'идеи были отвегрнуты', 'с презрением', 'выдавать деньги к-л', 'раздавать конфеты детям', 'многие годы жить на пособии по безработице', 'удерживать оплату до…', 'умолчать/удержать информацию от …', 'гнев, ярость', 'быть отмененным (о законе)', 'иметь хорошую осанку', 'в то время как, тогда как', 'волынка', 'американский лось', 'олень', 'уговаривать/склонять к-л сделать ч-л', 'подвергаться уговорам не делать ч-л', 'бороться с соблазном/искушением делать ч-л', 'деньги являются слишком большим искушением', 'заманчивое приглашение/ предложение', 'увлекательный/ захватывающий фильм', 'быть расположенным слушать', 'благосклонно относиться к идее', 'поддельный паспорт', 'развивать отношения/ дружбу', 'продвигаться вперед', 'притуплять, оглуплять, отуплять', 'упрямый человек', 'недостаточные/ скудные ресурсы', 'некачественные товары', 'халтурная работа/ обращение', 'политический переворот', 'приверженность', 'приверженец', '"комплексный; многоаспектный; многогранный"', 'форма правления, строй (общественный или государственный), устройство', 'оказывать давление на', 'напрягаться', 'лишать гражданских или избирательных прав', 'ненавидеть друг-друга', '"отвратительный; мерзкий, плохой, противный"', 'мастер, маэстро, мэтр, учитель ', 'фон, задник (the painted cloth at the back of a stage in a theatre)', 'история любви, происходящая на фоне войны', 'мнимый, предполагаемый', '"мечтательный; идеалистический; наивный; не от мира сего"', 'я должен повторить/п одчеркнуть, что…', 'юристы повторили/ подчеркнули, что…', 'повторение', 'вылечиться от болезни', 'оторваться от ч-л преследования', 'закоснелый, чёрствый, ожесточённый, упрямый', 'закоснелый, чёрствый, ожесточённый, упрямый', 'закоснелый, чёрствый, ожесточённый, упрямый']
word_meaning = ['lest', 'сhildren need encouragement from parents', 'a contingency fund', 'a contingency fund plan', 'to be liable to make a fuss', 'to be liable for the safety', 'to mull things over ', 'debunk', 'to be a complete shambles', 'socially inept', 'to be totally inept at telling jokes', 'ineptly', 'ineptitude', 'to backtrack on one’s promises', 'reckless driving', 'recklessly', 'recklessness', 'a modern-day version of Shakespeare', 'to be shunned by colleagues', 'to shun publicity', 'the event is sponsored by', 'sponsorship', 'merciful', 'to preach the gospel', 'deranged fan', 'a deranged criminal', 'to smack children', 'to give smb. a smack', 'to pull one’s tail', 'to pull the plug out', 'to pull off one’s boots', 'to pull up one’s socks', 'to pull a muscle', 'pull a gun/knife, etc on sb', 'pull sth apart', 'pull sth apart', 'pull sb/sth apart', 'to pull at one’s sleeve', 'bus/ vehicle pulls away', 'smb pulls away from someone', 'to pull down the cinema', 'to pull in at the side of the road', 'to pull off the biggest deal', 'the car/ vehicle pulled off', 'to pull on jeans', 'car pulled out', 'to pull over', 'to pull through', 'to pull oneself together', 'a car pulled up', 'to pull up a chair', "I'm dreading smth.", 'I dread seeing him again.', "I dread to think what could have happened if we hadn't …", 'to outdo each other with smth', 'to outdo yourself', 'to maraud', 'thug', 'his throat had been slashed', 'to slash prices', 'slash', 'slash', 'to be vigilant', 'vigilance', 'trash', 'trash', 'to trash the place', 'favourable comments', 'to make a very favourable impression on smb.', 'favourable weather conditions', 'favourably', 'to be in dire need of help/ food', 'the situation is not as dire as…', 'to be in dire straits', 'to flush a toilet', 'flush sth away/down/out, etc', 'flush', 'flush sb/sth out', 'ethnic/ political/ marital strife', 'to fetch glasses/ key, etc.', 'to fetch $X in the auction', 'to be pretty far-fetched', 'shallow water', 'a shallow dish', 'the shallows', 'statehood', 'situation is bleak', 'the future is looking bleak', 'the place is bleak', 'a bleak landscape ', 'the future seems bleak', 'a bleak November day', 'to make much headway in/with smth.', 'to make little headway in the peace talks', 'chopper', 'to be taunted by classmates', 'to taunt smb. about one’s weight', 'hazmat', 'redemption', 'to be beyond redemption', 'conceive', 'conceive', 'the idea for the novel was conceived', 'to hit/ reach rock bottom', 'their marriage had hit rock bottom', 'rock-bottom prices', 'to suffer cuts and bruises after falling off a bike', 'to be badly bruised', 'to suffer serious bruising', 'rook', 'a spoilt brat', 'to gamble away all one’s savings', 'gamble on sth', 'render', 'to be was rendered speechless', 'payment for services rendered', 'the accident rendered …', 'to render a fair verdict', 'zealot, fanatic', 'UFO stands for …', 'the party stands for smth.', "I won't stand for it!", 'these dates are provisional', 'a man wielding a knife', 'to wield a lot of influence', 'an unwieldy object', 'the actors bowed after the performance', 'we bowed our heads in prayer', 'to bow out of politics', 'to bowed out of the race', 'to bow to public pressure', 'to bow down before the statue of Mary', 'a girl with a red bow in her hair', 'bow', 'bow', 'impersonating a police officer', 'to an impersonation of smb.', 'an Elvis impersonator', 'How many are we catering for?', 'to be catering smb’s wedding', 'the club caters for children between X and Y', 'the legislation caters to smth.', 'newspapers cater to business people', 'caterpillar', 'a lots of shoppers bustling about', 'the bustle of the big city', 'to be bustling with people', 'the debate about … has engaged the whole nation', 'to engaged a secretary to deal with smth', 'engage in sth', 'to engage someone in conversation', 'to jangle one’s keys', 'vending machine', 'a cowboy outfit', 'an outfit for the party', 'to curtail spending', 'new laws to curtail immigration', 'ramp up', 'puddle', 'herd immunity', 'to be ousted from power by a military coup', 'to champione the cause of free speech', 'restroom', 'to evade capture', 'to evade paying tax', 'to manage to evade the police', 'to evade the issue', 'to evade the question', 'to avoid/ evade/ sidestep a question', 'to be coerced into signing the agreement', 'to accused the police of coercion', 'to be coerced into hiding the drugs', 'extreme forms of coercion', 'to coerce smb. into an arranged marriage', 'A spooky place / house', 'a spooky old house', 'penal code', 'misogyny', 'to show scorn for someone or smth.', 'to scorn all suggestions', 'to disguise one’s scorn for smb.', 'ideas were scorned by …', 'with scorn', 'to dole out money to smb.', 'to dole out candy to the kids', 'to be on the dole for years', 'to withhold payment until …', 'to withhold information from …', 'ire', 'to be repealed', 'to have good posture', 'whereas', 'bagpipes', 'moose', 'deer', 'to tempt smb. to do smth with smb.', 'to be tempted not to do smth.', 'to resisted the temptation to do smth.', 'the money is too great a temptation', 'a tempting invitation/offer', 'fascinating movie', 'to be disposed to listen', 'to be well disposed towards the idea', 'a forged passport', 'to forged friendship', 'to forge ahead with smth.', 'stultify', 'an obstinate man', 'scarce resources', 'shoddy goods', 'shoddy work/ treatment', 'political/ social upheaval', 'adherence', 'adherent', 'multifaceted', 'polity', 'to exerte pressure on smb.', 'to exert oneself', 'disfranchise (dis·en·fran·chised)', 'to detest each other', 'detestable', 'maitre', 'backdrop', 'a love story set against the backdrop of war', 'putative', 'starry-eyed', 'I must reiterate that …', 'lawyers reiterated that …', 'reiteration', 'to shake off the cold', 'shake sb off', 'obdurate', 'obdurate', 'obdurate']
example_list = ['lest', 'encouragement', 'contingency', 'contingency', 'be liable to do sth', 'liable', 'mull sth over', 'debunk', 'be a shambles', 'inept', 'inept', 'ineptly', 'ineptitude', 'backtrack', 'reckless', 'recklessly', 'recklessness', 'modern-day', 'shun', 'shun', 'sponsor', 'sponsorship', 'merciful', 'gospel', 'deranged', 'deranged', 'smack', 'smack', 'тянуть, тащить ', 'тянуть, тащить ', 'тянуть, тащить ', 'тянуть, тащить ', 'pull a muscle', 'pull a gun/knife, etc on sb', 'pull sth apart', 'pull sth apart', 'pull sb/sth apart', 'pull at sth', 'pull away', 'pull away', 'pull sth down', 'pull in/into sth', 'pull sth off', 'pull off', 'pull on sth', 'pull out', 'pull over', 'pull through', 'pull yourself together', 'pull up', 'pull up a chair', 'dread', 'dread', 'I dread to think', 'outdo', 'outdo', 'maraud', 'thug', 'slash', 'slash', 'slash', 'slash', 'vigilant', 'vigilance', 'trash', 'trash', 'trash', 'favourable', 'favourable', 'favourable', 'favourably', 'dire', 'dire', 'dire', 'flush', 'flush sth away/down/out, etc', 'flush', 'flush sb/sth out', 'strife', 'fetch', 'fetch', 'far-fetched', 'shallow', 'shallow', 'the shallows', 'statehood', 'bleak', 'bleak', 'bleak', 'bleak', 'bleak', 'bleak', 'make headway', 'make headway', 'chopper', 'taunt', 'taunt', 'hazmat', 'redemption', 'be beyond redemption', 'conceive', 'conceive', 'conceive', 'rock bottom', 'rock bottom', 'rock bottom', 'bruise', 'bruise', 'bruising', 'rook', 'brat', 'gamble', 'gamble on sth', 'render', 'render', 'render', 'render', 'render', 'zealot, fanatic', 'stand for sth', 'stand for sth', 'not stand for sth', 'provisional', 'wield', 'wield influence/power, etc', 'unwieldy', 'bow', 'bow', 'bow out', 'bow out', 'bow to sth/sb', 'bow down', 'bow', 'bow', 'bow', 'impersonate', 'impersonation', 'impersonator', 'cater', 'cater', 'cater for sb/sth', 'cater to sb/sth', 'cater to sb/sth', 'caterpillar', 'bustle', 'bustle', 'bustle with sth', 'engage', 'engage', 'engage in sth', 'engage sb in sth', 'jangle', 'vending machine', 'outfit', 'outfit', 'curtail', 'curtail', 'ramp up', 'puddle', 'herd immunity', 'oust', 'champion', 'restroom', 'evade', 'evade', 'evade', 'evade', 'evade', 'evade', 'coerce', 'coercion', 'coerce', 'coercion', 'coercion', 'spooky', 'spooky', 'penal code', 'misogyny', 'scorn', 'scorn', 'scorn', 'scorn', 'scorn', 'dole sth out', 'dole sth out', 'the dole', 'withhold', 'withhold', 'ire', 'repeal', 'posture', 'whereas', 'bagpipes', 'moose', 'deer', 'tempt', 'tempt', 'temptation', 'temptation', 'tempting', 'fascinating', 'be disposed to do sth', 'be favourably/well, etc disposed towards sth', 'forge', 'forge', 'forge ahead', 'stultify', 'obstinate', 'scarce', 'shoddy', 'shoddy', 'upheaval', 'adherence', 'adherent', 'multifaceted', 'polity', 'exert', 'exert yourself', 'disfranchise (dis·en·fran·chised)', 'detest', 'detestable', 'maitre', 'backdrop', 'backdrop', 'putative', 'starry-eyed', 'reiterate', 'reiterate', 'reiteration', 'shake sth off', 'shake sb off', 'obdurate', 'obdurate', 'obdurate']
example_meaning = ['чтобы не, как бы не', 'поощрение, ободрение', 'непредвиденное обстоятельство', 'непредвиденное обстоятельство', 'быть способным сделать ч-л', 'ответственный ', 'обдумывать, размышлять ', 'разоблачать, развенчивать', 'быть путаницей, неразберихой', 'неумелый, неспособный', 'неумелый, неспособный', 'неумело', 'неумение, неспособность', 'отказываться от своих слов', 'безрассудный, неосторожный', 'безрассудно, неосторожно', 'безрассудство, неосторожность', 'современный', 'избегать, держаться в стороне', 'избегать, держаться в стороне', 'финансировать, спонсировать', 'финансирование', 'милосердный, сострадательный, полный сочувствия', 'евангелие', 'психически неуравновешенный', 'психически неуравновешенный', 'шлепать', 'шлепок', 'pull', 'pull', 'pull', 'pull', 'растянуть мышцу', 'выхватывать пистолет/нож и т. д.', 'разрывать на куски', 'разносить в пух и прах, критиковать', 'разнимать, разрывать', 'дергать', 'отъезжать', 'отступать от к-', 'сносить (здание)', 'подъезжать к чему-либо', 'успешно завершить какое-либо дело', 'отъезжать', 'натягивать (одежду)', 'выезжать (на дорогу)', 'подъехать к обочине и остановиться', 'выжить', 'взять себя в руки', 'притормозить, остановиться', 'придвигать стул', 'бояться, страшиться', 'бояться, страшиться', 'я содрогаюсь при мысли …', 'превзойти', 'превзойти', 'мародёрствовать, грабить, совершать набеги', 'хулиган', 'разрезать, полосовать', 'резко сокращать, снижать', 'глубокий порез, глубокая рана', 'косая черта', 'бдительный', 'бдительность', 'мусор, хлам', 'дрянь, халтура', 'громить', 'благоприятный, благосклонный', 'благоприятный, благосклонный', 'благоприятный', 'благоприятно', 'ужасный, серьезный', 'ужасный, серьезный', 'ужасный, серьезный', 'спускать воду (в туалете)', 'смывать, выбрасывать в туалет', 'покраснеть, зардеться', 'выманивать', 'конфликт, борьба', '(сходить и) принести', 'выручать (за проданную вещь)', 'натянутый, «притянутый за уши» (об аргументе, замечании, сравнении и т. п.)', 'мелкий, неглубокий', 'мелкий, неглубокий', 'мелководье', 'государственность', 'мрачный ', 'мрачный ', 'мрачный ', 'унылый', 'унылый', 'унылый', 'продвигаться вперед', 'продвигаться вперед', 'вертолет', 'дразнить, насмехаться', 'дразнить, насмехаться', '"опасное вещество;\xa0взрывчатый материал"', 'спасение', 'быть безнадежным, неисправимым', 'забеременеть', 'постигать', 'задумывать', 'нижний предел', 'нижний предел', 'нижний предел', 'синяк', 'ушибать, ставить синяк', 'кровоподтеки', 'грач, ладья, жулик,\xa0мошенник', 'щенок, сопляк', 'играть в азартные игры', 'делать ставку', 'приводить в какое-либо состояние', 'приводить в какое-либо состояние', 'оказывать (услуги и т. д.), сообщать (мнение и т. д.)', 'приводить в какое-либо состояние', 'оказывать (услуги и т. д.), сообщать (мнение и т. д.)', 'фанатик', 'расшифровываться как, означать ', 'стоять за что-либо, поддерживать', 'не потерпеть чего-либо', 'временный, предварительный', 'держать в руках (оружие) ', 'обладать влиянием/властью и т.д.', 'громоздкий', 'склонять, кланяться ', 'склонять, кланяться ', 'уйти со сцены', 'уйти со сцены', 'уступать, покоряться чему-либо/кому-либо', 'склониться', 'бант', 'лук\xa0(оружие)', 'смычок', 'изображать, выдавать себя за кого-либо', 'изображение к-л', 'пародист, человек, выдающий себя за кого-либо', 'поставлять провизию и обслуживать гостей к-л мероприятия', 'поставлять провизию и обслуживать гостей к-л мероприятия', 'обслуживать, быть предназначенным для к-л/ ч-л', 'потворствовать, угождать', 'потворствовать, угождать', 'гусеница', 'сновать, суетиться', 'сновать, суетиться', 'бурлить', 'привлекать внимание, занимать', 'нанимать', 'участвовать', 'занимать к-л ч-о', 'бренчать', 'торговый аппарат', 'одежда, наряд     снаряжение', 'одежда, наряд     снаряжение', 'сокращать, ограничивать', 'сокращать, ограничивать', '"наращивать,\xa0расширять;\xa0увеличивать"', 'лужа', 'коллективный иммунитет', 'свергать, вытеснять', 'защищать, отстаивать', 'туалет', 'избегать, уклоняться', 'избегать, уклоняться', 'избегать, уклоняться', 'избегать, уклоняться', 'избегать, уклоняться', 'избегать, уклоняться', 'принуждать', 'принуждение', 'принуждать', 'принуждение', 'принуждение', 'страшный, жуткий', 'страшный, жуткий', 'уголовный кодекс', 'женоненавистничество', 'презирать, пренебрегать', 'презирать, пренебрегать', 'презрение, пренебрежение ', 'презирать, пренебрегать', 'презрение, пренебрежение', 'раздавать, выдавать', 'раздавать, выдавать', 'пособие по безработице ', 'умалчивать, удерживать ', 'умалчивать, удерживать', 'гнев, ярость', 'отменять (закон)', 'осанка', 'в то время как, тогда как', 'волынка', 'американский лось', 'олень', 'уговаривать, склонять', 'уговаривать, склонять', 'соблазн, искушение ', 'соблазн, искушение', 'заманчивый ', 'увлекательный, захватывающий', 'быть расположенным/склонным делать что-либо', 'благосклонно/хорошо и т. д. относиться к ч-л', 'подделывать', 'налаживать, развивать отношения', 'продвигаться вперед', 'притуплять, оглуплять, отуплять', 'упрямый', 'недостаточный, скудный', 'некачественный, халтурный', 'некачественный, халтурный', 'переворот', 'приверженность', 'приверженец', '"комплексный; многоаспектный; многогранный"', 'форма правления, строй (общественный или государственный), устройство', 'проявлять (власть), оказывать (влияние)', 'напрягаться', 'лишать гражданских или избирательных прав', 'ненавидеть', '"отвратительный; мерзкий, плохой, противный"', 'мастер, маэстро, мэтр, учитель ', 'фон, задник (the painted cloth at the back of a stage in a theatre)', 'фон, задник (the painted cloth at the back of a stage in a theatre)', 'мнимый, предполагаемый', '"мечтательный; идеалистический; наивный; не от мира сего"', 'повторять, подчеркивать', 'повторять, подчеркивать', 'повторение', 'избавляться', 'оторваться от преследования', 'закоснелый, чёрствый, ожесточённый, упрямый', 'закоснелый, чёрствый, ожесточённый, упрямый', 'закоснелый, чёрствый, ожесточённый, упрямый']
real_example = ['-', 'Children need lots of encouragement from their parents.', '-', '-', "He's liable to make a fuss if you wake him.", 'Corporate officials are liable for the safety of their employees.', 'I need time to mull things over before I decide what to do.', '-', 'The performance was a complete shambles.', '-', 'She was totally inept at telling jokes.', '-', '-', 'The government has backtracked on its promises.', '-', '-', '-', '-', 'He was shunned by colleagues and family alike.', 'She has always shunned publicity. / She shuns publicity.', 'The event is sponsored by First National Bank. / UK a sponsored walk (= a walk for charity)', '-', '-', '-', 'He was shot by a deranged fan.', '-', "Do you think it's right to smack children when they're naughty?", "Stop shouting or I'll give you a smack!", "If you keep pulling his tail, he'll bite you.", "No wonder it's not working, someone's pulled the plug out .", 'He pulled off his boots.', 'She bent down and pulled up her socks.', '-', 'He pulled a gun on us and demanded money.', '-', '-', '-', 'Stop pulling at my sleeve.', 'If a vehicle pulls away, it starts moving. / I just managed to get on the bus before it pulled away.', 'If you pull away from someone who is holding you, you suddenly move your body backwards, away from them.', "They've started pulling down the old cinema.", 'If a vehicle pulls in or pulls into somewhere, it moves in that direction and stops there. / They pulled in at the side of the road.', 'He is about to pull off his biggest deal yet. / Cruz expects to win the fight, but no one else thinks he can pull it off.', 'phrasal verb UK- If a vehicle pulls off, it starts moving. / The car pulled off and sped up the road. (see also pull away) / US - pull off sth to leave a road in order to stop or to turn into another road', 'I pulled on my jeans and ran downstairs.', 'If a vehicle pulls out, it starts moving onto a road or onto a different part of the road. / That car pulled out right in front of me. (see also pull away)', 'If a vehicle pulls over, it moves to the side of the road and stops.', '-', '-', 'If a vehicle pulls up, it stops, often for a short time. / A car pulled up outside the bank and two men got out.', "Why don't you pull up a chair and join us?", "I'm dreading the first day at my new school.", '-', "I dread to think what could have happened if we hadn't been wearing seat belts.", 'They are always trying to outdo each other with their jokes and funny stories. / The skaters were trying to outdo each other.', 'You’ve really outdone yourself (=done something extremely well) this time!', '-', '-', 'His throat had been slashed.', '-', 'a long, deep cut', 'a mark (/)', "Police have asked people to be vigilant after yesterday's bomb attack.", '-', 'US ( UK rubbish )', "It's better than the trash she usually reads.", 'Vandals broke in and trashed the place.', 'His comments were highly favourable.', 'She made a very favourable impression on us.', 'The opposite is unfavourable', '-', "He's in dire need of help. / The country is in dire need of food aid.", 'Officials say the situation is not as dire as they first thought.', '-', 'If you flush a toilet, or if it flushes, its contents empty and it fills with water again.', '-', 'If you flush, your face becomes red and hot, usually because you are embarrassed or angry.', '-', 'a period of ethnic/political/marital strife', 'Can you fetch my glasses from the bedroom? / Rushworth went to fetch the key to the gate.', 'The painting is expected to fetch $50,000 in the auction. The tractor should fetch over $10,000.', 'Her story was pretty far-fetched.', '-', '-', '-', '-', '-', '-', '-', '-', 'Without a job, the future can seem bleak.', '-', "The builders aren't making much headway with our new house.", 'They have made little headway in the peace talks.', '-', '-', 'kids taunted him about his weight', 'от hazardous material', '-', '-', '-', 'I cannot conceive of anything more horrible.', 'The original idea for the novel was conceived in Rome.', 'By June, their marriage had hit rock bottom.', 'By June, their marriage had hit rock bottom.', '-', 'to suffer cuts and bruises after falling off a bike', 'to be badly bruised in the accident', 'to suffer serious bruising in the attack', '-', '-', 'He gambled away all of our savings.', '-', 'The trees rendered the road as dark as a tunnel. - деревья превратили дорогу в темный тоннель', 'She was rendered speechless upon hearing the news.', '-', 'The accident rendered her left leg useless.', '-', '-', "UFO stands for 'unidentified flying object'", 'The party stands for low taxes and individual freedom.', 'If you will not stand for something… (см. if и will)', 'These dates are only provisional at the moment.', '-', 'During the Middle Ages, the Church wielded a lot of influence.', '-', '-', '-', 'He bowed out of politics at the age of 70.', 'Two more Republicans have bowed out of the race.', 'The government are refusing to bow to public pressure.', 'To bowed down before the statue of Mary.', '-', '-', '-', 'Impersonating a police officer is a serious offence.', 'He did an impersonation of Bill Clinton.', '-', 'How many are we catering for at the wedding reception?', 'Who’s catering your daughter’s wedding?', 'The club caters for children between the ages of 4 and 12.', 'This legislation simply caters to unacceptable racist opinions.', 'newspapers that cater to business people', '-', 'There were lots of shoppers bustling about.', '-', 'The town centre was bustling with people.', 'The debate about food safety has engaged the whole nation.', 'I have engaged a secretary to deal with all my paperwork.', '-', 'If you engage someone in conversation, you start a conversation with them.', '-', '-', '-', 'I need a new outfit for the party.', '-', '-', '-', '-', '-', 'He was ousted from power by a military coup.', 'She championed the cause of free speech.', '-', '-', '-', 'He managed to evade the police.', '-', '-', '-', 'Employees said they were coerced into signing the agreement.', 'They accused the police of coercion', 'The women were coerced into hiding the drugs.', '-', '-', '-', '-', '-', '-', '-', 'You scorned all my suggestions.', 'He could barely disguise his scorn for her.', 'Skinner’s ideas were scorned by many American psychologists.', 'He invested his reply with scorn.', 'My parents are always doling out money to my sisters.', 'Vera was doling out candy to the kids.', "He's been on the dole for years.", 'The company has decided to withhold payment until the job has been finished.', 'They said McShane had withheld information from Congress. - He was accused of withholding vital information from the police.', '-', 'In 1933, Prohibition was finally repealed.', 'She has very good posture.', 'His parents were rich, whereas mine had to struggle. - Nowadays the trip takes six hours, whereas then it took several weeks. - Stafford had years of experience, whereas Lufkin was new to the job. - Denotative language is factual, whereas connotative language is emotional.', '-', '-', '-', "She's trying to tempt me to go shopping with her.", "I'm tempted not to go to my next class.", 'I resisted the temptation to have another piece of chocolate cake.', 'He knew crime was wrong but the money was too great a temptation.', '-', 'I found the movie fascinating.', "I tried to tell her but she didn't seem disposed to listen.", 'She seems well disposed towards the idea.', '-', 'The group forged friendships that have lasted more than twenty years.', 'The organizers are forging ahead with a programme of public events.', '-', "He's a very rude and obstinate man.", '-', '-', '-', '-', '-', '-', '-', '-', 'My parents exerted a lot of pressure on me to do well at school. - Powerful people exerted pressure on the paper not to run the story.', 'She was too ill to exert herself much.', '-', 'They used to be friends, but now they absolutely detest each other.', '-', '-', 'The attack took place against a backdrop of rising tensions between the two communities.', 'a love story set against the backdrop of war', '-', '-', 'I must reiterate that we have no intention of signing this contract.', 'Lawyers reiterated that there was no direct evidence against Mr. Evans', '-', 'I hope I can shake off this cold before the weekend.', '-', '-', '-', '-']

num=[]
for i in range(0,len(word_list)):
    num.append(i)

#print('word_list =', word_list)
#print('word_meaning =', word_meaning)
#print('example_list =', example_list)
#print('example_meaning =', example_meaning)
#print('real_example =', real_example)


global rand_num
global secret_num
global right_answers_stat
global wrong_answers_stat
global stop_statistics

right_answers_stat=0
wrong_answers_stat=0
stop_statistics = False

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
    global stop_statistics
    
    
    def build(self, btn1_txt='Answer 1', btn2_txt='Answer 2', btn3_txt='Answer 3', btn4_txt='Answer 4'):
     
        superBox = BoxLayout(orientation ='vertical') 

        q_label = Label(text = 'What is the right translation of this word?', font_size = 32)

        q_word_label = Label(text = 'WORD', font_size = 60, color = 'orange')

        o_text = TextInput(text='Examples:', readonly='True', foreground_color = 'black', line_height = 1, font_name = 'DejaVuSans.ttf')

        statistics_label = Label(text= 'Statistics...')


        btn1 = Button(text = btn1_txt,
                    font_size = 72,
                    font_name = "DejaVuSans.ttf",
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

#############################################
            
        def get_font_size(num_of_letters):

            if num_of_letters < 22:
                font_size = int(64*screen_coeff)
            elif num_of_letters < 26:
                font_size = int(56*screen_coeff)
            elif num_of_letters < 30:
                font_size = int(48*screen_coeff)
            elif num_of_letters < 36:
                font_size = int(40*screen_coeff)
            elif num_of_letters < 46:
                font_size = int(32*screen_coeff)
            elif num_of_letters < 62:
                font_size = int(24*screen_coeff)
            elif num_of_letters < 90:
                font_size = int(16*screen_coeff)
            else:
                font_size = 4
            return(font_size)

############################################
                
        def new_question( btn1_txt='Answer 1', btn2_txt='Answer 2', btn3_txt='Answer 3', btn4_txt='Answer 4'):
            global stop_statistics
            btn1.disabled = False
            btn2.disabled = False
            btn3.disabled = False
            btn4.disabled = False
            btn1.background_color = (1, 1, 1, 1)
            btn2.background_color = (1, 1, 1, 1)
            btn3.background_color = (1, 1, 1, 1)
            btn4.background_color = (1, 1, 1, 1)
            stop_statistics = False
            choose_combination()

            q_word_label.text = word_list[secret_num[0]] 
            q_word_label.font_size = get_font_size(len(word_list[secret_num[0]]))
            btn1.text = b'/ r\xc9\xaa\xcb\x88v\xc9\x9c\xcb\x90s /'.decode('utf-8') + 'привет'
            btn1.text = word_meaning[rand_num[0]] 
            btn1.font_size = get_font_size(len(word_meaning[rand_num[0]]))

            btn2.text = word_meaning[rand_num[1]] 
            btn2.font_size = get_font_size(len(word_meaning[rand_num[1]]))
            
            btn3.text = word_meaning[rand_num[2]] 
            btn3.font_size = get_font_size(len(word_meaning[rand_num[2]]))

            btn4.text = word_meaning[rand_num[3]] 
            btn4.font_size = get_font_size(len(word_meaning[rand_num[3]]))
            

            o_text.text = ''
            btn_next.disabled = True

        def show_statistics():
            statistics_label.text = 'Right Answers: ' + str(right_answers_stat) + '   ' + 'Wrong Answers: ' + str(wrong_answers_stat)
            
        def show_result(my_answer, right_answer):
            global stop_statistics
            stop_statistics = True
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
                o_text.text = example_list[secret_num[0]] + ' - ' + example_meaning[secret_num[0]] + '\n' + real_example[secret_num[0]]
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
                o_text.text = example_list[secret_num[0]] + ' - ' + example_meaning[secret_num[0]] + '\n' + real_example[secret_num[0]]       
                btn_next.disabled = False
                show_statistics()

        def check_result(my_answer):
            global right_answers_stat
            global wrong_answers_stat
            global stop_statistics
            right_answer = -1
            if stop_statistics == False:
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
