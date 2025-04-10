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
      'Повседневность', 'Постапокалиптика', 'Психологический триллер', 'Триллер', 'Исэкай', 'Романтика', 'Спокон', 'Токусацу', 'Фэнтези',
      'Супер сила', 'Приключения', 'Сёнэн', 'Экшен', 'Фантастика', 'Пародия', 'Исторический', 'Сверхъестественное', 'Сэйнэн', 'Этти', 'Сёнен'
    ]
    for genreName in genresName:
        genres.objects.create (name=genreName)

def addTypes (apps, scheme_editor):
    types_model = apps.get_model('main', 'types_model')
    types_name = ['Сериал', 'Фильм']
    for type_name in types_name:
        types_model.objects.create (name=type_name)

def addStudios (apps, scheme_editor):
    studiosModel = apps.get_model('main', 'studios')
    studiosList = [
        {
            'name': 'A-1 Pictures',
            'imageName': 'A-1_Logo.png'
        },
        {
            'name': 'Madhouse',
            'imageName': 'Madhouse_studio_logo.png'

        },
        {
            'name': 'J.C.STAFF',
            'imageName': 'J.C.Staff_Logo.png'
        },
        {
            'name': 'Sunrise',
            'imageName': 'sunrise.jpg'
        },
        {
            'name': 'Bandai Namco Pictures',
            'imageName': 'Bandai_Namco_logo.png'
        },
        {
            'name': 'Wit Studio',
            'imageName': 'Wit_studio.png'
        },
        {
            'name': 'EMT squared',
            'imageName': 'EMT_Squared_logo.gif'
        },
        {
            'name': 'Feel',
            'imageName': 'feel.png'
        },
        {
            'name': 'Studio Pierrot',
            'imageName': 'Studio_Pierrot_logo.png'
        },
        {
            'name': 'Studio Deen',
            'imageName': 'Studio_Deen_logo.png'
        },
        {
            'name': 'Bones',
            'imageName': 'Bones_logo.png'
        },
        {
            'name': 'Manglobe',
            'imageName': 'manglobe.png'
        },
        {
            'name': 'CloverWorks',
            'imageName': 'CloverWorks_Logo.png'
        },
        {
            'name': 'Silver Link',
            'imageName': 'Silver_Link_Logo.png'
        },
        {
            'name': 'Studio Colorido',
            'imageName': 'Studio_Colorido.png'
        },
        {
            'name': 'Lapin Track',
            'imageName': 'Lapin_Track_Logo.png'
        },
        {
            'name': 'NAZ',
            'imageName': 'Naz_Logo.png'
        },
        {
            'name': 'Science Saru',
            'imageName': 'Science_SARU_logo.png'
        },
        {
            'name': 'Ashi Productions',
            'imageName': 'Ashi_Productions.png'
        },
        {
            'name': 'Studio 4°С',
            'imageName': 'Studio_4°С.gif'
        },
        {
            'name': 'Production I.G',
            'imageName': 'Production_I.G_Logo.png'
        },
        {
            'name': 'MAPPA',
            'imageName': 'MAPPA_Logo.svg.png'
        },
        {
            'name': 'Brain\'s Base',
            'imageName': 'Brains_Base_logo.svg.png'
        },
        {
            'name': 'Drive',
            'imageName': 'Drive_Studio_Logo.png'
        },
        {
            'name': 'Toho',
            'imageName': 'Toho_Logo.svg.jpg'
        }
    ]
    base_dir = Path(__file__).parent
    photo_path = base_dir / 'initial_photos' / 'studios' / 'picture'

    for studioList in studiosList:
        files = photo_path.glob(studioList['imageName'])
        files = [file for file in files if file.is_file()]
        with open(files[0].relative_to(os.getcwd(), walk_up=True), 'rb') as file:
            djangoFile = File(file, name=studioList['imageName'])
            studiosModel.objects.create (
                name=studioList['name'],
                image=djangoFile
            )

def addFranchises (apps, scheme_editor):
    franchises_model = apps.get_model('main', 'franchises')
    franchises_name = [
        'sonny_boy', 'gintama', 'Toradora',
        'Attack_on_Titan', 'Train_to_the_End_of_the_World', 'Golden_time',
        'My_Teen_Romantic_Comedy_SNAFU', 'GTO', 'KonoSuba',
        'Noragami', 'Samurai_Champloo', 'Vinland_Saga',
        'My_Dress-Up_Darling', 'Tanaka-kun_is_Always_Listless', 'My_Oni_Girl',
        'Shoshimin_How_to_Become_Ordinary', 'Id_Invaded', 'Death_Parade',
        'Dandadan', '365_Days_to_the_Wedding', 'Erased',
        'Tekkonkinkreet', 'Btooom', 'AWhiskerAway',
        'zero_no_tsukaima', 'frieren'
    ]
    for franchise_name in franchises_name:
        franchises_model.objects.create (name=franchise_name)

def addAnime (apps, scheme_editor):
    anime = apps.get_model('main', 'anime')

    genreAnime = apps.get_model('main', 'genreAnime')
    genres = apps.get_model('main', 'genres')
    studiosModel = apps.get_model('main', 'studios')
    types_model = apps.get_model('main', 'types_model')
    franchises_model = apps.get_model('main', 'franchises')

    animesField = [
        {
            'anime': {
                'name': 'Сонни Бой',
                'trailer': 'https://www.youtube.com/embed/6LiyZ0p_uLw?si=34XIQHzHyN-rq_lB',
                'releaseYear': '2021-01-01',
                'review': 8,
                'description': '16 августа, середина долгих летних каникул. Пустые школьные классы, в которых никого нет, тоскливые дни... внезапно прерванные неожиданным происшествием — здание школы, Нагара и 36 его одноклассников вдруг перемещаются в другое измерение!\nТам подростки, брошенные на произвол судьбы, сталкиваются со многими загадочными ситуациями и явлениями. Но главное — приобретают различные способности, находящиеся за пределами человеческого понимания. Некоторые радуются открытым в себе силам и устраивают беспорядки, другие пытаются занять место лидера группы, остальные же — отчаянно ищут способ вернуться в мир, из которого они прибыли. Недоверие, неконтролируемая ревность и стремление к лидерству приводят к конфликтам. В водовороте вопросов, которые возникают один за другим, начинается жизнь на грани выживания. Смогут ли Нагара и его друзья покорить этот мир и благополучно вернуться домой?',
                'portraitImgName': 'sonnyboy.jpg',
                'studios': ['Madhouse'],
                'typeName': 'Сериал',
                'franchise': 'sonny_boy'
            },
            'genres': [
                'Детектив',
                'Научная фантастика',
                'Супер сила'
             ]
        },
        {
            'anime': {
                'name': 'Гинтама',
                'trailer': 'https://www.youtube.com/embed/YQC3ot0IjiA?si=AyVfrIWwxnEETlFD',
                'releaseYear': '2003-01-01',
                'review': 7,
                'description': 'Гинтама - шедевр нашего времени, который заслужено признан одним если не из самых лучших сёненов и комедий, среди аниме и манги. Хочу ещё поговорить про структуру сюжета. Достаточно включить рандомный эпизод, вам без проблем может попасться серия, в котором будет обыгрываться какая-то ситуация и не дай бог она будет не обставлена каким-то невообразимо забавным образом.',
                'portraitImgName': 'gintama.jpg',
                'studios': ['Sunrise', 'Bandai Namco Pictures'],
                'typeName': 'Сериал',
                'franchise': 'gintama'
            },
            'genres': [
                'Комедия',
                'Фантастика',
                'Пародия',
                'Приключения'
             ]
        },
        {
            'anime': {
                'name': 'Тора дора',
                'trailer': 'https://www.youtube.com/embed/ya570uUgQNc?si=S-rwaF8fCds3KkD1',
                'releaseYear': '2008-01-01',
                'review': 7,
                'description': 'Семнадцатилетний парень Рюдзи, которого все боятся из-за страшного взгляда, влюбляется в одноклассницу Минори, а его соседка Тайга влюбляется в Китамару. Они решают объединить свои усилия, но может быть они просто не в тех влюбились?',
                'portraitImgName': 'toradora.jpg',
                'studios': ['J.C.STAFF'],
                'typeName': 'Сериал',
                'franchise': 'Toradora'
            },
            'genres': [
                'Комедия',
                'Романтика',
                'Повседневность'
             ]
        },
        {
            'anime': {
                'name': 'Атака титанов',
                'trailer': 'https://www.youtube.com/embed/MGRm4IzK1SQ?si=w2qkot2_Q3F0QUVI',
                'releaseYear': '2013-01-01',
                'review': 9,
                'description': 'Эрен и его семья живут в безопасности, ведь от гигантских человекоподобных людоедов, именуемых титанами, их и весь город защищает огромная непреодолимая стена. Но в тот день случилось непредвиденное и привычная жизнь всего человечества обратилась в сплошной кошмар.',
                'portraitImgName': 'attackOnTitan.jpg',
                'studios': ['Wit Studio', 'Production I.G', 'MAPPA'],
                'typeName': 'Сериал',
                'franchise': 'Attack_on_Titan'
            },
            'genres': [
                'Драма',
                'Фэнтези',
                'Приключения',
                'Сёнэн',
                'Экшен'
             ]
        },
        {
            'anime': {
                'name': 'Куда едет поезд судного дня?',
                'trailer': 'https://www.youtube.com/embed/XLWzhcMOcVo?si=GeS6KO7BuweEXmJV',
                'releaseYear': '2024-01-01',
                'review': 7,
                'description': 'В непримечательном на первый взгляд провинциальном городке с жителями происходят странные вещи. Однако Сидзуру Тикура больше беспокоится о своей пропавшей подруге. Решив найти её, Сидзуру вместе с тремя другими девочками садится на заброшенный поезд и отправляется во внешний мир, не зная, смогут ли они вернуться живыми. Что ждёт их на конечной остановке?',
                'portraitImgName': 'trainTotheEndoftheWorld.jpg',
                'studios': ['EMT squared'],
                'typeName': 'Сериал',
                'franchise': 'Train_to_the_End_of_the_World'
            },
            'genres': [
                'Приключения'
             ]
        },
        {
            'anime': {
                'name': 'Золотая пора',
                'trailer': 'https://www.youtube.com/embed/44njDYJ5OJA?si=DSxkmBPx8LkpbONx',
                'releaseYear': '2013-01-01',
                'review': 7,
                'description': 'Тада Банри – свежеиспечённый первокурсник одного Токийского университета – умудрился заблудиться сразу же после окончания торжественной линейки. И вот, попутно проклиная всё на свете, юноша столкнулся с Янагисавой Мицуо. Товарищи по несчастью быстро нашли общий язык... Но кто бы мог подумать! У ворот ВУЗ-а их встретила писанная красавица.',
                'portraitImgName': 'goldenTime.jpg',
                'studios': ['J.C.STAFF'],
                'typeName': 'Сериал',
                'franchise': 'Golden_time'
            },
            'genres': [
                'Романтика',
                'Драма',
                'Комедия',
                'Повседневность'
             ]
        },
        {
            'anime': {
                'name': 'Как и ожидалось, моя школьная романтическая жизнь не удалась',
                'trailer': 'https://www.youtube.com/embed/u-bpwWPNEpE?si=_rbaZyje3L5Ay7ru',
                'releaseYear': '2013-01-01',
                'review': 8,
                'description': 'Хачиман Хикигая семнадцать лет. Это самый яркий представитель пессимистически настроенных людей, он уверен в том, что дружба, любовь и преданность – это самая наглая ложь, а поддержание этой теории - всего лишь договоренность тех, кто однажды ошибся, но признавать этого просто не хочет.',
                'portraitImgName': 'MyYouthRomanticComedyIsWrong.jpg',
                'studios': ['Brain\'s Base', 'Feel'],
                'typeName': 'Сериал',
                'franchise': 'My_Teen_Romantic_Comedy_SNAFU'
            },
            'genres': [
                'Романтика',
                'Комедия',
                'Повседневность'
             ]
        },
        {
            'anime': {
                'name': 'Крутой учитель Онидзука',
                'trailer': 'https://www.youtube.com/embed/aZcEfuNsyKM?si=TjHL6Z1TDCM37wFv',
                'releaseYear': '1999-01-01',
                'review': 9,
                'description': 'Бывший член нагоняющей на горожан ужас банды «Онибаку», байкер Эйкити Онидзука, ставит перед собой цель стать самым крутым школьным учителем. Почему учителем? Да просто в школах полно сексуальных старшеклассниц!',
                'portraitImgName': 'GTO.jpg',
                'studios': ['Studio Pierrot'],
                'typeName': 'Сериал',
                'franchise': 'GTO'
            },
            'genres': [
                'Комедия',
                'Повседневность',
                'Драма',
                'Сёнэн'
            ]
        },
        {
            'anime': {
                'name': 'Богиня благословляет этот прекрасный мир',
                'trailer': 'https://www.youtube.com/embed/s0TXMXF3Qyo?si=OR6ckacFpNSqOszp',
                'releaseYear': '2016-01-01',
                'review': 9,
                'description': 'Кадзума Сато – настоящий затворник, который неожиданно распрощался с жизненной дорогой и оказался в альтернативной реальности. Там он повстречал дерзкую богиню Аква, которая предложила новичку вместо превращения в насекомого воспользоваться уникальным шансом и попасть в игровую вселенную, где необходимо уничтожить Князя Тьмы.',
                'portraitImgName': 'KonoSuba.jpg',
                'studios': ['Studio Deen', 'J.C.STAFF', 'Drive'],
                'typeName': 'Сериал',
                'franchise': 'KonoSuba'
            },
            'genres': [
                'Комедия',
                'Приключения',
                'Пародия',
                'Фэнтези'
            ]
        },
        {
            'anime': {
                'name': 'Бездомный Бог',
                'trailer': 'https://www.youtube.com/embed/gEVlI1ZLpFI?si=LcDCmQhEGTKVWLIg',
                'releaseYear': '2014-01-01',
                'review': 8,
                'description': 'Малоизвестный Бог Ято не имеет собственного храма, но мечтает стать уважаемым божеством с миллионами верующих. Правда, Ято не особо стремится прилагать усилия для достижения данной цели. Однажды обычная школьница Хиёри спасает его от дорожной аварии ценой собственной жизни.',
                'portraitImgName': 'Noragami.jpg',
                'studios': ['Bones'],
                'typeName': 'Сериал',
                'franchise': 'Noragami'
            },
            'genres': [
                'Комедия',
                'Приключения',
                'Сёнэн',
                'Экшен'
            ]
        },
        {
            'anime': {
                'name': 'Самурай Чамплу',
                'trailer': 'https://www.youtube.com/embed/xWKzbhAUeZE?si=jBDl85ajITJcFQL9',
                'releaseYear': '2004-01-01',
                'review': 9,
                'description': 'Мугэн - мечник с повадками брейкдансера, вспыльчивый, грубый и вечно голодный мужлан. Дзин - благородный, хорошо воспитанный ронин, чьё прошлое скрывает мрачную тайну. Нет в мире двух других самураев, настолько непохожих друг на друга - а судьба не только сводит их в поединке, но и заставляет присоединиться к Фуу',
                'portraitImgName': 'Samurai_Champloo.jpg',
                'studios': ['Manglobe'],
                'typeName': 'Сериал',
                'franchise': 'Samurai_Champloo'
            },
            'genres': [
                'Комедия',
                'Приключения',
                'Экшен',
                'Исторический'
            ]
        },
        {
            'anime': {
                'name': 'Сага о Винланде',
                'trailer': 'https://www.youtube.com/embed/Vt7Rwfj7bHU?si=TM8Us0daoqP0lSzB',
                'releaseYear': '2019-01-01',
                'review': 8,
                'description': 'Времена господства викингов. Людей, известных своими жестокими обычаями. Торфинн — сын одного из величайших викингов. Вот только вырос мальчик без отца, так как тот погиб на поле боя. Желая отомстить, Торфинн поклялся убить виновного, однако юноше ещё только предстоит овладеть искусством боя.',
                'portraitImgName': 'Vinland_Saga.jpg',
                'studios': ['Wit Studio', 'MAPPA'],
                'typeName': 'Сериал',
                'franchise': 'Vinland_Saga'
            },
            'genres': [
                'Приключения',
                'Драма',
                'Боевик'
            ]
        },
        {
            'anime': {
                'name': 'Эта фарфоровая кукла влюбилась',
                'trailer': 'https://www.youtube.com/embed/BqrwazH7PhU?si=zIVF2sLdSH0AUyoM',
                'releaseYear': '2022-01-01',
                'review': 8,
                'description': 'Замкнутый старшеклассник Годзё Вакана мечтает мастерить японских кукол. В нём до сих пор живы болезненные воспоминания из детства, когда друг Годзё высмеял его увлечение куклами. Однажды модная жизнерадостная и сексуальная красавица Марин Китагава застала Годзё за шитьем. С этого момента одинокий «кукольник» забыл о тишине и спокойствии.',
                'portraitImgName': 'Sono_Bisque_Doll_wa_Koi_wo_Suru.jpg',
                'studios': ['CloverWorks'],
                'typeName': 'Сериал',
                'franchise': 'My_Dress-Up_Darling'
            },
            'genres': [
                'Повседневность',
                'Романтика',
                'Комедия'
            ]
        },
        {
            'anime': {
                'name': 'Всегда вялый танака-кун',
                'trailer': 'https://www.youtube.com/embed/MWVEG7kDQfo?si=cs6ReW0KU9_y_ADd',
                'releaseYear': '2016-01-01',
                'review': 8,
                'description': 'Танака — обычный школьник, который не проявляет интереса ни к учёбе, ни к спорту, а на уроках всегда спит. Но у юноши есть друг Ота, который во всём проявляет активность и успеваемость. Несмотря на то, что друзья — полные противоположности, они продолжают дружить. До чего же доведёт эта дружба?',
                'portraitImgName': 'Tanaka-kun_wa_Itsumo_Kedaruge.jpg',
                'studios': ['Silver Link'],
                'typeName': 'Сериал',
                'franchise': 'Tanaka-kun_is_Always_Listless'
            },
            'genres': [
                'Повседневность',
                'Сёнэн',
                'Комедия'
            ]
        },
        {
            'anime': {
                'name': 'Моя подруга – демон',
                'trailer': 'https://www.youtube.com/embed/sWhtovYy3E0?si=j0onRNPx9N3EtG52',
                'releaseYear': '2024-01-01',
                'review': 9,
                'description': 'История Хиираги Яцусэ, первокурсника старшей школы, который изо всех сил пытается завести друзей, несмотря на свои усилия угодить другим. Его жизнь принимает неожиданный поворот, когда однажды летним днем ​​он встречает Цумуги, девушку-они (демона), ищущую свою мать в человеческом мире. Таинственным образом начинает падать снег... и начинается их приключение.',
                'portraitImgName': 'MyOniGirl.jpg',
                'studios': ['Studio Colorido'],
                'typeName': 'Сериал',
                'franchise': 'My_Oni_Girl'
            },
            'genres': [
                'Приключения'
            ]
        },
        {
            'anime': {
                'name': 'Маленький гражданин',
                'trailer': 'https://www.youtube.com/embed/U1agV6NfMqU?si=gmpOCDqVnaa3-R9I',
                'releaseYear': '2024-01-01',
                'review': 9,
                'description': 'Кобато хочет стать простым, маленьким человеком. Ему на всю жизнь хватило боли, которую порой приносит работа головой. Именно поэтому он поклялся вместе с одноклассницей Осанай добиться желанного: пойти в старшую школу и тихо-мирно в ней учиться. Увы, но судьба имеет на него другие планы. Что ни день, так случается что-то новое! Так удастся ли Кобато с Осанай хотя бы день прожить спокойно?',
                'portraitImgName': 'HowtoBecomeOrdinary.jpeg',
                'studios': ['Lapin Track'],
                'typeName': 'Сериал',
                'franchise': 'Shoshimin_How_to_Become_Ordinary'
            },
            'genres': [
                'Повседневность',
                'Детектив'
            ]
        },
        {
            'anime': {
                'name': 'ID: Вторжение',
                'trailer': 'https://www.youtube.com/embed/AcvLglA-KfE?si=NNmNfdmVa_Jl6bKz',
                'releaseYear': '2020-01-01',
                'review': 9,
                'description': 'Добро пожаловать в поразительный виртуальный мир! Детективу Сакайдо предстоит расследовать жестокое убийство девочки, о которой известно только имя — Каэру. Это дело отличается от всех, какими он занимался прежде… Ведь сам мир начинает вертеться вокруг него, подвергая сомнению всё, что думает и во что верит Сакайдо!',
                'portraitImgName': 'IdInvaded.jpeg',
                'studios': ['NAZ'],
                'typeName': 'Сериал',
                'franchise': 'Id_Invaded'
            },
            'genres': [
                'Детектив',
                'Психологический триллер',
                'Фантастика'
            ]
        },
        {
            'anime': {
                'name': 'Парад смерти',
                'trailer': 'https://www.youtube.com/embed/EbNKpwe_lM4?si=Y6zryEA5KufTiHQe',
                'releaseYear': '2015-01-01',
                'review': 9,
                'description': 'Что если смерть – это не конец, а лишь начало. Существует ли Рай и Ад? Этот вопрос тысячелетиями терзал человеческий разум. И тайна загробной жизни всегда интересовала смертных. Но что если все гораздо проще? Например, если после смерти вы должны пройти суд, который определит, куда вы должны отправиться – в Ад или на Небеса?',
                'portraitImgName': 'DeathParade.jpeg',
                'studios': ['Madhouse'],
                'typeName': 'Сериал',
                'franchise': 'Death_Parade'
            },
            'genres': [
                'Детектив',
                'Драма',
                'Психологический триллер'
            ]
        },
        {
            'anime': {
                'name': 'Дандадан',
                'trailer': 'https://www.youtube.com/embed/0XJxfbN36Uw?si=MRrXKBhmUV-JVJf3',
                'releaseYear': '2024-01-01',
                'review': 9,
                'description': 'Старшеклассники Момо Аясэ и Кэн Такакуре самозабвенно изучают паранормальные явления. Девушка ищет в нашем мире призраков, а Кэн занят поиском пришельцев. В какой-то момент их изыскания пересекаются. И, о ужас, мир атакуют и призраки, и пришельцы. Особенно досталось Момо, которую похищают пришельцы. Благодаря разблокировке экстрасенсорных способностей девушка сбегает и начинает помогать Кэну. Тот в свою очередь заполучил контроль над мощным духом. Теперь у ребят есть силы для борьбы с жутким врагом, но хватит ли у них решимости?',
                'portraitImgName': 'dandadan.jpeg',
                'studios': ['Science Saru'],
                'typeName': 'Сериал',
                'franchise': 'Dandadan'
            },
            'genres': [
                'Комедия',
                'Экшен',
                'Сёнэн',
                'Сверхъестественное'
            ]
        },
        {
            'anime': {
                'name': 'Вы правда женитесь?',
                'trailer': 'https://www.youtube.com/embed/AiVwg7do7Ik?si=h996Wmyydzjbdj0s',
                'releaseYear': '2024-01-01',
                'review': 8,
                'description': 'Работа в туристическом агентстве безоблачна и интересна. Девушка Рика и парень Такуя довольны сложившимся в офисе укладом. Будучи домоседами и одиночками по жизни, они не стремятся к новым высотам карьерной лестницы. Скорей, наоборот, их пугают любые перспективы изменений на работе и в быту. Узнав о том, что фирма планирует использовать неженатых и незамужних сотрудников для открытия заграничного филиала, Рика и Такуя решаются на фиктивную помолвку. Им кажется, что это простой и надежный выход из сложившейся ситуации, но молодые люди даже не подозревают куда их приведет подобное решение. Так чем же закончится игра во влюбленных голубков?',
                'portraitImgName': '365DaystotheWedding.jpg',
                'studios': ['Ashi Productions'],
                'typeName': 'Сериал',
                'franchise': '365_Days_to_the_Wedding'
            },
            'genres': [
                'Сэйнэн',
                'Романтика'
            ]
        },
        {
            'anime': {
                'name': 'Город, в котором меня нет',
                'trailer': 'https://www.youtube.com/embed/-MfjTJvMLn0?si=Wgks01X5jj7b4Wic',
                'releaseYear': '2016-01-01',
                'review': 9,
                'description': 'Обыкновенный тридцатилетний молодой человек, неудачник в жизни Сатору Фуджинума. Ему почти тридцать, в этом возрасте многие уже управляют фирмами и складывают хорошие счета, герой считает копейки, полученные на развозе пиццы и рисует мангу, в чем он не преуспевает. Но всё не просто, в невзрачном парне кроются большие способности, он обладает «возрождением». Он имеет возможность отмотать часы времени обратно и спасти кого-то от гибели. Дар может проявиться когда угодно, но это не мешает парню помогать людям, хотя порой это проходит как набор случайных событий, от которых остаются травмы.',
                'portraitImgName': 'Erased.jpeg',
                'studios': ['A-1 Pictures'],
                'typeName': 'Сериал',
                'franchise': 'Erased'
            },
            'genres': [
                'Детектив',
                'Психологический триллер',
                'Сверхъестественное',
                'Сэйнэн'
            ]
        },
        {
            'anime': {
                'name': 'Железобетон',
                'trailer': 'https://www.youtube.com/embed/PfQjc2hs34Y?si=zbVHsOM4Y43HjYGO',
                'releaseYear': '2006-01-01',
                'review': 7,
                'description': 'В Городе Сокровищ дети-сироты Чёрный и Белый правят на улицах с помощью насилия и террора. Эти потерянные мальчики абсолютно не похожи друг на друга: Чёрный — негодяй, олицетворяющий всё плохое в городе, а Белый — невинный дурачок, оторванный от мира. Вместе они хотят предотвратить план якудза по превращению города в парк развлечений. Разрушительному Чёрному необходимо спасти город от ужасной судьбы, в то время как добрый Белый должен спасти Чёрного от его тёмной природы.',
                'portraitImgName': 'Tekkonkinkreet.jpeg',
                'studios': ['Studio 4°С'],
                'typeName': 'Фильм',
                'franchise': 'Tekkonkinkreet'
            },
            'genres': [
                'Сэйнэн',
                'Экшен',
                'Приключения',
                'Сверхъестественное',
                'Триллер'
            ]
        },
        {
            'anime': {
                'name': 'Бтууум!',
                'trailer': 'https://www.youtube.com/embed/H92d6YZkVO8?si=c2zEP17p92tyvVEi',
                'releaseYear': '2012-01-01',
                'review': 7,
                'description': 'Мечты сбываются. И парень Рёта Сакамото полностью оценил иронию данного выражения. Ведь что у него было в реальной жизни? Да почти ничего. Ни работы, ни друзей, ни девушки. Он сидит на шее у матери и постоянно играет в онлайн-игры. И там, в этих играх, всё по-другому — Рёта входит в топ-рейтинг игроков Японии онлайн-игры «Btoom!» И однажды молодой человек, которому надоели все проблемы реального мира, просто захотел убежать туда, в виртуальность, и уснул... А проснулся уже на тропическом острове с осознанием того, что он как-то попал в игру. Плохие новости — первый же встречный попытался его убить, причём, видимо, он не один здесь такой псих. Хорошие новости — мечты действительно сбываются! И теперь Рёте придётся со всем этим разбираться.',
                'portraitImgName': 'Btooom.jpeg',
                'studios': ['Madhouse'],
                'typeName': 'Сериал',
                'franchise': 'Btooom'
            },
            'genres': [
                'Сэйнэн',
                'Экшен',
                'Фантастика',
                'Триллер'
            ]
        },
        {
            'anime': {
                'name': 'Сквозь слёзы я притворяюсь кошкой',
                'trailer': 'https://www.youtube.com/embed/Fj9GUyJuu9U?si=yobeC8nNXhIukrlo',
                'releaseYear': '2020-01-01',
                'review': 8,
                'description': 'Миё Сасаки по прозвищу «Мугэ» — активная и яркая девушка, по уши влюблённая в одноклассника Кэнто Хинодэ. Все попытки Миё привлечь внимание юноши заканчиваются провалом, однако ситуация меняется, когда та находит магическую маску, позволяющую превращаться в «Таро» — милую белую кошку, которую так любит Кэнто. Ход событий кажется заманчивым, но со временем граница между девушкой и кошкой начинает исчезать.',
                'portraitImgName': 'AWhiskerAway.jpg',
                'studios': ['Studio Colorido', 'Toho'],
                'typeName': 'Сериал',
                'franchise': 'AWhiskerAway'
            },
            'genres': [
                'Драма',
                'Романтика',
                'Сверхъестественное'
            ]
        },
        {
            'anime': {
                'name': 'Подручный Луизы-Нулизы',
                'trailer': 'https://www.youtube.com/embed/j-UofYKswhI?si=zs3uIGr98k0oGJNR',
                'releaseYear': '2006-01-01',
                'review': 8,
                'description': 'Луиза-Франсуаза де Лавальер учится в Академии волшебства Тристейн. Правда, академические успехи обходят мадмуазель стороной: ей не удается правильно воспроизвести ни одного заклинания, у нее не выходит ни одна трансформация. Но самое тяжелое испытание Луизе (прозванной вредными сокурсниками «Нулизой» сообразно уровню способностей) приходится пережить на втором курсе, в торжественный день Вызова Фамилиаров, талисманов и прислужников начинающих магов. Вместо дракона, саламандры, орла или черной кошки невезучей Луизе достается в ручные любимцы... Хираго Сайто, обыкновенный японский старшеклассник.',
                'portraitImgName': 'ZeronoTsukaima.jpeg',
                'studios': ['J.C.STAFF'],
                'typeName': 'Сериал',
                'franchise': 'zero_no_tsukaima'
            },
            'genres': [
                'Экшен',
                'Приключения',
                'Комедия',
                'Фэнтези',
                'Романтика',
                'Этти',
                'Исэкай'
            ]
        },
        {
            'anime': {
                'name': 'Подручный Луизы-Нулизы: Рыцарь двух лун',
                'trailer': 'https://www.youtube.com/embed/j-UofYKswhI?si=zs3uIGr98k0oGJNR',
                'releaseYear': '2007-01-01',
                'review': 8,
                'description': 'Второй сезон рассказывает о событиях, происходящих через некоторое время после окончания войны. Отношения Луизы и Сайто начинают понемногу налаживаться, ведь она знает, что ради неё Сайто отказался от своей единственной возможности вернуться назад в Токио. И в то время как Луиза начинает использовать загадочную Магию Пустоты из тайной книги, которую ей дала Её Величество Принцесса Генриетта, перед королевством Тристейн появляется новый враг...',
                'portraitImgName': 'Zero_no_Tsukaima_Futatsuki_no_Kishi.jpeg',
                'studios': ['J.C.STAFF'],
                'typeName': 'Сериал',
                'franchise': 'zero_no_tsukaima'
            },
            'genres': [
                'Экшен',
                'Приключения',
                'Комедия',
                'Фэнтези',
                'Романтика',
                'Этти',
                'Исэкай'
            ]
        },
        {
            'anime': {
                'name': 'Подручный Луизы-Нулизы: Хоровод трёх принцесс',
                'trailer': 'https://www.youtube.com/embed/j-UofYKswhI?si=zs3uIGr98k0oGJNR',
                'releaseYear': '2008-01-01',
                'review': 8,
                'description': 'После героических действий Сайто в войне с Альбионом, Сайто и Луиза возвращаются в Тристейн. Однако там их поджидают очередные неприятности — руны Гандальфа на руке Сайто исчезают, и теперь они с Луизой больше не являются мастером и фамильяром. Борясь с очередным кризисом в своих отношениях, они отправляются на поиски эльфа, обладающего силой возвращать умерших к жизни, и который может знать причину того, почему Сайто потерял силу Гандальфа.',
                'portraitImgName': 'Zero_no_Tsukaima_Princesses_no_Rondo.jpeg',
                'studios': ['J.C.STAFF'],
                'typeName': 'Сериал',
                'franchise': 'zero_no_tsukaima'
            },
            'genres': [
                'Экшен',
                'Приключения',
                'Комедия',
                'Фэнтези',
                'Романтика',
                'Этти',
                'Исэкай'
            ]
        },
        {
            'anime': {
                'name': 'Подручный Луизы-Нулизы: Финал',
                'trailer': 'https://www.youtube.com/embed/j-UofYKswhI?si=zs3uIGr98k0oGJNR',
                'releaseYear': '2012-01-01',
                'review': 8,
                'description': 'Четвёртый и последний сезон о приключениях парочки Сайто и Луизы. Сайто и Луиза балансируют на грани своих отношений и чувствуют, что пора делать следующий шаг. Однако прежде личных дел им придётся заняться делами государственными — королева Генриетта посылает их в Ромалию, чтобы заручиться поддержкой Папы, высшего духовного лица. Правда оказалось, что всё не так просто — планы королевы рухнули и возникла угроза с юга, от могущественной Галлии. Но герои не унывают и выбираются с честью из всех переделок, что им уготовила судьба! Ну и по ходу дела разбираются в своих личных делах!',
                'portraitImgName': 'Zero_no_Tsukaima_F.jpeg',
                'studios': ['J.C.STAFF'],
                'typeName': 'Сериал',
                'franchise': 'zero_no_tsukaima'
            },
            'genres': [
                'Экшен',
                'Приключения',
                'Комедия',
                'Фэнтези',
                'Романтика',
                'Этти',
                'Исэкай'
            ]
        },
        {
            'anime': {
                'name': 'Провожающая в последний путь Фрирен',
                'trailer': 'https://www.youtube.com/embed/4sAOCa4rtuM?si=G3D4N0bdIPARDcBf',
                'releaseYear': '2024-01-01',
                'review': 9,
                'description': 'Одержав победу над Королём демонов, отряд героя Химмеля вернулся домой. Приключение, растянувшееся на десятилетие, подошло к завершению. Волшебница-эльф Фрирен и её отважные товарищи принесли людям мир и разошлись в разные стороны, чтобы спокойно прожить остаток жизни. Однако не всех членов отряда ждёт одинаковая участь. Для эльфов время течёт иначе, поэтому Фрирен вынужденно становится свидетелем того, как её спутники один за другим постепенно уходят из жизни. Девушка осознала, что годы, проведённые в отряде героя, пронеслись в один миг, как падающая звезда в бескрайнем космосе её жизни, и столкнулась с сожалениями об упущенных возможностях. Сможет ли она смириться со смертью друзей и понять, что значит жизнь для окружающих её людей? Фрирен начинает новое путешествие, чтобы найти ответ.',
                'portraitImgName': 'Frieren_Beyond_Journeys_End.jpeg',
                'studios': ['Madhouse'],
                'typeName': 'Сериал',
                'franchise': 'frieren'
            },
            'genres': [
                'Сёнен',
                'Приключения',
                'Драма',
                'Фэнтези'
            ]
        }
    ]

    base_dir = Path(__file__).parent
    photo_path = base_dir / 'initial_photos' / 'anime' / 'portraitImage'

    for animeField in animesField:
        files = photo_path.glob(animeField['anime']['portraitImgName'])
        files = [file for file in files if file.is_file()]
        with open(files[0].relative_to(os.getcwd(), walk_up=True), 'rb') as file:
            djangoFile = File(file, name=animeField['anime']['portraitImgName'])
            createdAnime = anime.objects.create (
                name=animeField['anime']['name'],
                trailer=animeField['anime']['trailer'],
                releaseYear=animeField['anime']['releaseYear'],
                review=animeField['anime']['review'],
                description=animeField['anime']['description'],
                portraitImage=djangoFile,
                type_field = types_model.objects.get(name=animeField['anime']['typeName']),
                franchise = franchises_model.objects.get(name=animeField['anime']['franchise'])
            )
        for animeStudioName in animeField['anime']['studios']:
            createdAnime.studio.add(studiosModel.objects.get(name=animeStudioName))
        for genre in animeField['genres']:
            genreAnime.objects.create(animeID = createdAnime, genreID=genres.objects.get(name=genre))

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addGenres),
        migrations.RunPython(addStudios),
        migrations.RunPython(addTypes),
        migrations.RunPython(addFranchises),
        migrations.RunPython(addAnime)
    ]