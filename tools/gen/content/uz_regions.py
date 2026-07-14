# -*- coding: utf-8 -*-
"""Этап 9 (uz) — Hududlar /uz/regions/. 14 hudud + hub. hreflang ru/uz."""
from engine import Page, DOMAIN, BRAND, alts

# slug, Nomi, loc (…da), admin, local(uz, 2 gap), access(uz, 1 abzats)
UZ_REGIONS = [
("tashkent", "Toshkent", "Toshkentda", "Toshkent shahri",
 """<p>Toshkent — O‘zbekistonning poytaxti va eng yirik shahri, mamlakatning asosiy ma’muriy,
ishbilarmonlik va tibbiyot markazi. Bu yerda yirik klinikalar, ixtisoslashtirilgan markazlar va
ko‘pchilik yo‘nalishlardagi yetakchi shifokorlar to‘plangan.</p>
<p>Odatda boshqa hududlar aholisi tor mutaxassis maslahati uchun aynan Toshkentga keladi.</p>""",
 """<p>Katta shaharning paradoksi — mutaxassislar ko‘p bo‘lsa-da, navbat va bandlik. Toshkent
aholisi uchun AIVITA vaqtni tejaydi: tahlillarni tahlil qilish, ikkinchi fikr olish yoki takroriy
maslahatni onlayn olish mumkin, yarim kunni yo‘lga sarflamasdan.</p>"""),
("samarkand", "Samarqand", "Samarqandda", "Samarqand viloyati",
 """<p>Samarqand — dunyodagi eng qadimiy shaharlardan biri va O‘zbekistonning ikkinchi muhim
markazi, Registon ansambli tufayli YUNESKO merosiga kiritilgan. Bu universitetlar va tibbiyot
muassasalari bo‘lgan yirik hududiy markaz.</p>
<p>Shahar atrofida katta viloyat bor, uning aholisiga tor mutaxassislarga tushish uzoq bo‘ladi.</p>""",
 """<p>Viloyat aholisi uchun AIVITA — poytaxtga bormasdan kerakli mutaxassisga tushish yo‘li: onlayn
maslahat Samarqanddagi ham, Toshkentdagi ham shifokor bilan mumkin, qabullar tarixi esa kartada
saqlanadi.</p>"""),
("bukhara", "Buxoro", "Buxoroda", "Buxoro viloyati",
 """<p>Buxoro — Buyuk ipak yo‘lidagi qadimiy shahar va YUNESKO merosi obyekti, ko‘p asrlik tarixga,
jumladan tibbiy tarixga ega: bu o‘lka buyuk olim va shifokor Ibn Sino (Avitsenna) nomi bilan
bog‘liq.</p>
<p>Buxoro viloyati katta hududni qamrab oladi, u yerda arzon tibbiy maslahatga ehtiyoj sezilarli.</p>""",
 """<p>AIVITA o‘lka tibbiy an’analarini raqamli shaklda davom ettiradi: Buxoro viloyati aholisi
shifokor maslahatini onlayn oladi, elektron karta yuritadi va kerak bo‘lsa poytaxt mutaxassisiga
masofadan chiqadi.</p>"""),
("andijan", "Andijon", "Andijonda", "Andijon viloyati",
 """<p>Andijon — gavjum Farg‘ona vodiysining asosiy shaharlaridan biri va Zahiriddin Boburning
vatani. Bu mamlakat sharqidagi yirik sanoat va hududiy markaz, aholi zichligi yuqori.</p>
<p>Zich qurilish va katta aholi poliklinikalarga jiddiy yuk tug‘diradi, navbatlar uzun bo‘ladi.</p>""",
 """<p>AIVITA telemeditsinasi bu yo‘lni yengillashtiradi: Andijon aholisi shifokorga oid ayrim
savollarni onlayn hal qiladi, vaqtni tejaydi. Kerakli mutaxassis viloyatda bo‘lmasa, uni boshqa
hududdan masofadan olish mumkin.</p>"""),
("namangan", "Namangan", "Namanganda", "Namangan viloyati",
 """<p>Namangan — Farg‘ona vodiysida joylashgan O‘zbekistonning eng yirik va aholisi zich
shaharlaridan biri. Bu savdo va hunarmandchilik rivojlangan muhim hududiy markaz.</p>
<p>Atrofdagi tumanlar aholisiga viloyat markazidagi tor mutaxassislarga yetib borish har doim ham
qulay emas.</p>""",
 """<p>AIVITA shifokorni onlayn yaqinlashtiradi: Namangan yoki qishloq aholisi uydan maslahatga
yoziladi, kartani telefonda yuritadi va kerak bo‘lsa Toshkent mutaxassisi bilan maslahatlashadi.</p>"""),
("fergana", "Farg‘ona", "Farg‘onada", "Farg‘ona viloyati",
 """<p>Farg‘ona — Farg‘ona viloyatining markazi, unumdor Farg‘ona vodiysi qoq markazidagi ko‘kalamzor
shahar. Hudud qishloq xo‘jaligiga ixtisoslashgan, ko‘plab kichik shahar va qishloqlar bor.</p>
<p>Vodiy aholi punktlari orasidagi masofa va tuman kasalxonalari bandligi shifokorga yo‘lni sezilarli
qiladi.</p>""",
 """<p>AIVITA orqali onlayn maslahat bu yo‘lni tejaydi: tahlil natijalarini tahlil qilish, davolashni
tuzatish yoki ikkinchi fikr olish masofadan mumkin, elektron karta esa butun tarixni bir joyda
saqlaydi.</p>"""),
("nukus", "Nukus", "Nukusda", "Qoraqalpog‘iston Respublikasi",
 """<p>Nukus — Qoraqalpog‘iston Respublikasining poytaxti, O‘zbekistonning eng g‘arbiy va maydoni
bo‘yicha eng katta hududi. Shahar Savitskiy nomidagi noyob to‘plamli muzeyi bilan mashhur.</p>
<p>Katta masofalar va poytaxtdan uzoqlik respublika aholisining tor mutaxassislarga kirishini
qiyinlashtiradi.</p>""",
 """<p>Aynan shu sababli telemeditsina bu yerda ayniqsa qimmatli: istalgan hududdagi kerakli
mutaxassis onlayn mavjud, uzoq yo‘lsiz. Qoraqalpog‘iston aholisi kartani yuritishi va mutaxassislar
bilan masofadan maslahatlashishi mumkin.</p>"""),
("urgench", "Urganch", "Urganchda", "Xorazm viloyati",
 """<p>Urganch — O‘zbekiston g‘arbidagi Xorazm viloyatining markazi va YUNESKO merosiga kirgan qadimiy
Xivaga asosiy darvoza. Bu tarixiy Xorazmning muhim transport va hududiy tuguni.</p>
<p>Xorazmning yirik tibbiyot markazlaridan uzoqligi maslahat uchun safarlarni vaqt jihatidan
qimmat qiladi.</p>""",
 """<p>AIVITA Xorazm viloyati aholisiga uzoq safarsiz onlayn maslahat olish va karta yuritishga
yordam beradi, telemeditsina esa Urganchdan poytaxt mutaxassislariga kirishni ochadi.</p>"""),
("karshi", "Qarshi", "Qarshida", "Qashqadaryo viloyati",
 """<p>Qarshi — O‘zbekiston janubidagi Qashqadaryo viloyatining markazi, boy tarixga ega yirik sanoat
va agrar hudud. Bu mamlakat janubiy qismining muhim iqtisodiy markazlaridan biri.</p>
<p>Viloyat katta va asosan qishloqdan iborat, shuning uchun tuman markazlaridan tashqarida
mutaxassislarga kirish cheklangan.</p>""",
 """<p>Shifokorga onlayn kirish bu yerda ayniqsa foydali: AIVITA orqali Qarshi va tumanlar aholisi
mutaxassis bilan masofadan maslahatlashadi, murakkab holatlarni poytaxt shifokorlari bilan
muhokama qiladi.</p>"""),
("termez", "Termiz", "Termizda", "Surxondaryo viloyati",
 """<p>Termiz — O‘zbekistonning eng janubiy shahri, Afg‘oniston chegarasidagi Surxondaryo viloyatining
markazi. Bu boy tarixiy va arxeologik merosga hamda issiq iqlimga ega qadimiy shahar.</p>
<p>Janubning yirik tibbiyot markazlaridan uzoqligi viloyat aholisiga tor maslahat uchun safarlarni
qiyinlashtiradi.</p>""",
 """<p>Telemeditsina bu yerda ayniqsa talab qilinadi: AIVITA Surxondaryo aholisiga istalgan hududdan
shifokor maslahatini onlayn olish, karta yuritish va masofa tufayli murojaatni keyinga
qoldirmaslik imkonini beradi.</p>"""),
("jizzakh", "Jizzax", "Jizzaxda", "Jizzax viloyati",
 """<p>Jizzax — Toshkent va Samarqand orasida joylashgan Jizzax viloyatining markazi. Bu poytaxtni
janub va markaz bilan bog‘lovchi muhim transport yo‘nalishidagi agrar hudud.</p>
<p>Yirik shaharlarga yaqin bo‘lsa-da, qishloq tumanlari aholisiga tor mutaxassislarga yetib borish
uzoq bo‘ladi.</p>""",
 """<p>AIVITA telemeditsinasi aynan shu yerda qulay: qo‘shni yirik shaharlarga bormasdan shifokorga
onlayn murojaat qilish, sog‘liq tarixini kartada yuritish va kerak bo‘lsa poytaxt mutaxassisiga
masofadan chiqish mumkin.</p>"""),
("navoi", "Navoiy", "Navoiyda", "Navoiy viloyati",
 """<p>Navoiy — Navoiy viloyatining markazi, kon-metallurgiya sanoati atrofida o‘sgan nisbatan yosh
sanoat shahri. Viloyat mamlakat markazida katta hududni egallaydi, aholi zichligi past.</p>
<p>Aholi punktlari orasidagi katta masofa shifokorga yo‘lni, ayniqsa chekka qishloqlar uchun,
sezilarli qiladi.</p>""",
 """<p>Shifokorga onlayn kirish bu yerda ayniqsa qulay: AIVITA Navoiy viloyati aholisini
mutaxassislar bilan masofadan bog‘laydi, elektron karta va monitoring esa tashriflar orasida
sog‘liqni kuzatishga yordam beradi.</p>"""),
("gulistan", "Guliston", "Gulistonda", "Sirdaryo viloyati",
 """<p>Guliston — Sirdaryo viloyatining markazi, mamlakat markaziy qismidagi agrar shahar, Toshkentga
yaqin. Hudud Sirdaryo bo‘yidagi rivojlangan qishloq xo‘jaligi bilan mashhur.</p>
<p>Poytaxtga yaqinlik — ijobiy jihat, ammo kichik viloyat markazida o‘z tor mutaxassislari har doim
ham yetarli emas.</p>""",
 """<p>AIVITA telemeditsinasi buni qoplaydi: Guliston aholisi ayrim maslahatlarni onlayn oladi,
murakkab holatlarni poytaxt mutaxassisi bilan masofadan muhokama qiladi, safarlarga vaqt sarflamasdan.</p>"""),
("syrdarya", "Sirdaryo viloyati", "Sirdaryo viloyatida", "Sirdaryo viloyati",
 """<p>Sirdaryo viloyati mamlakat markazida, Sirdaryo bo‘yida joylashgan va mamlakatning aholi zichligi
past hududlaridan biri. Bu asosan agrar o‘lka bo‘lib, markazi Guliston shahri.</p>
<p>Aholi zichligining pastligi tor mutaxassislar kam nuqtalarda to‘planganini anglatadi, ularga
qishloq aholisi borishi kerak.</p>""",
 """<p>AIVITA telemeditsinasi bu muammoni hal qiladi: kerakli yo‘nalishdagi shifokor mamlakatning
istalgan nuqtasidan onlayn mavjud. Viloyat aholisi AI-checkupdan o‘tishi, karta yuritishi va
yagona tuman kasalxonasi jadvaliga bog‘lanmasdan mutaxassisga yozilishi mumkin.</p>"""),
]


def region_page(slug, name, loc, admin, local, access):
    body = f"""
<p class="lede"><strong>AIVITA {loc} va butun {admin} aholisiga tibbiy yordamni onlayn olishda
yordam beradi: shifokorlarga yozilish, elektron tibbiy karta yuritish va AI-checkupdan
o‘tish.</strong> Platforma butun O‘zbekiston bo‘ylab ishlaydi, shuning uchun telemeditsina
istalgan hududdagi shifokorni mavjud qiladi.</p>

<h2>{loc} onlayn shifokorlar va klinikalar</h2>
<p>AIVITA orqali {loc} bemorlar kerakli mutaxassislikdagi shifokorni tanlaydi, profilni ko‘radi va
onlayn maslahatga yoziladi. Navbatda turish yoki shahar bo‘ylab yurish shart emas: tahlillarni
tahlil qilish, ikkinchi fikr olish yoki davolashni muhokama qilish masofadan mumkin, tayinlovlar
esa kartada saqlanadi.</p>

<h2>Hudud va tibbiyotga kirish haqida</h2>
{local}

<h2>AIVITA {loc} aholisiga qanday yordam beradi</h2>
{access}

<h2>Telemeditsina: istalgan hududdan shifokor</h2>
<p>AIVITA’ning hudud aholisi uchun asosiy ustunligi — yaqinda bo‘lmasligi mumkin bo‘lgan
mutaxassislarga kirish. Agar kerakli shifokor {loc} bo‘lmasa, siz Toshkent yoki boshqa yirik
markazdagi mutaxassis bilan onlayn maslahatlashishingiz mumkin. Bu ayniqsa tor yo‘nalishlar va
ikkinchi fikr uchun muhim.</p>

<h2>{loc} nima mavjud</h2>
<ul>
  <li><a href="/uz/features/ai-checkup/">AI-checkup</a> — 60 soniyada tez o‘z-o‘zini tekshirish.</li>
  <li><a href="/uz/features/doctors/">Onlayn shifokorlar</a> — turli yo‘nalish mutaxassislari maslahati.</li>
  <li><a href="/uz/features/medcard/">Elektron tibbiy karta</a> — butun sog‘liq tarixi telefonda.</li>
  <li><a href="/uz/features/monitoring/">Monitoring</a> — aqlli soat va brasletlardan ko‘rsatkichlar.</li>
</ul>
<p>Bularning barchasi rus va o‘zbek tillarida ishlaydi, shuning uchun AIVITA’dan foydalanish
{admin} har bir aholisi uchun qulay.</p>
"""
    faq = [
        (f"{loc} shifokorga onlayn qanday yozilaman?",
         f"AIVITA’ni oching, mutaxassislik va shifokorni, qulay vaqtni tanlang va yozilishni tasdiqlang. Maslahat onlayn o‘tadi, shuning uchun {loc} va atrofdagi tumanlar aholisiga ham mavjud."),
        (f"{loc} poytaxt shifokoriga tushsam bo‘ladimi?",
         "Ha. AIVITA telemeditsinasi Toshkent yoki boshqa hududdagi mutaxassis bilan shahringizdan chiqmasdan maslahatlashish imkonini beradi."),
        ("Klinikaga borish shartmi?",
         "Ko‘p savollar — tahlillarni tahlil qilish, takroriy qabul, ikkinchi fikr — onlayn hal qilinadi. Ko‘rik yoki muolaja kerak bo‘lsa, shifokor yuzma-yuz tashrifni aytadi."),
        ("Maslahatlar qaysi tilda?",
         "AIVITA rus, o‘zbek va ingliz tillarida ishlaydi. Siz o‘zingizga qulay shifokor va tilni tanlashingiz mumkin."),
        ("AIVITA’dan foydalanish qancha turadi?",
         "AI-checkup, karta va monitoring bepul. Faqat onlayn maslahatlar to‘lanadi."),
    ]
    schema = [{"@type": "Service", "name": f"{loc} onlayn shifokorlar — AIVITA",
               "serviceType": "Telemeditsina",
               "provider": {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/"},
               "areaServed": {"@type": "AdministrativeArea", "name": admin},
               "availableChannel": {"@type": "ServiceChannel", "serviceUrl": DOMAIN + f"/uz/regions/{slug}/"}}]
    return Page(
        path=f"uz/regions/{slug}", lang="uz",
        title=f"{loc} onlayn shifokorlar va klinikalar — maslahat | AIVITA",
        description=f"{loc} onlayn shifokorlar: mutaxassislarga yozilish, elektron tibbiy karta va AI-checkup. AIVITA butun O‘zbekiston bo‘ylab ishlaydi — telemeditsina istalgan hududdan shifokorga kirishni ochadi.",
        h1=f"{loc} onlayn shifokorlar va klinikalar",
        body=body, faq=faq, section="regions",
        crumbs=[("Bosh sahifa", "/uz/"), ("Hududlar", "/uz/regions/"), (name, None)],
        hreflang=alts(f"regions/{slug}", langs=("ru", "uz")),
        disclaimer=True,
        related=[("Onlayn shifokorlar", "/uz/features/doctors/"),
                 ("Barcha hududlar", "/uz/regions/"),
                 ("Imkoniyatlar", "/uz/features/")],
    )


def hub():
    cards = "".join(
        f'<a class="card" href="/uz/regions/{slug}/"><h3>{name}</h3>'
        f'<p>{loc} onlayn shifokorlar va telemeditsina.</p><span class="more">Ochish →</span></a>'
        for slug, name, loc, admin, local, access in UZ_REGIONS
    )
    body = f"""
<p class="lede"><strong>AIVITA butun O‘zbekiston bo‘ylab ishlaydi — barcha 12 viloyat,
Qoraqalpog‘iston Respublikasi va Toshkent shahrida.</strong> Telemeditsina tufayli istalgan hudud
aholisi shifokorlar, elektron tibbiy karta va AI-checkupga ega bo‘ladi, poytaxt mutaxassisini esa
shahringizdan chiqmasdan onlayn olish mumkin.</p>

<h2>O‘zbekiston hududlari</h2>
<p>O‘z hududingizni tanlang va u yerda onlayn shifokorlar hamda telemeditsinadan qanday
foydalanishni bilib oling. Ma’muriy jihatdan O‘zbekiston 12 viloyat, Qoraqalpog‘iston Respublikasi
va Toshkent shahriga bo‘linadi — barchasi xizmat bilan qamrab olingan.</p>
<div class="grid grid-3">{cards}</div>

<h2>Nega telemeditsina hududlar uchun muhim</h2>
<p>Kuchli mutaxassislar va zamonaviy diagnostika yirik shaharlarda to‘plangan, viloyat aholisi esa
ko‘pincha maslahat uchun uzoqqa borishga majbur. AIVITA bu to‘siqni olib tashlaydi: onlayn qabul
shifokorni siz qayerda bo‘lishingizdan qat’i nazar mavjud qiladi. Bu vaqt va yo‘l xarajatlarini
tejaydi va ayniqsa tor mutaxassisliklar hamda ikkinchi fikr uchun muhim. Ko‘p viloyat aholisi uchun
bu profil shifokorining maslahati u shahringizda bor-yo‘qligiga bog‘liq bo‘lmasligini va faqat
poytaxtga safar chog‘ida emas, muntazam kuzatilish imkoniyati paydo bo‘lishini anglatadi.</p>

<h2>Qanday mutaxassislar onlayn mavjud</h2>
<p>AIVITA orqali istalgan hududda turli yo‘nalish shifokorlariga yozilish mumkin — terapevt,
pediatr, kardiolog, ginekolog va boshqalar. Batafsil ro‘yxat <a href="/uz/features/doctors/">onlayn
shifokorlar</a> bo‘limida. Agar kerakli shifokor shahringizda bo‘lmasa, telemeditsina boshqa
hududdagi mutaxassisga kirishni ochadi — bu, ayniqsa, viloyatlar aholisi uchun muhim, chunki
profilaktika va kuzatuv endi safarga bog‘liq bo‘lmaydi.</p>

<h2>Uch tilda yagona kirish</h2>
<p>Barcha hududlarda AIVITA bir xil ishlaydi — rus, o‘zbek va ingliz tillarida. Karta, AI-checkup va
monitoring bepul, onlayn maslahatlarni esa o‘z yoki istalgan boshqa hududdagi shifokordan olish
mumkin. Yagona platforma g‘arbdagi Qoraqalpog‘istondan sharqdagi Farg‘ona vodiysigacha bemorlarni
birlashtiradi.</p>
"""
    return Page(
        path="uz/regions", lang="uz",
        title="O‘zbekiston hududlari — barcha viloyatlarda onlayn shifokorlar | AIVITA",
        description="AIVITA O‘zbekistonning barcha hududlarida ishlaydi: 12 viloyat, Qoraqalpog‘iston va Toshkent. Onlayn shifokorlar, telemeditsina, elektron tibbiy karta va AI-checkup hududingizda 3 tilda.",
        h1="O‘zbekiston hududlarida onlayn shifokorlar",
        body=body, section="regions",
        crumbs=[("Bosh sahifa", "/uz/"), ("Hududlar", None)],
        hreflang=alts("regions", langs=("ru", "uz")),
        related=[("Onlayn shifokorlar", "/uz/features/doctors/"),
                 ("Imkoniyatlar", "/uz/features/"),
                 ("Biz haqimizda", "/uz/about/")],
    )


def pages():
    return [hub()] + [region_page(*r) for r in UZ_REGIONS]
