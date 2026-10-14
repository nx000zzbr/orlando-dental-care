#!/usr/bin/env python3
"""Generates the five pages of the Orlando Dental Care site from one set of shared parts.
Run `python3 build.py` after editing; the .html files are the output."""
import json, pathlib

ROOT = pathlib.Path(__file__).parent

def t(en, es):
    """One piece of text in both languages. CSS shows the active one."""
    return f'<span data-l="en">{en}</span><span data-l="es">{es}</span>'

PHONE = '407‑737‑9444'
TEL = 'tel:+14077379444'
MAIL = 'orlandodentalcare@gmail.com'

PAGES = [
    ('index.html', 'Home', 'Inicio'),
    ('services.html', 'Services', 'Servicios'),
    ('doctor.html', 'Dr. Santos', 'Dra. Santos'),
    ('testimonials.html', 'Testimonials', 'Testimonios'),
    ('contact.html', 'Contact', 'Contacto'),
]

def head(title, desc):
    return f'''<!doctype html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0b5c66">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="es_US">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Dentist","name":"Orlando Dental Care","url":"https://www.odcare.com/","telephone":"+1-407-737-9444","email":"orlandodentalcare@gmail.com","address":{{"@type":"PostalAddress","streetAddress":"5211 Curry Ford Rd, Suite 1","addressLocality":"Orlando","addressRegion":"FL","postalCode":"32812","addressCountry":"US"}},"geo":{{"@type":"GeoCoordinates","latitude":28.5244315,"longitude":-81.320402}},"openingHoursSpecification":{{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"17:00"}},"founder":{{"@type":"Person","name":"Dr. A. Viviana Santos","jobTitle":"Dentist"}},"knowsLanguage":["en","es"]}}</script>
<script>try{{var l=localStorage.getItem('odc-lang');if(l==='es'||l==='en'){{document.documentElement.dataset.lang=l;document.documentElement.lang=l;}}}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Albert+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='12' fill='%230b5c66'/%3E%3Crect x='12' y='14' width='8' height='36' rx='2' fill='%23cfe6f4'/%3E%3Crect x='23' y='22' width='8' height='28' rx='2' fill='%23c9dcb8'/%3E%3Crect x='34' y='18' width='8' height='32' rx='2' fill='%23f5a93a'/%3E%3Crect x='45' y='26' width='8' height='24' rx='2' fill='%23f3ead6'/%3E%3C/svg%3E">
<link rel="stylesheet" href="styles.css">
</head>
<body>
'''

def header(current):
    links = ''
    for f, en, es in PAGES:
        cur = ' aria-current="page"' if f == current else ''
        links += f'<a href="{f}"{cur}>{t(en, es)}</a>'
    return f'''<a class="skip" href="#main">{t("Skip to content", "Ir al contenido")}</a>
<header class="site-head">
  <div class="wrap head-row">
    <a class="brand" href="index.html" aria-label="Orlando Dental Care, home">
      <span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
      <span class="brand-name">Orlando Dental Care</span>
    </a>
    <nav class="menu" id="menu" aria-label="Main">{links}</nav>
    <div class="head-actions">
      <button class="lang" id="lang" type="button" aria-label="Cambiar idioma / Change language">{t("Español", "English")}</button>
      <a class="btn btn-primary head-cta" href="contact.html">{t("Book a visit", "Reservar cita")}</a>
      <button class="burger" id="burger" type="button" aria-expanded="false" aria-controls="menu">{t("Menu", "Menú")}</button>
    </div>
  </div>
</header>
<main id="main">
'''

def footer():
    return f'''</main>
<footer class="site-foot">
  <div class="wrap foot-grid">
    <div>
      <a class="brand brand-light" href="index.html"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i><i></i></span><span class="brand-name">Orlando Dental Care</span></a>
      <p class="foot-text">{t("Family dentistry in English and Spanish, in southeast Orlando. Dr. A. Viviana Santos, DDS.", "Odontología familiar en español e inglés, en el sureste de Orlando. Dra. A. Viviana Santos.")}</p>
    </div>
    <div>
      <h2 class="foot-h">{t("Visit", "Visítenos")}</h2>
      <p class="foot-text">5211 Curry Ford Rd, Suite 1<br>Orlando, FL 32812<br><a href="{TEL}">{PHONE}</a><br><a href="mailto:{MAIL}">{MAIL}</a></p>
    </div>
    <div>
      <h2 class="foot-h">{t("Hours", "Horario")}</h2>
      <p class="foot-text">{t("Monday to Friday", "Lunes a viernes")}<br>9:00 a.m. – 5:00 p.m.<br><span class="open-now" data-open-now></span></p>
    </div>
    <div>
      <h2 class="foot-h">{t("Pages", "Páginas")}</h2>
      <p class="foot-text foot-links">{''.join(f'<a href="{f}">{t(en, es)}</a>' for f, en, es in PAGES)}</p>
    </div>
  </div>
  <div class="wrap foot-bottom">
    <p>© 2026 Orlando Dental Care</p>
    <p class="foot-credit">{t("Postcards: Tichnor Brothers Collection, Boston Public Library (CC BY 2.0) and Tichnor Bros. via Wikimedia Commons (public domain). Map © OpenStreetMap contributors.", "Postales: colección Tichnor Brothers, Boston Public Library (CC BY 2.0) y Tichnor Bros. vía Wikimedia Commons (dominio público). Mapa © colaboradores de OpenStreetMap.")}</p>
  </div>
</footer>
<script src="main.js" defer></script>
</body>
</html>
'''

def section_title(colour, en, es, tag='h2', lead=None):
    out = f'<span class="bar bar-{colour}" aria-hidden="true"></span><{tag} class="h2">{t(en, es)}</{tag}>'
    if lead:
        out += f'<p class="lead">{t(*lead)}</p>'
    return f'<div class="section-title">{out}</div>'

# ---------- drawings (one flat style, used small on cards and large on the services page) ----------
ART = {
    'cosmetic': '<svg viewBox="0 0 400 400" aria-hidden="true" focusable="false"><path d="M80 60c0-50 80-50 120-10 40-40 120-40 120 10 0 70-20 110-40 140-10 60-20 140-50 150-20 5-25-60-30-90-5 30-10 95-30 90-30-10-40-90-50-150-20-30-40-70-40-140z"/><path d="M330 10l14 44 44 14-44 14-14 44-14-44-44-14 44-14z"/></svg>',
    'general': '<svg viewBox="0 0 400 400" aria-hidden="true" focusable="false"><path d="M40 120c0-50 80-50 120-10 40-40 120-40 120 10 0 70-20 110-40 140-10 60-20 140-50 150-20 5-25-60-30-90-5 30-10 95-30 90-30-10-40-90-50-150-20-30-40-70-40-140z"/><g transform="rotate(-38 270 230)"><rect x="150" y="212" width="300" height="34" rx="17"/><rect x="112" y="184" width="86" height="90" rx="10"/></g></svg>',
    'restorative': '<svg viewBox="0 0 400 400" aria-hidden="true" focusable="false"><path d="M110 50c0-50 180-50 180 0 0 70-20 100-40 120H150c-20-20-40-50-40-120z"/><rect x="170" y="170" width="60" height="26"/><path d="M160 196h80l-22 190h-36z"/><rect x="150" y="214" width="100" height="12"/><rect x="153" y="242" width="94" height="12"/><rect x="156" y="270" width="88" height="12"/><rect x="159" y="298" width="82" height="12"/><rect x="162" y="326" width="76" height="12"/><rect x="165" y="354" width="70" height="12"/></svg>',
    'advanced': '<svg viewBox="0 0 400 400" aria-hidden="true" focusable="false"><path fill-rule="evenodd" d="M50 400V210C50 80 350 80 350 210v190h-50V220c0-70-200-70-200 0v180z"/><g class="knock"><circle cx="78" cy="300" r="22"/><circle cx="86" cy="222" r="22"/><circle cx="125" cy="168" r="22"/><circle cx="200" cy="146" r="22"/><circle cx="275" cy="168" r="22"/><circle cx="314" cy="222" r="22"/><circle cx="322" cy="300" r="22"/></g></svg>',
}

SERVICES = [
    ('cosmetic', 'sky', ('Cosmetic dentistry', 'Odontología estética'),
     ('Treatments that change how a smile looks, planned so the result still looks like you.',
      'Tratamientos que cambian cómo se ve una sonrisa, planeados para que el resultado siga pareciéndose a usted.'),
     [('Teeth whitening', 'Blanqueamiento dental'), ('Porcelain veneers', 'Carillas de porcelana'), ('Invisalign clear aligners', 'Alineadores transparentes Invisalign'), ('Dental implants', 'Implantes dentales'), ('Tooth-colored fillings', 'Empastes del color del diente'), ('Dental crowns', 'Coronas dentales')]),
    ('general', 'sage', ('General dentistry', 'Odontología general'),
     ('The exams and cleanings that keep teeth and gums strong for a lifetime.',
      'Los exámenes y limpiezas que mantienen dientes y encías fuertes toda la vida.'),
     [('Exams and cleanings', 'Exámenes y limpiezas'), ('Digital X‑rays', 'Radiografías digitales'), ('Gum (periodontal) care', 'Cuidado de encías (periodontal)'), ('Mercury‑free fillings', 'Empastes sin mercurio'), ('Root canal treatment', 'Tratamiento de conducto'), ('Dentures, conventional or on implants', 'Prótesis, convencionales o sobre implantes'), ('Sealants', 'Sellantes')]),
    ('restorative', 'orange', ('Restorative dentistry', 'Odontología restauradora'),
     ('Replacing and rebuilding teeth, so you bite, chew and eat the way you used to.',
      'Reemplazar y reconstruir dientes, para que muerda, mastique y coma como antes.'),
     [('Replacing one, several or all missing teeth', 'Reemplazo de uno, varios o todos los dientes'), ('Implant placement and restoration', 'Colocación y restauración de implantes'), ('Simple and complicated extractions', 'Extracciones simples y complejas'), ('Wisdom teeth removal', 'Extracción de muelas del juicio'), ('Full‑mouth extractions with dentures or implants', 'Extracciones completas con prótesis o implantes')]),
    ('advanced', 'teal', ('Advanced and family care', 'Cuidado avanzado y familiar'),
     ('The cases that usually mean a referral somewhere else, done here, by the same dentist.',
      'Los casos que suelen significar una remisión a otro lugar, hechos aquí, por la misma dentista.'),
     [('Periodontics, the treatment of gum disease', 'Periodoncia, tratamiento de la enfermedad de las encías'), ('Pediatric dentistry', 'Odontología pediátrica'), ('Oral cancer screening', 'Detección de cáncer oral'), ('Orthodontics with Invisalign', 'Ortodoncia con Invisalign'), ('Emergency dental care', 'Urgencias dentales')]),
]

TESTIMONIALS = [
    (('“Dr. Santos is kind and caring with a delicate touch, and simply outstanding results. I couldn’t recommend her highly enough! 10 out of 10 for sure!”',
      '“La Dra. Santos es amable y atenta, con un toque delicado, y resultados sencillamente extraordinarios. ¡No podría recomendarla más! 10 de 10, seguro.”'), 'Veronica Mendez', 'sky'),
    (('“From my first visit to Orlando Dental Care, I have felt at ease and very well cared for.”',
      '“Desde mi primera visita a Orlando Dental Care me he sentido tranquilo y muy bien atendido.”'), 'Hubert van Alphen', 'sage'),
    (('“The best dental experience of my life.”', '“La mejor experiencia dental de mi vida.”'), 'Rose Fragoso', 'orange'),
]

def visit_bar():
    segs = [('sand', 15, ('About 15 minutes', 'Unos 15 minutos'), ('Exam and photographs', 'Examen y fotografías')),
            ('sage', 10, ('10 minutes', '10 minutos'), ('Digital X‑rays', 'Radiografías digitales')),
            ('orange', 20, ('20 minutes', '20 minutos'), ('Your options, explained', 'Sus opciones, explicadas')),
            ('teal', 25, ('As long as you need', 'El tiempo que necesite'), ('Your decision', 'Su decisión'))]
    clauses = [('First', 'Primero', 'Dr. Santos looks at every tooth and your gums, and takes photographs.', 'la Dra. Santos revisa cada diente y sus encías, y toma fotografías.'),
               ('Then', 'Luego', 'digital X‑rays, at a fraction of the old dose.', 'radiografías digitales, con una fracción de la dosis de antes.'),
               ('Then', 'Después', 'she lays out more than one treatment plan, with what each one costs.', 'le presenta más de un plan de tratamiento, con lo que cuesta cada uno.'),
               ('Last', 'Al final', 'you choose. Nothing starts until you say so.', 'usted decide. Nada empieza hasta que usted lo diga.')]
    steps = ''
    for (c, g, d, l), (w_en, w_es, c_en, c_es) in zip(segs, clauses):
        steps += (f'<div class="step" style="--grow:{g}"><div class="seg seg-{c}"><strong>{t(*d)}</strong><span>{t(*l)}</span></div>'
                  f'<p><strong>{t(w_en, w_es)}</strong> {t(c_en, c_es)}</p></div>')
    return f'<div class="visit-steps">{steps}</div>'

def tilemap():
    g = json.load(open(ROOT / 'assets/map/grid.json'))
    tiles = ''.join(f'<img src="assets/map/{g["z"]}-{x}-{y}.png" width="256" height="256" alt="" loading="lazy">' for y in g['rows'] for x in g['cols'])
    return (f'<div class="tilemap" role="img" aria-label="Map of 5211 Curry Ford Road, Orlando"><div class="tilemap-grid">{tiles}'
            f'<span class="tilemap-pin" style="left:{g["marker"][0]*100:.2f}%;top:{g["marker"][1]*100:.2f}%"></span></div></div>')

def cta_band():
    return f'''<section class="band band-teal">
  <div class="wrap band-row">
    <div>
      <h2 class="h2 h2-light">{t("Ready for a first visit?", "¿Agendamos su primera visita?")}</h2>
      <p class="band-text">{t("Call, or send a message and the front desk will get back to you the same business day.", "Llame o envíe un mensaje y la recepción le responde el mismo día hábil.")}</p>
    </div>
    <div class="btn-row">
      <a class="btn btn-orange" href="contact.html">{t("Book a visit", "Reservar cita")}</a>
      <a class="btn btn-ghost-light" href="{TEL}">{t("Call", "Llamar")} {PHONE}</a>
    </div>
  </div>
</section>'''

# =================================================================== HOME
def home():
    service_cards = ''.join(f'''
    <article class="card card-service">
      <span class="bar bar-{colour}" aria-hidden="true"></span>
      <div class="card-art art-{colour}">{ART[key]}</div>
      <h3 class="h3">{t(*name)}</h3>
      <ul class="plain">{''.join(f'<li>{t(*i)}</li>' for i in items[:3])}</ul>
      <a class="more" href="services.html#{key}">{t("See the full list", "Ver la lista completa")} →</a>
    </article>''' for key, colour, name, lead, items in SERVICES)
    quotes = ''.join(f'''
    <blockquote class="card card-quote">
      <span class="bar bar-{colour}" aria-hidden="true"></span>
      <p>{t(*q)}</p>
      <footer>{name}, {t("patient", "paciente")}</footer>
    </blockquote>''' for q, name, colour in TESTIMONIALS)
    return f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <p class="kicker">{t("Family dentistry · Orlando, FL · Hablamos español", "Odontología familiar · Orlando, FL · Hablamos español")}</p>
      <h1 class="h1">{t("Your whole smile, one address.", "Toda su sonrisa, en un solo lugar.")}</h1>
      <p class="lead">{t("Dr. A. Viviana Santos treats families at 5211 Curry Ford Road, from cleanings to implants, in English and Spanish. One dentist, every treatment, with options to fit your budget.", "La Dra. A. Viviana Santos atiende familias en 5211 Curry Ford Road, desde limpiezas hasta implantes, en español y en inglés. Una sola dentista, todos los tratamientos, con opciones para su presupuesto.")}</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html">{t("Book a visit", "Reservar cita")}</a>
        <a class="btn btn-ghost" href="{TEL}">{t("Call", "Llamar")} {PHONE}</a>
      </div>
      <ul class="trust">
        <li><span class="dot dot-teal"></span>{t("In Orlando since 1999", "En Orlando desde 1999")}</li>
        <li><span class="dot dot-orange"></span>{t("Member, American Dental Association", "Miembro de la American Dental Association")}</li>
        <li><span class="dot dot-sage"></span>{t("Children and adults", "Niños y adultos")}</li>
      </ul>
    </div>
    <aside class="card visit-card" aria-label="Plan your visit">
      <div class="stripe" aria-hidden="true"><i class="bar-sky"></i><i class="bar-sage"></i><i class="bar-orange"></i><i class="bar-teal"></i></div>
      <h2 class="h3">{t("Plan your visit", "Planee su visita")}</h2>
      <dl class="facts">
        <div><dt>{t("Today", "Hoy")}</dt><dd><span class="open-now" data-open-now></span></dd></div>
        <div><dt>{t("Hours", "Horario")}</dt><dd>{t("Monday to Friday, 9 a.m. to 5 p.m.", "Lunes a viernes, 9 a.m. a 5 p.m.")}</dd></div>
        <div><dt>{t("Address", "Dirección")}</dt><dd>5211 Curry Ford Rd, Suite 1<br>Orlando, FL 32812</dd></div>
        <div><dt>{t("Phone", "Teléfono")}</dt><dd><a href="{TEL}">{PHONE}</a></dd></div>
        <div><dt>{t("Languages", "Idiomas")}</dt><dd>{t("English and Spanish", "Español e inglés")}</dd></div>
      </dl>
      <div class="btn-row visit-card-actions">
        <a class="btn btn-primary" href="contact.html">{t("Book a visit", "Reservar cita")}</a>
        <a class="more" href="contact.html">{t("Directions", "Cómo llegar")} →</a>
      </div>
    </aside>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <ul class="facts-row">
      <li><span class="bar bar-sky" aria-hidden="true"></span><strong>{t("One dentist for everything", "Una sola dentista para todo")}</strong><span>{t("Cleanings, fillings, crowns and implants, all by Dr. Santos, nothing referred away.", "Limpiezas, empastes, coronas e implantes, todo con la Dra. Santos, sin remisiones.")}</span></li>
      <li><span class="bar bar-sage" aria-hidden="true"></span><strong>{t("English and Spanish", "Español e inglés")}</strong><span>{t("The whole visit, from the phone call to the treatment plan, in your language.", "Toda la visita, desde la llamada hasta el plan de tratamiento, en su idioma.")}</span></li>
      <li><span class="bar bar-orange" aria-hidden="true"></span><strong>{t("Options for your budget", "Opciones para su presupuesto")}</strong><span>{t("More than one treatment plan, explained, so the choice stays yours.", "Más de un plan de tratamiento, explicado, para que la decisión sea suya.")}</span></li>
      <li><span class="bar bar-teal" aria-hidden="true"></span><strong>{t("Children and adults", "Niños y adultos")}</strong><span>{t("Pediatric and family dentistry, and emergency care when a tooth can’t wait.", "Odontología pediátrica y familiar, y urgencias cuando un diente no puede esperar.")}</span></li>
    </ul>
  </div>
</section>

<section class="section section-paper" id="services">
  <div class="wrap">
    <div class="section-head">
      {section_title("teal", "Services", "Servicios", lead=("Four areas of care, one office. Each one is explained in full on the services page.", "Cuatro áreas de atención, un solo consultorio. Cada una se explica completa en la página de servicios."))}
      <a class="btn btn-ghost" href="services.html">{t("All services", "Todos los servicios")}</a>
    </div>
    <div class="grid-4">{service_cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {section_title("orange", "Your first visit", "Su primera visita", lead=("About an hour. Each part of the bar is as long as that step takes.", "Alrededor de una hora. Cada parte de la barra dura lo que dura esa etapa."))}
    {visit_bar()}
  </div>
</section>

<section class="section section-paper">
  <div class="wrap doctor-grid">
    <div class="postcards" aria-hidden="true">
      <img src="assets/bogota-catedral-postcard.jpg" width="1600" height="1015" alt="" loading="lazy">
      <img src="assets/orlando-eola-postcard.jpg" width="1024" height="649" alt="" loading="lazy">
    </div>
    <div>
      {section_title("sky", "Meet Dr. A. Viviana Santos", "Conozca a la Dra. A. Viviana Santos")}
      <p>{t("Born in Bogotá, Colombia, Dr. Santos graduated from El Bosque University in 1996, moved to Florida in 1999 and completed the IEDP program at the University of Florida. She treats children and adults, from a first filling to complex implant, restorative and cosmetic cases.", "Nacida en Bogotá, Colombia, la Dra. Santos se graduó en la Universidad El Bosque en 1996, se mudó a Florida en 1999 y completó el programa IEDP de la Universidad de Florida. Atiende niños y adultos, desde un primer empaste hasta casos complejos de implantes, restauración y estética.")}</p>
      <p>{t("Member of the American Dental Association, the Florida Dental Association and the Central District Dental Association.", "Miembro de la American Dental Association, la Florida Dental Association y la Central District Dental Association.")}</p>
      <a class="btn btn-ghost" href="doctor.html">{t("Her story", "Su historia")}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      {section_title("sage", "What patients say", "Lo que dicen los pacientes")}
      <a class="btn btn-ghost" href="testimonials.html">{t("All testimonials", "Todos los testimonios")}</a>
    </div>
    <div class="grid-3">{quotes}</div>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap contact-grid">
    <div>
      {section_title("teal", "Find us", "Dónde estamos")}
      <dl class="facts facts-large">
        <div><dt>{t("Address", "Dirección")}</dt><dd>5211 Curry Ford Rd, Suite 1<br>Orlando, FL 32812</dd></div>
        <div><dt>{t("Hours", "Horario")}</dt><dd>{t("Monday to Friday, 9 a.m. to 5 p.m.", "Lunes a viernes, 9 a.m. a 5 p.m.")} <span class="open-now" data-open-now></span></dd></div>
        <div><dt>{t("Phone", "Teléfono")}</dt><dd><a href="{TEL}">{PHONE}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
      </dl>
      <div class="btn-row">
        <a class="btn btn-primary" href="contact.html">{t("Contact page", "Página de contacto")}</a>
        <a class="btn btn-ghost" href="https://www.google.com/maps/dir/?api=1&destination=5211+Curry+Ford+Rd+Suite+1+Orlando+FL+32812" target="_blank" rel="noopener">{t("Directions", "Cómo llegar")}</a>
      </div>
    </div>
    {tilemap()}
  </div>
</section>
'''

# =================================================================== SERVICES
def services():
    blocks = ''
    for i, (key, colour, name, lead, items) in enumerate(SERVICES):
        li = ''.join(f'<li>{t(*x)}</li>' for x in items)
        blocks += f'''
<section class="section {"section-paper" if i % 2 else ""}" id="{key}">
  <div class="wrap service-grid">
    <div>
      {section_title(colour, name[0], name[1])}
      <p class="lead">{t(*lead)}</p>
      <ul class="checks">{li}</ul>
      <a class="btn btn-primary" href="contact.html">{t("Ask about this care", "Consultar sobre esto")}</a>
    </div>
    <div class="service-art art-{colour}">{ART[key]}</div>
  </div>
</section>'''
    jump = ''.join(f'<a href="#{key}"><span class="dot dot-{colour}"></span>{t(*name)}</a>' for key, colour, name, _, _ in SERVICES)
    return f'''
<section class="page-head">
  <div class="wrap">
    <p class="kicker">{t("Services", "Servicios")}</p>
    <h1 class="h1">{t("Everything your smile needs, in one office.", "Todo lo que su sonrisa necesita, en un solo consultorio.")}</h1>
    <p class="lead">{t("Dr. Santos performs every treatment below herself, so you are never sent somewhere else for the next step.", "La Dra. Santos realiza ella misma todos los tratamientos de esta lista, así nunca lo envían a otro lugar para el siguiente paso.")}</p>
    <nav class="jump" aria-label="Service areas">{jump}</nav>
  </div>
</section>
{blocks}
{cta_band()}
'''

# =================================================================== DOCTOR
def doctor():
    timeline = [
        ('sky', '1996', ('Dental degree, El Bosque University, Bogotá', 'Título de odontóloga, Universidad El Bosque, Bogotá')),
        ('sage', '1997', ('Specialty in public health, Universidad del Rosario', 'Especialización en salud pública, Universidad del Rosario')),
        ('orange', '1999', ('Moves to Florida', 'Se muda a Florida')),
        ('teal', t('2000s', 'Años 2000'), ('IEDP program, University of Florida; passes her boards', 'Programa IEDP, Universidad de Florida; aprueba sus exámenes de licencia')),
        ('sand', t('Today', 'Hoy'), ('Orlando Dental Care, 5211 Curry Ford Road', 'Orlando Dental Care, 5211 Curry Ford Road')),
    ]
    tl = ''.join(f'<li><span class="bar bar-{c}" aria-hidden="true"></span><strong>{y}</strong><span>{t(*d)}</span></li>' for c, y, d in timeline)
    return f'''
<section class="page-head">
  <div class="wrap">
    <p class="kicker">{t("Meet the doctor", "Conozca a la doctora")}</p>
    <h1 class="h1">{t("Dr. A. Viviana Santos", "Dra. A. Viviana Santos")}</h1>
    <p class="lead">{t("A dentist from Bogotá who has cared for Orlando families since 1999, in English and Spanish.", "Una odontóloga de Bogotá que cuida a las familias de Orlando desde 1999, en español y en inglés.")}</p>
  </div>
</section>

<section class="section">
  <div class="wrap doctor-grid">
    <div class="doctor-photo">
      <div class="photo-slot">
        <span class="stripe" aria-hidden="true"><i class="bar-sky"></i><i class="bar-sage"></i><i class="bar-orange"></i><i class="bar-teal"></i></span>
        <p>{t("Portrait of Dr. Santos", "Retrato de la Dra. Santos")}</p>
        <small>{t("Photo to be supplied by the office", "Foto a entregar por el consultorio")}</small>
      </div>
    </div>
    <div>
      {section_title("sky", "Her story", "Su historia")}
      <p>{t("A native of Bogotá, Colombia, Dr. A. Viviana Santos received her dental degree in 1996 from El Bosque University. After graduation she completed a specialty in public health at Universidad del Rosario. In 1999 she moved to Florida, went on to the University of Florida and graduated from the IEDP program. After passing her boards, she began serving her community’s dental needs.", "Nacida en Bogotá, Colombia, la Dra. A. Viviana Santos recibió su título de odontóloga en 1996 en la Universidad El Bosque. Después de graduarse completó una especialización en salud pública en la Universidad del Rosario. En 1999 se mudó a Florida, continuó en la Universidad de Florida y se graduó del programa IEDP. Tras aprobar sus exámenes de licencia, empezó a atender las necesidades dentales de su comunidad.")}</p>
      <p>{t("In her Orlando practice Dr. Santos performs a wide range of treatments, from fillings to complex implant, restorative and cosmetic cases. Having devoted countless hours to treating children and adults, she is an expert at putting patients of all ages at ease. Nothing brings her more satisfaction than a treatment plan tailored to each patient’s oral and overall health.", "En su consultorio de Orlando, la Dra. Santos realiza una amplia gama de tratamientos, desde empastes hasta casos complejos de implantes, restauración y estética. Tras incontables horas atendiendo a niños y adultos, es experta en tranquilizar a pacientes de todas las edades. Nada le da más satisfacción que un plan de tratamiento hecho a la medida de la salud oral y general de cada paciente.")}</p>
      <p>{t("Dr. Santos lives in Orlando with her husband and daughters.", "La Dra. Santos vive en Orlando con su esposo y sus hijas.")}</p>
    </div>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap two-col">
    <div>
      {section_title("orange", "Training and practice", "Formación y trayectoria")}
      <ol class="timeline">{tl}</ol>
    </div>
    <div>
      {section_title("teal", "Memberships", "Membresías")}
      <ul class="checks">
        <li>American Dental Association</li>
        <li>Florida Dental Association</li>
        <li>Central District Dental Association</li>
      </ul>
      {section_title("sage", "From Bogotá to Orlando", "De Bogotá a Orlando")}
      <div class="postcards postcards-row">
        <figure><img src="assets/bogota-hotel-granada-postcard.jpg" width="1599" height="1000" alt="Vintage postcard of the Hotel Granada in Bogotá" loading="lazy"><figcaption>Bogotá, {t("1940s postcard", "postal de los años 40")}</figcaption></figure>
        <figure><img src="assets/orlando-courthouse-postcard.jpg" width="1024" height="653" alt="Vintage postcard of the Orange County court house in Orlando" loading="lazy"><figcaption>Orlando, {t("1940s postcard", "postal de los años 40")}</figcaption></figure>
      </div>
    </div>
  </div>
</section>
{cta_band()}
'''

# =================================================================== TESTIMONIALS
def testimonials():
    cards = ''.join(f'''
    <blockquote class="card card-quote card-quote-large">
      <span class="bar bar-{colour}" aria-hidden="true"></span>
      <p>{t(*q)}</p>
      <footer>{name}, {t("patient", "paciente")}</footer>
    </blockquote>''' for q, name, colour in TESTIMONIALS)
    return f'''
<section class="page-head">
  <div class="wrap">
    <p class="kicker">{t("Testimonials", "Testimonios")}</p>
    <h1 class="h1">{t("What patients say", "Lo que dicen los pacientes")}</h1>
    <p class="lead">{t("A sample of what patients have said about the practice over the years.", "Una muestra de lo que los pacientes han dicho del consultorio a lo largo de los años.")}</p>
  </div>
</section>
<section class="section">
  <div class="wrap grid-3 grid-stretch">{cards}</div>
</section>
<section class="section section-paper">
  <div class="wrap two-col">
    <div>
      {section_title("orange", "Been a patient?", "¿Ha sido paciente?")}
      <p>{t("A short review helps the next family find the office. It takes a minute on Google.", "Una reseña corta ayuda a la siguiente familia a encontrar el consultorio. Toma un minuto en Google.")}</p>
      <a class="btn btn-primary" href="https://www.google.com/search?q=Orlando+Dental+Care+Curry+Ford+Rd+reviews" target="_blank" rel="noopener">{t("Leave a Google review", "Dejar una reseña en Google")}</a>
    </div>
    <div>
      {section_title("sky", "New here?", "¿Nuevo aquí?")}
      <p>{t("Your first visit is an exam and a conversation about options and budget, nothing more. Nobody will lecture you, however long it has been.", "Su primera visita es un examen y una conversación sobre opciones y presupuesto, nada más. Nadie te va a regañar, por mucho tiempo que haya pasado.")}</p>
      <a class="btn btn-ghost" href="contact.html">{t("Book a first visit", "Reservar primera visita")}</a>
    </div>
  </div>
</section>
'''

# =================================================================== CONTACT
def contact():
    faqs = [
        (('Do you speak Spanish?', '¿Hablan español?'), ('Yes. Dr. Santos is from Bogotá, and the whole visit, from the phone call to the treatment plan, can happen in Spanish.', 'Sí. La Dra. Santos es de Bogotá, y toda la visita, desde la llamada hasta el plan de tratamiento, puede ser en español.')),
        (('Do you see children?', '¿Atienden niños?'), ('Yes. Pediatric dentistry is part of the practice, and many families book everyone for the same afternoon.', 'Sí. La odontología pediátrica es parte del consultorio, y muchas familias reservan para todos la misma tarde.')),
        (('What if I have a toothache today?', '¿Y si tengo dolor de muela hoy?'), (f'Call <a href="{TEL}">{PHONE}</a>. Emergency dental care is part of what the office does, and same‑day times are kept open whenever possible.', f'Llame al <a href="{TEL}">{PHONE}</a>. Las urgencias dentales son parte del trabajo del consultorio, y se reservan horas para el mismo día siempre que es posible.')),
        (('Do you take my insurance?', '¿Aceptan mi seguro?'), ('Most PPO plans are accepted. Call with the details on your card and the front desk will check before you come in.', 'Se aceptan la mayoría de los planes PPO. Llame con los datos de su tarjeta y la recepción lo verifica antes de su visita.')),
        (('Where do I park?', '¿Dónde estaciono?'), ('Suite 1 at 5211 Curry Ford Road has free parking at the door, with step‑free access from the lot.', 'La Suite 1 en 5211 Curry Ford Road tiene estacionamiento gratis en la puerta, con acceso sin escalones.')),
    ]
    faq = ''.join(f'<details class="faq"><summary>{t(*q)}</summary><p>{t(*a)}</p></details>' for q, a in faqs)
    return f'''
<section class="page-head">
  <div class="wrap">
    <p class="kicker">{t("Contact", "Contacto")}</p>
    <h1 class="h1">{t("Book a visit or ask a question.", "Reserve una cita o haga una pregunta.")}</h1>
    <p class="lead">{t("Call during office hours, or send a message and the front desk will reply the same business day.", "Llame en horario de oficina o envíe un mensaje y la recepción responde el mismo día hábil.")}</p>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div>
      {section_title("teal", "The office", "El consultorio")}
      <dl class="facts facts-large">
        <div><dt>{t("Address", "Dirección")}</dt><dd>5211 Curry Ford Rd, Suite 1<br>Orlando, FL 32812</dd></div>
        <div><dt>{t("Hours", "Horario")}</dt><dd>{t("Monday to Friday, 9 a.m. to 5 p.m.", "Lunes a viernes, 9 a.m. a 5 p.m.")}<br><span class="open-now" data-open-now></span></dd></div>
        <div><dt>{t("Phone", "Teléfono")}</dt><dd><a href="{TEL}">{PHONE}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
        <div><dt>{t("Languages", "Idiomas")}</dt><dd>{t("English and Spanish", "Español e inglés")}</dd></div>
      </dl>
      <a class="btn btn-ghost" href="https://www.google.com/maps/dir/?api=1&destination=5211+Curry+Ford+Rd+Suite+1+Orlando+FL+32812" target="_blank" rel="noopener">{t("Directions in Google Maps", "Cómo llegar en Google Maps")}</a>
    </div>
    <form class="card form" id="contact-form" action="mailto:{MAIL}" method="post">
      <span class="stripe" aria-hidden="true"><i class="bar-sky"></i><i class="bar-sage"></i><i class="bar-orange"></i><i class="bar-teal"></i></span>
      <h2 class="h3">{t("Send a message", "Envíenos un mensaje")}</h2>
      <label>{t("Name", "Nombre")}<input id="f-name" name="name" type="text" required autocomplete="name"></label>
      <label>{t("Phone or email", "Teléfono o correo")}<input id="f-contact" name="contact" type="text" required autocomplete="tel"></label>
      <label>{t("What do you need?", "¿Qué necesita?")}<select id="f-reason" name="reason">
        <option value="first" data-en="A first visit" data-es="Una primera visita">A first visit</option>
        <option value="cleaning" data-en="Cleaning and exam" data-es="Limpieza y examen">Cleaning and exam</option>
        <option value="pain" data-en="I have pain" data-es="Tengo dolor">I have pain</option>
        <option value="cosmetic" data-en="Cosmetic question" data-es="Pregunta de estética">Cosmetic question</option>
        <option value="other" data-en="Something else" data-es="Otra cosa">Something else</option>
      </select></label>
      <label>{t("Message", "Mensaje")}<textarea id="f-msg" name="message" rows="4"></textarea></label>
      <button class="btn btn-primary" type="submit">{t("Send", "Enviar")}</button>
      <p class="form-note">{t("Sending opens your email app with the message filled in. Or just call:", "Al enviar se abre su correo con el mensaje listo. O simplemente llame:")} <a href="{TEL}">{PHONE}</a></p>
    </form>
  </div>
</section>

<section class="section section-paper">
  <div class="wrap">
    {section_title("sage", "Where we are", "Dónde estamos")}
    {tilemap()}
    <p class="map-credit">© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors · <a href="https://www.openstreetmap.org/?mlat=28.5244315&mlon=-81.3204020#map=17/28.52443/-81.32040" target="_blank" rel="noopener">{t("Open the map", "Abrir el mapa")}</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    {section_title("orange", "Good to know", "Vale la pena saber")}
    {faq}
  </div>
</section>
'''

BUILD = {
    'index.html': ('Orlando Dental Care', 'Family dentistry in English and Spanish at 5211 Curry Ford Road, Orlando. Dr. A. Viviana Santos, from cleanings to implants.', home),
    'services.html': ('Services · Orlando Dental Care', 'Cosmetic, general, restorative and advanced dentistry, all by Dr. A. Viviana Santos in Orlando.', services),
    'doctor.html': ('Dr. A. Viviana Santos · Orlando Dental Care', 'Meet Dr. A. Viviana Santos, a dentist from Bogotá caring for Orlando families since 1999.', doctor),
    'testimonials.html': ('Testimonials · Orlando Dental Care', 'What patients say about Orlando Dental Care and Dr. Santos.', testimonials),
    'contact.html': ('Contact · Orlando Dental Care', 'Book a visit at Orlando Dental Care: address, hours, phone, map and a contact form.', contact),
}

for fname, (title, desc, fn) in BUILD.items():
    (ROOT / fname).write_text(head(title, desc) + header(fname) + fn() + footer())
    print('wrote', fname)

# The published copy: the home page without its document wrappers (the publisher adds its own),
# with the other pages, styles, script and images sent alongside as files.
import re
home_html = (ROOT / 'index.html').read_text()
inner_head = re.search(r'<head>(.*?)</head>', home_html, re.S).group(1)
inner_body = re.search(r'<body>(.*?)</body>', home_html, re.S).group(1)
inner_head = '\n'.join(l for l in inner_head.splitlines() if not l.strip().startswith('<meta charset') and not l.strip().startswith('<meta name="viewport"'))
(ROOT / 'dist').mkdir(exist_ok=True)
(ROOT / 'dist/artifact.html').write_text(inner_head + '\n' + inner_body)
print('wrote dist/artifact.html')
