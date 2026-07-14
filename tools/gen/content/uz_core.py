# -*- coding: utf-8 -*-
"""Этап 9 (uz) — ядро: bosh sahifa, imkoniyatlar (hub+6), kimlar uchun (3), biz haqimizda."""
from engine import Page, DOMAIN, BRAND, alts

CRF = ("Imkoniyatlar", "/uz/features/")


def home():
    body = """
<p class="lede"><strong>AIVITA — O‘zbekistonda sog‘liqni saqlash bo‘yicha raqamli
ekotizim.</strong> Bitta ilovada siz 60 soniyada AI-checkupdan o‘tasiz, elektron tibbiy karta
yuritasiz, dori mosligini tekshirasiz, aqlli soatlardan sog‘liq ko‘rsatkichlarini kuzatasiz va
shifokorga onlayn yozilasiz — rus, o‘zbek va ingliz tillarida.</p>

<div class="stats">
  <div class="stat"><div class="num">60 soniya</div><div class="lbl">AI-checkup uchun</div></div>
  <div class="stat"><div class="num">5 tizim</div><div class="lbl">organizm baholanadi</div></div>
  <div class="stat"><div class="num">250+</div><div class="lbl">katalogdagi shifokor</div></div>
  <div class="stat"><div class="num">14</div><div class="lbl">O‘zbekiston hududi</div></div>
  <div class="stat"><div class="num">3 til</div><div class="lbl">ru · uz · en</div></div>
</div>

<div class="cta-row">
  <a class="btn btn-primary" href="/uz/features/ai-checkup/">AI-checkupdan o‘tish</a>
  <a class="btn btn-ghost" href="/uz/features/">Barcha imkoniyatlar</a>
</div>

<h2>AIVITA nima qila oladi?</h2>
<p>AIVITA ilgari tarqoq bo‘lgan narsalarni bir joyga jamlaydi: sog‘liqni o‘z-o‘zini tekshirish,
kasallik tarixi, dorilar nazorati, taqiladigan qurilmalardan ma’lumotlar va shifokor bilan
aloqa. Har bir vosita alohida ishlaydi va boshqalar bilan birgalikda yanada kuchayadi.</p>

<div class="grid grid-3">
  <a class="card" href="/uz/features/ai-checkup/"><div class="ic">🩺</div><h3>Organizm AI-checkup</h3><p>Bir marta bosib, 60 soniyada tekshiruvdan o‘ting va sog‘lig‘ingiz haqida biling.</p><span class="more">Batafsil →</span></a>
  <a class="card" href="/uz/features/drug-checker/"><div class="ic">💊</div><h3>Dori mosligini tekshirish</h3><p>Tabletkani ichishdan oldin dorilar mosligi va o‘zaro ta’sirini bilib oling.</p><span class="more">Batafsil →</span></a>
  <a class="card" href="/uz/features/medcard/"><div class="ic">📁</div><h3>Elektron tibbiy karta</h3><p>Tahlillar, qabullar va tayinlovlar bir joyda — faqat sizning ruxsatingiz bilan shifokorga ochiladi.</p><span class="more">Batafsil →</span></a>
  <a class="card" href="/uz/features/monitoring/"><div class="ic">📈</div><h3>Sog‘liq monitoringi</h3><p>Puls, bosim, uyqu va qadamlar aqlli soatlardan — yagona sog‘liq kundaligida.</p><span class="more">Batafsil →</span></a>
  <a class="card" href="/uz/features/doctors/"><div class="ic">👩‍⚕️</div><h3>Onlayn shifokorlar</h3><p>O‘zbekistonning istalgan hududidan kerakli mutaxassisga yoziling — navbatsiz.</p><span class="more">Batafsil →</span></a>
  <a class="card" href="/uz/features/sos/"><div class="ic">🚨</div><h3>SOS-yordam</h3><p>Favqulodda vaziyatda harakatlar tartibi va ma’lumotlaringizga tez kirish.</p><span class="more">Batafsil →</span></a>
</div>

<h2>Bo‘limlar</h2>
<div class="grid grid-3">
  <a class="card" href="/uz/features/"><div class="ic">🧩</div><h3>Imkoniyatlar</h3><p>AI-checkup, tibbiy karta, dori tekshiruvi, monitoring, shifokorlar, SOS.</p><span class="more">Ochish →</span></a>
  <a class="card" href="/uz/blog/"><div class="ic">📰</div><h3>Sog‘liq blogi</h3><p>Simptomlar, sog‘lom turmush tarzi va qurilmalar haqida tushunarli maqolalar.</p><span class="more">Ochish →</span></a>
  <a class="card" href="/uz/regions/"><div class="ic">📍</div><h3>O‘zbekiston hududlari</h3><p>Barcha 14 hududda onlayn shifokorlar va telemeditsina.</p><span class="more">Ochish →</span></a>
</div>

<h2>Klinikalar va biznes uchun</h2>
<p>AIVITA — katta ekotizimning bir qismi. Klinikalar ishini <a href="/medsoft/">MedSoft</a> tibbiy
axborot tizimi bilan avtomatlashtiradi va AIVITA katalogidan bemorlar oladi. Batafsil —
<a href="/uz/about/">biz haqimizda</a> bo‘limida.</p>
"""
    faq = [
        ("AIVITA nima?", "AIVITA — O‘zbekistonda sog‘liqni saqlash uchun ilova va ekotizim. U AI-checkup, elektron tibbiy karta, dori mosligini tekshirish, aqlli soatlardan monitoring va onlayn shifokorlarni birlashtiradi. Interfeys rus, o‘zbek va ingliz tillarida."),
        ("AIVITA shifokor o‘rnini bosadimi?", "Yo‘q. AIVITA sog‘likni kuzatishga, tarixni saqlashga va o‘z vaqtida murojaat qilishga yordam beradi, lekin tashxis qo‘ymaydi va davolashni tayinlamaydi. Barcha tibbiy qarorlarni shifokor qabul qiladi."),
        ("AIVITA’dan foydalanish qancha turadi?", "Asosiy funksiyalar — o‘z-o‘zini tekshirish, tibbiy karta yuritish va monitoring — bepul. Onlayn maslahatlar shifokor va klinikaga qarab alohida to‘lanadi."),
        ("AIVITA qaysi hududlarda ishlaydi?", "AIVITA butun O‘zbekiston bo‘ylab ishlaydi. Telemeditsina tufayli siz qayerda bo‘lishingizdan qat’i nazar istalgan hududdagi shifokorga murojaat qilishingiz mumkin."),
        ("Ilova qaysi tillarda mavjud?", "AIVITA uch tilda ishlaydi: rus, o‘zbek (lotin) va ingliz. Tilni istalgan vaqtda almashtirish mumkin, tibbiy ma’lumotlar saqlanib qoladi."),
    ]
    schema = [{"@type": "MedicalWebPage", "url": DOMAIN + "/uz/", "inLanguage": "uz",
               "name": "AIVITA — O‘zbekistonda sog‘liq", "isPartOf": {"@id": DOMAIN + "/#website"}}]
    return Page(
        path="uz", lang="uz",
        title="AIVITA — O‘zbekistonda sog‘liq: AI-checkup, tibbiy karta, onlayn shifokorlar",
        description="AIVITA — O‘zbekistonda raqamli sog‘liq ekotizimi: 60 soniyada AI-checkup, elektron tibbiy karta, dori mosligini tekshirish, aqlli soatlardan monitoring va onlayn shifokorlar 3 tilda.",
        h1="Doim yoningizdagi tibbiyot",
        body=body, faq=faq, schema=schema, section="",
        crumbs=[], disclaimer=True,
        hreflang={"ru": "/", "uz": "/uz/", "en": "/en/"},
        related=[("Imkoniyatlar", "/uz/features/"), ("Sog‘liq blogi", "/uz/blog/"),
                 ("Hududlar", "/uz/regions/")],
    )


def _feat(slug, title, desc, h1, body, faq, related, sname, sdesc, disclaimer=True):
    return Page(
        path=f"uz/features/{slug}", lang="uz", title=title, description=desc, h1=h1,
        body=body, faq=faq, related=related, section="features",
        crumbs=[("Bosh sahifa", "/uz/"), CRF, (h1, None)],
        hreflang=alts(f"features/{slug}"),
        disclaimer=disclaimer,
        schema=[{"@type": "Service", "name": sname, "description": sdesc,
                 "serviceType": "Onlayn sog‘liq xizmati",
                 "provider": {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/"},
                 "areaServed": {"@type": "Country", "name": "O‘zbekiston"},
                 "availableChannel": {"@type": "ServiceChannel", "serviceUrl": DOMAIN + f"/uz/features/{slug}/"}}],
    )


def f_aicheckup():
    body = """
<p class="lede"><strong>AIVITA AI-checkup — bir marta bosib, 60 soniyada o‘tiladigan organizmning
onlayn tekshiruvi.</strong> Siz o‘zingizni qanday his qilayotganingiz haqidagi oddiy savollarga
javob berasiz, tizim esa organizmning beshta asosiy tizimini baholab, tushunarli manzarani
ko‘rsatadi: nima me’yorda va nimaga e’tibor berish kerak.</p>

<h2>Organizmning onlayn checkup nima?</h2>
<p>Checkup — hech narsa bezovta qilmayotgan yoki kam bezovta qilayotgan paytda sog‘liqni
profilaktik tekshirish. Klinikadagi klassik checkup — tahlillar va ko‘riklar to‘plami. AIVITA
AI-checkup laboratoriya tekshiruvlarini almashtirmaydi, lekin birinchi qadamni qo‘yishga yordam
beradi: asosiy ko‘rsatkichlar joyidami yoki yo‘qligini tushunish uchun qulay boshlanish nuqtasi.</p>

<h2>Tekshiruvdan qanday o‘tiladi?</h2>
<p>AIVITA’ni oching va bosh ekranda checkupni ishga tushiring. Ilova savollarni bloklar bo‘yicha
beradi: yurak va bosim, nafas, hazm, uyqu va energiya, hissiy holat. Har bir savolga tayyor javob
variantlari bor — hech narsa yozish shart emas. Bir daqiqadan so‘ng siz ustuvorliklari bilan
natijani olasiz va kerak bo‘lsa qaysi mutaxassisga murojaat qilishni bilib olasiz.</p>

<h2>AI-checkup nimani ko‘rsatadi?</h2>
<p>Natija — tashxis emas, e’tibor xaritasi. Siz organizmning qaysi tizimlarini turmush tarzi
bilan qo‘llab-quvvatlash kerakligini, qaysi ko‘rsatkichlarni aniqroq o‘lchash kerakligini va
qaysi shikoyatlar yuzma-yuz maslahatni talab qilishini ko‘rasiz. Natijani <a href="/uz/features/medcard/">tibbiy kartaga</a>
saqlab, qabulda shifokorga ko‘rsatish mumkin.</p>

<h2>Checkup shifokor o‘rnini bosadimi?</h2>
<p>Yo‘q. AI-checkup — profilaktika va o‘z-o‘zini kuzatish vositasi. U signallarni o‘z vaqtida
sezishga yordam beradi, lekin tashxis qo‘ymaydi va davolashni tayinlamaydi. Agar checkup xavotirli
javoblarni ko‘rsatsa yoki o‘tkir simptomlar bo‘lsa, <a href="/uz/features/doctors/">shifokorga
onlayn</a> yoziling yoki klinikaga murojaat qiling.</p>

<h2>Checkupdan qanchalik tez-tez o‘tish kerak?</h2>
<p>Yengil o‘z-o‘zini tekshiruvdan 1–3 oyda bir marta o‘tish mumkin, shuningdek o‘zingizni his
qilishingiz o‘zgarganda. Muntazamlik bir martalik tekshiruvdan muhimroq: natijalarni vaqt bo‘yicha
solishtirib, siz va shifokoringiz tendensiyani ko‘rasiz. Kattalar uchun to‘liq tibbiy ko‘rikni
odatda yiliga bir marta tavsiya qilishadi.</p>
"""
    faq = [
        ("AI-checkup qancha vaqt oladi?", "O‘rtacha 60 soniya. Savollar qisqa va tayyor javob variantlari bilan, shuning uchun tekshiruvdan bir marta bosib o‘tish mumkin."),
        ("Checkup uchun tahlillar kerakmi?", "Yo‘q. Asosiy AI-checkup sizning javoblaringizga asoslanadi. Agar yangi tahlillaringiz bo‘lsa, ularni kartaga qo‘shsangiz, manzara aniqroq bo‘ladi."),
        ("AI-checkup tashxis qo‘yadimi?", "Yo‘q. Checkup nimaga e’tibor berishni ko‘rsatadi va qaysi shifokorga murojaat qilishni maslahat beradi. Tashxisni faqat shifokor qo‘yadi."),
        ("Bu bepulmi?", "Ha, AIVITA’dagi asosiy AI-checkup bepul. Natijalar bo‘yicha shifokorga yozilsangiz, onlayn maslahatlar to‘lanishi mumkin."),
        ("Checkupdan o‘zbek tilida o‘tsam bo‘ladimi?", "Ha. AIVITA rus, o‘zbek va ingliz tillarida ishlaydi. Tilni istalgan vaqtda almashtirish mumkin."),
    ]
    related = [("Elektron tibbiy karta", "/uz/features/medcard/"),
               ("Onlayn shifokorlar", "/uz/features/doctors/"),
               ("Sog‘liq monitoringi", "/uz/features/monitoring/")]
    return _feat("ai-checkup",
                 "Organizm AI-checkup onlayn — bir marta bosib tekshiruv | AIVITA",
                 "AIVITA’da organizm AI-checkupdan 60 soniyada o‘ting: oddiy savollarga javob bering va sog‘lig‘ingiz haqida biling. 5 tizim baholanadi. Shifokor o‘rnini bosmaydi.",
                 "Organizm AI-checkup onlayn", body, faq, related,
                 "Organizm AI-checkup", "Sog‘liq holatini 60 soniyada onlayn tekshirish.")


def f_drug():
    body = """
<p class="lede"><strong>AIVITA’da dori tekshiruvi — tabletkani ichishdan oldin preparatlar
mosligi va ularning o‘zaro ta’siri xavfini ko‘rsatuvchi xizmat.</strong> Siz qabul qilayotgan yoki
qilmoqchi bo‘lgan dorilarni qo‘shasiz, tizim esa ularni birga ishlatish mumkinligini aytadi.</p>

<h2>Nega dorilar mosligini tekshirish kerak?</h2>
<p>Bir vaqtning o‘zida bir nechta preparat qabul qilish — odatiy holat: biri bosimdan, ikkinchisi
shamollashdan, uchinchisi vitamin. Ammo ba’zi dorilar bir-birining ta’sirini kuchaytiradi yoki
kamaytiradi, ayrim birikmalar esa xavfli bo‘lishi mumkin. Bu ayniqsa keksalar, homilador ayollar
va surunkali kasalliklari borlar uchun muhim.</p>

<h2>O‘zaro ta’sir tekshiruvi qanday ishlaydi?</h2>
<p>Dorilar nomini kiriting — bittalab yoki ro‘yxat bilan. AIVITA ta’sir etuvchi moddalarni
solishtiradi va ular o‘rtasida muhim o‘zaro ta’sir bor-yo‘qligini, ular qanchalik jiddiyligini
ko‘rsatadi. Agar birikma ehtiyotkorlik talab qilsa, siz tushunarli izoh va shifokor bilan
maslahatlashish tavsiyasini ko‘rasiz.</p>

<h2>Natija nimani ko‘rsatadi?</h2>
<p>Natija — ruxsat yoki taqiq emas, balki mo‘ljal. Siz muayyan juft preparatga e’tibor darajasini
(masalan «xavfsiz», «ehtiyotkorlik talab qiladi», «tavsiya etilmaydi»), qisqa izohni va keyin nima
qilish kerakligini ko‘rasiz. AIVITA dorilarni bekor qilmaydi va tayinlamaydi — yakuniy qarorni
sizning tarixingizni biladigan shifokor qabul qiladi.</p>

<h2>Onlayn tekshiruvga ishonsa bo‘ladimi?</h2>
<p>Xizmat ta’sir etuvchi moddalarning o‘zaro ta’siri haqidagi ma’lum ma’lumotlarga tayanadi,
lekin u sizning individual holatingizni — dozalar, yondosh kasalliklar, allergiya, buyrak va jigar
xususiyatlarini — to‘liq ko‘rmaydi. Shuning uchun moslik tekshiruvi maslahatning o‘rnini bosmaydi.
Tayinlangan dorini onlayn tekshiruv asosida hech qachon boshlamang yoki to‘xtatmang.</p>

<h2>Kimga ayniqsa foydali?</h2>
<p>Bir vaqtda bir nechta preparat qabul qiladiganlar; retseptsiz dori sotib oluvchilar; bolalarga
dori beradigan ota-onalar; keksalar va ularga g‘amxo‘rlik qiluvchilar uchun. Bu holatlarda tez
tekshiruv tasodifiy xato xavfini kamaytiradi va shifokorga to‘g‘ri savollar berishga yordam beradi.</p>
"""
    faq = [
        ("AIVITA’da dori tekshiruvi nima qiladi?", "U preparatlar bir-biriga mosligini ko‘rsatadi va mumkin bo‘lgan o‘zaro ta’sirlardan ogohlantiradi. Bu xatolar profilaktikasi, davolashni tayinlash emas."),
        ("Tekshiruv bo‘yicha dori ichish yoki ichmaslikni hal qilsa bo‘ladimi?", "Yo‘q. Preparatni qabul qilish, bekor qilish yoki almashtirish haqida qarorni faqat shifokor qabul qiladi."),
        ("Xizmat dozani hisobga oladimi?", "Asosiy tekshiruv ta’sir etuvchi moddalarga qaraydi. Individual dozani, kasalliklaringizni va allergiyani shifokor baholaydi."),
        ("Bu bepulmi?", "Ha, AIVITA’da asosiy moslik tekshiruvi bepul."),
        ("Xizmat xavf ko‘rsatsa nima qilish kerak?", "Sarosimaga tushmang va davolashni keskin to‘xtatmang. Natijani saqlab, shifokor bilan muhokama qiling."),
    ]
    related = [("Elektron tibbiy karta", "/uz/features/medcard/"),
               ("Onlayn shifokorlar", "/uz/features/doctors/"),
               ("AI-checkup", "/uz/features/ai-checkup/")]
    return _feat("drug-checker",
                 "Dori mosligini onlayn tekshirish — preparatlar o‘zaro ta’siri | AIVITA",
                 "AIVITA’da dorilar mosligini onlayn tekshiring: qabuldan oldin preparatlar o‘zaro ta’sirini biling. Tushunarli natija. Shifokor maslahatining o‘rnini bosmaydi.",
                 "Dori mosligini tekshirish", body, faq, related,
                 "Dori mosligini tekshirish", "Dori preparatlari o‘zaro ta’siri va mosligini onlayn tekshirish.")


def f_medcard():
    body = """
<p class="lede"><strong>AIVITA elektron tibbiy kartasi — bir joyda saqlanadigan shaxsiy sog‘liq
tarixingiz: tahlillar, qabullar, tashxislar va tayinlovlar.</strong> Ma’lumotlar sizda saqlanadi
va shifokorga faqat sizning ruxsatingiz bilan, muayyan maslahat uchun ochiladi.</p>

<h2>Elektron tibbiy karta nima?</h2>
<p>Bu — bemorning qog‘oz kartasining raqamli varianti, faqat uni yo‘qotib qo‘yib bo‘lmaydi, uyda
unutib qoldirib bo‘lmaydi. AIVITA’da karta sog‘lig‘ingizga oid hamma narsani jamlaydi: tahlil
natijalari, shifokor xulosalari, qabullar tarixi, tayinlangan dorilar, monitoring ma’lumotlari.
Bularning barchasi telefondan istalgan vaqtda mavjud.</p>

<h2>Nega ilovada karta yuritish kerak?</h2>
<p>Kasallik tarixi qog‘ozlar bo‘ylab tarqoq bo‘lganda, shifokor uni tiklashga vaqt sarflaydi, siz
esa muhim narsani unutish xavfi bilan yashaysiz. Yagona karta bu muammoni hal qiladi: qabulda
mutaxassis to‘liq manzarani darhol ko‘radi — qaysi tahlillar topshirilgan, avval nima tayinlangan,
nimaga allergiya bor.</p>

<h2>Ma’lumotlarimni kim ko‘radi?</h2>
<p>Sukut bo‘yicha — faqat siz. Shifokor kartaning kerakli qismini faqat siz uni muayyan maslahat
uchun ochganingizda oladi. Qabuldan so‘ng ruxsatni yopish mumkin. Siz kim nimani ko‘rishini o‘zingiz
boshqarasiz va istalgan vaqtda ruxsatni bekor qilishingiz mumkin.</p>

<h2>Qog‘oz tahlillarni kartaga qanday o‘tkazish mumkin?</h2>
<p>Hujjatlarni qo‘lda kiritish yoki suratga olish mumkin. Tahlil natijalari va xulosalar kartaga
yuklanadi va sanalar bo‘yicha tartiblanadi. Agar qog‘oz tahlillarni yo‘qotib qo‘ygan bo‘lsangiz,
elektron karta xronologiyani tiklashga yordam beradi: bir marta kiritganingiz endi yo‘qolmaydi.</p>

<h2>Butun oila uchun tibbiy karta</h2>
<p>AIVITA’da yaqinlaringizning — masalan, ilovadan o‘zi foydalanmaydigan bolalar va keksa
ota-onalarning — kartasini yuritish mumkin. Bu <a href="/uz/for/moms/">onalar</a> va oilaga
g‘amxo‘rlik qiluvchilar uchun qulay: emlash jadvali, kasalliklar tarixi va tayinlovlar doim
qo‘l ostida.</p>
"""
    faq = [
        ("Elektron tibbiy kartada nima saqlanadi?", "Tahlillar, shifokor xulosalari, qabullar tarixi, tayinlangan dorilar, AI-checkup natijalari va monitoring ma’lumotlari. Hammasi sanalar bo‘yicha tartiblangan."),
        ("Tibbiy ma’lumotlarim xavfsizmi?", "Ha. Kartaga faqat sizda kirish bor. Shifokor ma’lumotlarni faqat siz maslahat uchun ochganingizda ko‘radi va istalgan vaqtda yopishingiz mumkin."),
        ("Bolaning kartasini yuritsam bo‘ladimi?", "Ha. AIVITA’da yaqinlaringiz — bolalar va keksa qarindoshlarning kartasini, jumladan emlash jadvalini yuritish mumkin."),
        ("Eski qog‘oz tahlillarni qanday qo‘shaman?", "Ularni qo‘lda kiritish yoki suratga olish mumkin. Hujjatlar sanalar bo‘yicha saqlanadi va yo‘qolmaydi."),
        ("Bu bepulmi?", "Ha, AIVITA’da elektron tibbiy karta yuritish bepul."),
    ]
    related = [("AI-checkup", "/uz/features/ai-checkup/"),
               ("Sog‘liq monitoringi", "/uz/features/monitoring/"),
               ("Onlayn shifokorlar", "/uz/features/doctors/")]
    return _feat("medcard",
                 "Elektron tibbiy karta onlayn — telefonda sog‘liq tarixi | AIVITA",
                 "AIVITA elektron tibbiy kartasi: tahlillar, qabullar, tashxislar va tayinlovlar bir joyda. Kirish sizda, shifokor faqat ruxsat bilan ko‘radi. Butun oila uchun.",
                 "Elektron tibbiy karta", body, faq, related,
                 "Elektron tibbiy karta", "Shaxsiy tibbiy tarixni saqlash va yuritish.", disclaimer=False)


def f_doctors():
    body = """
<p class="lede"><strong>AIVITA’da onlayn shifokorlar — O‘zbekistonning istalgan hududidan kerakli
yo‘nalishdagi mutaxassisga uydan chiqmasdan yozilish imkoniyati.</strong> Telemeditsina masofani
yo‘qotadi: Toshkentdagi shifokor Nukusdagi bemorga ham mavjud bo‘ladi.</p>

<div class="stats">
  <div class="stat"><div class="num">250+</div><div class="lbl">katalogdagi shifokor</div></div>
  <div class="stat"><div class="num">14</div><div class="lbl">O‘zbekiston hududi</div></div>
  <div class="stat"><div class="num">3 til</div><div class="lbl">ru · uz · en</div></div>
</div>

<h2>Shifokorning onlayn maslahati nima?</h2>
<p>Onlayn maslahat (telemeditsina) — video yoki audio aloqa orqali o‘tadigan qabul. Shifokor
shikoyatlar haqida so‘raydi, <a href="/uz/features/medcard/">tibbiy kartangizni</a> va tahlil
natijalarini o‘rganadi, savollarga javob beradi va yuzma-yuz tashrif kerakmi yoki yo‘qligini hal
qiladi. Bu maslahatlar, tahlillarni tahlil qilish va takroriy qabullar uchun qulay.</p>

<h2>AIVITA’da shifokorga qanday yozilish mumkin?</h2>
<p>Mutaxassislik tanlang, shifokorlar profillarini ko‘ring, qulay vaqtni tanlang va yozilishni
tasdiqlang. Maslahatdan oldin kartaning kerakli qismini shifokorga ochsangiz, u tarixingizni
oldindan ko‘radi. Qabuldan so‘ng tayinlovlar kartada saqlanadi.</p>

<h2>Istalgan hududdan shifokor — bu qanday ishlaydi?</h2>
<p>Telemeditsina O‘zbekiston uchun ayniqsa qimmatli, chunki kuchli mutaxassislar yirik shaharlarda
to‘plangan. AIVITA orqali istalgan hududdagi bemor — Samarqand, Buxoro, Farg‘ona yoki
Qoraqalpog‘istondan — yaqinida bo‘lmasligi mumkin bo‘lgan shifokorga kirish imkoniyatiga ega
bo‘ladi. Maslahat uchun yuzlab kilometr yurish shart emas.</p>

<h2>Qachon onlayn yetarli, qachon yuzma-yuz kerak?</h2>
<p>Onlayn tahlillarni tahlil qilish, takroriy qabullar, surunkali davolashni tuzatish va
profilaktika savollari uchun yaxshi. Yuzma-yuz tashrif ko‘rik, o‘lchovlar yoki muolajalar
kerak bo‘lganda — masalan, o‘tkir og‘riq, jarohat, yuqori haroratda zarur. Onlayn qabuldagi
shifokor vaziyat yuzma-yuz tekshiruvni talab qilsa, buni aytadi.</p>

<h2>Telemeditsina xavfsizligi va chegaralari</h2>
<p>Onlayn maslahat shoshilinch yordamning o‘rnini bosmaydi. Xavfli simptomlarda — ko‘krakdagi
kuchli og‘riq, nafas qisilishi, hushdan ketish — onlayn qabulni kutmang, <a href="/uz/features/sos/">SOS-yordam</a>dan
foydalaning va tez yordam chaqiring. Telemeditsina — yuzma-yuz tibbiyotni to‘ldiruvchi vosita.</p>
"""
    faq = [
        ("Shifokorga onlayn qanday yozilaman?", "Mutaxassislikni tanlang, shifokorlar profillarini ko‘ring, vaqt tanlang va yozilishni tasdiqlang. Qabuldan oldin kartaning kerakli qismini ochish mumkin."),
        ("Boshqa shahardagi shifokorga tushsam bo‘ladimi?", "Ha. Telemeditsina tufayli O‘zbekistonning istalgan hududidagi shifokor onlayn mavjud — hech qayerga borish shart emas."),
        ("Onlayn maslahat yuzma-yuz qabulning o‘rnini bosadimi?", "Har doim emas. U tahlillarni tahlil qilish va takroriy qabullar uchun yaxshi, lekin ko‘rik kerak bo‘lsa shifokor yuzma-yuz tashrifga yo‘naltiradi."),
        ("Favqulodda holatda nima qilish kerak?", "Onlayn qabulni kutmang. Xavfli simptomlarda SOS-yordamdan foydalaning va tez yordam chaqiring."),
        ("Maslahat qaysi tilda o‘tadi?", "Siz rus, o‘zbek yoki ingliz tilida gaplashadigan shifokorni tanlashingiz mumkin."),
    ]
    related = [("Elektron tibbiy karta", "/uz/features/medcard/"),
               ("Hududlar", "/uz/regions/"),
               ("SOS-yordam", "/uz/features/sos/")]
    return _feat("doctors",
                 "O‘zbekistonda onlayn shifokorlar — maslahat va yozilish | AIVITA",
                 "AIVITA’da shifokorga onlayn yoziling: terapevt, pediatr, ginekolog, kardiolog va boshqa mutaxassislar O‘zbekistonning istalgan hududidan. Navbatsiz telemeditsina 3 tilda.",
                 "Onlayn shifokorlar", body, faq, related,
                 "Shifokorlarning onlayn maslahati", "O‘zbekiston bo‘ylab turli mutaxassis shifokorlar bilan onlayn maslahat.")


def f_sos():
    body = """
<p class="lede"><strong>AIVITA’da SOS-yordam — favqulodda vaziyatda harakatlar tartibini
maslahat beradigan va muhim tibbiy ma’lumotlaringizga tez kirishni ta’minlaydigan bo‘lim.</strong>
Har soniya qadrli bo‘lganda, eng muhimi qo‘l ostida bo‘ladi: nima qilish va qanday ma’lumot berish.</p>

<h2>SOS-yordam nima qiladi?</h2>
<p>SOS bo‘limi favqulodda vaziyatda kerak bo‘ladigan narsalarni bir joyga jamlaydi: keng tarqalgan
holatlar bo‘yicha birinchi yordam bo‘yicha qisqa ko‘rsatmalar, sog‘lig‘ingiz haqidagi asosiy
ma’lumotlar (qon guruhi, allergiyalar, surunkali kasalliklar, doimiy dorilar) va favqulodda aloqa
uchun kontaktlar. Bu tez yordam o‘rnini bosmaydi, balki to‘g‘ri harakat qilishga yordam beradi.</p>

<h2>Ma’lumotlarga tez kirish nega kerak?</h2>
<p>Favqulodda vaziyatda odam ko‘pincha o‘z kasalliklari va allergiyasi haqida o‘zi ayta olmaydi —
stress, og‘riq yoki hushdan ketish tufayli. Agar muhim ma’lumot oldindan <a href="/uz/features/medcard/">tibbiy
kartaga</a> kiritilgan va SOS-profilga chiqarilgan bo‘lsa, atrofdagilar yoki tibbiyot xodimlari
nima bilan kasalligingizni tezroq tushunadi.</p>

<h2>Oldindan qanday tayyorgarlik ko‘rish kerak?</h2>
<p>SOS qanchalik erta sozlangan bo‘lsa, shunchalik yaxshi ishlaydi. Profilga qon guruhi, ma’lum
allergiyalar, surunkali tashxislar, doimiy dorilar va yaqin insonning kontaktini kiriting. Buni
tinch vaziyatda qiling — shunda kritik damda hammasi tayyor bo‘ladi.</p>

<h2>SOS tez yordam o‘rnini bosmaydi</h2>
<div class="callout disclaimer"><strong>Muhim.</strong> Hayotga xavf soluvchi holatlarda —
ko‘krakdagi kuchli og‘riq, nafas qisilishi, hushdan ketish, kuchli qon ketish, insult belgilari —
darhol tez yordam chaqiring. O‘zbekistonda — <strong>103</strong> (tez yordam) va
<strong>112</strong> (yagona xizmat). AIVITA SOS-yordami — ma’lumot va qo‘llab-quvvatlash, tibbiy
yordam emas.</div>

<h2>Kimga ayniqsa foydali?</h2>
<p>Surunkali kasalliklari va allergiyasi borlar, keksalar, kichik bolali ota-onalar, ko‘p sayohat
qiladigan yoki sport bilan shug‘ullanadiganlar uchun. Oldindan tayyorlangan SOS-profil qimmatli
daqiqalarni tejashi mumkin.</p>
"""
    faq = [
        ("AIVITA’da SOS-yordam nima?", "Bu — birinchi yordam ko‘rsatmalari va sog‘liq haqidagi asosiy ma’lumotlarga (allergiya, surunkali kasalliklar, qon guruhi) tez kirishni ta’minlaydigan favqulodda bo‘lim."),
        ("SOS tez yordam chaqirish o‘rnini bosadimi?", "Yo‘q. Hayotga xavf soluvchi holatlarda darhol tez yordam (103) yoki yagona xizmat (112) ga qo‘ng‘iroq qilish kerak."),
        ("SOS-profilga nima kiritish kerak?", "Qon guruhi, allergiyalar, surunkali tashxislar, doimiy dorilar va yaqin insonning kontaktini. Buni oldindan qilgan ma’qul."),
        ("SOS ma’lumotlarimni kim ko‘radi?", "Qaysi ma’lumotni favqulodda profilga chiqarishni siz o‘zingiz hal qilasiz, toki kritik damda yordam beruvchilar ko‘ra olsin."),
        ("SOS-profilni yangilash kerakmi?", "Ha, o‘zgarishlarda yangilang: yangi dori, yangi tashxis yoki allergiya."),
    ]
    related = [("Elektron tibbiy karta", "/uz/features/medcard/"),
               ("Onlayn shifokorlar", "/uz/features/doctors/"),
               ("AI-checkup", "/uz/features/ai-checkup/")]
    return _feat("sos",
                 "SOS-yordam — favqulodda harakatlar tartibi va ma’lumotlar | AIVITA",
                 "AIVITA’da SOS-yordam: favqulodda vaziyatda harakatlar tartibi va muhim sog‘liq ma’lumotlaringizga tez kirish. Tez yordam o‘rnini bosmaydi — xavf bo‘lsa 103 ga qo‘ng‘iroq qiling.",
                 "SOS-yordam", body, faq, related,
                 "SOS-yordam", "Birinchi yordam ko‘rsatmalari va bemor ma’lumotlariga kirish bilan favqulodda bo‘lim.")


def f_monitoring():
    body = """
<p class="lede"><strong>AIVITA’da sog‘liq monitoringi — ko‘rsatkichlaringizning yagona kundaligi:
puls, bosim, uyqu, qand, suv va qadamlar.</strong> Ma’lumotlar aqlli soatlar va fitnes-brasletlardan
avtomatik tarzda olinadi, ilova esa sog‘liq dinamikasini vaqt bo‘yicha ko‘rsatadi.</p>

<div class="stats">
  <div class="stat"><div class="num">6</div><div class="lbl">asosiy ko‘rsatkich</div></div>
  <div class="stat"><div class="num">24/7</div><div class="lbl">fon rejimida yig‘ish</div></div>
  <div class="stat"><div class="num">1</div><div class="lbl">sog‘liq kundaligi</div></div>
</div>

<h2>AIVITA qaysi ko‘rsatkichlarni kuzatadi?</h2>
<p>Monitoring kundalik sog‘liqning asosiy parametrlarini qamrab oladi: puls, arterial bosim, uyqu
sifati va davomiyligi, qand darajasi (mos qurilmalarda), ichilgan suv miqdori, qadamlar soni va
jismoniy faollik. Birgalikda bu ko‘rsatkichlar turmush tarzining tushunarli manzarasini beradi.</p>

<h2>Aqlli soat va brasletni qanday ulash mumkin?</h2>
<p>AIVITA mashhur taqiladigan qurilmalar bilan ishlaydi. <strong>Mi Band</strong> va Xiaomi
brasletlari, <strong>Apple Watch</strong> soatlari, <strong>Samsung Galaxy Watch</strong>
qurilmalari va boshqa fitnes-trekerlar egalari ularni ilova bilan bog‘lashi mumkin, shunda puls,
uyqu va faollik ma’lumotlari avtomatik olinadi.</p>

<h2>Sog‘liq dinamikasi va sog‘liq kundaligi nima?</h2>
<p>Bosim yoki pulsning bitta o‘lchovi kam narsani aytadi — dinamika muhim. AIVITA ko‘rsatkichlaringiz
kundan-kunga va haftadan-haftaga qanday o‘zgarishini ko‘rsatadi: uyqu yaxshilanyaptimi, faollik
o‘syaptimi, bosim barqarormi. Sog‘liq kundaligi butun o‘lchovlar tarixini saqlaydi.</p>

<h2>Sog‘liq kuratsiyasi nima?</h2>
<p>Sog‘liq kuratsiyasi — ko‘rsatkichlaringizni shunchaki yig‘ish emas, balki vaqt bo‘yicha anglab
kuzatib borish. AIVITA ma’lumotlarni harakatga aylantirishga yordam beradi: nimaga e’tibor berishni
maslahat beradi, bosimni o‘lchashni yoki suv ichishni eslatadi. Monitoring ma’lumotlari <a href="/uz/features/medcard/">kartada</a>
saqlanadi.</p>

<h2>Shifokorga braslet ma’lumotlari nega kerak?</h2>
<p>Bir necha haftadagi ko‘rsatkichlar kabinetdagi bitta o‘lchovdan qimmatliroq. Shifokor bosim kun
davomida qanday o‘zgarishini, qanday uxlashingizni, qanchalik faolligingizni ko‘radi — va vaziyatni
aniqroq baholaydi. Monitoring ma’lumotlari <a href="/uz/features/doctors/">shifokor bilan onlayn</a>
suhbat uchun yaxshi asos.</p>
"""
    faq = [
        ("Monitoring qaysi qurilmalarni qo‘llab-quvvatlaydi?", "AIVITA mashhur fitnes-brasletlar va aqlli soatlar — Mi Band va boshqa Xiaomi qurilmalari, Apple Watch, Samsung Galaxy Watch va boshqa trekerlar bilan ishlaydi."),
        ("Sog‘liq monitoringi nimani kuzatadi?", "Puls, arterial bosim, uyqu, qand (mos qurilmalarda), suv, qadamlar va faollik — hammasi yagona sog‘liq kundaligida."),
        ("Sog‘liq dinamikasi nima?", "Bu — ko‘rsatkichlaringizning vaqt bo‘yicha o‘zgarishi. AIVITA tendensiyani ko‘rsatadi, alohida raqamlarni emas."),
        ("Ma’lumotlarni qo‘lda kiritish kerakmi?", "Qurilma ulangandan so‘ng puls, uyqu va faollik avtomatik olinadi. Ba’zi ko‘rsatkichlarni, masalan suvni, qo‘lda belgilash mumkin."),
        ("Shifokor monitoring ma’lumotlarimni ko‘radimi?", "Ha, agar ularni maslahat uchun ochsangiz. Ma’lumotlar kartada saqlanadi va shifokor dinamikani ko‘radi."),
    ]
    related = [("Elektron tibbiy karta", "/uz/features/medcard/"),
               ("Onlayn shifokorlar", "/uz/features/doctors/"),
               ("AI-checkup", "/uz/features/ai-checkup/")]
    return _feat("monitoring",
                 "Sog‘liq monitoringi — aqlli soatlardan puls, bosim, uyqu | AIVITA",
                 "AIVITA’da sog‘liq monitoringi: puls, bosim, uyqu, qand, suv va qadamlar aqlli soatlar va fitnes-brasletlardan (Mi Band, Apple Watch, Samsung). Dinamika va sog‘liq kundaligi bir joyda.",
                 "Sog‘liq monitoringi", body, faq, related,
                 "Sog‘liq ko‘rsatkichlari monitoringi", "Aqlli soatlar va brasletlardan sog‘liq ko‘rsatkichlarini yig‘ish va tahlil qilish.")


def features_hub():
    cards = [
        ("🩺", "Organizm AI-checkup", "Bir marta bosib 60 soniyada tekshiruvdan o‘ting.", "/uz/features/ai-checkup/"),
        ("💊", "Dori mosligini tekshirish", "Preparatlar mosligi va o‘zaro ta’siri — qabuldan oldin.", "/uz/features/drug-checker/"),
        ("📁", "Elektron tibbiy karta", "Tahlillar, qabullar va tayinlovlar bir joyda.", "/uz/features/medcard/"),
        ("📈", "Sog‘liq monitoringi", "Aqlli soatlardan puls, bosim, uyqu — dinamika bilan.", "/uz/features/monitoring/"),
        ("👩‍⚕️", "Onlayn shifokorlar", "Istalgan hududdan shifokorga navbatsiz yozilish.", "/uz/features/doctors/"),
        ("🚨", "SOS-yordam", "Favqulodda vaziyatda harakatlar tartibi va ma’lumotlar.", "/uz/features/sos/"),
    ]
    ic = "".join(f'<a class="card" href="{h}"><div class="ic">{i}</div><h3>{t}</h3><p>{d}</p>'
                 f'<span class="more">Batafsil →</span></a>' for i, t, d, h in cards)
    body = f"""
<p class="lede"><strong>AIVITA sog‘liqqa g‘amxo‘rlikning oltita vositasini bitta ilovada
birlashtiradi.</strong> Har biri mustaqil ishlaydi, lekin birgalikda ular to‘liq manzara beradi:
tez o‘z-o‘zini tekshirishdan shifokor maslahati va ko‘rsatkichlar dinamikasigacha. Quyida har bir
vosita nima uchun kerakligi qisqacha izohlangan, toki siz o‘zingizga mos boshlanish nuqtasini
tezroq topasiz va ortiqcha tashrifga vaqt sarflamaysiz.</p>
<div class="grid grid-3">{ic}</div>

<h2>AIVITA imkoniyatlari qanday birga ishlaydi</h2>
<p>Oddiy stsenariy: siz AI-checkupdan o‘tasiz va natijani kartaga saqlaysiz. Agar biror narsa
e’tibor talab qilsa — shifokorga onlayn yozilib, unga kerakli ma’lumotlarni ochasiz. Shifokor
braslet dinamikasini ham ko‘radi. Yangi dori sotib olishdan oldin uning mosligini tekshirasiz.</p>

<h2>Nega bu O‘zbekistonda muhim</h2>
<p>Kuchli mutaxassislar va zamonaviy diagnostika yirik shaharlarda to‘plangan, yaxshi profilaktika
esa hamon navbat, qog‘ozbozlik va tarqoq ma’lumotlarga bog‘lanib qoladi. AIVITA imkoniyatlari
bu to‘siqlarni olib tashlaydi: telemeditsina istalgan <a href="/uz/regions/">hududdan</a> shifokorga
kirishni ochadi, elektron karta esa tahlillar papkasining o‘rnini bosadi, o‘z-o‘zini tekshirish esa
qachon haqiqatan shifokor kerakligini o‘z vaqtida tushunishga yordam beradi. Hammasi tanish tilda —
rus yoki o‘zbek tilida — ishlaydi va maxsus bilim talab qilmaydi.</p>

<h2>Bitta ilova o‘nlab o‘rniga</h2>
<p>Ilgari buning uchun alohida xizmatlar kerak edi: qadamlar uchun bitta ilova, shifokorga
yozilish uchun boshqasi, qog‘oz tahlillar papkasi, dorilar haqida internetda qidiruv. AIVITA
hammasini yagona tizimga jamlaydi — rus, o‘zbek va ingliz tillarida, O‘zbekistonning istalgan
hududida. Bu vaqtni tejaydi va sog‘liq haqidagi muhim ma’lumotni yo‘qotish xavfini kamaytiradi.</p>

<h2>Nimadan boshlash kerak</h2>
<p>Eng oddiy birinchi qadam — <a href="/uz/features/ai-checkup/">AI-checkupdan</a> o‘tib, natijani
kartaga saqlash. Keyin <a href="/uz/features/monitoring/">aqlli soat yoki brasletni</a> ulang,
kunlik ko‘rsatkichlar dinamikasini kuzating va <a href="/uz/features/sos/">SOS-profilni</a> sozlang.
Savol tug‘ilsa — <a href="/uz/features/doctors/">shifokorga onlayn</a> yoziling. Har bir vosita
alohida foydali, lekin aynan birgalikda ular AIVITA yaratilgan maqsadni beradi: o‘z sog‘lig‘ingiz
va yaqinlaringiz sog‘lig‘i uchun xotirjamlik.</p>
"""
    return Page(
        path="uz/features", lang="uz",
        title="AIVITA imkoniyatlari — AI-checkup, tibbiy karta, onlayn shifokorlar",
        description="AIVITA imkoniyatlari: 60 soniyada AI-checkup, elektron tibbiy karta, dori mosligini tekshirish, aqlli soatlardan sog‘liq monitoringi, onlayn shifokorlar va SOS-yordam.",
        h1="AIVITA imkoniyatlari",
        body=body, section="features",
        crumbs=[("Bosh sahifa", "/uz/"), ("Imkoniyatlar", None)],
        hreflang=alts("features"),
        related=[("Sog‘liq blogi", "/uz/blog/"), ("Oila uchun", "/uz/for/family/"),
                 ("Hududlar", "/uz/regions/")],
    )


# ---------------- Kimlar uchun (for) ----------------
def _aud(slug, title, desc, h1, body, faq, related, crumb, cta=None, disclaimer=True):
    return Page(
        path=f"uz/for/{slug}", lang="uz", title=title, description=desc, h1=h1,
        body=body, faq=faq, related=related, section="",
        crumbs=[("Bosh sahifa", "/uz/"), ("Kimlar uchun", None), (crumb, None)],
        hreflang=alts(f"for/{slug}", langs=("ru", "uz")), cta=cta, disclaimer=disclaimer,
        schema=[{"@type": "WebPage", "name": h1, "url": DOMAIN + f"/uz/for/{slug}/",
                 "inLanguage": "uz", "isPartOf": {"@id": DOMAIN + "/#website"}}],
    )


def for_moms():
    body = """
<p class="lede"><strong>Ona uchun AIVITA — bolaning va butun oilaning sog‘lig‘ini nazoratda
ushlaydigan yordamchi.</strong> Ilovada bola tibbiy kartasini yuritish, emlashlarni eslab qolish,
xavotirli simptomlarni tez tekshirish va pediatrga onlayn tushish qulay.</p>

<h2>AIVITA onaga har kuni qanday yordam beradi?</h2>
<p>Kichik bola bilan navbat va qog‘ozlarga vaqt deyarli yo‘q. AIVITA eng muhimini telefonda
jamlaydi: bolaning <a href="/uz/features/medcard/">tibbiy kartasi</a>, eslatmali emlash jadvali
va <a href="/uz/features/doctors/">pediatrga onlayn</a> tez kirish. Bola kasal bo‘lganda, nima
bilan kasallanganini va nima tayinlanganini eslash shart emas.</p>

<h2>Bola kasal bo‘lsa nima qilish kerak?</h2>
<p>Avvalo — sarosimaga tushmaslik va holatni baholash. Yengil <a href="/uz/features/ai-checkup/">checkup</a>
vaziyat qanchalik jiddiy ekanini tushunishga yordam beradi, pediatrning onlayn maslahati esa uyda
hal qilish mumkinmi yoki yuzma-yuz tashrif kerakmi, hal qilishga yordam beradi. AIVITA tashxis
qo‘ymaydi: qarorni doim shifokor qabul qiladi.</p>

<h2>Emlashlar va profilaktika ortiqcha tashvishsiz</h2>
<p>Emlash taqvimini unutish oson. AIVITA bolaning emlash tarixini saqlaydi va keyingi sanalarni
eslatadi, toki hech narsa o‘tkazib yuborilmasin. Shu yerda bolalar sog‘lig‘i haqida tushunarli
materiallar ham bor. Bu xavotirni kamaytiradi va qarorlarni tinch qabul qilishga yordam beradi.</p>

<h2>Nafaqat bolalar, balki o‘zingiz haqingizda ham</h2>
<p>Onalar ko‘pincha o‘z sog‘lig‘ini keyinga qoldiradi. AIVITA o‘zingizni unutmaslikka yordam
beradi: muntazam o‘z-o‘zini tekshirish, kartani yuritish, <a href="/uz/features/monitoring/">uyqu
va faollik monitoringi</a>. Sog‘lom ona — tinch oila.</p>

<h2>Ishonchli ma’lumot, mish-mishlar emas</h2>
<p>Bolalar sog‘lig‘i atrofida internetda ko‘p qarama-qarshi ma’lumot bor. AIVITA blogida
simptomlar, emlashlar va parvarish haqida tushunarli va ishonchli maqolalar to‘plangan — qo‘rqitmasdan
va mo‘jiza va’da qilmasdan. Bu tasodifiy forumlarga emas, tekshirilgan ma’lumotga tayanib qaror
qabul qilishga yordam beradi.</p>

<h2>Butun oila uchun bitta ilova</h2>
<p>AIVITA’da oilaning bir necha a’zosi — bolalar, turmush o‘rtoq, keksa ota-onalar kartasini
yuritish mumkin. Ma’lumotlar odamlar bo‘yicha ajratilgan va kerakli damda qo‘l ostida: shifokor
qabulida, safarda yoki favqulodda vaziyatda. Batafsil — <a href="/uz/for/family/">oila uchun</a>
sahifasida.</p>
"""
    faq = [
        ("AIVITA’da bola kartasini yuritsam bo‘ladimi?", "Ha. Ona bola tibbiy kartasini yuritishi mumkin: kasalliklar tarixi, tahlillar, tayinlovlar va emlash jadvali — bir joyda."),
        ("AIVITA emlashlarni eslatadimi?", "Ha, ilova bolaning emlash taqvimini saqlaydi va keyingi sanalarni eslatadi."),
        ("Pediatr bilan onlayn maslahatlashsam bo‘ladimi?", "Ha. AIVITA orqali istalgan hududdan pediatrga onlayn maslahatga yozilish mumkin."),
        ("Ilova bolaga shifokor chaqirish o‘rnini bosadimi?", "Yo‘q. Yuqori harorat tushmaganda, nafas qisilganda va boshqa xavotirli simptomlarda bolani yuzma-yuz ko‘rsatish kerak."),
        ("Ona uchun qancha turadi?", "Karta yuritish, emlash taqvimi va o‘z-o‘zini tekshirish bepul. Onlayn maslahatlar to‘lanishi mumkin."),
    ]
    related = [("Oila uchun", "/uz/for/family/"),
               ("Elektron tibbiy karta", "/uz/features/medcard/"),
               ("Onlayn shifokorlar", "/uz/features/doctors/")]
    return _aud("moms",
                "Onalar uchun AIVITA — bola va oila sog‘lig‘i nazoratda",
                "Onalar uchun AIVITA: bola tibbiy kartasi, eslatmali emlash jadvali, onlayn pediatr va simptomlarni tez tekshirish. Bola va o‘zingiz haqingizda g‘amxo‘rlik bitta ilovada.",
                "Onalar uchun AIVITA", body, faq, related, "Onalar uchun")


def for_family():
    body = """
<p class="lede"><strong>Butun oila uchun AIVITA — har birining sog‘lig‘i saqlanadigan yagona joy:
bolalar, turmush o‘rtoqlar va keksa ota-onalar.</strong> Bitta ilova tahlillarni yo‘qotmaslikka,
qabul va emlashlarni eslab qolishga va o‘z vaqtida kerakli shifokorga tushishga yordam beradi.</p>

<h2>Oilaga umumiy ilova nega kerak?</h2>
<p>Har bir oilada kasallik tarixi ertami-kechmi qog‘ozlar to‘plamiga aylanadi. AIVITA oilaning
barcha a’zolari <a href="/uz/features/medcard/">kartalarini</a> bir joyda, odamlar bo‘yicha
ajratib jamlaydi. Qabulda bolaning nima bilan kasallanganini yoki buvining qanday dori ichishini
eslash shart emas — hammasi yozilgan.</p>

<h2>Keksa ota-onalar haqida g‘amxo‘rlik</h2>
<p>Keksa ota-onalarga muntazamlik ayniqsa muhim: bosim nazorati, dori qabuli, rejali tashriflar.
AIVITA ularning kartasini yuritishga, <a href="/uz/features/monitoring/">ko‘rsatkichlarni
kuzatishga</a>, <a href="/uz/features/drug-checker/">dori mosligini tekshirishga</a> yordam beradi.
Agar ota-onalar boshqa hududda yashasa, telemeditsina masofadan g‘amxo‘rlik qilish imkonini beradi.</p>

<h2>Bolalar va o‘smirlar</h2>
<p>Bolalar uchun emlashlar, kasalliklar tarixi va pediatrga tez kirish muhim. Ota-onalar bola
kartasini yuritadi va emlash haqida eslatma oladi. Batafsil — <a href="/uz/for/moms/">onalar uchun</a>
sahifasida.</p>

<h2>Favqulodda vaziyatlar</h2>
<p>Biror narsa yuz berganda, asosiy ma’lumotlar qo‘l ostida bo‘lishi muhim: qon guruhi, allergiyalar,
surunkali kasalliklar. AIVITA <a href="/uz/features/sos/">SOS-profili</a> bu ma’lumotni oilaning
har bir a’zosi uchun saqlaydi. Hayotga xavf bo‘lsa, darhol tez yordam chaqirish kerak.</p>

<h2>Masofadagi yaqinlar</h2>
<p>Ko‘p oilalarda kimdir boshqa shaharda yashaydi. Telemeditsina va yagona karta tufayli siz keksa
ota-onalarni yoki boshqa hududdagi qarindoshlarni ham qo‘llab-quvvatlashingiz mumkin: ular shifokorga
onlayn yoziladi, siz esa ularning sog‘lig‘i dinamikasini kuzatib borasiz.</p>

<h2>Sog‘liq — umumiy odat</h2>
<p>Sog‘liqqa g‘amxo‘rlik oilaviy odatga aylanganda, uni kuzatish osonroq. AIVITA tarqoq
harakatlarni tushunarli tizimga aylantiradi: har kimning o‘z manzarasi bor, lekin ularni bitta
ilovadan boshqarish mumkin — qulay tilda va O‘zbekistonning istalgan hududida.</p>
"""
    faq = [
        ("AIVITA’ga oilaning necha a’zosini qo‘shsa bo‘ladi?", "Ilovada bir necha a’zoning — bolalar, turmush o‘rtoq, keksa ota-onalarning kartasini odamlar bo‘yicha ajratib yuritish mumkin."),
        ("Ota-onalar sog‘lig‘ini masofadan kuzatsam bo‘ladimi?", "Ha. Telemeditsina va karta yuritish boshqa hududdagi keksa ota-onalarga ham yordam berish imkonini beradi."),
        ("Barcha a’zolar ma’lumotlari xavfsizmi?", "Ha. Har bir kartaga kirishni siz nazorat qilasiz, shifokor esa faqat ochilganda ko‘radi."),
        ("AIVITA keksalar uchun mosmi?", "Ha. Keksa insonning kartasini yuritadigan qarindosh ilovadan foydalanib, bosimni kuzatib, uni shifokorga yozishi mumkin."),
        ("Bu oila uchun pulli mi?", "Karta yuritish, monitoring va o‘z-o‘zini tekshirish bepul. Faqat onlayn maslahatlar to‘lanadi."),
    ]
    related = [("Onalar uchun", "/uz/for/moms/"),
               ("Elektron tibbiy karta", "/uz/features/medcard/"),
               ("Sog‘liq monitoringi", "/uz/features/monitoring/")]
    return _aud("family",
                "Butun oila uchun AIVITA — bolalar, ota-onalar va yaqinlar sog‘lig‘i",
                "Butun oila uchun AIVITA: bolalar, turmush o‘rtoqlar va keksa ota-onalar kartasi bitta ilovada, sog‘liq monitoringi, onlayn shifokorlar va SOS-profil. O‘zbekistonning istalgan hududida.",
                "Butun oila uchun AIVITA", body, faq, related, "Oila uchun")


def for_doctors():
    body = """
<p class="lede"><strong>Shifokor uchun AIVITA — yangi bemorlar kanali va qulay onlayn qabul
vositasi.</strong> Mutaxassis katalogdan yozilishlar oladi, bemor ruxsati bilan uning kartasini
ko‘radi va maslahatlarni masofadan olib boradi, klinika esa ishini <a href="/medsoft/">MedSoft</a>
tizimi bilan avtomatlashtiradi.</p>

<h2>AIVITA shifokorga bemor topishga qanday yordam beradi?</h2>
<p>AIVITA katalogi bemorlarga shifokorlarni mutaxassislik va hudud bo‘yicha ko‘rsatadi. Bemor
mutaxassisni tanlaydi, profilni ko‘radi va onlayn yoziladi — shifokor esa reklama va vositachisiz
murojaatlar oqimini oladi, jumladan boshqa hududlardan.</p>

<h2>Kartaga kirish bilan onlayn qabul</h2>
<p>Onlayn maslahatda shifokor bemor ochgan narsani ko‘radi: tahlillar, qabullar tarixi, tayinlovlar,
<a href="/uz/features/monitoring/">monitoring</a> ma’lumotlari. Bu masofaviy qabulni mazmunli
qiladi. Qabuldan so‘ng tayinlovlar bemor kartasida saqlanadi.</p>

<h2>MedSoft orqali klinika avtomatlashuvi</h2>
<p>Agar shifokor klinikada ishlasa, rutinani <a href="/medsoft/">MedSoft</a> o‘z zimmasiga oladi —
19 modulli tibbiy axborot tizimi: jadval, elektron kartalar, kassa, ombor, hisobot. MedSoft’ga
ulangan klinika AIVITA katalogidan bevosita bemorlar oladi.</p>

<h2>Bu klinikaga nima beradi?</h2>
<p>Kamroq qog‘ozbozlik va yo‘qolgan ma’lumotlar, tushunarli yozilish va jadval, katalogdan bemorlar
kirishi, yuklama va daromad bo‘yicha tahlil. Shifokor esa bemorga e’tibor qaratadi.</p>

<h2>Klinikaga nima beradi — batafsilroq</h2>
<p>MedSoft kichik klinikalar uchun tez ishga tushirishni, setlar va yirik markazlar uchun esa
binolar, bo‘limlar, rollar va yig‘ma hisobotli versiyani taklif qiladi. Shifokor jurnallarni
to‘ldirish bilan emas, bemor bilan shug‘ullanadi, boshqaruv esa yuklama va daromadning shaffof
manzarasini oladi. Katalogdan kelgan bemorlar bilan ishlash reklama xarajatlarisiz o‘sish beradi.</p>

<h2>Shifokor yoki klinika nimadan boshlashi kerak?</h2>
<p>MedSoft demonstratsiyasini so‘rashdan va AIVITA katalogida profil joylashtirishdan boshlash
mumkin. Keyin klinika modullarni o‘z jarayonlariga moslaydi, bemorlar esa onlayn yozila boshlaydi.
Batafsil — <a href="/medsoft/">MedSoft klinikalar uchun</a> bo‘limida.</p>
"""
    faq = [
        ("Shifokor AIVITA’dan qanday bemor oladi?", "Shifokor yoki klinika katalogda mutaxassislik va hudud bo‘yicha profil joylashtiradi, bemorlar esa onlayn yoziladi. Bu vositachisiz murojaatlar oqimi."),
        ("Shifokor bemor kartasini ko‘radimi?", "Ha, lekin faqat bemor ochgan qismini. Qabuldan so‘ng tayinlovlar uning kartasida saqlanadi."),
        ("AIVITA va MedSoft bog‘lanishi nima?", "MedSoft — klinikani avtomatlashtirish tizimi, AIVITA — bemor xizmati. MedSoft’dagi klinika AIVITA katalogidan bevosita bemor oladi."),
        ("AIVITA xususiy shifokorga mosmi?", "Ha. Xususiy mutaxassis onlayn qabullar o‘tkazishi va katalogdan yozilishlar olishi mumkin."),
        ("Demonstratsiyani qanday so‘rash mumkin?", "MedSoft bo‘limida ariza qoldiring — jamoa tizimni ko‘rsatadi va katalogga ulanishga yordam beradi."),
    ]
    related = [("MedSoft klinikalar uchun", "/medsoft/"),
               ("Onlayn shifokorlar", "/uz/features/doctors/"),
               ("Biz haqimizda", "/uz/about/")]
    return _aud("doctors",
                "Shifokorlar va klinikalar uchun AIVITA — onlayn bemorlar",
                "Shifokorlar uchun AIVITA: katalogdan bemorlar oqimi, kartaga kirish bilan onlayn qabullar va MedSoft orqali klinika avtomatlashuvi. Amaliyotingizni bir kabinetdan tashqariga kengaytiring.",
                "Shifokorlar uchun AIVITA", body, faq, related, "Shifokorlar uchun",
                disclaimer=False,
                cta=("Klinikani MedSoft va AIVITA’ga ulang",
                     "Klinika ishini avtomatlashtiring va AIVITA katalogidan bemorlar oling. MedSoft demonstratsiyasini so‘rang.",
                     "Demo so‘rash", "/medsoft/"))


def about():
    body = """
<p class="lede"><strong>AIVITA — O‘zbekistonda sog‘liqni saqlash bo‘yicha raqamli ekotizim bo‘lib,
bemorlar, klinikalar va mutaxassislarni uch tilda birlashtiradi.</strong> Bizning maqsadimiz —
sifatli tibbiy yordamni shahar va tildan qat’i nazar har bir kishiga yetkazish.</p>

<h2>Bizning maqsadimiz</h2>
<p>Biz sog‘liqqa g‘amxo‘rlik navbat, masofa va qog‘ozbozlikka bog‘lanib qolmasligi kerak deb
hisoblaymiz. AIVITA insonni tibbiyot bilan sodda bog‘laydi: o‘z-o‘zini tekshirish, elektron tibbiy
karta, dori tekshiruvi, monitoring va onlayn shifokorlar — bitta ilovada. Biz O‘zbekistonning
barcha hududlarida ishlaymiz.</p>

<h2>AIVITA ekotizimi</h2>
<p>AIVITA — bitta ilova emas, balki uchta o‘zaro bog‘liq yo‘nalishdan iborat ekotizim: bemorlar
uchun xizmat, klinikalar uchun tizim va go‘zallik salonlari uchun yechim.</p>

<div class="grid grid-3">
  <div class="card"><div class="ic">🩺</div><h3>AIVITA — bemorlarga</h3>
  <p>AI-checkup, elektron tibbiy karta, dori tekshiruvi, sog‘liq monitoringi va onlayn shifokorlar.</p>
  <a class="more" href="/uz/features/">Imkoniyatlar →</a></div>

  <div class="card"><div class="ic">🏥</div><h3>MedSoft — klinikalarga</h3>
  <p>Klinikalarni avtomatlashtirish uchun tibbiy axborot tizimi. MedSoft’dagi klinikalar AIVITA
  katalogidan bemorlar oladi.</p>
  <a class="more" href="/medsoft/">MedSoft haqida →</a></div>

  <div class="card"><div class="ic">💄</div><h3>AIVITA Beauty — salonlarga</h3>
  <p>Go‘zallik salonlari uchun yechim: kosmetolog va ustalarga onlayn yozilish, kosmetologiya va
  vizaj xizmatlari.</p>
  <span class="more">Ekotizim qismi</span></div>
</div>

<h2>AIVITA Beauty: go‘zallik va parvarish</h2>
<p>AIVITA Beauty ekotizimni estetika va parvarish tomon kengaytiradi. Bu go‘zallik salonlari va
ularning mijozlari uchun yo‘nalish: go‘zallik saloniga onlayn yozilish, kosmetologiya, vizaj va
parvarish xizmatlari. Mijozga salonni topib, onlayn yozilish qulay, salonga esa jadvalni yuritish
va qo‘ng‘iroqsiz yozilishlar olish qulay.</p>

<h2>Biz butun O‘zbekiston bo‘ylab ishlaymiz</h2>
<p>AIVITA barcha <a href="/uz/regions/">hududlarda</a> mavjud — Qoraqalpog‘istondan Farg‘ona
vodiysigacha. Telemeditsina tufayli istalgan shahar aholisi shifokorlarga kirish imkoniga ega
bo‘ladi, rus, o‘zbek va ingliz tillaridagi interfeys esa xizmatni har kimga tushunarli qiladi.</p>

<h2>Bizning tamoyillarimiz</h2>
<p>Biz shifokor o‘rnini bosmaymiz va tashxis qo‘ymaymiz — biz odamlarga sog‘liqqa g‘amxo‘rlik
qilishga yordam beramiz. Biz shaxsiy ma’lumotlarga ehtiyot bo‘lamiz: kartaga kirishni bemorning
o‘zi nazorat qiladi. Va biz ishonchli ma’lumotga tayanamiz.</p>
"""
    faq = [
        ("AIVITA nima?", "O‘zbekistonda sog‘liqni saqlash bo‘yicha raqamli ekotizim: bemorlar uchun xizmat, klinikalar uchun MedSoft tizimi va salonlar uchun AIVITA Beauty. Uch tilda ishlaydi."),
        ("AIVITA ekotizimiga nimalar kiradi?", "Uchta yo‘nalish: bemorlar uchun AIVITA (checkup, karta, onlayn shifokorlar), klinikalar uchun MedSoft va salonlar uchun AIVITA Beauty."),
        ("AIVITA Beauty nima?", "Go‘zallik salonlari va mijozlar uchun yo‘nalish: salonga onlayn yozilish, kosmetologiya va vizaj xizmatlari."),
        ("AIVITA qaysi hududlarda ishlaydi?", "O‘zbekistonning barcha hududlarida. Telemeditsina istalgan shahardan shifokorlarga kirishni ochadi, interfeys esa uch tilda."),
        ("AIVITA shifokor o‘rnini bosadimi?", "Yo‘q. AIVITA sog‘liqqa g‘amxo‘rlik qilishga yordam beradi, lekin tashxis qo‘ymaydi va davolashni tayinlamaydi — buni shifokor qiladi."),
    ]
    schema = [
        {"@type": "AboutPage", "name": "AIVITA haqida", "url": DOMAIN + "/uz/about/",
         "inLanguage": "uz", "isPartOf": {"@id": DOMAIN + "/#website"}},
        {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/", "email": "hello@aivita.uz",
         "areaServed": "UZ", "logo": DOMAIN + "/assets/og-image.svg"},
    ]
    return Page(
        path="uz/about", lang="uz",
        title="AIVITA haqida — O‘zbekistonda sog‘liq ekotizimi",
        description="AIVITA haqida: maqsad, AIVITA (bemorlar), MedSoft (klinikalar) va AIVITA Beauty (go‘zallik salonlari) ekotizimi. O‘zbekistonning barcha hududlarida uch tilda ishlaymiz.",
        h1="AIVITA haqida",
        body=body, faq=faq, schema=schema, section="about",
        crumbs=[("Bosh sahifa", "/uz/"), ("Biz haqimizda", None)],
        hreflang=alts("about", langs=("ru", "uz", "en")),
        disclaimer=True,
        related=[("Imkoniyatlar", "/uz/features/"), ("Hududlar", "/uz/regions/"),
                 ("Sog‘liq blogi", "/uz/blog/")],
    )


def pages():
    return [home(), features_hub(), f_aicheckup(), f_drug(), f_medcard(),
            f_doctors(), f_sos(), f_monitoring(),
            for_moms(), for_family(), for_doctors(), about()]
