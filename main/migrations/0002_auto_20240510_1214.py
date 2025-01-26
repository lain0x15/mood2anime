# Generated by Django 3.2.19 on 2024-05-10 12:14

from django.db import migrations
from django.core.files import File
from pathlib import Path
import os

def addGenres (apps, scheme_editor):
    genres = apps.get_model('main', 'genres')
    genresName = [ 'Апокалиптика', 'Боевик', 'Боевые искусства', 'Детектив', 'Добуцу',
      'Драма', 'Идолы', 'Икудзи', 'Исторические произведения', 'Кайто', 'Киберпанк', 'Комедия',
      'Махо-сёдзё', 'Моэ', 'Меха', 'Мистика', 'Научная фантастика', 'Отаку', 'Парапсихология', 'Паропанк/Стимпанк',
      'Повседневность', 'Постапокалиптика', 'Психологический триллер', 'Триллер', 'исэкай', 'Романтика', 'Спокон', 'Токусацу', 'Фэнтези',
      'Супер сила', 'Приключения', 'Сёнэн', 'Экшен', 'Фантастика', 'Пародия', 'Исторический', 'Сверхъестественное', 'Сэйнэн', 'Этти'
    ]
    for genreName in genresName:
        genres.objects.create (name=genreName)

def addMood (apps, scheme_editor):
    mood = apps.get_model('main', 'mood')
    moodsName = [ 
        {
            'name': 'Весёлое',
            'fileName': 'cheerful.png'
        },
        {
            'name': 'Мрачное',
            'fileName': 'gloomy.png'
        },
        {
            'name': 'Меланхоличное',
            'fileName': 'melancholy.png'
        },
        {
            'name': 'Чиловое',
            'fileName': 'chill.png'
        },
        {
            'name': 'Влюблённое',
            'fileName': 'romantic.png'
        },
        {
            'name': 'Странное',
            'fileName': 'weird.png'
        },
        {
            'name': 'Хорни',
            'fileName': 'horny.png'
        },
        {
            'name': 'Сонное',
            'fileName': 'sleepy.png'
        },
        {
            'name': 'Злое',
            'fileName': 'angry.png'
        },
        {
            'name': 'Одинокий',
            'fileName': 'lonely.png'
        },
        {
            'name': 'Напряжённое',
            'fileName': 'tense.png'
        },
        {
            'name': 'Задумчивое',
            'fileName': 'thoughtful.png'
        }
    ]
    base_dir = Path(__file__).parent
    photo_path = base_dir / 'initial_photos'
    
    for moodName in moodsName:
        files = photo_path.glob(moodName['fileName'])
        files = [file for file in files if file.is_file()]
        with open(files[0].relative_to(os.getcwd(), walk_up=True), 'rb') as file:
            djangoFile = File(file)
            mood.objects.create (name=moodName['name'], img=djangoFile)

def addAnime (apps, scheme_editor):
    anime = apps.get_model('main', 'anime')
    
    genreAnime = apps.get_model('main', 'genreAnime')
    genres = apps.get_model('main', 'genres')
    
    moodAnime = apps.get_model('main', 'moodAnime')
    moods = apps.get_model('main', 'mood')
    
    animesField = [
        {
            'anime': {
                'name': 'Сонни Бой',
                'trailer': 'https://www.youtube.com/embed/6LiyZ0p_uLw?si=34XIQHzHyN-rq_lB',
                'releaseYear': '2021-01-01',
                'review': 7,
                'description': '16 августа, середина долгих летних каникул. Пустые школьные классы, в которых никого нет, тоскливые дни... внезапно прерванные неожиданным происшествием — здание школы, Нагара и 36 его одноклассников вдруг перемещаются в другое измерение!'
            },
            'genres': [
                'Детектив',
                'Научная фантастика',
                'Супер сила'
             ],
            'moods': [
                'Задумчивое',
                'Одинокий',
                'Странное'
            ] 
        },
        {
            'anime': {
                'name': 'Гинтама',
                'trailer': 'https://www.youtube.com/embed/YQC3ot0IjiA?si=AyVfrIWwxnEETlFD',
                'releaseYear': '2003-01-01',
                'review': 7,
                'description': 'Гинтама - шедевр нашего времени, который заслужено признан одним если не из самых лучших сёненов и комедий, среди аниме и манги. Хочу ещё поговорить про структуру сюжета. Достаточно включить рандомный эпизод, вам без проблем может попасться серия, в котором будет обыгрываться какая-то ситуация и не дай бог она будет не обставлена каким-то невообразимо забавным образом.'
            },
            'genres': [
                'Комедия',
                'Фантастика',
                'Пародия',
                'Приключения'
             ],
            'moods': [
                'Весёлое',
                'Чиловое'
            ] 
        },
        {
            'anime': {
                'name': 'Тора дора',
                'trailer': 'https://www.youtube.com/embed/ya570uUgQNc?si=S-rwaF8fCds3KkD1',
                'releaseYear': '2008-01-01',
                'review': 7,
                'description': 'Семнадцатилетний парень Рюдзи, которого все боятся из-за страшного взгляда, влюбляется в одноклассницу Минори, а его соседка Тайга влюбляется в Китамару. Они решают объединить свои усилия, но может быть они просто не в тех влюбились?'
            },
            'genres': [
                'Комедия',
                'Романтика',
                'Повседневность'
             ],
            'moods': [
                'Весёлое',
                'Влюблённое',
                'Чиловое'
            ] 
        },
        {
            'anime': {
                'name': 'Атака титанов',
                'trailer': 'https://www.youtube.com/embed/MGRm4IzK1SQ?si=w2qkot2_Q3F0QUVI',
                'releaseYear': '2013-01-01',
                'review': 9,
                'description': 'Эрен и его семья живут в безопасности, ведь от гигантских человекоподобных людоедов, именуемых титанами, их и весь город защищает огромная непреодолимая стена. Но в тот день случилось непредвиденное и привычная жизнь всего человечества обратилась в сплошной кошмар.'
            },
            'genres': [
                'Драма',
                'Фэнтези',
                'Приключения',
                'Сёнэн',
                'Экшен'
             ],
            'moods': [
                'Мрачное',
                'Напряжённое'
            ] 
        },
        {
            'anime': {
                'name': 'Куда едет поезд судного дня?',
                'trailer': 'https://www.youtube.com/embed/XLWzhcMOcVo?si=GeS6KO7BuweEXmJV',
                'releaseYear': '2024-01-01',
                'review': 7,
                'description': 'В непримечательном на первый взгляд провинциальном городке с жителями происходят странные вещи. Однако Сидзуру Тикура больше беспокоится о своей пропавшей подруге. Решив найти её, Сидзуру вместе с тремя другими девочками садится на заброшенный поезд и отправляется во внешний мир, не зная, смогут ли они вернуться живыми. Что ждёт их на конечной остановке?'
            },
            'genres': [
                'Приключения'
             ],
            'moods': [
                'Чиловое'
            ] 
        },
        {
            'anime': {
                'name': 'Золотая пора',
                'trailer': 'https://www.youtube.com/embed/44njDYJ5OJA?si=DSxkmBPx8LkpbONx',
                'releaseYear': '2013-01-01',
                'review': 7,
                'description': 'Тада Банри – свежеиспечённый первокурсник одного Токийского университета – умудрился заблудиться сразу же после окончания торжественной линейки. И вот, попутно проклиная всё на свете, юноша столкнулся с Янагисавой Мицуо. Товарищи по несчастью быстро нашли общий язык... Но кто бы мог подумать! У ворот ВУЗ-а их встретила писанная красавица.'
            },
            'genres': [
                'Романтика',
                'Драма',
                'Комедия',
                'Повседневность'
             ],
            'moods': [
                'Влюблённое',
                'Весёлое'
            ]
        },
        {
            'anime': {
                'name': 'Как и ожидалось, моя школьная романтическая жизнь не удалась',
                'trailer': 'https://www.youtube.com/embed/u-bpwWPNEpE?si=_rbaZyje3L5Ay7ru',
                'releaseYear': '2013-01-01',
                'review': 8,
                'description': 'Хачиман Хикигая семнадцать лет. Это самый яркий представитель пессимистически настроенных людей, он уверен в том, что дружба, любовь и преданность – это самая наглая ложь, а поддержание этой теории - всего лишь договоренность тех, кто однажды ошибся, но признавать этого просто не хочет.'
            },
            'genres': [
                'Романтика',
                'Комедия',
                'Повседневность'
             ],
            'moods': [
                'Задумчивое',
                'Одинокий',
                'Меланхоличное'
            ]
        },
        {
            'anime': {
                'name': 'Крутой учитель Онидзука',
                'trailer': 'https://www.youtube.com/embed/aZcEfuNsyKM?si=TjHL6Z1TDCM37wFv',
                'releaseYear': '1999-01-01',
                'review': 9,
                'description': 'Бывший член нагоняющей на горожан ужас банды «Онибаку», байкер Эйкити Онидзука, ставит перед собой цель стать самым крутым школьным учителем. Почему учителем? Да просто в школах полно сексуальных старшеклассниц!'
            },
            'genres': [
                'Комедия',
                'Повседневность',
                'Драма',
                'Сёнэн'
            ],
            'moods': [
                'Весёлое'
            ]
        },
        {
            'anime': {
                'name': 'Богиня благословляет этот прекрасный мир',
                'trailer': 'https://www.youtube.com/embed/s0TXMXF3Qyo?si=OR6ckacFpNSqOszp',
                'releaseYear': '2016-01-01',
                'review': 9,
                'description': 'Кадзума Сато – настоящий затворник, который неожиданно распрощался с жизненной дорогой и оказался в альтернативной реальности. Там он повстречал дерзкую богиню Аква, которая предложила новичку вместо превращения в насекомого воспользоваться уникальным шансом и попасть в игровую вселенную, где необходимо уничтожить Князя Тьмы.'
            },
            'genres': [
                'Комедия',
                'Приключения',
                'Пародия',
                'Фэнтези'
            ],
            'moods': [
                'Весёлое'
            ]
        },
        {
            'anime': {
                'name': 'Бездомный Бог',
                'trailer': 'https://www.youtube.com/embed/gEVlI1ZLpFI?si=LcDCmQhEGTKVWLIg',
                'releaseYear': '2014-01-01',
                'review': 8,
                'description': 'Малоизвестный Бог Ято не имеет собственного храма, но мечтает стать уважаемым божеством с миллионами верующих. Правда, Ято не особо стремится прилагать усилия для достижения данной цели. Однажды обычная школьница Хиёри спасает его от дорожной аварии ценой собственной жизни.'
            },
            'genres': [
                'Комедия',
                'Приключения',
                'Сёнэн',
                'Экшен'
            ],
            'moods': [
                'Весёлое',
                'Чиловое'
            ]  
        },
        {
            'anime': {
                'name': 'Самурай Чамплу',
                'trailer': 'https://www.youtube.com/embed/xWKzbhAUeZE?si=jBDl85ajITJcFQL9',
                'releaseYear': '2004-01-01',
                'review': 9,
                'description': 'Мугэн - мечник с повадками брейкдансера, вспыльчивый, грубый и вечно голодный мужлан. Дзин - благородный, хорошо воспитанный ронин, чьё прошлое скрывает мрачную тайну. Нет в мире двух других самураев, настолько непохожих друг на друга - а судьба не только сводит их в поединке, но и заставляет присоединиться к Фуу'
            },
            'genres': [
                'Комедия',
                'Приключения',
                'Экшен',
                'Исторический'
            ],
            'moods': [
                'Весёлое',
                'Чиловое',
            ]
        },
        {
            'anime': {
                'name': 'Сага о Винланде',
                'trailer': 'https://www.youtube.com/embed/Vt7Rwfj7bHU?si=TM8Us0daoqP0lSzB',
                'releaseYear': '2019-01-01',
                'review': 8,
                'description': 'Времена господства викингов. Людей, известных своими жестокими обычаями. Торфинн — сын одного из величайших викингов. Вот только вырос мальчик без отца, так как тот погиб на поле боя. Желая отомстить, Торфинн поклялся убить виновного, однако юноше ещё только предстоит овладеть искусством боя.'
            },
            'genres': [
                'Приключения',
                'Драма',
                'Боевик'
            ],
            'moods': [
                'Мрачное',
                'Злое'
            ]
        },
        {
            'anime': {
                'name': 'Эта фарфоровая кукла влюбилась',
                'trailer': 'https://www.youtube.com/embed/BqrwazH7PhU?si=zIVF2sLdSH0AUyoM',
                'releaseYear': '2022-01-01',
                'review': 8,
                'description': 'Замкнутый старшеклассник Годзё Вакана мечтает мастерить японских кукол. В нём до сих пор живы болезненные воспоминания из детства, когда друг Годзё высмеял его увлечение куклами. Однажды модная жизнерадостная и сексуальная красавица Марин Китагава застала Годзё за шитьем. С этого момента одинокий «кукольник» забыл о тишине и спокойствии.'
            },
            'genres': [
                'Повседневность',
                'Романтика',
                'Комедия'
            ],
            'moods': [
                'Хорни',
                'Влюблённое'
            ]
        },
        {
            'anime': {
                'name': 'Всегда вялый танака-кун',
                'trailer': 'https://www.youtube.com/embed/MWVEG7kDQfo?si=cs6ReW0KU9_y_ADd',
                'releaseYear': '2016-01-01',
                'review': 8,
                'description': 'Танака — обычный школьник, который не проявляет интереса ни к учёбе, ни к спорту, а на уроках всегда спит. Но у юноши есть друг Ота, который во всём проявляет активность и успеваемость. Несмотря на то, что друзья — полные противоположности, они продолжают дружить. До чего же доведёт эта дружба?'
            },
            'genres': [
                'Повседневность',
                'Сёнэн',
                'Комедия'
            ],
            'moods': [
                'Сонное'
            ]
        },
        {
            'anime': {
                'name': 'Моя подруга – демон',
                'trailer': 'https://www.youtube.com/embed/sWhtovYy3E0?si=j0onRNPx9N3EtG52',
                'releaseYear': '2024-01-01',
                'review': 9,
                'description': 'История Хиираги Яцусэ, первокурсника старшей школы, который изо всех сил пытается завести друзей, несмотря на свои усилия угодить другим. Его жизнь принимает неожиданный поворот, когда однажды летним днем ​​он встречает Цумуги, девушку-они (демона), ищущую свою мать в человеческом мире. Таинственным образом начинает падать снег... и начинается их приключение.'
            },
            'genres': [
                'Приключения'
            ],
            'moods': [
                'Влюблённое',
                'Чиловое'
            ]
        },
        {
            'anime': {
                'name': 'Маленький гражданин',
                'trailer': 'https://www.youtube.com/embed/U1agV6NfMqU?si=gmpOCDqVnaa3-R9I',
                'releaseYear': '2024-01-01',
                'review': 9,
                'description': 'Кобато хочет стать простым, маленьким человеком. Ему на всю жизнь хватило боли, которую порой приносит работа головой. Именно поэтому он поклялся вместе с одноклассницей Осанай добиться желанного: пойти в старшую школу и тихо-мирно в ней учиться. Увы, но судьба имеет на него другие планы. Что ни день, так случается что-то новое! Так удастся ли Кобато с Осанай хотя бы день прожить спокойно?'
            },
            'genres': [
                'Повседневность',
                'Детектив'
            ],
            'moods': [
                'Чиловое',
                'Задумчивое'
            ]
        },
        {
            'anime': {
                'name': 'ID: Вторжение',
                'trailer': 'https://www.youtube.com/embed/AcvLglA-KfE?si=NNmNfdmVa_Jl6bKz',
                'releaseYear': '2020-01-01',
                'review': 9,
                'description': 'Добро пожаловать в поразительный виртуальный мир! Детективу Сакайдо предстоит расследовать жестокое убийство девочки, о которой известно только имя — Каэру. Это дело отличается от всех, какими он занимался прежде… Ведь сам мир начинает вертеться вокруг него, подвергая сомнению всё, что думает и во что верит Сакайдо!'
            },
            'genres': [
                'Детектив',
                'Психологический триллер',
                'Фантастика'
            ],
            'moods': [
                'Напряжённое',
                'Мрачное'
            ]
        },
        {
            'anime': {
                'name': 'Парад смерти',
                'trailer': 'https://www.youtube.com/embed/EbNKpwe_lM4?si=Y6zryEA5KufTiHQe',
                'releaseYear': '2015-01-01',
                'review': 9,
                'description': 'Что если смерть – это не конец, а лишь начало. Существует ли Рай и Ад? Этот вопрос тысячелетиями терзал человеческий разум. И тайна загробной жизни всегда интересовала смертных. Но что если все гораздо проще? Например, если после смерти вы должны пройти суд, который определит, куда вы должны отправиться – в Ад или на Небеса?'
            },
            'genres': [
                'Детектив',
                'Драма',
                'Психологический триллер'
            ],
            'moods': [
                'Напряжённое',
                'Мрачное'
            ]
        },
        {
            'anime': {
                'name': 'Дандадан',
                'trailer': 'https://www.youtube.com/embed/0XJxfbN36Uw?si=MRrXKBhmUV-JVJf3',
                'releaseYear': '2024-01-01',
                'review': 9,
                'description': 'Старшеклассники Момо Аясэ и Кэн Такакуре самозабвенно изучают паранормальные явления. Девушка ищет в нашем мире призраков, а Кэн занят поиском пришельцев. В какой-то момент их изыскания пересекаются. И, о ужас, мир атакуют и призраки, и пришельцы. Особенно досталось Момо, которую похищают пришельцы. Благодаря разблокировке экстрасенсорных способностей девушка сбегает и начинает помогать Кэну. Тот в свою очередь заполучил контроль над мощным духом. Теперь у ребят есть силы для борьбы с жутким врагом, но хватит ли у них решимости?'
            },
            'genres': [
                'Комедия',
                'Экшен',
                'Сёнэн',
                'Сверхъестественное'
            ],
            'moods': [
                'Весёлое',
                'Чиловое'
            ]
        },
        {
            'anime': {
                'name': 'Вы правда женитесь?',
                'trailer': 'https://www.youtube.com/embed/AiVwg7do7Ik?si=h996Wmyydzjbdj0s',
                'releaseYear': '2024-01-01',
                'review': 8,
                'description': 'Работа в туристическом агентстве безоблачна и интересна. Девушка Рика и парень Такуя довольны сложившимся в офисе укладом. Будучи домоседами и одиночками по жизни, они не стремятся к новым высотам карьерной лестницы. Скорей, наоборот, их пугают любые перспективы изменений на работе и в быту. Узнав о том, что фирма планирует использовать неженатых и незамужних сотрудников для открытия заграничного филиала, Рика и Такуя решаются на фиктивную помолвку. Им кажется, что это простой и надежный выход из сложившейся ситуации, но молодые люди даже не подозревают куда их приведет подобное решение. Так чем же закончится игра во влюбленных голубков?'
            },
            'genres': [
                'Сэйнэн',
                'Романтика'
            ],
            'moods': [
                'Влюблённое'
            ]
        },
        {
            'anime': {
                'name': 'Город, в котором меня нет',
                'trailer': 'https://www.youtube.com/embed/-MfjTJvMLn0?si=Wgks01X5jj7b4Wic',
                'releaseYear': '2016-01-01',
                'review': 9,
                'description': 'Обыкновенный тридцатилетний молодой человек, неудачник в жизни Сатору Фуджинума. Ему почти тридцать, в этом возрасте многие уже управляют фирмами и складывают хорошие счета, герой считает копейки, полученные на развозе пиццы и рисует мангу, в чем он не преуспевает. Но всё не просто, в невзрачном парне кроются большие способности, он обладает «возрождением». Он имеет возможность отмотать часы времени обратно и спасти кого-то от гибели. Дар может проявиться когда угодно, но это не мешает парню помогать людям, хотя порой это проходит как набор случайных событий, от которых остаются травмы.'
            },
            'genres': [
                'Детектив',
                'Психологический триллер',
                'Сверхъестественное',
                'Сэйнэн'
            ],
            'moods': [
                'Мрачное',
                'Задумчивое',
                'Напряжённое'
            ]
        },
        {
            'anime': {
                'name': 'Железобетон',
                'trailer': 'https://www.youtube.com/embed/PfQjc2hs34Y?si=zbVHsOM4Y43HjYGO',
                'releaseYear': '2006-01-01',
                'review': 7,
                'description': 'В Городе Сокровищ дети-сироты Чёрный и Белый правят на улицах с помощью насилия и террора. Эти потерянные мальчики абсолютно не похожи друг на друга: Чёрный — негодяй, олицетворяющий всё плохое в городе, а Белый — невинный дурачок, оторванный от мира. Вместе они хотят предотвратить план якудза по превращению города в парк развлечений. Разрушительному Чёрному необходимо спасти город от ужасной судьбы, в то время как добрый Белый должен спасти Чёрного от его тёмной природы.'
            },
            'genres': [
                'Сэйнэн',
                'Экшен',
                'Приключения',
                'Сверхъестественное',
                'Триллер'
            ],
            'moods': [
                'Мрачное',
                'Напряжённое',
                'Злое'
            ]
        },
        {
            'anime': {
                'name': 'Бтууум!',
                'trailer': 'https://www.youtube.com/embed/H92d6YZkVO8?si=c2zEP17p92tyvVEi',
                'releaseYear': '2012-01-01',
                'review': 7,
                'description': 'Мечты сбываются. И парень Рёта Сакамото полностью оценил иронию данного выражения. Ведь что у него было в реальной жизни? Да почти ничего. Ни работы, ни друзей, ни девушки. Он сидит на шее у матери и постоянно играет в онлайн-игры. И там, в этих играх, всё по-другому — Рёта входит в топ-рейтинг игроков Японии онлайн-игры «Btoom!» И однажды молодой человек, которому надоели все проблемы реального мира, просто захотел убежать туда, в виртуальность, и уснул... А проснулся уже на тропическом острове с осознанием того, что он как-то попал в игру. Плохие новости — первый же встречный попытался его убить, причём, видимо, он не один здесь такой псих. Хорошие новости — мечты действительно сбываются! И теперь Рёте придётся со всем этим разбираться.'
            },
            'genres': [
                'Сэйнэн',
                'Экшен',
                'Фантастика',
                'Триллер'
            ],
            'moods': [
                'Мрачное',
                'Злое'
            ]
        },
        {
            'anime': {
                'name': 'Сквозь слёзы я притворяюсь кошкой',
                'trailer': 'https://www.youtube.com/embed/Fj9GUyJuu9U?si=yobeC8nNXhIukrlo',
                'releaseYear': '2020-01-01',
                'review': 8,
                'description': 'Миё Сасаки по прозвищу «Мугэ» — активная и яркая девушка, по уши влюблённая в одноклассника Кэнто Хинодэ. Все попытки Миё привлечь внимание юноши заканчиваются провалом, однако ситуация меняется, когда та находит магическую маску, позволяющую превращаться в «Таро» — милую белую кошку, которую так любит Кэнто. Ход событий кажется заманчивым, но со временем граница между девушкой и кошкой начинает исчезать.'
            },
            'genres': [
                'Драма',
                'Романтика',
                'Сверхъестественное'
            ],
            'moods': [
                'Влюблённое'
            ]
        },
        {
            'anime': {
                'name': 'Подручный Луизы-Нулизы',
                'trailer': 'https://www.youtube.com/embed/j-UofYKswhI?si=zs3uIGr98k0oGJNR',
                'releaseYear': '2006-01-01',
                'review': 9,
                'description': 'Луиза-Франсуаза де Лавальер учится в Академии волшебства Тристейн. Правда, академические успехи обходят мадмуазель стороной: ей не удается правильно воспроизвести ни одного заклинания, у нее не выходит ни одна трансформация. Но самое тяжелое испытание Луизе (прозванной вредными сокурсниками «Нулизой» сообразно уровню способностей) приходится пережить на втором курсе, в торжественный день Вызова Фамилиаров, талисманов и прислужников начинающих магов. Вместо дракона, саламандры, орла или черной кошки невезучей Луизе достается в ручные любимцы... Хираго Сайто, обыкновенный японский старшеклассник.'
            },
            'genres': [
                'Экшен',
                'Приключения',
                'Комедия',
                'Фэнтези',
                'Романтика',
                'Этти'
            ],
            'moods': [
                'Хорни',
                'Чиловое'
            ]
        }
    ]

    for animeField in animesField:
        createdAnime = anime.objects.create (**animeField['anime'])
        for genre in animeField['genres']:
            genreAnime.objects.create(animeID = createdAnime, genreID=genres.objects.get(name=genre))
        for mood in animeField['moods']:
            moodAnime.objects.create(animeID = createdAnime, moodID=moods.objects.get(name=mood))

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addGenres),
        migrations.RunPython(addMood),
        migrations.RunPython(addAnime)
    ]