# -*- coding: utf-8 -*-
"""Этап 6 — Медицинский туризм. RU /medical-tourism/ + полная EN /en/medical-tourism/.

Только реальные возможности платформы: врачи, онлайн-запись, медкарта, 3 языка.
Никаких обещаний трансферов, отелей и услуг, которых нет.
"""
from engine import Page, DOMAIN, BRAND, alts


def _svc(name, desc, url, lang):
    return {"@type": "Service", "name": name, "description": desc,
            "serviceType": "Medical tourism" if lang == "en" else "Медицинский туризм",
            "provider": {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/"},
            "areaServed": {"@type": "Country", "name": "Uzbekistan" if lang == "en" else "Узбекистан"},
            "availableChannel": {"@type": "ServiceChannel", "serviceUrl": DOMAIN + url}}


# ===================================================================== RU
def ru_index():
    body = """
<p class="lede"><strong>Медицинский туризм в Узбекистане — это лечение и обследование для
гостей из других стран по доступным ценам.</strong> Всё чаще пациенты приезжают в Узбекистан за
стоматологией, чекапами и консультациями специалистов, а AIVITA помогает организовать
медицинскую часть поездки: найти врача, записаться и вести медкарту на своём языке.</p>

<h2>Почему Узбекистан?</h2>
<p>У медицинского туризма в Узбекистане несколько причин. Во-первых, цены на многие медицинские
и стоматологические услуги заметно ниже, чем в Европе и ряде соседних стран, при сопоставимом
качестве в хороших частных клиниках. Во-вторых, для граждан многих государств действует
безвизовый въезд или упрощённая электронная виза, что облегчает поездку. В-третьих, страна
удобно расположена и хорошо связана авиасообщением с регионом.</p>

<h2>Что чаще всего лечат?</h2>
<p>Наиболее популярные направления — <a href="/medical-tourism/dental/">стоматология</a>
(лечение, протезирование, имплантация), комплексные <a href="/medical-tourism/checkup/">
обследования и чекапы</a>, консультации узких специалистов. Частные клиники крупных городов —
Ташкента, Самарканда — предлагают современное оборудование и врачей с опытом, а разница в цене
позволяет совместить лечение с поездкой.</p>

<h2>Как AIVITA помогает медицинскому туристу?</h2>
<p>AIVITA — это цифровой помощник для медицинской части поездки. Через платформу можно заранее
проконсультироваться с врачом онлайн, выбрать специалиста, записаться на приём и вести
<a href="/features/medcard/">электронную медкарту</a> на русском, узбекском или английском
языке. Это снимает языковой барьер и помогает спланировать лечение ещё до приезда. Подробнее —
на странице <a href="/medical-tourism/how-it-works/">как это работает</a>.</p>

<h2>Честно о том, что мы делаем и не делаем</h2>
<p>AIVITA помогает именно с медицинской частью: поиск врача, онлайн-консультации, запись,
хранение медкарты и общение на понятном языке. Мы не занимаемся организацией перелётов,
трансферов и проживания и не обещаем того, чего не предоставляем. Вопросы визы, билетов и
гостиниц вы решаете самостоятельно или через профильные сервисы, а медицинскую часть берёт на
себя AIVITA.</p>

<h2>С чего начать?</h2>
<p>Начните с онлайн-консультации: опишите задачу врачу, обсудите варианты и план. Так вы приедете
уже с пониманием, что и где будете делать, а история консультаций и рекомендаций сохранится в
медкарте. Это экономит время на месте и делает поездку предсказуемой.</p>
"""
    faq = [
        ("Почему лечиться в Узбекистане выгодно?", "Цены на многие медицинские и стоматологические услуги ниже, чем в Европе и ряде соседних стран, при хорошем качестве в частных клиниках. Для граждан многих стран действует безвизовый въезд или электронная виза."),
        ("Что чаще всего лечат медицинские туристы?", "Наиболее популярны стоматология, комплексные обследования и чекапы, а также консультации узких специалистов."),
        ("Как AIVITA помогает медицинскому туристу?", "AIVITA помогает с медицинской частью: онлайн-консультация до приезда, выбор врача, запись и ведение медкарты на русском, узбекском или английском."),
        ("Организует ли AIVITA перелёты и отели?", "Нет. AIVITA занимается только медицинской частью — врачи, консультации, запись и медкарта. Визу, билеты и проживание вы организуете самостоятельно."),
        ("На каком языке можно общаться?", "На русском, узбекском и английском. Это снимает языковой барьер при планировании и во время лечения."),
    ]
    return Page(
        path="medical-tourism", lang="ru",
        title="Медицинский туризм в Узбекистане — лечение и обследование | AIVITA",
        description="Медицинский туризм в Узбекистане: доступные цены на стоматологию, чекапы и консультации специалистов. AIVITA помогает с медицинской частью — врач онлайн, запись и медкарта на 3 языках.",
        h1="Медицинский туризм в Узбекистане",
        body=body, faq=faq, section="medical-tourism",
        crumbs=[("Главная", "/"), ("Медицинский туризм", None)],
        hreflang=alts("medical-tourism", langs=("ru", "en")),
        disclaimer=True,
        related=[("Стоматологический туризм", "/medical-tourism/dental/"),
                 ("Обследование для иностранцев", "/medical-tourism/checkup/"),
                 ("Как это работает", "/medical-tourism/how-it-works/")],
    )


def ru_dental():
    body = """
<p class="lede"><strong>Стоматологический туризм в Узбекистане — это лечение и протезирование
зубов для гостей из других стран по ценам заметно ниже европейских.</strong> Стоматология —
одно из самых востребованных направлений медицинского туризма, потому что качественное лечение
за рубежом часто обходится дорого, а в Узбекистане сопоставимые услуги стоят меньше.</p>

<h2>Почему едут лечить зубы в Узбекистан?</h2>
<p>Главная причина — соотношение цены и качества. Лечение кариеса, протезирование, имплантация и
эстетическая стоматология в хороших частных клиниках крупных городов выполняются на современном
оборудовании, а стоимость ниже, чем во многих странах. Для объёмных работ — нескольких имплантов
или полного протезирования — разница в цене может окупить саму поездку.</p>

<h2>Какие услуги востребованы?</h2>
<p>Чаще всего медицинские туристы обращаются за имплантацией, протезированием, лечением и
восстановлением зубов, а также за эстетическими процедурами. Такие работы требуют планирования и
иногда нескольких визитов, поэтому важно заранее обсудить план с врачом — это удобно сделать
онлайн через AIVITA ещё до приезда.</p>

<h2>Как AIVITA помогает спланировать лечение зубов?</h2>
<p>Через AIVITA можно заранее проконсультироваться со <a href="/doctors/stomatolog/">
стоматологом</a> онлайн, описать задачу, приложить снимки и результаты и обсудить примерный план
и порядок визитов. Вся история хранится в <a href="/features/medcard/">медкарте</a> на удобном
языке. Так вы приезжаете уже с планом, а не тратите время на месте, и понимаете, чего ожидать.</p>

<h2>Что важно учесть?</h2>
<p>Стоматологическое лечение и процедуры проводятся очно в клинике — онлайн-консультация помогает
спланировать, но не заменяет приём. Объёмные работы требуют времени, поэтому закладывайте
достаточно дней на поездку. Уточняйте план, сроки и гарантии непосредственно у клиники и врача.
AIVITA помогает с медицинской частью и общением, но не занимается организацией поездки.</p>

<h2>С чего начать?</h2>
<p>Начните с онлайн-консультации стоматолога: обсудите, что нужно сделать, сколько это займёт и
как спланировать визиты. Имея план и записанную историю в медкарте, вы сможете спокойно
организовать поездку и приехать подготовленным.</p>
"""
    faq = [
        ("Почему лечить зубы в Узбекистане дешевле?", "Стоимость стоматологических услуг здесь ниже, чем во многих странах, при современном оборудовании и опытных врачах в хороших частных клиниках. На объёмных работах разница особенно заметна."),
        ("Какие стоматологические услуги востребованы у туристов?", "Имплантация, протезирование, лечение и восстановление зубов, эстетическая стоматология."),
        ("Можно ли спланировать лечение зубов заранее?", "Да. Через AIVITA можно проконсультироваться со стоматологом онлайн, приложить снимки и обсудить план и порядок визитов до приезда."),
        ("Заменяет ли онлайн-консультация приём?", "Нет. Лечение и процедуры проводятся очно. Онлайн помогает спланировать поездку и понять объём работ."),
        ("Сколько времени закладывать на поездку?", "Зависит от объёма: имплантация и протезирование могут требовать нескольких визитов. Уточняйте сроки у врача заранее."),
    ]
    return Page(
        path="medical-tourism/dental", lang="ru",
        title="Стоматологический туризм в Узбекистане — лечение зубов | AIVITA",
        description="Стоматологический туризм в Узбекистане: имплантация, протезирование и лечение зубов по ценам ниже европейских. Планирование лечения онлайн со стоматологом через AIVITA на 3 языках.",
        h1="Стоматологический туризм в Узбекистане",
        body=body, faq=faq, section="medical-tourism",
        crumbs=[("Главная", "/"), ("Медицинский туризм", "/medical-tourism/"), ("Стоматология", None)],
        hreflang=alts("medical-tourism/dental", langs=("ru", "en")),
        disclaimer=True,
        related=[("Медицинский туризм", "/medical-tourism/"),
                 ("Стоматолог онлайн", "/doctors/stomatolog/"),
                 ("Как это работает", "/medical-tourism/how-it-works/")],
    )


def ru_checkup():
    body = """
<p class="lede"><strong>Обследование для иностранцев в Узбекистане — это возможность пройти
комплексный чекап организма по доступной цене во время поездки.</strong> Многие приезжают
специально ради диагностики: проверить здоровье, сдать анализы и получить консультации
специалистов дешевле, чем дома, и без долгого ожидания.</p>

<h2>Что такое медицинский чекап?</h2>
<p>Чекап — это комплексная профилактическая проверка состояния здоровья: набор анализов,
инструментальных исследований и консультаций. Он помогает оценить основные показатели, выявить
скрытые риски и получить рекомендации. Для медицинских туристов чекап удобен тем, что позволяет
за короткий срок пройти многое в одном месте.</p>

<h2>Почему обследоваться в Узбекистане удобно?</h2>
<p>Стоимость лабораторных и инструментальных исследований в Узбекистане ниже, чем во многих
странах, а частные клиники крупных городов предлагают современное оборудование и быстрый доступ
без долгих очередей. Это позволяет совместить обследование с поездкой и уложиться в несколько
дней. Начать оценку здоровья можно ещё до приезда с <a href="/features/ai-checkup/">AI-чекапа</a>
в приложении.</p>

<h2>Как AIVITA помогает с обследованием?</h2>
<p>Через AIVITA можно заранее обсудить с врачом онлайн, какие исследования вам нужны, чтобы не
делать лишнего. После обследования результаты удобно хранить в <a href="/features/medcard/">
электронной медкарте</a> и обсуждать их с врачом — на русском, узбекском или английском.
Расшифровку и рекомендации можно получить онлайн, в том числе уже после возвращения домой.</p>

<h2>Что важно знать?</h2>
<p>Сами исследования (анализы, УЗИ, осмотры) проводятся очно в клинике. AIVITA помогает
спланировать обследование, сохранить и разобрать результаты, но не заменяет лабораторию.
Объём чекапа стоит подбирать индивидуально с врачом, а не делать «всё подряд»: разумный набор
исследований информативнее и дешевле избыточного.</p>

<h2>С чего начать?</h2>
<p>Начните с онлайн-консультации: врач поможет определить, какой чекап вам подходит, исходя из
возраста, жалоб и целей. Так вы приедете с планом обследования и не потратите время и деньги на
лишнее, а результаты останутся с вами в медкарте.</p>
"""
    faq = [
        ("Что такое медицинский чекап?", "Это комплексная профилактическая проверка здоровья: анализы, исследования и консультации, которые помогают оценить основные показатели и выявить скрытые риски."),
        ("Почему обследоваться в Узбекистане выгодно?", "Стоимость исследований ниже, чем во многих странах, а частные клиники предлагают современное оборудование и быстрый доступ без долгих очередей."),
        ("Как AIVITA помогает с обследованием?", "Помогает заранее обсудить нужные исследования онлайн, хранить результаты в медкарте и разобрать их с врачом на удобном языке, в том числе после возвращения домой."),
        ("Можно ли начать до приезда?", "Да, можно пройти AI-чекап в приложении и обсудить с врачом, какой набор обследований подойдёт именно вам."),
        ("Заменяет ли AIVITA лабораторию?", "Нет. Анализы и исследования проводятся очно в клинике. AIVITA помогает спланировать, сохранить и разобрать результаты."),
    ]
    return Page(
        path="medical-tourism/checkup", lang="ru",
        title="Обследование и чекап для иностранцев в Узбекистане | AIVITA",
        description="Медицинское обследование и чекап для иностранцев в Узбекистане по доступной цене. Планирование и расшифровка результатов онлайн с врачом через AIVITA, медкарта на 3 языках.",
        h1="Обследование для иностранцев в Узбекистане",
        body=body, faq=faq, section="medical-tourism",
        crumbs=[("Главная", "/"), ("Медицинский туризм", "/medical-tourism/"), ("Обследование", None)],
        hreflang=alts("medical-tourism/checkup", langs=("ru", "en")),
        disclaimer=True,
        related=[("Медицинский туризм", "/medical-tourism/"),
                 ("AI-чекап организма", "/features/ai-checkup/"),
                 ("Как это работает", "/medical-tourism/how-it-works/")],
    )


def ru_how():
    body = """
<p class="lede"><strong>AIVITA помогает организовать медицинскую часть поездки в Узбекистан:
найти врача, проконсультироваться онлайн до приезда, записаться на приём и вести медкарту на
своём языке.</strong> Мы отвечаем за медицину и общение, а не за перелёты и отели.</p>

<h2>Шаг 1. Консультация до приезда</h2>
<p>Всё начинается с онлайн-консультации. Вы описываете задачу — лечение зубов, обследование,
консультация специалиста — и обсуждаете с врачом план ещё дома. Это помогает понять, что вас
ждёт, сколько времени займёт и как подготовиться, чтобы не терять дни на месте.</p>

<h2>Шаг 2. Выбор врача и запись</h2>
<p>Через <a href="/features/doctors/">каталог AIVITA</a> вы выбираете специалиста нужного
профиля, смотрите профиль и записываетесь на удобное время. Заранее известные план и запись
делают поездку предсказуемой: вы приезжаете к конкретному врачу в конкретное время.</p>

<h2>Шаг 3. Электронная медкарта</h2>
<p>Вся история — консультации, снимки, анализы, назначения — хранится в
<a href="/features/medcard/">электронной медкарте</a> и доступна вам и врачу с вашего
разрешения. Не нужно возить бумажные документы: всё под рукой в телефоне, а после возвращения
домой вы сохраняете доступ к результатам и рекомендациям.</p>

<h2>Шаг 4. Общение на трёх языках</h2>
<p>Языковой барьер — частая проблема медицинского туризма. AIVITA работает на русском, узбекском
и английском, поэтому вы понимаете врача, а врач — вас. Это особенно важно, когда речь идёт о
здоровье и точности назначений.</p>

<h2>Что делает AIVITA, а что — нет</h2>
<p>AIVITA берёт на себя медицинскую часть: поиск врача, онлайн-консультации, запись, медкарту и
общение на понятном языке. Мы не организуем визы, билеты, трансферы и проживание и не обещаем
услуг, которых не оказываем. Такое честное разделение помогает вам точно понимать, на что
рассчитывать.</p>

<h2>Итог</h2>
<p>С AIVITA медицинская часть поездки становится понятной и управляемой: вы приезжаете с планом,
записью и врачом, который вас ждёт, а история здоровья остаётся с вами. Начните с
<a href="/medical-tourism/">онлайн-консультации</a> — и спланируйте лечение заранее.</p>
"""
    faq = [
        ("Как AIVITA помогает организовать лечение?", "Через онлайн-консультацию до приезда, выбор врача и запись, ведение медкарты и общение на трёх языках. Вы приезжаете с готовым планом."),
        ("Можно ли проконсультироваться до приезда?", "Да. Онлайн-консультация помогает обсудить план, сроки и подготовку ещё дома, чтобы не терять время на месте."),
        ("Где хранятся мои медицинские данные?", "В электронной медкарте, доступной вам и врачу с вашего разрешения. Доступ сохраняется и после возвращения домой."),
        ("Организует ли AIVITA визу, билеты и отель?", "Нет. AIVITA отвечает только за медицинскую часть. Визу, билеты и проживание вы организуете самостоятельно."),
        ("На каких языках работает платформа?", "На русском, узбекском и английском — это снимает языковой барьер при планировании и лечении."),
    ]
    return Page(
        path="medical-tourism/how-it-works", lang="ru",
        title="Как AIVITA помогает медицинскому туристу в Узбекистане | AIVITA",
        description="Как это работает: AIVITA помогает медицинскому туристу в Узбекистане — онлайн-консультация до приезда, выбор врача и запись, электронная медкарта и общение на 3 языках. Без организации поездки.",
        h1="Как AIVITA помогает медицинскому туристу",
        body=body, faq=faq, section="medical-tourism",
        crumbs=[("Главная", "/"), ("Медицинский туризм", "/medical-tourism/"), ("Как это работает", None)],
        hreflang=alts("medical-tourism/how-it-works", langs=("ru", "en")),
        disclaimer=False,
        related=[("Медицинский туризм", "/medical-tourism/"),
                 ("Врачи онлайн", "/features/doctors/"),
                 ("Электронная медкарта", "/features/medcard/")],
    )


# ===================================================================== EN
EN_CTA = ("Plan the medical part of your trip with AIVITA",
          "Consult a doctor online before you arrive, choose a specialist, book an appointment and keep your medical card — in English.",
          "See how it works", "/en/medical-tourism/how-it-works/")


def en_index():
    body = """
<p class="lede"><strong>Medical tourism in Uzbekistan means affordable treatment and health
check-ups for visitors from other countries.</strong> More and more patients come to Uzbekistan
for dental care, check-ups and specialist consultations, and AIVITA helps you organise the
medical side of the trip: find a doctor, book an appointment and keep your medical records in
your own language.</p>

<h2>Why Uzbekistan?</h2>
<p>Medical tourism in Uzbekistan is growing for several reasons. First, many medical and dental
services cost noticeably less than in Europe and some neighbouring countries, while quality in
good private clinics is comparable. Second, citizens of many countries can enter Uzbekistan
visa-free or with a simplified e-visa, which makes the trip easier. Third, the country is
conveniently located and well connected by air within the region.</p>

<h2>What do people come for?</h2>
<p>The most popular directions are <a href="/en/medical-tourism/dental/">dental care</a>
(treatment, prosthetics, implants), comprehensive
<a href="/en/medical-tourism/checkup/">health check-ups</a>, and consultations with specialists.
Private clinics in major cities such as Tashkent and Samarkand offer modern equipment and
experienced doctors, and the price difference lets you combine treatment with travel.</p>

<h2>How AIVITA helps a medical traveller</h2>
<p>AIVITA is a digital assistant for the medical part of your trip. Through the platform you can
consult a doctor online in advance, choose a specialist, book an appointment and keep an
<a href="/en/features/">electronic medical card</a> in English, Russian or Uzbek. This removes
the language barrier and helps you plan treatment before you even arrive. Learn more on the
<a href="/en/medical-tourism/how-it-works/">how it works</a> page.</p>

<h2>Honest about what we do and don't do</h2>
<p>AIVITA helps with the medical part: finding a doctor, online consultations, booking, storing
your medical card and communicating in a language you understand. We do not arrange flights,
transfers or accommodation, and we don't promise services we don't provide. Visas, tickets and
hotels you arrange yourself; the medical side is handled by AIVITA.</p>

<h2>Where to start</h2>
<p>Start with an online consultation: describe your goal to a doctor, discuss the options and a
plan. This way you arrive already knowing what you'll do and where, and your history of
consultations and recommendations stays in your medical card.</p>
"""
    faq = [
        ("Why is treatment in Uzbekistan cost-effective?", "Many medical and dental services cost less than in Europe and some neighbouring countries, with good quality in private clinics. Citizens of many countries can enter visa-free or with an e-visa."),
        ("What do medical tourists come for?", "Most often dental care, comprehensive check-ups, and consultations with specialists."),
        ("How does AIVITA help a medical traveller?", "AIVITA helps with the medical part: an online consultation before arrival, choosing a doctor, booking and keeping your medical card in English, Russian or Uzbek."),
        ("Does AIVITA arrange flights and hotels?", "No. AIVITA handles only the medical part — doctors, consultations, booking and medical records. Visas, tickets and accommodation you organise yourself."),
        ("What languages can I use?", "English, Russian and Uzbek. This removes the language barrier when planning and during treatment."),
    ]
    return Page(
        path="en/medical-tourism", lang="en",
        title="Medical Tourism in Uzbekistan — Treatment & Check-ups | AIVITA",
        description="Medical tourism in Uzbekistan: affordable dental care, health check-ups and specialist consultations. AIVITA helps with the medical part — doctor online, booking and medical card in 3 languages.",
        h1="Medical Tourism in Uzbekistan",
        body=body, faq=faq, section="medical-tourism",
        crumbs=[("Home", "/en/"), ("Medical tourism", None)],
        hreflang=alts("medical-tourism", langs=("ru", "en")),
        disclaimer=True, cta=EN_CTA,
        related=[("Dental tourism", "/en/medical-tourism/dental/"),
                 ("Health check-up for foreigners", "/en/medical-tourism/checkup/"),
                 ("How it works", "/en/medical-tourism/how-it-works/")],
    )


def en_dental():
    body = """
<p class="lede"><strong>Dental tourism in Uzbekistan means dental treatment and prosthetics for
international visitors at prices well below European ones.</strong> Dentistry is one of the most
popular medical tourism directions, because quality dental care abroad is often expensive, while
in Uzbekistan comparable services cost less.</p>

<h2>Why come to Uzbekistan for dental care?</h2>
<p>The main reason is the balance of price and quality. Fillings, prosthetics, implants and
aesthetic dentistry in good private clinics of major cities are done with modern equipment, while
the cost is lower than in many countries. For larger work — several implants or full prosthetics —
the price difference can pay for the trip itself.</p>

<h2>Which services are in demand?</h2>
<p>Most often medical tourists come for implants, prosthetics, treatment and restoration of
teeth, and aesthetic procedures. Such work requires planning and sometimes several visits, so it
is important to discuss the plan with a dentist in advance — which is easy to do online through
AIVITA before you arrive.</p>

<h2>How AIVITA helps you plan dental treatment</h2>
<p>Through AIVITA you can consult a <a href="/en/features/">dentist online</a> in advance,
describe your goal, attach images and results, and discuss an approximate plan and order of
visits. Your whole history is stored in the electronic medical card in a language you understand.
So you arrive with a plan instead of losing time on site, and you know what to expect.</p>

<h2>What to keep in mind</h2>
<p>Dental treatment and procedures are performed in person at the clinic — an online consultation
helps you plan but does not replace a visit. Larger work takes time, so allow enough days for the
trip. Confirm the plan, timelines and guarantees directly with the clinic and dentist. AIVITA
helps with the medical part and communication, not with organising the trip.</p>

<h2>Where to start</h2>
<p>Start with an online dentist consultation: discuss what needs to be done, how long it will
take and how to plan the visits. With a plan and a recorded history in your medical card, you can
calmly organise the trip and arrive prepared.</p>
"""
    faq = [
        ("Why is dental care in Uzbekistan cheaper?", "Dental services cost less than in many countries, with modern equipment and experienced dentists in good private clinics. The difference is especially noticeable on larger work."),
        ("Which dental services are popular with tourists?", "Implants, prosthetics, treatment and restoration of teeth, and aesthetic dentistry."),
        ("Can I plan dental treatment in advance?", "Yes. Through AIVITA you can consult a dentist online, attach images and discuss the plan and order of visits before arrival."),
        ("Does an online consultation replace a visit?", "No. Treatment and procedures are done in person. Online helps you plan the trip and understand the scope of work."),
        ("How many days should I allow?", "It depends on the scope: implants and prosthetics may require several visits. Confirm timelines with the dentist in advance."),
    ]
    return Page(
        path="en/medical-tourism/dental", lang="en",
        title="Dental Tourism in Uzbekistan (Tashkent) — Implants & Prosthetics | AIVITA",
        description="Dental tourism in Uzbekistan and Tashkent: implants, prosthetics and dental treatment at prices below European ones. Plan treatment online with a dentist via AIVITA in 3 languages.",
        h1="Dental Tourism in Uzbekistan",
        body=body, faq=faq, section="medical-tourism",
        crumbs=[("Home", "/en/"), ("Medical tourism", "/en/medical-tourism/"), ("Dental", None)],
        hreflang=alts("medical-tourism/dental", langs=("ru", "en")),
        disclaimer=True, cta=EN_CTA,
        related=[("Medical tourism", "/en/medical-tourism/"),
                 ("Health check-up for foreigners", "/en/medical-tourism/checkup/"),
                 ("How it works", "/en/medical-tourism/how-it-works/")],
    )


def en_checkup():
    body = """
<p class="lede"><strong>A health check-up for foreigners in Uzbekistan is a chance to have a
comprehensive body check-up at an affordable price during your trip.</strong> Many people come
specifically for diagnostics: to check their health, run tests and get specialist consultations
cheaper than at home and without long waiting.</p>

<h2>What is a medical check-up?</h2>
<p>A check-up is a comprehensive preventive assessment of your health: a set of tests, instrumental
examinations and consultations. It helps evaluate key indicators, reveal hidden risks and get
recommendations. For medical tourists a check-up is convenient because it lets you go through a
lot in one place within a short time.</p>

<h2>Why get checked in Uzbekistan?</h2>
<p>The cost of laboratory and instrumental tests in Uzbekistan is lower than in many countries,
and private clinics in major cities offer modern equipment and quick access without long queues.
This lets you combine the check-up with your trip and fit it into a few days. You can begin
assessing your health before arrival with the <a href="/en/features/">AI check-up</a> in the app.</p>

<h2>How AIVITA helps with the check-up</h2>
<p>Through AIVITA you can discuss with a doctor online in advance which examinations you actually
need, so you don't do anything unnecessary. After the check-up, results are convenient to store in
your electronic medical card and discuss with a doctor — in English, Russian or Uzbek. You can get
the interpretation and recommendations online, including after you return home.</p>

<h2>What to keep in mind</h2>
<p>The examinations themselves (tests, ultrasound, physical exams) are done in person at the
clinic. AIVITA helps you plan the check-up, store and review the results, but does not replace a
laboratory. The scope of the check-up is best chosen individually with a doctor rather than doing
"everything at once": a sensible set of tests is more informative and cheaper than an excessive one.</p>

<h2>Where to start</h2>
<p>Start with an online consultation: a doctor will help decide which check-up suits you based on
your age, complaints and goals. This way you arrive with an examination plan and don't waste time
and money on the unnecessary, while the results stay with you in your medical card.</p>
"""
    faq = [
        ("What is a medical check-up?", "A comprehensive preventive assessment of health: tests, examinations and consultations that help evaluate key indicators and reveal hidden risks."),
        ("Why get a check-up in Uzbekistan?", "Tests cost less than in many countries, and private clinics offer modern equipment and quick access without long queues."),
        ("How does AIVITA help with a check-up?", "It helps discuss the needed examinations online in advance, store results in your medical card and review them with a doctor in your language, including after you return home."),
        ("Can I start before arrival?", "Yes, you can run an AI check-up in the app and discuss with a doctor which set of examinations suits you."),
        ("Does AIVITA replace a laboratory?", "No. Tests and examinations are done in person at the clinic. AIVITA helps you plan, store and review the results."),
    ]
    return Page(
        path="en/medical-tourism/checkup", lang="en",
        title="Health Check-up in Uzbekistan for Foreigners — Price & Plan | AIVITA",
        description="Health check-up in Uzbekistan for foreigners at an affordable price. Plan examinations and review results online with a doctor via AIVITA, medical card in 3 languages.",
        h1="Health Check-up for Foreigners in Uzbekistan",
        body=body, faq=faq, section="medical-tourism",
        crumbs=[("Home", "/en/"), ("Medical tourism", "/en/medical-tourism/"), ("Check-up", None)],
        hreflang=alts("medical-tourism/checkup", langs=("ru", "en")),
        disclaimer=True, cta=EN_CTA,
        related=[("Medical tourism", "/en/medical-tourism/"),
                 ("Dental tourism", "/en/medical-tourism/dental/"),
                 ("How it works", "/en/medical-tourism/how-it-works/")],
    )


def en_how():
    body = """
<p class="lede"><strong>AIVITA helps you organise the medical part of a trip to Uzbekistan: find
a doctor, consult online before arrival, book an appointment and keep your medical card in your
language.</strong> We handle medicine and communication — not flights and hotels.</p>

<h2>Step 1. Consultation before arrival</h2>
<p>Everything starts with an online consultation. You describe your goal — dental treatment, a
check-up, a specialist consultation — and discuss a plan with a doctor while still at home. This
helps you understand what to expect, how long it will take and how to prepare, so you don't lose
days on site.</p>

<h2>Step 2. Choosing a doctor and booking</h2>
<p>Through the AIVITA catalogue you choose a specialist of the right profile, view the profile and
book a convenient time. A known plan and booking make the trip predictable: you arrive to a
specific doctor at a specific time.</p>

<h2>Step 3. Electronic medical card</h2>
<p>Your whole history — consultations, images, tests, prescriptions — is stored in the electronic
medical card and available to you and the doctor with your permission. No need to carry paper
documents: everything is in your phone, and after you return home you keep access to the results
and recommendations.</p>

<h2>Step 4. Communication in three languages</h2>
<p>The language barrier is a common problem in medical tourism. AIVITA works in English, Russian
and Uzbek, so you understand the doctor and the doctor understands you. This matters especially
when it comes to health and the accuracy of prescriptions.</p>

<h2>What AIVITA does and does not do</h2>
<p>AIVITA handles the medical part: finding a doctor, online consultations, booking, the medical
card and communication in a clear language. We do not arrange visas, tickets, transfers or
accommodation, and we don't promise services we don't provide. This honest split helps you know
exactly what to count on.</p>

<h2>In short</h2>
<p>With AIVITA the medical part of the trip becomes clear and manageable: you arrive with a plan,
a booking and a doctor expecting you, while your health history stays with you. Start with an
<a href="/en/medical-tourism/">online consultation</a> and plan your treatment in advance.</p>
"""
    faq = [
        ("How does AIVITA help organise treatment?", "Through an online consultation before arrival, choosing a doctor and booking, keeping a medical card and communicating in three languages. You arrive with a ready plan."),
        ("Can I consult before arrival?", "Yes. An online consultation helps discuss the plan, timelines and preparation while still at home, so you don't lose time on site."),
        ("Where is my medical data stored?", "In an electronic medical card available to you and the doctor with your permission. Access remains after you return home."),
        ("Does AIVITA arrange visa, tickets and hotel?", "No. AIVITA is responsible only for the medical part. Visas, tickets and accommodation you organise yourself."),
        ("What languages does the platform support?", "English, Russian and Uzbek — this removes the language barrier when planning and during treatment."),
    ]
    return Page(
        path="en/medical-tourism/how-it-works", lang="en",
        title="How AIVITA Helps Medical Tourists in Uzbekistan | AIVITA",
        description="How it works: AIVITA helps medical tourists in Uzbekistan — online consultation before arrival, choosing a doctor and booking, electronic medical card and communication in 3 languages.",
        h1="How AIVITA Helps Medical Tourists",
        body=body, faq=faq, section="medical-tourism",
        crumbs=[("Home", "/en/"), ("Medical tourism", "/en/medical-tourism/"), ("How it works", None)],
        hreflang=alts("medical-tourism/how-it-works", langs=("ru", "en")),
        disclaimer=False, cta=EN_CTA,
        related=[("Medical tourism", "/en/medical-tourism/"),
                 ("Dental tourism", "/en/medical-tourism/dental/"),
                 ("Health check-up for foreigners", "/en/medical-tourism/checkup/")],
    )


def pages():
    return [ru_index(), ru_dental(), ru_checkup(), ru_how(),
            en_index(), en_dental(), en_checkup(), en_how()]
