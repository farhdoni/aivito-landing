# -*- coding: utf-8 -*-
"""Этап 9 (en) — home, features (hub+6), about. hreflang ru/uz/en. Medical tourism — в medical_tourism.py."""
from engine import Page, DOMAIN, BRAND, alts

CRF = ("Features", "/en/features/")


def home():
    body = """
<p class="lede"><strong>AIVITA is a digital health ecosystem in Uzbekistan.</strong> In one app you
run an AI check-up in 60 seconds, keep an electronic medical card, check drug compatibility, track
your health metrics from smartwatches, and book a doctor online — in Russian, Uzbek and English.</p>

<div class="stats">
  <div class="stat"><div class="num">60 sec</div><div class="lbl">for an AI check-up</div></div>
  <div class="stat"><div class="num">5 systems</div><div class="lbl">of the body assessed</div></div>
  <div class="stat"><div class="num">250+</div><div class="lbl">doctors in the catalogue</div></div>
  <div class="stat"><div class="num">14</div><div class="lbl">regions of Uzbekistan</div></div>
  <div class="stat"><div class="num">3 languages</div><div class="lbl">ru · uz · en</div></div>
</div>

<div class="cta-row">
  <a class="btn btn-primary" href="/en/features/ai-checkup/">Run an AI check-up</a>
  <a class="btn btn-ghost" href="/en/features/">All features</a>
</div>

<h2>What AIVITA can do</h2>
<p>AIVITA brings together what used to be scattered: health self-assessment, medical history, drug
control, data from wearable devices and communication with a doctor. Each tool works on its own and
becomes more powerful together with the others.</p>

<div class="grid grid-3">
  <a class="card" href="/en/features/ai-checkup/"><div class="ic">🩺</div><h3>Body AI check-up</h3><p>One tap, 60 seconds — go through a check-up and learn about your health.</p><span class="more">Learn more →</span></a>
  <a class="card" href="/en/features/drug-checker/"><div class="ic">💊</div><h3>Drug checker</h3><p>Compatibility of medicines and interaction risks — before you take a pill.</p><span class="more">Learn more →</span></a>
  <a class="card" href="/en/features/medcard/"><div class="ic">📁</div><h3>Electronic medical card</h3><p>Tests, visits and prescriptions in one place — opened to a doctor only with your permission.</p><span class="more">Learn more →</span></a>
  <a class="card" href="/en/features/monitoring/"><div class="ic">📈</div><h3>Health monitoring</h3><p>Pulse, blood pressure, sleep and steps from smartwatches — in a single health diary.</p><span class="more">Learn more →</span></a>
  <a class="card" href="/en/features/doctors/"><div class="ic">👩‍⚕️</div><h3>Doctors online</h3><p>Book a specialist from any region of Uzbekistan — telemedicine without queues.</p><span class="more">Learn more →</span></a>
  <a class="card" href="/en/features/sos/"><div class="ic">🚨</div><h3>SOS help</h3><p>An action plan and quick access to your key data in an emergency.</p><span class="more">Learn more →</span></a>
</div>

<h2>For travellers and clinics</h2>
<p>AIVITA also helps international patients: see the <a href="/en/medical-tourism/">medical tourism</a>
section on treatment and check-ups in Uzbekistan. Clinics automate their work with the
<a href="/medsoft/">MedSoft</a> system and receive patients from the AIVITA catalogue. Learn more in
the <a href="/en/about/">about</a> section.</p>
"""
    faq = [
        ("What is AIVITA?", "AIVITA is an app and ecosystem for health in Uzbekistan. It combines an AI check-up, an electronic medical card, drug-compatibility checks, monitoring from smartwatches and online doctor bookings. The interface is available in Russian, Uzbek and English."),
        ("Does AIVITA replace a doctor?", "No. AIVITA helps you look after your health, keep your history and reach out in time, but it does not diagnose or prescribe treatment. All medical decisions are made by a doctor."),
        ("How much does AIVITA cost?", "Core features — self-assessment, keeping a medical card and monitoring — are free. Online consultations are paid separately depending on the doctor and clinic."),
        ("Which regions does AIVITA work in?", "AIVITA works across Uzbekistan. Thanks to telemedicine you can reach a doctor from any region, wherever you are."),
        ("Which languages is the app available in?", "AIVITA works in three languages: Russian, Uzbek and English. You can switch language at any time, and your medical data is preserved."),
    ]
    schema = [{"@type": "MedicalWebPage", "url": DOMAIN + "/en/", "inLanguage": "en",
               "name": "AIVITA — health in Uzbekistan", "isPartOf": {"@id": DOMAIN + "/#website"}}]
    return Page(
        path="en", lang="en",
        title="AIVITA — Health in Uzbekistan: AI Check-up, Medical Card, Doctors Online",
        description="AIVITA is a digital health ecosystem in Uzbekistan: a 60-second AI check-up, electronic medical card, drug-compatibility checker, monitoring from smartwatches and online doctors in 3 languages.",
        h1="Healthcare that is always with you",
        body=body, faq=faq, schema=schema, section="",
        crumbs=[], disclaimer=True,
        hreflang={"ru": "/", "uz": "/uz/", "en": "/en/"},
        related=[("Features", "/en/features/"), ("Medical tourism", "/en/medical-tourism/"),
                 ("About AIVITA", "/en/about/")],
    )


def _feat(slug, title, desc, h1, body, faq, related, sname, sdesc, disclaimer=True):
    return Page(
        path=f"en/features/{slug}", lang="en", title=title, description=desc, h1=h1,
        body=body, faq=faq, related=related, section="features",
        crumbs=[("Home", "/en/"), CRF, (h1, None)],
        hreflang=alts(f"features/{slug}"),
        disclaimer=disclaimer,
        schema=[{"@type": "Service", "name": sname, "description": sdesc,
                 "serviceType": "Online health service",
                 "provider": {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/"},
                 "areaServed": {"@type": "Country", "name": "Uzbekistan"},
                 "availableChannel": {"@type": "ServiceChannel", "serviceUrl": DOMAIN + f"/en/features/{slug}/"}}],
    )


def f_aicheckup():
    body = """
<p class="lede"><strong>AIVITA's AI check-up is an online body assessment you can complete with one
tap in 60 seconds.</strong> You answer a series of simple questions about how you feel, and the system
evaluates five main body systems and shows a clear picture: what is fine and what deserves attention.</p>

<h2>What is an online body check-up?</h2>
<p>A check-up is a preventive assessment of your health when nothing, or almost nothing, is bothering
you. A classic clinic check-up is a set of tests and examinations. AIVITA's AI check-up does not
replace lab tests, but it helps you take the first step: understand whether your main indicators are
in order and decide whether a deeper examination is needed.</p>

<h2>How do you take the check-up?</h2>
<p>Open AIVITA and start the check-up on the home screen. The app asks questions in blocks: heart and
blood pressure, breathing, digestion, sleep and energy, emotional state. Every question has ready
answer options — nothing to type. In a minute you get a result with priorities and, if needed, a
suggestion of which specialist to see.</p>

<h2>What does the AI check-up show?</h2>
<p>The result is not a diagnosis but a map of attention. You see which body systems to support through
lifestyle, which indicators to measure more precisely, and which complaints require an in-person
consultation. You can save the result to your <a href="/en/features/medcard/">medical card</a> and
show it to a doctor.</p>

<h2>Does the check-up replace a doctor?</h2>
<p>No. The AI check-up is a tool for prevention and self-observation. It helps you notice signals in
time, but it does not diagnose or prescribe. If the check-up shows worrying answers or you have acute
symptoms, book a <a href="/en/features/doctors/">doctor online</a> or go to a clinic.</p>

<h2>How often should you take it?</h2>
<p>A light self-check can be done every 1–3 months to track dynamics, and whenever your well-being
changes. Regularity matters more than a one-off check: comparing results over time lets you and your
doctor see the trend. A full medical check-up for adults is usually recommended once a year.</p>
"""
    faq = [
        ("How long does the AI check-up take?", "About 60 seconds. The questions are short with ready answers, so you can complete it with one tap."),
        ("Do I need test results to take it?", "No. The basic AI check-up is based on your answers. If you have recent test results, you can add them to your card for a more precise picture."),
        ("Does the AI check-up make a diagnosis?", "No. It shows what to pay attention to and suggests which doctor to see. Only a doctor makes a diagnosis."),
        ("Is it free?", "Yes, the basic AI check-up in AIVITA is free. Online consultations may be paid if you decide to book one."),
        ("Can I take it in English?", "Yes. AIVITA works in Russian, Uzbek and English, and you can switch language at any time."),
    ]
    related = [("Electronic medical card", "/en/features/medcard/"),
               ("Doctors online", "/en/features/doctors/"),
               ("Health monitoring", "/en/features/monitoring/")]
    return _feat("ai-checkup",
                 "Body AI Check-up Online — One-Tap Assessment | AIVITA",
                 "Take an online body AI check-up in AIVITA in 60 seconds: answer simple questions and learn about your health. 5 body systems assessed. Does not replace a doctor.",
                 "Body AI check-up online", body, faq, related,
                 "Body AI check-up", "An online assessment of health status in 60 seconds.")


def f_drug():
    body = """
<p class="lede"><strong>The drug checker in AIVITA shows medicine compatibility and interaction risks
before you take a pill.</strong> You add the medicines you take or plan to take, and the system tells
you whether they can be combined and what to watch out for.</p>

<h2>Why check drug compatibility?</h2>
<p>Taking several medicines at once is common: one for blood pressure, another for a cold, plus
vitamins. But some medicines strengthen or weaken each other, and certain combinations can be unsafe.
This is especially important for older people, pregnant women and those with chronic conditions.</p>

<h2>How does the interaction check work?</h2>
<p>Enter the names of the medicines — one by one or as a list. AIVITA compares the active substances
and shows whether there are significant interactions and how serious they are. If a combination
requires caution, you see a clear explanation and a recommendation to discuss it with a doctor or
pharmacist.</p>

<h2>What does the result show?</h2>
<p>The result is guidance, not a permission or a ban. You see the level of attention for a given pair
of medicines, a short explanation and a hint on what to do next. AIVITA does not cancel or prescribe
medicines — the final decision is always made by a doctor who knows your history.</p>

<h2>Can you trust an online check?</h2>
<p>The service relies on known data about interactions of active substances, but it does not see your
individual situation as a whole: doses, comorbidities, allergies, kidney and liver specifics. So the
compatibility check is a tool for preventing mistakes and a reason to talk to a specialist, not a
replacement for a consultation. Never start or stop a prescribed medicine based on an online check.</p>

<h2>Who benefits most?</h2>
<p>People who take several medicines at once; those who buy over-the-counter drugs; parents who give
medicines to children; older people and their carers. In all these cases a quick check reduces the risk
of an accidental mistake and helps you ask the doctor the right questions.</p>
"""
    faq = [
        ("What does the AIVITA drug checker do?", "It shows whether medicines are compatible and warns about possible interactions. It is help with preventing mistakes, not a prescription."),
        ("Can I decide whether to take a medicine based on the check?", "No. The decision to take, stop or change a medicine is made only by a doctor. The check is a reason to ask precise questions."),
        ("Does the service account for dosage?", "The basic check looks at active substances. Your individual dose, conditions and allergies are assessed by a doctor."),
        ("Is it free?", "Yes, the basic compatibility check in AIVITA is free."),
        ("What if the service shows a risk?", "Don't panic or stop treatment abruptly. Save the result and discuss it with a doctor or pharmacist."),
    ]
    related = [("Electronic medical card", "/en/features/medcard/"),
               ("Doctors online", "/en/features/doctors/"),
               ("AI check-up", "/en/features/ai-checkup/")]
    return _feat("drug-checker",
                 "Drug Compatibility Checker Online — Medicine Interactions | AIVITA",
                 "Check drug compatibility online in AIVITA: learn about medicine interactions before taking them. Clear result and recommendations. Does not replace a doctor's consultation.",
                 "Drug compatibility checker", body, faq, related,
                 "Drug compatibility checker", "Online check of medicine interactions and compatibility.")


def f_medcard():
    body = """
<p class="lede"><strong>The AIVITA electronic medical card is your personal health history in one
place: tests, visits, diagnoses and prescriptions.</strong> The data is kept by you and opened to a
doctor only with your permission — for a specific consultation.</p>

<h2>What is an electronic medical card?</h2>
<p>An electronic medical card is a digital version of the paper patient record, only you can't lose it
or leave it at home. In AIVITA the card collects everything related to your health: test results,
doctor's conclusions, visit history, prescribed medicines, data from
<a href="/en/features/monitoring/">monitoring</a> and <a href="/en/features/ai-checkup/">AI check-ups</a>.</p>

<h2>Why keep a card in an app?</h2>
<p>When your history is scattered across papers and different clinics, the doctor spends time restoring
it and you risk forgetting something important. A single card solves this: at the appointment the
specialist immediately sees the full picture — which tests were done, what was prescribed before, what
you are allergic to. This speeds up the consultation and reduces repeat tests.</p>

<h2>Who sees my data?</h2>
<p>By default, only you. A doctor gets access to the needed part of the card only when you open it for
a specific consultation, and access can be closed afterwards. You manage who sees what and can revoke
permission at any time.</p>

<h2>How do you move paper tests into the card?</h2>
<p>You can add documents manually or by photographing them. Test results and conclusions are stored in
the card by date and type. If you lose paper results, the electronic card helps restore the timeline:
whatever you once entered will no longer be lost.</p>

<h2>A card for the whole family</h2>
<p>In AIVITA you can keep cards for loved ones — for example children and elderly parents who don't use
the app themselves. This is convenient for parents and carers: a child's vaccination schedule, illness
history and prescriptions are always at hand.</p>
"""
    faq = [
        ("What is stored in the electronic medical card?", "Tests, doctor's conclusions, visit history, prescribed medicines, AI check-up results and monitoring data — all organised by date."),
        ("Is my medical data safe?", "Yes. Only you have access to the card. A doctor sees data only when you open it for a specific consultation, and you can close access at any time."),
        ("Can I keep a child's card?", "Yes. In AIVITA you can keep cards for loved ones — children and elderly relatives, including the vaccination schedule."),
        ("How do I add old paper tests?", "You can enter them manually or photograph them. Documents are saved in the card by date and won't be lost."),
        ("Is it free?", "Yes, keeping an electronic medical card in AIVITA is free."),
    ]
    related = [("AI check-up", "/en/features/ai-checkup/"),
               ("Health monitoring", "/en/features/monitoring/"),
               ("Doctors online", "/en/features/doctors/")]
    return _feat("medcard",
                 "Electronic Medical Card Online — Health History in Your Phone | AIVITA",
                 "AIVITA electronic medical card: tests, visits, diagnoses and prescriptions in one place. Access is yours, a doctor sees data only with your permission. A card for the whole family.",
                 "Electronic medical card", body, faq, related,
                 "Electronic medical card", "Storing and keeping personal medical history: tests, visits, prescriptions.", disclaimer=False)


def f_doctors():
    body = """
<p class="lede"><strong>Doctors online in AIVITA let you book a consultation with the right specialist
from any region of Uzbekistan without leaving home.</strong> Telemedicine erases distances: a doctor in
Tashkent is available to a patient in Nukus.</p>

<div class="stats">
  <div class="stat"><div class="num">250+</div><div class="lbl">doctors in the catalogue</div></div>
  <div class="stat"><div class="num">14</div><div class="lbl">regions of Uzbekistan</div></div>
  <div class="stat"><div class="num">3 languages</div><div class="lbl">ru · uz · en</div></div>
</div>

<h2>What is an online doctor consultation?</h2>
<p>An online consultation (telemedicine) is an appointment held over video or audio. The doctor asks
about your complaints, reviews your <a href="/en/features/medcard/">medical card</a> and test results,
answers questions and decides whether an in-person visit is needed. It's convenient for consultations,
reviewing test results, adjusting treatment and follow-up appointments.</p>

<h2>How do you book a doctor in AIVITA?</h2>
<p>Choose a specialty, view doctors' profiles, pick a convenient time and confirm the booking. Before
the consultation you can open the needed part of your card to the doctor so they see your history in
advance. After the appointment, prescriptions are saved in the card.</p>

<h2>A doctor from any region — how does it work?</h2>
<p>Telemedicine is especially valuable for Uzbekistan, where strong specialists are concentrated in
large cities. Through AIVITA a patient from any <a href="/en/">region</a> gets access to a doctor who
may not be nearby. There's no need to travel hundreds of kilometres for a consultation.</p>

<h2>When is online enough, and when is an in-person visit needed?</h2>
<p>Online works well for reviewing tests, follow-up appointments, adjusting chronic therapy, prevention
questions and second opinions. An in-person visit is needed when an examination, measurements or
procedures are required — for acute pain, injury or high fever. The doctor will tell you if an
in-person visit is needed.</p>

<h2>Safety and the limits of telemedicine</h2>
<p>An online consultation does not replace emergency care. For threatening symptoms — severe chest pain,
difficulty breathing, loss of consciousness — don't wait for an appointment, use
<a href="/en/features/sos/">SOS help</a> and call an ambulance. Telemedicine complements in-person
medicine, making it more accessible.</p>
"""
    faq = [
        ("How do I book a doctor online?", "Choose a specialty, view profiles, pick a time and confirm the booking. Before the appointment you can open the needed part of your card."),
        ("Can I reach a doctor from another city?", "Yes. Thanks to telemedicine a doctor from any region of Uzbekistan is available online — no need to travel."),
        ("Does an online consultation replace an in-person visit?", "Not always. It's good for reviewing tests, follow-ups and prevention questions, but if an examination is needed the doctor will refer you for an in-person visit."),
        ("What should I do in an emergency?", "Don't wait for an appointment. For threatening symptoms use SOS help and call an ambulance."),
        ("What language is the consultation in?", "You can choose a doctor who speaks Russian, Uzbek or English — AIVITA supports all three languages."),
    ]
    related = [("Electronic medical card", "/en/features/medcard/"),
               ("Medical tourism", "/en/medical-tourism/"),
               ("SOS help", "/en/features/sos/")]
    return _feat("doctors",
                 "Doctors Online in Uzbekistan — Consultation & Booking | AIVITA",
                 "Book a doctor online in AIVITA: therapist, paediatrician, gynaecologist, cardiologist and other specialists from any region of Uzbekistan. Telemedicine without queues in 3 languages.",
                 "Doctors online", body, faq, related,
                 "Online doctor consultations", "Booking and video consultations with doctors of various specialties across Uzbekistan.")


def f_sos():
    body = """
<p class="lede"><strong>SOS help in AIVITA is an emergency section that suggests an action plan in a
critical situation and gives quick access to your important medical data.</strong> When every second
counts, the essentials are at hand: what to do and what information to give.</p>

<h2>What does SOS help do?</h2>
<p>The SOS section gathers what you need in an emergency: brief first-aid instructions for common
conditions, your key health data (blood type, allergies, chronic conditions, regular medicines) and
emergency contacts. It's not a replacement for an ambulance, but a helper that reduces panic and helps
you act correctly in the first minutes.</p>

<h2>Why quick access to data matters</h2>
<p>In an emergency a person often can't describe their conditions and allergies — due to stress, pain or
loss of consciousness. If important information is entered into the <a href="/en/features/medcard/">
medical card</a> in advance and placed in the SOS profile, those around you or medics understand faster
what you have and what is contraindicated.</p>

<h2>How to prepare in advance</h2>
<p>SOS works best the earlier you set it up. Enter your blood type, known allergies, chronic diagnoses,
regular medicines and a contact of a loved one. Do it calmly — then everything is ready in a critical
moment. Update the data when something changes.</p>

<h2>SOS does not replace an ambulance</h2>
<div class="callout disclaimer"><strong>Important.</strong> For life-threatening conditions — severe
chest pain, difficulty breathing, loss of consciousness, heavy bleeding, signs of a stroke — call an
ambulance immediately. In Uzbekistan the emergency numbers are <strong>103</strong> (ambulance) and
<strong>112</strong> (unified service). AIVITA's SOS help is support and information, not medical care.</div>

<h2>Who benefits most from the SOS section?</h2>
<p>People with chronic conditions and allergies, older people, parents of small children, and those who
travel or do sport often. In all these cases a prepared SOS profile and a clear action plan can save
precious minutes.</p>
"""
    faq = [
        ("What is SOS help in AIVITA?", "It's an emergency section with first-aid guidance and quick access to your key health data — allergies, chronic conditions, blood type."),
        ("Does SOS replace calling an ambulance?", "No. For life-threatening conditions you must call an ambulance (103) or the unified service (112). SOS is informational support, not medical care."),
        ("What data should I put in the SOS profile?", "Blood type, allergies, chronic diagnoses, regular medicines and a contact of a loved one. It's best to do this in advance."),
        ("Who sees my SOS data?", "You decide which data to place in the emergency profile so it's available to those helping you in a critical moment."),
        ("Should I update the SOS profile?", "Yes, update it when things change: a new medicine, diagnosis or allergy."),
    ]
    related = [("Electronic medical card", "/en/features/medcard/"),
               ("Doctors online", "/en/features/doctors/"),
               ("AI check-up", "/en/features/ai-checkup/")]
    return _feat("sos",
                 "SOS Help — Emergency Action Plan and Data Access | AIVITA",
                 "SOS help in AIVITA: an action plan in an emergency and quick access to your important health data. Does not replace an ambulance — for a threat to life call 103.",
                 "SOS help", body, faq, related,
                 "SOS help", "An emergency section with first-aid guidance and access to key patient data.")


def f_monitoring():
    body = """
<p class="lede"><strong>Health monitoring in AIVITA is a single diary of your metrics: pulse, blood
pressure, sleep, sugar, water and steps.</strong> The data is pulled automatically from smartwatches
and fitness bands, and the app shows your health dynamics over time — not isolated numbers, but a trend.</p>

<div class="stats">
  <div class="stat"><div class="num">6</div><div class="lbl">key metrics</div></div>
  <div class="stat"><div class="num">24/7</div><div class="lbl">background data collection</div></div>
  <div class="stat"><div class="num">1</div><div class="lbl">health diary</div></div>
</div>

<h2>Which metrics does AIVITA track?</h2>
<p>Monitoring covers the main parameters of everyday health: heart rate, blood pressure, quality and
duration of sleep, sugar level (with compatible devices), amount of water, number of steps and physical
activity. Together these metrics form a clear picture of your lifestyle.</p>

<h2>How do you connect a smartwatch or fitness band?</h2>
<p>AIVITA works with popular wearables. Owners of <strong>Mi Band</strong> and Xiaomi bands,
<strong>Apple Watch</strong>, <strong>Samsung Galaxy Watch</strong> and other trackers can link them to
the app so that pulse, sleep and activity data are pulled automatically. No need to enter numbers by
hand — the health diary fills itself.</p>

<h2>What are health dynamics and the health diary?</h2>
<p>A single measurement of blood pressure or pulse says little — dynamics matter. AIVITA shows how your
metrics change day by day and week by week: is your sleep improving, is your activity growing, is your
blood pressure stable. The health diary stores the whole history and makes the trend visible.</p>

<h2>What is health curation?</h2>
<p>Health curation is the meaningful accompaniment of your metrics over time, not just their collection.
AIVITA helps turn data into action: it suggests what to pay attention to, reminds you to measure blood
pressure or drink water. Monitoring data is saved in your <a href="/en/features/medcard/">medical card</a>.</p>

<h2>Why does a doctor need band data?</h2>
<p>Metrics over several weeks are more valuable than a single measurement in the office. The doctor sees
how blood pressure behaves at different times, how you sleep, how active you are — and can assess the
situation more precisely. Monitoring data is a good basis for a talk with a
<a href="/en/features/doctors/">doctor online</a>.</p>
"""
    faq = [
        ("Which devices does monitoring support?", "AIVITA works with popular fitness bands and smartwatches — Mi Band and other Xiaomi devices, Apple Watch, Samsung Galaxy Watch and other trackers."),
        ("What does health monitoring track?", "Pulse, blood pressure, sleep, sugar (with compatible devices), water, steps and activity — all in a single health diary."),
        ("What are health dynamics?", "It's how your metrics change over time. AIVITA shows the trend — how pulse, sleep and activity change day by day, not isolated numbers."),
        ("Do I need to enter data manually?", "After connecting a wearable, pulse, sleep and activity data are pulled automatically. Some metrics, such as water, can be marked manually."),
        ("Will a doctor see my monitoring data?", "Yes, if you open it for a consultation. Data is saved in the card and the doctor sees the dynamics over a period, not a one-off measurement."),
    ]
    related = [("Electronic medical card", "/en/features/medcard/"),
               ("Doctors online", "/en/features/doctors/"),
               ("AI check-up", "/en/features/ai-checkup/")]
    return _feat("monitoring",
                 "Health Monitoring — Pulse, Blood Pressure, Sleep from Smartwatches | AIVITA",
                 "Health monitoring in AIVITA: pulse, blood pressure, sleep, sugar, water and steps from smartwatches and fitness bands (Mi Band, Apple Watch, Samsung). Dynamics and a health diary in one place.",
                 "Health monitoring", body, faq, related,
                 "Health metrics monitoring", "Collecting and analysing health metrics from smartwatches and fitness bands.")


def features_hub():
    cards = [
        ("🩺", "Body AI check-up", "One tap, 60 seconds — go through a check-up.", "/en/features/ai-checkup/"),
        ("💊", "Drug checker", "Compatibility and interaction risks before you take a pill.", "/en/features/drug-checker/"),
        ("📁", "Electronic medical card", "Tests, visits and prescriptions in one place.", "/en/features/medcard/"),
        ("📈", "Health monitoring", "Pulse, blood pressure, sleep from smartwatches — with dynamics.", "/en/features/monitoring/"),
        ("👩‍⚕️", "Doctors online", "Book a specialist from any region without queues.", "/en/features/doctors/"),
        ("🚨", "SOS help", "An action plan and data access in an emergency.", "/en/features/sos/"),
    ]
    ic = "".join(f'<a class="card" href="{h}"><div class="ic">{i}</div><h3>{t}</h3><p>{d}</p>'
                 f'<span class="more">Learn more →</span></a>' for i, t, d, h in cards)
    body = f"""
<p class="lede"><strong>AIVITA combines six tools for health care in one app.</strong> Each works on its
own, but together they give a complete picture: from a quick self-check to a doctor's consultation and
tracking metrics over time. Below are the tools with a note on what each is for.</p>
<div class="grid grid-3">{ic}</div>

<h2>How AIVITA's features work together</h2>
<p>The scenario is simple: you take an AI check-up and save the result to your card. If something needs
attention, you book a doctor online and open the needed data to them. The doctor sees not only the
check-up but the dynamics from your band. Before buying a new medicine, you check its compatibility.</p>

<h2>Why this matters in Uzbekistan</h2>
<p>Strong specialists and modern diagnostics are concentrated in large cities. AIVITA's features remove
these barriers: telemedicine opens access to a doctor from any region, and the electronic card replaces
a folder of paper tests. Everything works in Russian, Uzbek and English.</p>

<h2>One app instead of ten</h2>
<p>Previously this required separate services: one app for steps, another for booking a doctor, a folder
of paper tests, an internet search about medicines. AIVITA brings it all into a single system in three
languages — Russian, Uzbek and English — available in any region of Uzbekistan. This saves time and
reduces the risk of losing important health information.</p>

<h2>Where to start</h2>
<p>The simplest first step is to take an <a href="/en/features/ai-checkup/">AI check-up</a> and save the
result to your card. Then connect a <a href="/en/features/monitoring/">smartwatch or band</a> to see the
dynamics of your metrics and set up your <a href="/en/features/sos/">SOS profile</a>. When a question
comes up, book a <a href="/en/features/doctors/">doctor online</a>. Each tool is useful on its own, but
together they give what AIVITA was built for: peace of mind about your health and your loved ones'.</p>
"""
    return Page(
        path="en/features", lang="en",
        title="AIVITA Features — AI Check-up, Medical Card, Doctors Online",
        description="AIVITA features: a 60-second AI check-up, electronic medical card, drug-compatibility checker, health monitoring from smartwatches, online doctors and SOS help.",
        h1="AIVITA features",
        body=body, section="features",
        crumbs=[("Home", "/en/"), ("Features", None)],
        hreflang=alts("features"),
        related=[("Medical tourism", "/en/medical-tourism/"), ("About AIVITA", "/en/about/"),
                 ("Health monitoring", "/en/features/monitoring/")],
    )


def about():
    body = """
<p class="lede"><strong>AIVITA is a digital health ecosystem in Uzbekistan that connects patients,
clinics and specialists in three languages.</strong> Our mission is to make quality medical care
accessible to everyone in the country, regardless of city or language.</p>

<h2>Our mission</h2>
<p>We believe health care should not be blocked by queues, distances and paperwork. AIVITA connects a
person with medicine simply: self-assessment, an electronic medical card, a drug checker, monitoring and
online doctors — in one app. We work across all regions of Uzbekistan and build a service you can trust
with your health.</p>

<h2>The AIVITA ecosystem</h2>
<p>AIVITA is not a single app but an ecosystem of three connected directions: a service for patients, a
system for clinics and a solution for beauty salons.</p>

<div class="grid grid-3">
  <div class="card"><div class="ic">🩺</div><h3>AIVITA — for patients</h3>
  <p>AI check-up, electronic medical card, drug checker, health monitoring and online doctors.</p>
  <a class="more" href="/en/features/">Features →</a></div>

  <div class="card"><div class="ic">🏥</div><h3>MedSoft — for clinics</h3>
  <p>A medical information system for clinic automation. Clinics on MedSoft receive patients from the
  AIVITA catalogue.</p>
  <a class="more" href="/medsoft/">About MedSoft →</a></div>

  <div class="card"><div class="ic">💄</div><h3>AIVITA Beauty — for salons</h3>
  <p>A solution for beauty salons: online booking with cosmetologists, cosmetology and make-up services.</p>
  <span class="more">Part of the ecosystem</span></div>
</div>

<h2>AIVITA Beauty: beauty and care</h2>
<p>AIVITA Beauty extends the ecosystem towards aesthetics and care. It's a direction for beauty salons
and their clients: online booking at a salon, cosmetology and make-up services. It's convenient for a
client to find a salon and book online, and for a salon to manage its schedule.</p>

<h2>We work across all of Uzbekistan</h2>
<p>AIVITA is available in all regions of Uzbekistan — from Karakalpakstan to the Fergana Valley. Thanks
to telemedicine, residents of any city get access to doctors, and an interface in Russian, Uzbek and
English makes the service clear to everyone.</p>

<h2>Our principles</h2>
<p>We do not replace a doctor and do not make diagnoses — we help people care for their health and reach
out to specialists in time. We are careful with personal data: access to the medical card is controlled
by the patient. And we rely on trustworthy information, not promises of miracles.</p>
"""
    faq = [
        ("What is AIVITA?", "A digital health ecosystem in Uzbekistan: a service for patients, the MedSoft system for clinics and AIVITA Beauty for salons. It works in three languages."),
        ("What is in the AIVITA ecosystem?", "Three directions: AIVITA for patients (check-up, card, online doctors), MedSoft for clinic automation and AIVITA Beauty for online salon booking."),
        ("What is AIVITA Beauty?", "A direction for beauty salons and clients: online salon booking, cosmetology and make-up services."),
        ("Which regions does AIVITA work in?", "All regions of Uzbekistan. Telemedicine opens access to doctors from any city, and the interface is in Russian, Uzbek and English."),
        ("Does AIVITA replace a doctor?", "No. AIVITA helps you care for your health and reach specialists in time, but it does not diagnose or prescribe — that is done by a doctor."),
    ]
    schema = [
        {"@type": "AboutPage", "name": "About AIVITA", "url": DOMAIN + "/en/about/",
         "inLanguage": "en", "isPartOf": {"@id": DOMAIN + "/#website"}},
        {"@type": "Organization", "name": BRAND, "url": DOMAIN + "/", "email": "hello@aivita.uz",
         "areaServed": "UZ", "logo": DOMAIN + "/assets/og-image.svg"},
    ]
    return Page(
        path="en/about", lang="en",
        title="About AIVITA — Health Ecosystem in Uzbekistan",
        description="About AIVITA: mission, an ecosystem of AIVITA (patients), MedSoft (clinics) and AIVITA Beauty (beauty salons). We work across all regions of Uzbekistan in three languages.",
        h1="About AIVITA",
        body=body, faq=faq, schema=schema, section="about",
        crumbs=[("Home", "/en/"), ("About", None)],
        hreflang=alts("about", langs=("ru", "uz", "en")),
        disclaimer=True,
        related=[("Features", "/en/features/"), ("Medical tourism", "/en/medical-tourism/"),
                 ("Doctors online", "/en/features/doctors/")],
    )


def pages():
    return [home(), features_hub(), f_aicheckup(), f_drug(), f_medcard(),
            f_doctors(), f_sos(), f_monitoring(), about()]
