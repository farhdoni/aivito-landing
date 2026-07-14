# -*- coding: utf-8 -*-
"""Этап 9 (uz) — Blog /uz/blog/. Top-10 maqola (tibbiyot) + hub. hreflang ru/uz."""
from engine import Page, DOMAIN, BRAND, alts


def art(a):
    slug = a["slug"]
    schema = [{
        "@type": "Article", "headline": a["h1"], "description": a["desc"],
        "datePublished": a["date"], "dateModified": a["date"], "inLanguage": "uz",
        "author": {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/"},
        "publisher": {"@type": "Organization", "name": BRAND,
                      "logo": {"@type": "ImageObject", "url": DOMAIN + "/assets/og-image.svg"}},
        "mainEntityOfPage": DOMAIN + f"/uz/blog/{slug}/",
        "image": DOMAIN + "/assets/og-image.svg", "articleSection": "Tibbiyot",
    }]
    return Page(
        path=f"uz/blog/{slug}", lang="uz", title=a["title"], description=a["desc"],
        h1=a["h1"], body=a["body"], faq=a["faq"], related=a["related"],
        section="blog", updated=a["date"], og_type="article",
        crumbs=[("Bosh sahifa", "/uz/"), ("Blog", "/uz/blog/"), (a["h1"], None)],
        hreflang=alts(f"blog/{slug}", langs=("ru", "uz")),
        disclaimer=a.get("disclaimer", True), schema=schema,
    )


ARTS = [
{
"slug": "5-simptomov-nelzya-ignorirovat", "date": "2026-02-03",
"title": "E’tiborsiz qoldirib bo‘lmaydigan 5 simptom — qachon shifokorga?",
"desc": "Kechiktirib bo‘lmaydigan beshta xavotirli simptom: ko‘krak og‘rig‘i, nafas qisilishi, vazn yo‘qotish, qon va to‘satdan holsizlik. Ular nimani anglatishi va nima qilish kerak.",
"h1": "E’tiborsiz qoldirib bo‘lmaydigan 5 simptom",
"body": """
<p class="lede"><strong>Ba’zi simptomlar — organizmning charchoqqa yozib bo‘lmaydigan
signali.</strong> Ko‘krak og‘rig‘i, to‘satdan nafas qisilishi, sababsiz vazn yo‘qotish, bo‘lmasligi
kerak bo‘lgan joydagi qon va keskin holsizlik — beshta belgi, bunda imkon qadar tez shifokorga
murojaat qilish kerak.</p>

<h2>1. Ko‘krakdagi og‘riq yoki bosim</h2>
<p>Ko‘krakdagi og‘riq, og‘irlik yoki qisilish — ayniqsa qo‘lga, bo‘yinga yoki jag‘ga tarqalsa,
nafas qisilishi, sovuq ter yoki ko‘ngil aynishi bilan birga kelsa — yurak muammolari belgisi
bo‘lishi mumkin. Bunday og‘riqni «oyoqda» o‘tkazib bo‘lmaydi. U birinchi marta paydo bo‘lsa yoki
kuchaysa, darhol tez yordam chaqiring.</p>

<h2>2. To‘satdan nafas qisilishi</h2>
<p>Ilgari bo‘lmagan, tinch holatda yoki kichik yukda havo yetishmasligi hissi — jiddiy simptom.
Nafas qisilishi yurak, o‘pka yoki kamqonlik bilan bog‘liq bo‘lishi mumkin, lekin ularni tekshiruvsiz
ajratib bo‘lmaydi. Nafas keskin qiyinlashsa, ko‘krak og‘rig‘i yoki lablar ko‘karishi bilan kelsa —
bu shoshilinch holat.</p>

<h2>3. Sababsiz vazn yo‘qotish</h2>
<p>Vazn parhez va yuksiz ketsa — masalan, bir necha oyda bir necha kilogramm — bu har doim ham yaxshi
xabar emas. Sababsiz sezilarli vazn yo‘qotish qalqonsimon bez, hazm, moddalar almashinuvi
kasalliklari bilan kelishi mumkin. <a href="/uz/features/doctors/">Terapevtga</a> murojaat qiling:
u tekshiruv tayinlaydi.</p>

<h2>4. Bo‘lmasligi kerak bo‘lgan qon</h2>
<p>Balg‘amdagi, siydikdagi, najasdagi qon, shuningdek g‘ayrioddiy qon ketishlar — har qanday yoshda
e’tiborsiz qoldirib bo‘lmaydigan simptom. Sabablari turlicha, aynan shuning uchun yuzma-yuz
diagnostika kerak. Internet orqali tashxis qo‘yishga urinmang va murojaatni kechiktirmang.</p>

<h2>5. To‘satdan holsizlik, uvishish yoki nutq buzilishi</h2>
<p>Qo‘l yoki oyoqdagi keskin holsizlik, yuzning qiyshayishi, chalkash nutq, to‘satdan kuchli bosh
og‘rig‘i yoki muvozanat yo‘qolishi — insult belgilari bo‘lishi mumkin. Bu yerda hisob daqiqalarga
boradi: qanchalik tez shifokorlarga yetib borsa, tiklanish imkoniyati shunchalik yuqori. Belgilarni
sezib, darhol tez yordam chaqiring.</p>

<h2>Xavotirli signallarni qanday o‘tkazib yubormaslik kerak</h2>
<p>Ko‘p jiddiy holatlar sezilmas o‘zgarishlardan boshlanadi. Muntazam
<a href="/uz/features/ai-checkup/">o‘z-o‘zini tekshirish</a> va o‘zni his qilishga e’tibor ularni
ertaroq sezishga yordam beradi. Nimadir xavotirga solsa-yu, ammo hozir hayotga xavf solmasa,
maslahatni kechiktirmang — <a href="/uz/features/doctors/">shifokorga onlayn</a> yoziling.</p>

<h2>Qachon darhol tez yordam chaqirish kerak</h2>
<p>O‘ylanmang va tez yordam (103) yoki yagona xizmat (112) ga qo‘ng‘iroq qiling, agar: ko‘krakdagi
kuchli og‘riq, keskin nafas qisilishi, insult belgilari, ko‘p qon ketishi, hushdan ketish, talvasa
yoki shishli kuchli allergik reaksiya bo‘lsa. Bu holatlarda kutish xavfli.</p>
""",
"faq": [
("Qaysi simptomlarda darhol tez yordam kerak?", "Ko‘krakdagi kuchli og‘riq, keskin nafas qisilishi, insult belgilari (yuz qiyshayishi, qo‘l holsizligi, nutq buzilishi), ko‘p qon ketishi va og‘ir allergik reaksiya."),
("Qo‘lga tarqaladigan ko‘krak og‘rig‘i nimani anglatadi?", "Bu yurak muammolari belgisi bo‘lishi mumkin, ayniqsa nafas qisilishi va sovuq ter bilan. Og‘riq o‘tishini kutmasdan darhol tez yordam chaqiring."),
("Sababsiz vazn yo‘qotishdan xavotir olish kerakmi?", "Ha. Parhez va yuksiz sezilarli vazn kamayishi terapevtga murojaat qilib, tekshiruvdan o‘tish uchun sabab."),
("Simptomlar bo‘yicha internetda tashxis qo‘ysa bo‘ladimi?", "Yo‘q. Bir xil simptom turli holatlarda bo‘ladi. Tashxisni faqat shifokor ko‘rikdan so‘ng qo‘yadi."),
("Insult belgilarida qanchalik tez harakat qilish kerak?", "Imkon qadar tez. Yuz qiyshayishi, qo‘l holsizligi va nutq buzilishida darhol tez yordam chaqiring va belgilar qachon boshlanganini eslab qoling."),
],
"related": [("Yaxshi shifokorni qanday tanlash", "/uz/blog/kak-vybrat-vracha/"),
            ("Bosimni qanday to‘g‘ri o‘lchash", "/uz/blog/kak-izmerit-davlenie/"),
            ("SOS-yordam", "/uz/features/sos/")],
},
{
"slug": "biologicheskiy-vozrast", "date": "2026-02-10",
"title": "Biologik yosh: bu nima va uni qanday bilish mumkin",
"desc": "Biologik yosh nima, u pasport yoshidan qanday farq qiladi, unga qanday omillar ta’sir qiladi va turmush tarzi organizmni «yoshartirishga» qanday yordam beradi. Mish-mishlarsiz.",
"h1": "Biologik yosh: bu nima va uni pasaytirsa bo‘ladimi",
"body": """
<p class="lede"><strong>Biologik yosh — organizm qanchalik «eskirgani» ko‘rsatkichi bo‘lib, tug‘ilgandan
beri yillarni sanaydigan pasport yoshidan farq qiladi.</strong> Bir xil yoshdagi ikki kishi yurak,
tomirlar va moddalar almashinuvi holati bo‘yicha keskin farq qilishi mumkin.</p>

<h2>Biologik yosh pasport yoshidan qanday farq qiladi?</h2>
<p>Pasport yoshi o‘zgarmas: har yili bir yilga o‘sadi. Biologik yosh — baholovchi: u organizm holatini
shu yillar uchun o‘rtachaga nisbatan ko‘rsatadi. Agar odam faol bo‘lsa, chekmasa, yaxshi uxlasa va
to‘g‘ri ovqatlansa, uning biologik yoshi pasport yoshidan past bo‘lishi mumkin.</p>

<h2>Biologik yoshga nima ta’sir qiladi?</h2>
<p>Unga ko‘plab omillar ta’sir qiladi: jismoniy faollik, uyqu sifati, ovqatlanish, stress darajasi,
chekish va alkogol, tana vazni, arterial bosim va qand darajasi. Ularning bir qismi genetika bilan
belgilangan, lekin katta qismi — turmush tarzi, unga ta’sir qilish mumkin.</p>

<h2>Biologik yosh qanday baholanadi?</h2>
<p>Turli usullar bor — turmush tarzi bo‘yicha so‘rovnomalardan tortib laboratoriya belgilarigacha.
Ko‘rsatkichlarga (bosim, tinch holatdagi puls, faollik, uyqu, vazn) asoslangan oddiy baholar tashxis
emas, mo‘ljal beradi. Boshlang‘ich tasavvurni <a href="/uz/features/monitoring/">sog‘liq
monitoringi</a> va <a href="/uz/features/ai-checkup/">o‘z-o‘zini tekshirish</a> orqali olish mumkin.</p>

<h2>Biologik yoshni pasaytirsa bo‘ladimi?</h2>
<p>Vaqtni butunlay orqaga qaytarib bo‘lmaydi, lekin organizm holatini yaxshilash mumkin. Muntazam
mo‘tadil faollik yurak va tomirlarni mustahkamlaydi, sifatli uyqu asab tizimini tiklaydi,
muvozanatli ovqatlanish normal vaznni ushlab turishga yordam beradi, chekishdan voz kechish xavflarni
kamaytiradi.</p>

<h2>Nimadan boshlash kerak</h2>
<p>Hammasini birdan o‘zgartirish shart emas. Bitta odatni tanlang: masalan, kunlik yurishdan
boshlang yoki uyqu rejimini yo‘lga qo‘ying. Bir necha haftadan so‘ng keyingisini qo‘shing.
Ko‘rsatkichlar dinamikasini <a href="/uz/features/monitoring/">monitoringda</a> kuzating —
shunda harakatlaringiz natija berayotganini ko‘rasiz.</p>

<h2>Muntazam kuzatuvning roli</h2>
<p>Bir martalik o‘lchov kam narsa aytadi — dinamika muhim. Bosim, puls, uyqu va faollikni vaqt bo‘yicha
kuzatib, siz va shifokoringiz sog‘liq qaysi tomonga borayotganini ko‘rasiz. AIVITA bu ma’lumotlarni
yagona <a href="/uz/features/medcard/">kundalikda</a> jamlashga yordam beradi.</p>
""",
"faq": [
("Biologik yosh oddiy so‘z bilan nima?", "Bu — organizm holatining yoshingizga nisbatan bahosi. U turmush tarzi va sog‘liqqa qarab pasport yoshidan yuqori yoki past bo‘lishi mumkin."),
("Biologik yoshni pasaytirsa bo‘ladimi?", "Vaqtni qaytarib bo‘lmaydi, lekin organizm holatini yaxshilash mumkin: faollik, uyqu, ovqatlanish va chekishdan voz kechish ko‘rsatkichlarga ijobiy ta’sir qiladi."),
("Qaysi omillar biologik yoshga eng ko‘p ta’sir qiladi?", "Jismoniy faollik, uyqu sifati, ovqatlanish, stress, chekish va alkogol, vazn, bosim va qand. Aksariyati turmush tarziga bog‘liq."),
("Onlayn baholar aniqmi?", "Oddiy baholar mo‘ljal beradi, tibbiy tashxis emas. Aniq manzara uchun tekshiruv va shifokor bilan suhbat kerak."),
("Taraqqiyotni qanday kuzatish kerak?", "Ko‘rsatkichlar dinamikasini vaqt bo‘yicha kuzating. O‘zgarishlar aynan dinamikada ko‘rinadi, bir martalik o‘lchovda emas."),
],
"related": [("Elektron tibbiy karta: nega kerak", "/uz/blog/elektronnaya-medkarta/"),
            ("Bosimni qanday to‘g‘ri o‘lchash", "/uz/blog/kak-izmerit-davlenie/"),
            ("Sog‘liq monitoringi", "/uz/features/monitoring/")],
},
{
"slug": "sovmestimost-lekarstv", "date": "2026-02-17",
"title": "Dorilar mosligi: bir necha preparat qabul qilishda o‘zingizga zarar yetkazmaslik",
"desc": "Nega dorilar bir-biriga zid bo‘lishi mumkin, qaysi birikmalar xavfli, dorilar mosligini qanday tekshirish va nega shifokorga hamma narsani aytish muhim.",
"h1": "Dorilar mosligi: xavfli birikmalardan qanday qochish kerak",
"body": """
<p class="lede"><strong>Dorilar mosligi — turli preparatlarning bir vaqtda qabul qilinganda qanday
ta’sir qilishi.</strong> Ularning ba’zilari bir-birini kuchaytiradi yoki kuchsizlantiradi, ayrim
birikmalar esa xavfli bo‘lishi mumkin. Buni oldindan tushunish muhim.</p>

<h2>Nega dorilar bir-biriga zid keladi?</h2>
<p>Har bir preparat organizmdagi jarayonlarga ta’sir qiladi, ular bir nechta bo‘lganda bu ta’sirlar
kesishadi. Bir dori boshqasining chiqarilishini tezlashtirib, ta’sirini kamaytirishi mumkin; boshqasi
sekinlashtirib, ta’sirni nomaqbul darajaga oshirishi mumkin. Ba’zi birikmalar jigar, buyrak yoki
yurakka yukni oshiradi.</p>

<h2>Kim xavf guruhida?</h2>
<p>Moslikka alohida e’tibor bir necha preparatni doimiy qabul qiladiganlarga kerak: keksalar,
surunkali kasalliklari borlar, homilador ayollar. Xavf dorilarni turli shifokorlar bir-biridan
bexabar tayinlaganda yoki odam retseptsiz vositalar va BAD’larni o‘zi qo‘shganda ortadi.</p>

<h2>Dorilar mosligini qanday tekshirish mumkin?</h2>
<p>Birinchi qadam — qabul qilayotgan hamma narsaning to‘liq ro‘yxatini tuzish, jumladan vitaminlar va
qo‘shimchalar. Mumkin bo‘lgan o‘zaro ta’sirlarni tez baholashga AIVITA’dagi
<a href="/uz/features/drug-checker/">dori tekshiruvi</a> yordam beradi. Bu mutaxassis bilan suhbat
uchun mo‘ljal, uning qarorining o‘rnini bosmaydi.</p>

<h2>Nega shifokorga hamma narsani aytish muhim</h2>
<p>Shifokor o‘zaro ta’sirlarni faqat to‘liq manzarani bilsagina hisobga oladi. Qabul qilayotgan
barcha dorilar, qo‘shimchalar va o‘simlik vositalari haqida ayting — hatto ularni zararsiz deb
hisoblasangiz ham. Bularning barchasi <a href="/uz/features/medcard/">elektron kartada</a> yozilgan
bo‘lsa qulay.</p>

<h2>Nima qilib bo‘lmaydi</h2>
<p>Onlayn tekshiruv xavf ko‘rsatgani uchun tayinlangan dorini o‘zboshimchalik bilan bekor qilib yoki
dozani o‘zgartirib bo‘lmaydi — ba’zi preparatlarni keskin to‘xtatish o‘zaro ta’sirdan xavfliroq.
Dorilarni alkogol bilan yoki nima bo‘lsa u bilan ichib bo‘lmaydi. Har qanday o‘zgarish — shifokor
yoki farmatsevt orqali.</p>

<h2>Oddiy xavfsizlik qoidalari</h2>
<p>Dorilarning dolzarb ro‘yxatini yuriting va uni qo‘l ostida saqlang. Yangi dorilarni joriylardan
oldin mosligiga tekshiring. Aptekada farmatsevtdan retseptsiz vosita davolashingizga mos kelishini
so‘rang. Va tayinlovlarni kartada saqlang.</p>
""",
"faq": [
("Dorilarim mosligini qanday tekshiraman?", "Preparatlarning to‘liq ro‘yxatini tuzing va ularni dori tekshiruvi xizmatida tekshiring, so‘ng natijani shifokor bilan muhokama qiling. Onlayn tekshiruv — mo‘ljal, tayinlash emas."),
("Bir vaqtda bir necha dori ichish xavflimi?", "Har doim ham emas, lekin preparatlar soni ortishi bilan o‘zaro ta’sir xavfi oshadi. Ayniqsa keksalar va bir necha surunkali kasalligi borlar ehtiyot bo‘lishi kerak."),
("Vitaminlar va BAD dorilar bilan zid kelishi mumkinmi?", "Ha. Qo‘shimchalar va o‘simlik vositalari ham organizmga ta’sir qiladi va dorilar ta’sirini o‘zgartirishi mumkin, shuning uchun ular haqida shifokorga aytish kerak."),
("Tekshiruv xavfli birikma ko‘rsatsa nima qilish kerak?", "Dorini o‘zingiz bekor qilmang. Natijani saqlab, shifokor bilan muhokama qiling — ehtimol qabul vaqtini yoki dozani o‘zgartirish kerak bo‘ladi."),
("Nega shifokor barcha dorilar haqida so‘raydi?", "O‘zaro ta’sirlarni hisobga olib, zid preparat tayinlamaslik uchun. To‘liq ro‘yxat, ayniqsa kartada yozilgani, davolashni xavfsizroq qiladi."),
],
"related": [("Dori mosligini tekshirish", "/uz/features/drug-checker/"),
            ("Elektron tibbiy karta", "/uz/blog/elektronnaya-medkarta/"),
            ("Onlayn shifokorlar", "/uz/features/doctors/")],
},
{
"slug": "elektronnaya-medkarta", "date": "2026-02-24",
"title": "Elektron tibbiy karta: nega kerak va uni qanday yuritish kerak",
"desc": "Elektron tibbiy karta nima, u qog‘ozdan nimasi bilan qulay, unda nimani saqlash kerak va u shifokorga qanday yordam beradi. Bemor uchun oddiy qo‘llanma.",
"h1": "Elektron tibbiy karta: nega kerak",
"body": """
<p class="lede"><strong>Elektron tibbiy karta — sog‘lig‘ingizning raqamli tarixi: tahlillar,
qabullar, tashxislar va tayinlovlar bir joyda.</strong> Qog‘oz kartadan farqli, uni yo‘qotib yoki
uyda unutib bo‘lmaydi, shifokor esa ruxsatingiz bilan to‘liq manzarani soniyalar ichida ko‘radi.</p>

<h2>Elektron tibbiy karta nima?</h2>
<p>Bu — inson haqidagi tibbiy ma’lumotlarning raqamli ko‘rinishdagi tuzilgan ombori. Bunga tahlil
natijalari, shifokor xulosalari, kasalliklar tarixi, tayinlangan dorilar, emlashlar va sog‘liq
kuzatuvi ma’lumotlari kiradi. Bularning barchasi telefondan mavjud va sanalar bo‘yicha tartiblangan.</p>

<h2>Elektron karta qog‘ozdan nimasi bilan yaxshi?</h2>
<p>Qog‘oz karta yo‘qoladi, o‘chadi, bitta poliklinikada qoladi. Elektron karta doim yoningizda, uni
istalgan shifokorga tez ko‘rsatish mumkin va ko‘chishda yo‘qolmaydi. Tarix bir joyda bo‘lsa,
mutaxassis uni tiklashga vaqt sarflamaydi va allaqachon qilingan tahlillarni qayta tayinlamaydi.</p>

<h2>Kartada nima saqlash kerak?</h2>
<p>Barcha muhim narsalarni kiritish foydali: tahlil va tekshiruv natijalari, davolashdan keyingi
xulosalar, tashxislar, doimiy dorilar ro‘yxati, allergiyalar, emlashlar. Alohida
<a href="/uz/features/monitoring/">monitoring</a> ma’lumotlarini — bosim, puls, uyqu dinamikasini
belgilash kerak.</p>

<h2>Ma’lumotlarimni kim ko‘radi?</h2>
<p>AIVITA <a href="/uz/features/medcard/">kartasida</a> sukut bo‘yicha faqat sizda kirish bor.
Shifokor kerakli qismni faqat siz uni muayyan maslahat uchun ochganingizda oladi, qabuldan so‘ng
ruxsatni yopish mumkin. Kim nimani ko‘rishini doim siz hal qilasiz.</p>

<h2>Qog‘oz hujjatlarni qanday o‘tkazish mumkin?</h2>
<p>Eski tahlillar va xulosalarni qo‘lda kiritish yoki suratga olish mumkin — ular kartada sanalar
bo‘yicha saqlanadi. Agar qog‘oz natijalarni yo‘qotib qo‘ygan bo‘lsangiz, bor narsadan boshlab
kartani yuriting va yangi hujjatlarni darhol qo‘shing.</p>

<h2>Butun oila uchun karta</h2>
<p>Nafaqat o‘z, balki yaqinlar — bolalar va keksa ota-onalar kartasini yuritish qulay. Shunda
bolaning <a href="/uz/blog/grafik-privivok-detyam/">emlash jadvali</a>, kasalliklari tarixi va
tayinlovlar doim qo‘l ostida.</p>
""",
"faq": [
("Elektron tibbiy karta nima?", "Bu — sog‘liqning raqamli tarixi: tahlillar, qabullar, tashxislar, tayinlovlar va emlashlar bir joyda, telefondan mavjud va sanalar bo‘yicha tartiblangan."),
("U qog‘oz kartadan nimasi bilan qulay?", "Uni yo‘qotib yoki unutib bo‘lmaydi, doim qo‘l ostida va klinika o‘zgarganda ham yo‘qolmaydi. Shifokor to‘liq manzarani tez ko‘radi."),
("Ma’lumotlarimga kim kira oladi?", "Faqat siz. Shifokor ma’lumotlarni faqat siz maslahat uchun ochganingizda ko‘radi, qabuldan so‘ng yopish mumkin."),
("Eski qog‘oz tahlillarni qanday qo‘shaman?", "Ularni qo‘lda kiritish yoki suratga olish mumkin — hujjatlar sanalar bo‘yicha saqlanadi va yo‘qolmaydi."),
("Bolaning kartasini yuritsam bo‘ladimi?", "Ha. Yaqinlar — bolalar va keksa ota-onalar kartasini, jumladan emlash jadvalini yuritish qulay."),
],
"related": [("Elektron tibbiy karta", "/uz/features/medcard/"),
            ("Bosimni qanday to‘g‘ri o‘lchash", "/uz/blog/kak-izmerit-davlenie/"),
            ("Bolalar emlash jadvali", "/uz/blog/grafik-privivok-detyam/")],
},
{
"slug": "kak-vybrat-vracha", "date": "2026-03-03",
"title": "Yaxshi shifokorni qanday tanlash: nimaga e’tibor berish kerak",
"desc": "Shifokor tanlashning amaliy mezonlari: mutaxassislik, tajriba, sharhlar, qabul qanday o‘tishi va nega ishonch muhim. Onlayn mutaxassisni qanday tanlash va xato qilmaslik.",
"h1": "Yaxshi shifokorni qanday tanlash",
"body": """
<p class="lede"><strong>Yaxshi shifokor — bu faqat diplom emas, balki mos mutaxassislik, sizning
muammongizdagi tajriba va tushunarli tushuntira olish qobiliyati.</strong> Mutaxassisni tanlashda
nimaga qarash kerakligini ko‘rib chiqamiz.</p>

<h2>To‘g‘ri mutaxassislikdan boshlang</h2>
<p>Muvaffaqiyatning yarmi — kerakli mutaxassisga tushish. Umumiy shikoyatlar va birlamchi baholash
uchun <a href="/uz/features/doctors/">terapevt</a> mos: u yo‘naltiradi va kerak bo‘lsa profil
shifokorga jo‘natadi. Aniq muammo bilan to‘g‘ridan-to‘g‘ri mutaxassisga borgan ma’qul. Shubhalansangiz,
terapevtdan boshlang.</p>

<h2>Tajriba va profil regaliyadan muhimroq</h2>
<p>Umumiy staj emas, shifokor aynan sizning muammongiz bilan shug‘ullanishiga qarang. Shunga o‘xshash
holatlarni tez-tez ko‘radigan mutaxassis odatda tezroq yechim topadi. Shifokor qayerda ishlashi,
qaysi holatlarni olib borishi, sizning yoshingiz bilan tajribasi borligini bilish foydali.</p>

<h2>Sharhlarni qanday to‘g‘ri o‘qish kerak</h2>
<p>Sharhlar foydali, lekin ularga hushyor yondashuv kerak. Umumiy bahoga emas, mazmuniga e’tibor
bering: shifokor qanday muloqot qiladi, tayinlovlarni tushuntiradimi, e’tiborlimi. Yakka salbiy yoki
maqtov sharhlar umumiy qonuniyatdan kamroq ko‘rsatkichli.</p>

<h2>Shifokor sizga mos kelishini qanday tushunish mumkin?</h2>
<p>Yaxshi mutaxassis batafsil so‘raydi, nima bo‘layotganini va tayinlovlar nega kerakligini
tushuntiradi, savollardan bosh tortmaydi va sababsiz qo‘rqitmaydi. U tekshiruvga tayanadi va qo‘shimcha
diagnostika kerakligini halol aytadi. Qabuldan so‘ng nima qilishingizni tushunsangiz — bu yaxshi belgi.</p>

<h2>Xavotirli signallar</h2>
<p>Shifokor tashxisni so‘roq va ko‘riksiz darhol qo‘ysa; ko‘p qimmat tekshiruv va dorilarni izohsiz
tayinlasa; bosim o‘tkazsa, «kafolatlangan shifo» va’da qilsa yoki qo‘rqitsa — ehtiyot bo‘ling. Bunday
holatlarda ikkinchi fikr olish oqilona.</p>

<h2>Shifokorni onlayn tanlash</h2>
<p><a href="/uz/features/doctors/">AIVITA katalogi</a> orqali shifokorni mutaxassislik va hudud
bo‘yicha tanlab, profilni ko‘rib, onlayn maslahatga yozilish mumkin. Qabuldan oldin shifokorga
<a href="/uz/features/medcard/">kartaning</a> kerakli qismini oching. Telemeditsina, ayniqsa,
kerakli mutaxassis yaqinda bo‘lmaganda yordam beradi.</p>
""",
"faq": [
("Umumiy shikoyatlar bilan qaysi shifokorga borish kerak?", "Terapevtga. U birlamchi baholashni o‘tkazadi va kerak bo‘lsa profil mutaxassisga yo‘naltiradi, shunda vaqt yo‘qolmaydi."),
("Shifokor tajribasini qanday baholash mumkin?", "Umumiy stajga emas, shifokor aynan sizning muammongiz va yoshingiz bilan shug‘ullanishiga qarang. Profil tajriba umumiydan muhimroq."),
("Onlayn sharhlarga ishonsa bo‘ladimi?", "Qisman. Sharhlarning mazmuni — shifokor qanday muloqot qilishi — o‘rtacha bahodan muhimroq. Umumiy qonuniyat yakka holatlardan ko‘rsatkichliroq."),
("Yomon shifokor belgilari qanday?", "Ko‘riksiz darhol tashxis, ko‘p qimmat tekshiruvni izohsiz tayinlash, bosim va kafolatlangan shifo va’dasi. Bunday holatlarda ikkinchi fikr olish kerak."),
("Shifokorni onlayn qanday tanlash mumkin?", "AIVITA katalogida mutaxassislik va hududni tanlang, profilni o‘rganing va onlayn maslahatga yoziling, shifokorga kartaning kerakli qismini ochib."),
],
"related": [("O‘zbekistonda telemeditsina", "/uz/blog/telemedicina-v-uzbekistane/"),
            ("Onlayn shifokorlar", "/uz/features/doctors/"),
            ("E’tiborsiz qoldirib bo‘lmaydigan 5 simptom", "/uz/blog/5-simptomov-nelzya-ignorirovat/")],
},
{
"slug": "telemedicina-v-uzbekistane", "date": "2026-03-10",
"title": "O‘zbekistonda telemeditsina: shifokor maslahatini onlayn qanday olish mumkin",
"desc": "Telemeditsina nima, onlayn maslahat qanday o‘tadi, u qachon mos va qachon yuzma-yuz qabul kerak, va bu O‘zbekistonda barcha hududlar aholisi uchun qanday ishlaydi.",
"h1": "O‘zbekistonda telemeditsina",
"body": """
<p class="lede"><strong>Telemeditsina — klinikaga bormasdan, video yoki audio aloqa orqali shifokor
maslahati.</strong> O‘zbekiston uchun bu kuchli mutaxassislarni istalgan hudud aholisiga mavjud
qilish usuli: Toshkentdagi shifokor Nukus yoki Termizdagi bemorga maslahat berishi mumkin.</p>

<h2>Telemeditsina nima?</h2>
<p>Bu — shifokor va bemor onlayn muloqot qiladigan masofaviy tibbiy yordam. Shifokor shikoyatlar
haqida so‘raydi, <a href="/uz/features/medcard/">kartani</a> va tahlillarni o‘rganadi, savollarga
javob beradi va yuzma-yuz tashrif kerakmi, hal qiladi. Bu maslahatlar, tekshiruvlarni tahlil qilish
va takroriy qabullar uchun mos.</p>

<h2>Nega bu O‘zbekiston uchun ayniqsa muhim?</h2>
<p>Malakali mutaxassislar va zamonaviy diagnostika yirik shaharlarda to‘plangan, chekka tumandagi tor
shifokorga yetib borish esa uzoq. Telemeditsina bu to‘siqni olib tashlaydi: istalgan
<a href="/uz/regions/">hududdagi</a> bemor yaqinida bo‘lmasligi mumkin bo‘lgan mutaxassisga kirish
imkoniga ega bo‘ladi. Bu vaqt va yo‘l pulini tejaydi.</p>

<h2>Onlayn maslahat qanday o‘tadi?</h2>
<p>Siz kerakli mutaxassislikdagi shifokorni, qabul vaqtini tanlab, yozilishni tasdiqlaysiz. Maslahatdan
oldin kartaning bir qismini ochsangiz qulay. Belgilangan vaqtda videoqo‘ng‘iroq bo‘ladi: shikoyatlarni
aytasiz, shifokor savol beradi, kerak bo‘lsa biror narsani kameraga ko‘rsatishni so‘raydi. Qabuldan
so‘ng tavsiyalar kartada saqlanadi.</p>

<h2>Qachon telemeditsina yetarli?</h2>
<p>Onlayn tahlillarni tahlil qilish, takroriy qabullar, surunkali davolashni tuzatish, profilaktika
savollari va ikkinchi fikr uchun yaxshi. Bu klinikaga borish shart bo‘lmaganda, vaziyatni tushunish
yoki tavsiya olish kerak bo‘lganda qulay. Ko‘pincha bitta onlayn maslahat yetarli bo‘ladi.</p>

<h2>Qachon yuzma-yuz qabul kerak?</h2>
<p>Yuzma-yuz tashrif ko‘rik, o‘lchovlar yoki muolajalar kerak bo‘lganda zarur — o‘tkir og‘riq, jarohat,
yuqori harorat, masofadan baholab bo‘lmaydigan holatlarda. Yaxshi shifokor onlayn qabulda vaziyat
yuzma-yuz tekshiruvni talab qilsa, buni aytadi.</p>

<h2>Chegaralar va xavfsizlik</h2>
<p>Onlayn maslahat shoshilinch yordam o‘rnini bosmaydi. Xavfli simptomlarda — ko‘krakdagi kuchli
og‘riq, nafas qisilishi, insult belgilari — qabulni kutmang, <a href="/uz/features/sos/">SOS-yordam</a>dan
foydalaning va tez yordam (103) chaqiring. Qolgan hammasi uchun <a href="/uz/features/doctors/">AIVITA</a>
shifokorni yaqinlashtiradi.</p>
""",
"faq": [
("Telemeditsina nima?", "Bu — shifokorning onlayn, video yoki audio aloqa orqali maslahati. Shifokor shikoyatlarni so‘raydi, karta va tahlillarni o‘rganadi va yuzma-yuz tashrif kerakmi, hal qiladi."),
("Boshqa shahardagi shifokorga onlayn tushsam bo‘ladimi?", "Ha. Telemeditsina O‘zbekistonning istalgan hududidagi mutaxassis maslahatini safarsiz olish imkonini beradi."),
("Qachon onlayn maslahat yetarli?", "Tahlillarni tahlil qilish, takroriy qabullar, davolashni tuzatish, profilaktika savollari va ikkinchi fikr uchun. Ko‘pincha bitta maslahat yetarli."),
("Qachon yuzma-yuz qabul kerak?", "Ko‘rik, o‘lchovlar yoki muolajalar kerak bo‘lganda — o‘tkir og‘riq, jarohat, yuqori haroratda. Shifokor onlayn qabulda buni aytadi."),
("Telemeditsina tez yordam o‘rnini bosadimi?", "Yo‘q. Hayotga xavf soluvchi simptomlarda tez yordam (103) chaqirish kerak. Telemeditsina shoshilinch bo‘lmagan savollar uchun."),
],
"related": [("Yaxshi shifokorni qanday tanlash", "/uz/blog/kak-vybrat-vracha/"),
            ("Onlayn shifokorlar", "/uz/features/doctors/"),
            ("Hududlar", "/uz/regions/")],
},
{
"slug": "kak-izmerit-davlenie", "date": "2026-03-17",
"title": "Arterial bosimni uyda qanday to‘g‘ri o‘lchash kerak",
"desc": "Bosimni tonometr bilan uyda qanday o‘lchash: tayyorgarlik, to‘g‘ri holat, keng tarqalgan xatolar va bosim kundaligini qanday yuritish. Norma nima va qachon shifokorga.",
"h1": "Bosimni uyda qanday to‘g‘ri o‘lchash kerak",
"body": """
<p class="lede"><strong>Bosim o‘lchovi aniq bo‘lishi uchun tayyorgarlik, to‘g‘ri holat va xotirjamlik
muhim.</strong> Uy tonometri foydali vosita, lekin texnikadagi xatolar noto‘g‘ri raqamlar beradi,
ular tufayli behuda xavotirlanish yoki muammoni o‘tkazib yuborish mumkin.</p>

<h2>O‘lchovga qanday tayyorgarlik ko‘rish kerak?</h2>
<p>O‘lchovdan 30 daqiqa oldin kofe ichmang, chekmang va sport bilan shug‘ullanmang. Muolajadan oldin
5 daqiqa tinch o‘tiring. Kerak bo‘lsa hojatxonaga boring — to‘la siydik pufagi natijaga ta’sir qiladi.
Bosimni bir xil vaqtda o‘lchagan ma’qul, shunda ma’lumotlar solishtiriladigan bo‘ladi.</p>

<h2>To‘g‘ri holat</h2>
<p>Suyanchiqli stulga o‘tiring, unga suyaning, oyoqlarni chalishtirmang, tovonlar polda. Qo‘lni stolga
manjeta yurak sathida bo‘ladigan qilib qo‘ying. Manjetani yalang‘och yelkaga taqing (kiyim ustidan
emas), pastki chekkasi tirsak burmasidan 2–3 sm yuqorida. O‘lchov paytida gaplashmang va harakatlanmang.</p>

<h2>Keng tarqalgan xatolar</h2>
<p>Raqamlarni «yolg‘on» qiladigan xatolar: kofe yoki yukdan so‘ng darhol o‘lchash, muolaja paytida
gaplashish, qo‘l havoda yoki manjeta yurak sathida emasligi, juda bo‘sh yoki tor manjeta, kiyim
ustidan o‘lchash. Yana bir xato — bitta o‘lchov qilib xulosa chiqarish. Bosim tebranadi, shuning
uchun o‘lchovlar seriyasi va dinamika muhim.</p>

<h2>Necha marta o‘lchash kerak?</h2>
<p>Bosimni 1–2 daqiqa oralig‘ida ikki marta o‘lchab, o‘rtachasini yozgan foydali. Nazorat uchun
shifokorlar ko‘pincha buni bir necha kun ertalab va kechqurun qilishni tavsiya qiladi. Natijalarni
yozing — <a href="/uz/features/monitoring/">bosim kundaligini</a> ilovada yuritish qulay.</p>

<h2>Norma nima?</h2>
<p>Kattalar uchun taxminan 120/80 mm sim. ust. normal hisoblanadi, lekin chegaralar individual va
yosh hamda sog‘liq holatiga bog‘liq. Muttasil yuqori yoki past qiymatlar — o‘zboshimchalik bilan
davolashni tanlash emas, shifokorga murojaat qilish uchun sabab.</p>

<h2>Qachon shifokorga murojaat qilish kerak?</h2>
<p>Bosim muntazam normadan chiqsa, keskin sakrashlar, bosh og‘rig‘i, bosh aylanishi, ko‘krak og‘rig‘i
bo‘lsa — shifokorga murojaat qiling. Juda yuqori bosim kuchli bosh og‘rig‘i, ko‘rish yoki nutq
buzilishi bilan kelsa, shoshilinch yordam kerak. O‘lchovlar kundaligi shifokorga manzarani tez
tushunishga yordam beradi.</p>
""",
"faq": [
("Bosim o‘lchoviga qanday tayyorgarlik ko‘rish kerak?", "30 daqiqa oldin kofe ichmang, chekmang va yuklamang. O‘lchovdan oldin qulay holatda 5 daqiqa tinch o‘tiring."),
("To‘g‘ri holat qanday?", "Suyanchiqli stulda, oyoqlar chalishtirilmagan, qo‘l stolda, manjeta yurak sathida yalang‘och yelkada. O‘lchov paytida gaplashmang va harakatlanmang."),
("Bosimni necha marta o‘lchash kerak?", "1–2 daqiqa oralig‘ida ikki marta, o‘rtachasini yozib. Nazorat uchun — bir necha kun ertalab va kechqurun, dinamikani kuzatib."),
("Bosimni braslet bilan o‘lchasa bo‘ladimi?", "Brasletlar puls va umumiy dinamika uchun qulay, lekin bosim uchun kamroq aniq. Bosim nazorati uchun yelka tonometridan foydalaning."),
("Qachon bosim uchun shifokorga borish kerak?", "Bosim muntazam normadan chiqsa, keskin sakrashlar, bosh og‘rig‘i yoki ko‘krak og‘rig‘i bo‘lsa. Juda yuqori bosim ko‘rish yoki nutq buzilishi bilan kelsa, shoshilinch yordam kerak."),
],
"related": [("Sog‘liq monitoringi", "/uz/features/monitoring/"),
            ("Elektron tibbiy karta", "/uz/blog/elektronnaya-medkarta/"),
            ("E’tiborsiz qoldirib bo‘lmaydigan 5 simptom", "/uz/blog/5-simptomov-nelzya-ignorirovat/")],
},
{
"slug": "grafik-privivok-detyam", "date": "2026-03-24",
"title": "Bolalar emlash jadvali: vaksinatsiyani o‘tkazib yubormaslik",
"desc": "Emlash taqvimi nega kerak, u qanday tuzilgan, vaksinatsiya o‘tkazib yuborilganda nima qilish kerak va bolaning emlash jadvalini ilovada qanday qulay yuritish mumkin.",
"h1": "Bolalar emlash jadvali: hech narsani o‘tkazib yubormaslik",
"body": """
<p class="lede"><strong>Emlash taqvimi — bolani kerakli yoshda xavfli infeksiyalardan himoya qilishga
yordam beradigan vaksinatsiya jadvali.</strong> Muddatlarga rioya qilish muhim, lekin o‘tkazib
yuborishda sarosimaga tushmaslik yanada muhim: shifokor individual reja tuzishga yordam beradi.</p>

<h2>Emlash taqvimi nega kerak?</h2>
<p>Vaksinatsiya bola infeksiyalarga duch kelishidan oldin himoyani shakllantiradi. Taqvim emlashlarni
ular eng samarali va xavfsiz bo‘lgan yoshga bog‘laydi. Milliy emlash taqvimi asosiy vaksinalar to‘plami
va muddatlarni belgilaydi; u turli mamlakatlarda farq qilishi mumkin, shuning uchun shifokoringiz
tavsiyalariga tayaning.</p>

<h2>Jadval qanday tuzilgan?</h2>
<p>Emlashlar hayotning oy va yillari bo‘yicha taqsimlangan: bir qismi dastlabki oylarda, bir qismi 1–2
yoshda, bir qismi maktabgacha va maktab yoshida. Ba’zi vaksinalar himoya shakllanishi uchun oraliqlar
bilan bir necha doza talab qiladi. Shuning uchun nafaqat emlash faktiga, balki oraliqlarga ham rioya
qilish muhim.</p>

<h2>Emlash o‘tkazib yuborilsa nima qilish kerak?</h2>
<p>O‘tkazib yuborish — halokat emas va boshidan boshlash uchun sabab emas. Ko‘p hollarda vaksinatsiyani
shifokor tuzadigan individual jadval bo‘yicha davom ettirish mumkin. Hammasini birdan qoplashga
urinmang va sxemani internetdan tanlmang. <a href="/uz/features/doctors/">Pediatrga</a> murojaat qiling.</p>

<h2>Bolani emlashga qanday tayyorlash kerak?</h2>
<p>Vaksinatsiyadan oldin bola sog‘lom bo‘lishi kerak; shifokor uni ko‘rib, bugun emlash mumkinmi, hal
qiladi. Pediatrga allergiyalar, oldingi emlashlarga reaksiyalar va surunkali kasalliklar haqida ayting.
Emlashdan so‘ng holatni kuzating: haroratning biroz ko‘tarilishi yoki ukol joyi qizarishi — odatiy
reaksiya, lekin kuchli belgilar bo‘lsa shifokor bilan bog‘laning.</p>

<h2>Jadvalni qanday qulay yuritish mumkin?</h2>
<p>Emlash taqvimini yodda saqlash og‘ir, ayniqsa dozalar bir necha va oraliqlar turlicha bo‘lganda.
Uni bolaning <a href="/uz/features/medcard/">elektron kartasida</a> yuritish qulay: ilova vaksinatsiya
tarixini saqlaydi va keyingi sanalarni eslatadi. Bu ayniqsa <a href="/uz/for/moms/">onalarga</a>
yordam beradi.</p>

<h2>Mish-mishlar va ma’lumotga ishonch</h2>
<p>Emlashlar atrofida ko‘p mish-mish va qarama-qarshi ma’lumot bor. Shifokor tavsiyalari va rasmiy
manbalarga tayaning, mish-mish va forumlarga emas. Shubhalar bo‘lsa, ularni pediatr bilan muhokama
qiling — yaxshi shifokor har bir emlash nega kerakligini tinch tushuntiradi.</p>
""",
"faq": [
("Emlash taqvimi nima?", "Bu — bolaning yoshi bo‘yicha vaksinatsiya jadvali bo‘lib, uni infeksiyalardan eng samarali va xavfsiz muddatlarda himoya qilishga yordam beradi."),
("Emlash o‘tkazib yuborilsa nima qilish kerak?", "Boshidan boshlamaslik kerak. Ko‘p hollarda vaksinatsiyani pediatr tuzadigan individual jadval bo‘yicha davom ettiriladi."),
("Bolani emlashga qanday tayyorlash kerak?", "Bola sog‘lom bo‘lishi kerak; shifokor uni vaksinatsiyadan oldin ko‘radi. Allergiyalar va oldingi reaksiyalar haqida ayting."),
("Emlashdan keyingi harorat normalmi?", "Haroratning biroz ko‘tarilishi yoki ukol joyi qizarishi — odatiy reaksiya. Kuchli yoki g‘ayrioddiy belgilar bo‘lsa shifokor bilan bog‘laning."),
("Emlashlarni qanday unutmaslik kerak?", "Jadvalni bolaning elektron kartasida yuriting — ilova vaksinatsiya tarixini saqlaydi va keyingi sanalarni eslatadi."),
],
"related": [("Elektron tibbiy karta", "/uz/features/medcard/"),
            ("Onalar uchun AIVITA", "/uz/for/moms/"),
            ("Onlayn shifokorlar", "/uz/features/doctors/")],
},
{
"slug": "poteryal-analizy-chto-delat", "date": "2026-03-31",
"title": "Tahlillarni yo‘qotdim: nima qilish va natijalarni qanday tiklash kerak",
"desc": "Tahlil natijalarini yoki tibbiy hujjatlarni yo‘qotib qo‘ysangiz nima qilish kerak: ularni qanday tiklash, nusxalar qayerda saqlanadi va elektron karta kelajakda yo‘qotishdan qanday himoya qiladi.",
"h1": "Tahlillarni yo‘qotdim — nima qilish kerak?",
"body": """
<p class="lede"><strong>Agar tahlil natijalarini yo‘qotib qo‘ysangiz, ko‘p hollarda ularni tiklash
mumkin: nusxalar laboratoriya yoki klinikada saqlanadi.</strong> Bu takrorlanmasligi uchun esa tibbiy
hujjatlarni elektron shaklga o‘tkazgan ma’qul.</p>

<h2>Birinchi: sarosimaga tushmang</h2>
<p>Qog‘oz blankani yo‘qotish — keng tarqalgan holat va u deyarli har doim hal qilinadi. Tahlil natijalari
yagona nusxada mavjud emas: ma’lumotlar ularni bajargan laboratoriyada qoladi. Klinika va yo‘llagan
shifokor ham nusxaga ega bo‘lishi mumkin. Shuning uchun birinchi qadam — qayerda va qachon topshirganingizni
eslash.</p>

<h2>Natijalarni qanday tiklash mumkin?</h2>
<p>Tekshiruvdan o‘tgan laboratoriya yoki klinikaga murojaat qiling va natijalarni qayta berishni
so‘rang. Ko‘p laboratoriyalar ma’lumotlarni saqlaydi va nusxalarni so‘rov bo‘yicha, ba’zan pochtaga
elektron ko‘rinishda beradi. Topishga yordam beradigan hamma narsa asqotadi: sana, ma’lumotlaringiz,
buyurtma raqami yoki chek.</p>

<h2>Qachon tahlillarni qayta topshirish kerak?</h2>
<p>Ba’zan eski natijani tiklab bo‘lmaydi yoki u allaqachon dolzarb emas — masalan, ko‘p vaqt o‘tgan,
ko‘rsatkichlar esa tez o‘zgaradi. Shunda shifokor qayta topshirishni tavsiya qilishi mumkin. Bu har
doim ham yomon emas: yangi ma’lumotlar joriy holatni aniqroq aks ettiradi. Qimmat tekshiruvlarni
tayinlovsiz «har ehtimolga qarshi» qayta topshirmang.</p>

<h2>Boshqa hujjatlarni qanday yo‘qotmaslik kerak?</h2>
<p>Yo‘qotishdan eng yaxshi himoya — <a href="/uz/features/medcard/">elektron tibbiy karta</a> yuritish.
Natijani olishingiz bilan uni darhol ilovaga kiriting yoki suratga oling. Shunda qog‘oz blankani
oqibatsiz yo‘qotish mumkin: raqamli nusxa siz bilan qoladi, sanalar bo‘yicha tartiblangan.</p>

<h2>Nega elektron tarix qulayroq</h2>
<p>Qog‘oz hujjatlar yo‘qoladi, o‘chadi va bitta klinikada qoladi. Elektron
<a href="/uz/blog/elektronnaya-medkarta/">karta</a> doim qo‘l ostida, ko‘chishda yo‘qolmaydi va qabulda
mavjud. Shifokor tarqoq blankalarni emas, to‘liq manzarani ko‘radi, bu maslahatni tezlashtiradi.</p>

<h2>Qisqacha harakatlar rejasi</h2>
<p>Demak, tahlillarni yo‘qotsangiz: qayerda topshirganingizni eslang; laboratoriya yoki klinikadan
nusxa so‘rang; kerak bo‘lsa shifokor tayinlovi bilan qayta topshiring; va albatta elektron karta yurita
boshlang, toki bu oxirgi yo‘qotish bo‘lsin.</p>
""",
"faq": [
("Yo‘qolgan tahlillarni tiklash mumkinmi?", "Ha, ko‘p hollarda. Ma’lumotlar siz topshirgan laboratoriya yoki klinikada saqlanadi va ularni qayta so‘rash mumkin."),
("Natijalar nusxasini qanday olish mumkin?", "Laboratoriya yoki klinikaga sana va ma’lumotlaringiz yoki buyurtma raqami bilan murojaat qiling. Ko‘pchilik nusxa beradi, ba’zan pochtaga elektron ko‘rinishda."),
("Tahlillarni qayta topshirish kerakmi?", "Ba’zan ha — natija eskirsa yoki tiklab bo‘lmasa. Yangi ma’lumotlar aniqroq, lekin qimmat tekshiruvlarni tayinlovsiz qayta topshirmang."),
("Kelajakda hujjatlarni qanday yo‘qotmaslik kerak?", "Elektron karta yuriting: natijalarni darhol kiriting yoki suratga oling. Shunda qog‘oz blankani yo‘qotish oqibatsiz bo‘ladi."),
("Elektron karta qog‘ozdan nimasi bilan yaxshi?", "U doim qo‘l ostida, yo‘qolmaydi va klinika o‘zgarganda ham qolmaydi. Shifokor tarqoq blankalarni emas, to‘liq tarixni ko‘radi."),
],
"related": [("Elektron tibbiy karta: nega kerak", "/uz/blog/elektronnaya-medkarta/"),
            ("Elektron tibbiy karta", "/uz/features/medcard/"),
            ("Yaxshi shifokorni qanday tanlash", "/uz/blog/kak-vybrat-vracha/")],
},
{
"slug": "ai-v-medicine", "date": "2026-04-07",
"title": "Sun’iy intellekt tibbiyotda: u aslida qanday yordam beradi",
"desc": "Sun’iy intellekt bugungi tibbiyotda qanday qo‘llaniladi: diagnostikaga yordam, skrining, ma’lumotlarni qayta ishlash va o‘z-o‘zini tekshirish. AI nima qila oladi va nima shifokorda qolishi kerak.",
"h1": "Sun’iy intellekt tibbiyotda",
"body": """
<p class="lede"><strong>Tibbiyotdagi sun’iy intellekt — shifokorlar va bemorlarga ma’lumotni qayta
ishlashda yordam beradigan vosita, lekin u shifokor o‘rnini bosmaydi.</strong> AI ma’lumotlarni tez
tahlil qilish va qonuniyatlarni topish kerak bo‘lgan joyda yaxshi, qarorlar esa insonda qoladi.</p>

<h2>AI qayerda allaqachon yordam beradi?</h2>
<p>Bugun algoritmlar tibbiy tasvirlarni (rasmlar, tekshiruv natijalari) tahlil qilishga, ma’lumotlarni
tartiblashga, xavflarni erta aniqlashga va shifokorga nimaga e’tibor berishni maslahat berishga yordam
beradi. AI charchamaydi va katta hajmdagi ma’lumotni qayta ishlay oladi — lekin u aynan yordamchi,
mustaqil tashxis qo‘yuvchi emas.</p>

<h2>AI va sog‘liqni o‘z-o‘zini tekshirish</h2>
<p>Bemor uchun AI o‘z-o‘zini tekshirishda foydali: u his-tuyg‘u haqidagi javoblarni tushunarli manzaraga
aylantirib, qaysi mutaxassisga murojaat qilishni maslahat beradi. AIVITA’dagi
<a href="/uz/features/ai-checkup/">AI-checkup</a> shunday ishlaydi: u tashxis qo‘ymaydi, balki nimaga
e’tibor berishni ko‘rsatadi va shifokorga murojaat qilish ostonasini pasaytiradi.</p>

<h2>AI nimani qila olmaydi?</h2>
<p>AI bemorni ko‘rmaydi, hayot kontekstini his qilmaydi, javobgarlikni o‘z zimmasiga olmaydi va, ayniqsa
noodatiy holatlarda, xato qilishi mumkin. U ma’lumotlarga asoslangan ehtimollar bilan ishlaydi, lekin
shifokorning klinik fikrlashi, tajribasi va sezgisi o‘rnini bosmaydi.</p>

<h2>Nega shifokor asosiy bo‘lib qoladi</h2>
<p>Tashxis va davolash — dasturga topshirib bo‘lmaydigan javobgarlik. Shifokor ko‘rik, kasallik tarixi,
yondosh holatlar va algoritm ko‘rmasligi mumkin bo‘lgan individual xususiyatlarni hisobga oladi. AI
shifokorga tezroq va e’tiborliroq ishlashga yordam beradi, lekin yakuniy qaror doim insonda.</p>

<h2>AI sog‘liqni saqlash tizimiga qanday yordam beradi</h2>
<p>Klinikalar darajasida AI va raqamli tizimlar rutinani kamaytiradi: yozuvlar, kartalar yuritish,
ma’lumotlarni qayta ishlashni avtomatlashtiradi. Bu shifokor vaqtini bemor uchun bo‘shatadi. Bemor
xizmati va <a href="/medsoft/">klinika tibbiy tizimi</a> bog‘lanishi ma’lumotlarni yo‘qotmaslikka va
yordamni <a href="/uz/features/doctors/">telemeditsina</a> orqali mavjudroq qilishga yordam beradi.</p>

<h2>AI vositalariga qanday munosabatda bo‘lish kerak</h2>
<p>Oqilona yondashuv — AI’dan yordamchi sifatida foydalanish, orakul sifatida emas. U o‘z-o‘zini
tekshirish, sog‘liqni kuzatish va ma’lumotlarni tartiblash uchun foydali, lekin xulosalarni shifokorda
tekshirish kerak. Bitta algoritm asosida davolash haqida qaror qabul qilmang.</p>
""",
"faq": [
("AI tashxis qo‘ya oladimi?", "Yo‘q. AI ma’lumotlarni tahlil qilishga yordam beradi va nimaga e’tibor berishni maslahat beradi, lekin tashxisni shifokor ko‘rik va kasallik tarixini hisobga olib qo‘yadi."),
("AI bemorga qanday yordam beradi?", "O‘z-o‘zini tekshirishda: his-tuyg‘u haqidagi javoblarni tushunarli manzaraga aylantirib, qaysi shifokorga murojaat qilishni maslahat beradi. AI-checkup shunday ishlaydi."),
("Tibbiyotda AI’ga ishonsa bo‘ladimi?", "AI foydali yordamchi, lekin u, ayniqsa noodatiy holatlarda, xato qilishi mumkin. Uning xulosalarini mutaxassisda tekshirish kerak."),
("AI shifokorlar o‘rnini bosadimi?", "Yo‘q. AI ma’lumotlarni qayta ishlash va rutinani o‘z zimmasiga olib shifokorni kuchaytiradi, lekin klinik qaror va javobgarlik insonda qoladi."),
("AI klinikalarga nima bilan foydali?", "U rutinani kamaytiradi — yozuvlar va kartalar yuritishni avtomatlashtiradi — shifokor vaqtini bemor uchun bo‘shatadi va yordamni mavjudroq qiladi."),
],
"related": [("AI-checkup", "/uz/features/ai-checkup/"),
            ("O‘zbekistonda telemeditsina", "/uz/blog/telemedicina-v-uzbekistane/"),
            ("Onlayn shifokorlar", "/uz/features/doctors/")],
},
]


def hub():
    cards = "".join(
        f'<a class="card" href="/uz/blog/{a["slug"]}/"><h3>{a["h1"]}</h3>'
        f'<p>{a["desc"][:105]}…</p><span class="more">O‘qish →</span></a>' for a in ARTS
    )
    body = f"""
<p class="lede"><strong>AIVITA blogi — sog‘liq, turmush tarzi va tibbiyot haqida tushunarli
materiallar.</strong> Biz qo‘rqitmasdan va mo‘jiza va’da qilmasdan yozamiz: faqat qaror qabul
qilishga va o‘z vaqtida shifokorga murojaat qilishga yordam beradigan ishonchli ma’lumot.</p>

<h2>Tibbiyot haqida asosiy maqolalar</h2>
<p>Simptomlar, tekshiruvlar va shifokor bilan ishlashni tushunarli tarzda ko‘rib chiqamiz. Quyida —
o‘zbek tilidagi asosiy maqolalar.</p>
<div class="grid grid-3">{cards}</div>

<h2>Nega bunga ishonish mumkin</h2>
<p>Har bir maqola tekshirilgan ma’lumotga asoslanadi va shifokorga murojaat qilish o‘rnini bosmaydi.
Biz tashxis qo‘ymaymiz va dozalarni tayinlamaymiz — maqolalar sizga sog‘liq haqida ko‘proq bilib,
o‘z vaqtida to‘g‘ri qaror qabul qilishga yordam beradi. Ko‘proq materiallar bosqichma-bosqich qo‘shiladi.</p>

<h2>Sog‘liq — kunlik odat</h2>
<p>Maqolalarni o‘qing va bilimni amalda qo‘llang: <a href="/uz/features/ai-checkup/">AI-checkupdan</a>
o‘ting, <a href="/uz/features/monitoring/">ko‘rsatkichlarni</a> kuzating va savol tug‘ilsa
<a href="/uz/features/doctors/">shifokorga onlayn</a> yoziling. Sog‘liqqa g‘amxo‘rlik — bir martalik
jasorat emas, kichik kunlik qadamlar.</p>
"""
    return Page(
        path="uz/blog", lang="uz",
        title="Sog‘liq blogi AIVITA — simptomlar, tibbiyot, sog‘lom turmush",
        description="AIVITA blogi: simptomlar va tekshiruvlar, telemeditsina, elektron karta, bosim va emlashlar haqida tushunarli maqolalar o‘zbek tilida. Mish-mishlarsiz, shifokorga havolalar bilan.",
        h1="Sog‘liq blogi",
        body=body, section="blog",
        crumbs=[("Bosh sahifa", "/uz/"), ("Blog", None)],
        hreflang=alts("blog", langs=("ru", "uz")),
        related=[("Imkoniyatlar", "/uz/features/"), ("Hududlar", "/uz/regions/"),
                 ("Biz haqimizda", "/uz/about/")],
    )


def pages():
    return [hub()] + [art(a) for a in ARTS]
