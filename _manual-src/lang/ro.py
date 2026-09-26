T = {
    "title": "Ghid de utilizare",
    "subtitle": "Tot ce poate face Invoice Cove, ecran cu ecran.",
    "meta_desc": "Ghidul complet de utilizare pentru Invoice Cove - Offline Billing.",
    "lang_label": "Limba",
    "brand_alt": "Invoice Cove",
    "toc": "Cuprins",
    "footer_questions": "Întrebări?",
    "lede": (
        "Invoice Cove funcționează în întregime pe dispozitivul tău: facturile, ofertele, clienții și profilul firmei sunt păstrate local, "
        "nu pe vreun server Invoice Cove. Nu colectăm, nu vedem și nu primim nicio informație despre facturile tale sau despre modul "
        "în care folosești aplicația. Nu există analiză de utilizare, nu există urmărire, nu se trimite nimic în fundal. "
        "Singura dată când aplicația însăși are nevoie de internet este pentru achiziția unică Invoice Cove Pro, procesată prin Google Play. "
        "Detalii găsești în <a href=\"privacy.html\">Politica de confidențialitate</a>."
    ),
    "warn": (
        "Ține minte! Înainte să dezinstalezi aplicația sau să-i ștergi datele: nu păstrăm nicăieri o copie a acestor date. "
        "Dezinstalarea Invoice Cove sau ștergerea spațiului de stocare din setările Android șterge definitiv fiecare factură, ofertă, client "
        "și setare de pe acest dispozitiv — nu există o copie în cloud din care să restaurezi. Ca să-ți protejezi fișierele: fă o copie de siguranță cu "
        "Invoice Cove Pro (vezi <a href=\"#backup\">Copie de siguranță și restaurare</a>) sau exportă ce îți trebuie în Excel, CSV sau ZIP "
        "(vezi <a href=\"#export\">Exportul facturilor</a>)."
    ),
    "sections": {
        "home": ("Ecranul principal", [
            ("p", "Ecranul principal este punctul tău de pornire, cu câte o casetă pentru fiecare acțiune importantă: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} și "
                  "{{common_reports_title}}. Atinge o casetă ca să ajungi direct acolo."),
            ("p", "Bara de jos îți oferă acces rapid la {{nav_home}}, {{nav_new}} (factură nouă), "
                  "{{nav_invoices}}, {{nav_customers}} și {{nav_reports}}."),
            ("p", "Pictograma roată (⚙️) din colțul dreapta-sus al majorității ecranelor deschide <a href=\"#settings\">Detaliile firmei și setările</a>."),
        ]),
        "customers": ("Clienți", [
            ("p", "Ca să adaugi un client, mergi în fila {{nav_customers}} și atinge pictograma + sau folosește caseta {{home_new_customer_title}}. "
                  "Poți adăuga unul și în timp ce creezi o factură sau o ofertă. Pentru a crea un client este nevoie doar de nume. Câmpurile opționale includ: "
                  "{{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, adresa, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} și o nuanță de culoare pentru documentele clientului. Fiecare câmp arată un exemplu, ca să știi ce se completează acolo."),
            ("p", "Atinge un client ca să-l {{common_edit}}, să deschizi {{customers_view_history}} (facturi, oferte și ciorne) "
                  "sau să-l {{common_delete}}."),
            ("p", "Pe facturile și ofertele tale, datele clientului sunt tipărite sub numele lui într-o ordine fixă: numărul de client, codul fiscal, numărul de TVA, "
                  "numărul de la registrul comerțului, apoi adresa, emailul și telefonul. Tot ce lași necompletat nu apare."),
            ("note", "Salvarea funcționează diferit aici față de facturi. Un client are propriul buton {{customers_form_save_customer}} "
                     "(sau {{customers_form_save_changes}} la editare) și se salvează în clipa în care îl atingi. Dacă încerci să închizi formularul "
                     "cu modificări nesalvate, Invoice Cove îți cere mai întâi confirmarea."),
            ("note", "Ștergerea unui client nu șterge facturile și ofertele pe care le-ai emis deja pentru el. În schimb, <a href=\"#drafts\">ciornele</a> lui nefinalizate "
                     "se șterg odată cu el; Invoice Cove îți cere mai întâi confirmarea."),
        ]),
        "new-invoice": ("Crearea unei facturi", [
            ("p", "Din {{nav_new}} (sau din caseta {{home_new_invoice_title}}): alege un client (sau creează unul pe loc) "
                  "și stabilește data facturii și data scadenței, apoi adaugă articolele."),
            ("p", "Atinge {{newinvoice_add_item_details_button}} și completează descrierea, cantitatea, prețul unitar și, opțional, o unitate "
                  "(de exemplu h, buc sau kg) și o dată și o oră. Unitatea este tipărită lângă cantitate în PDF. Atinge creionul (✏️) de pe un articol ca să-l corectezi "
                  "sau coșul de gunoi (🗑️) ca să-l ștergi. Descrierile și prețurile folosite înainte îți sunt sugerate pe măsură ce scrii."),
            ("p", "Apoi adaugă, dacă este necesar, o cotă de taxă, o {{newinvoice_discount_label}} (procent sau sumă fixă) și "
                  "{{common_notes_label}}. Numărul facturii este atribuit automat (cu Invoice Cove Pro, poate fi editat), iar moneda se alege lângă el."),
            ("p", "{{common_preview_button}} generează un PDF temporar ca să vezi cum arată — nu se salvează nimic. "
                  "Butonul {{common_template_button}} arată ce șablon va fi folosit; atinge-l ca să alegi altul doar pentru acest document."),
            ("note", "{{newinvoice_generate_button}} face trei lucruri deodată: salvează factura, creează PDF-ul și deschide meniul de partajare al "
                     "dispozitivului ca să o poți trimite. Nu ești gata? Folosește {{newinvoice_save_draft_button}} — vezi <a href=\"#drafts\">Ciorne</a>."),
        ]),
        "drafts": ("Ciorne", [
            ("p", "Nu pierzi o factură la care încă lucrezi. De îndată ce ai ales un client și ai adăugat cel puțin un articol sau o notă, Invoice Cove "
                  "păstrează o ciornă și o actualizează la scurt timp după ce nu mai scrii și încă o dată când părăsești aplicația. Nu există "
                  "întrebarea „renunți la modificări?” când ieși din ecran; un mesaj scurt te anunță că ciorna a fost salvată."),
            ("p", "Atinge {{newinvoice_save_draft_button}} (sub {{newinvoice_generate_button}}) ca să pui factura deoparte intenționat: se salvează, iar "
                  "formularul se golește, gata pentru următoarea factură. Funcționează de îndată ce ai ales un client, chiar înainte să adaugi articole."),
            ("p", "Ciornele le găsești la {{nav_customers}} → clientul → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Fiecare ciornă arată când a fost modificată ultima dată, câte articole are și totalul. Atinge-o ca să "
                  "continui editarea sau ca să generezi factura; atinge coșul de gunoi ca s-o ștergi."),
            ("ul", [
                "O ciornă nu folosește niciodată un număr de factură și nu se numără în limita lunară gratuită. Numărul se atribuie abia când generezi factura "
                "finală — ciorna este atunci înlocuită de ea.",
                "O ciornă păstrează data facturii și data scadenței doar dacă le-ai ales tu; altfel, la redeschidere folosește data de azi.",
                "Ștergerea unui client șterge și ciornele lui (Invoice Cove îți cere mai întâi confirmarea). Ciornele sunt incluse într-o copie de siguranță.",
                "Ciornele există pentru facturi; ofertele nu au.",
            ]),
        ]),
        "invoices": ("Gestionarea facturilor", [
            ("p", "Fila {{nav_invoices}} grupează facturile într-un dosar pentru fiecare client, pe care le poți sorta după "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> sau <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Deschide un dosar ca să vezi facturile lui, sortate după dată, valoare, număr sau stare."),
            ("p", "Fiecare factură are o stare: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (a trecut de scadență), "
                  "{{invoices_status_partially_paid}} (s-a înregistrat un avans), {{invoices_status_paid}} sau "
                  "{{invoices_status_void}}. Atinge o factură ca s-o vezi ({{common_view}}), s-o trimiți din nou ({{common_share}}), s-o marchezi plătită sau anulată, sau s-o ștergi."),
            ("ul", [
                "{{invoices_action_mark_paid}} cere data plății și modul în care s-a plătit (transfer bancar, numerar, card, PayPal sau altul). "
                "După ce o factură este plătită, nu mai poate fi trecută înapoi la neplătită.",
                "{{deposit_record_title}} notează o plată în avans. Factura apare apoi ca {{invoices_status_partially_paid}}, iar avansul nu poate depăși totalul.",
                "{{invoices_action_mark_void}} păstrează factura în evidență, dar o marchează ca anulată. Este de preferat ștergerii, pentru că o factură ștearsă "
                "nu mai poate fi recuperată.",
            ]),
            ("p", "Cu Pro, dosarul unui client poate fi salvat sau partajat și ca ZIP cu PDF-uri, iar toată lista poate fi exportată pentru contabilul tău — vezi "
                  "<a href=\"#export\">Exportul facturilor</a>."),
        ]),
        "export": ("Exportul facturilor (Excel, CSV, ZIP)", [
            ("p", "Disponibil cu Invoice Cove Pro. Atinge pictograma de export (📄) din partea de sus a filei {{nav_invoices}}. Alege ce facturi includ "
                  "cu selectoarele de an și lună ({{invoices_export_all}}, un an sau o lună dintr-un an — sunt oferiți doar anii și lunile în care "
                  "ai facturi), apoi alege ce faci:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — un tabel Excel (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — același tabel ca fișier CSV.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — PDF-urile facturilor într-un singur ZIP, câte un dosar pentru fiecare client.",
                "{{invoices_export_delete}} — șterge definitiv facturile selectate, după două confirmări.",
            ]),
            ("p", "<em>Salvare</em> îți lasă alegerea locului din dispozitiv unde ajunge fișierul; <em>Partajare</em> deschide meniul de partajare Android ca să-l trimiți "
                  "prin email sau într-un mesaj."),
            ("p", "Excel și CSV sunt făcute pentru contabilul tău: implicit, un rând pentru fiecare factură — numărul și datele, numele, numărul, "
                  "codul fiscal, numărul de TVA, numărul de la registrul comerțului și adresa clientului, subtotalul, reducerea, cota de TVA, valoarea TVA și totalul "
                  "facturii, moneda, precum și starea, data și metoda plății. Titlurile coloanelor și cuvintele fixe (factură, plătit, neplătit, metode de plată) sunt "
                  "scrise în limba în care este setată aplicația."),
            ("p", "Ca să obții un rând pentru fiecare articol de pe factură, cu datele facturii repetate pe fiecare rând și cu descrierea, cantitatea, "
                  "unitatea, prețul și valoarea netă ale fiecărui articol adăugate, activează {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Crearea unei oferte", [
            ("p", "Caseta {{home_new_quote_title}} funcționează ca Factură nouă: aceleași câmpuri, aceleași butoane {{common_preview_button}} și {{common_template_button}}, același "
                  "{{newquote_generate_button}} care salvează, creează PDF-ul și deschide meniul de partajare dintr-o atingere, dar cu o "
                  "{{newquote_date_label}} și o dată {{newquote_valid_until_label}} în locul datei facturii și al scadenței."),
            ("p", "Ofertele nu au ciorne."),
        ]),
        "quotes": ("Gestionarea ofertelor și transformarea în factură", [
            ("p", "Ecranul {{common_quotes_title}} (din caseta de pe ecranul principal) listează ofertele pe clienți, la fel ca Facturile. Deschide o ofertă ca s-o "
                  "vezi sau s-o partajezi, folosește {{quotes_action_accept}} sau {{quotes_action_decline}} când clientul răspunde, "
                  "înregistrează un avans sau șterge-o. Avansul nu poate depăși totalul ofertei."),
            ("p", "Când un client acceptă o ofertă, folosește {{quotes_action_convert_to_invoice}} ca să transformi articolele bifate într-o factură reală, "
                  "editabilă independent. Scadența și reducerea pot fi încă ajustate, iar oferta inițială este marcată "
                  "{{quotes_status_converted}} și păstrată în evidența ta."),
        ]),
        "calendar": ("Calendar și mementouri", [
            ("p", "Ecranul {{calendar_title}} este o vedere lunară pentru notele tale. Atinge o zi ca să vezi sau să adaugi note; o notă are un titlu și un text și, "
                  "cu {{calendar_remind_me}} și o oră, îți trimite o notificare la data și ora stabilite. Prima zi a săptămânii urmează setările tale."),
            ("p", "Separat, Invoice Cove trimite mementouri de plată — notificări locale pentru facturile care se apropie de scadență sau au depășit-o. Nu se trimite nimic către sau de la un server."),
        ]),
        "reports": ("Rapoarte", [
            ("p", "{{common_reports_title}} îți dă o privire de ansamblu rapidă: sumele {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} și {{reports_stat_overdue}}, câte facturi ai, "
                  "<em>{{reports_revenue_by_month}}</em> și <em>{{reports_top_customers}}</em> după totalul facturat."),
            ("p", "Atinge cardul {{reports_stat_outstanding}} sau {{reports_stat_overdue}} ca să deschizi lista exact a acelor facturi."),
        ]),
        "settings": ("Detaliile firmei și setări", [
            ("p", "Deschide setările din pictograma roată; acest ecran se numește {{settings_title}}. Începe cu preferințele tale opționale: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} sau {{settings_theme_dark}}), "
                  "{{settings_invoice_template_label}} implicit, {{settings_tax_label_label}} (TVA, GST…), "
                  "{{settings_first_day_of_week_label}} și {{settings_due_date_default_label}}, care completează automat scadența (de exemplu Net 30). "
                  "Sub ele urmează {{settings_security_label}} (vezi <a href=\"#app-lock\">Blocarea aplicației</a>), "
                  "{{settings_item_suggestions_label}} și {{settings_backup_restore_label}} (vezi <a href=\"#backup\">Copie de siguranță și restaurare</a>)."),
            ("p", "{{settings_item_memory_title}} ține minte descrierile și prețurile articolelor ca să ți le sugereze pe măsură ce scrii; <em>{{common_clear}}</em> le uită, "
                  "fără să-ți atingă facturile."),
            ("p", "Mai jos este profilul firmei tale, tipărit pe fiecare factură și ofertă: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, un scurt slogan ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, {{settings_date_format_label}} pentru date, adresa, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (numărul de înregistrare, capitalul social și altele asemenea), "
                  "{{settings_business_logo_label}} și {{settings_payment_details_label}} (IBAN, link PayPal.me). Fiecare câmp "
                  "are un exemplu, iar orice câmp pe care îl lași necompletat nu apare pe facturile tale. Atinge {{common_done}} când "
                  "ai terminat; dacă ieși cu modificări nesalvate, ți se cere confirmarea."),
            ("p", "La final sunt afișate acest {{settings_user_manual}} și {{settings_share_this_app}}."),
        ]),
        "backup": ("Copie de siguranță și restaurare", [
            ("p", "Disponibil cu Invoice Cove Pro, la {{settings_backup_restore_label}}. {{settings_create_backup_title}} salvează "
                  "tot: facturi, oferte, ciorne, clienți, calendar, setări, logo-ul și PDF-urile, totul într-un singur fișier. Alege "
                  "{{backup_save_button}} ca să-l păstrezi unde vrei sau {{backup_share_button}} ca să-l trimiți într-un loc sigur."),
            ("p", "{{settings_restore_backup_title}} readuce totul, în caz că trebuie să muți datele pe un telefon nou. Funcționează doar pe o instalare proaspătă, înainte să fi "
                  "adăugat date, deci nu poate suprascrie niciodată ce ai deja. Invoice Cove verifică dacă fișierul este intact și îți spune dacă este deteriorat, "
                  "nu este o copie Invoice Cove sau a fost făcut de o versiune mai nouă a aplicației (actualizează mai întâi)."),
            ("note", "Un fișier de backup nu este criptat: oricine îl are poate citi datele tale. Păstrează-l într-un loc privat. PIN-ul de blocare a aplicației nu "
                     "este inclus niciodată în el."),
        ]),
        "app-lock": ("Blocarea aplicației", [
            ("p", "La {{settings_security_label}} poți activa {{settings_app_lock_title}}: Invoice Cove îți cere atunci PIN-ul "
                  "(sau amprenta) când aplicația este deschisă din nou de la zero sau după repornirea telefonului — nu de fiecare dată când revii la ea."),
            ("ul", [
                "{{settings_set_pin}}: alege un PIN de 4 cifre și confirmă-l.",
                "Primești apoi un cod de recuperare de 6 cifre, afișat o singură dată. Notează-l și păstrează-l într-un loc sigur.",
                "Dacă telefonul permite, deblochează cu amprenta ({{security_use_fingerprint}}).",
                "Ai uitat PIN-ul? Folosește {{security_forgot_pin}} și introdu codul de recuperare. După 5 încercări greșite trebuie să aștepți 30 de secunde – "
                "așteptarea crește la mai multe încercări greșite.",
            ]),
            ("note", "Dacă pierzi și PIN-ul, și codul de recuperare și nu ai configurat deblocarea cu amprentă, nu mai există nicio cale de a intra. Nu îl putem reseta "
                     "în locul tău."),
        ]),
        "languages": ("Limbi", [
            ("p", "Invoice Cove vorbește 13 limbi: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands și Svenska. Atinge pictograma rotundă cu steag din partea de sus a setărilor ca să schimbi limba — aplicația se schimbă imediat."),
            ("p", "Textul din PDF-urile tale și din exporturile Excel/CSV urmează limba în care este setată aplicația, iar acest ghid este disponibil în aceleași 13 limbi "
                  "(folosește bara de limbi din partea de sus a paginii)."),
        ]),
        "templates": ("Șabloane PDF", [
            ("p", "Invoice Cove oferă deocamdată 18 modele PDF: Classic, Client Color (colorat cu culoarea clientului), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves și Spooky Hollow."),
            ("p", "Alege șablonul implicit la Setări → {{settings_invoice_template_label}}: atinge un model, apoi {{common_done}}. Se "
                  "aplică tuturor documentelor pe care le generezi de atunci înainte. Pentru o singură factură sau ofertă, folosește butonul {{common_template_button}} "
                  "din formular."),
            ("p", "Fiecare șablon tipărește aceleași informații: datele firmei tale, datele clientului, articolele cu unitatea și data lor, totalurile, notele și "
                  "detaliile de plată — dar doar ce ai completat. Facturile lungi continuă pe o a doua pagină, cu totalul păstrat împreună cu ultimul articol."),
        ]),
        "free-vs-pro": ("Planul gratuit față de Invoice Cove Pro", [
            ("p", "Invoice Cove este gratuit, cu câteva limite rezonabile:"),
            ("ul", [
                "Până la 3 facturi generate pe lună calendaristică",
                "Până la 3 oferte generate pe lună calendaristică",
                "Până la 3 clienți simultan",
                "Numerele facturilor și ofertelor sunt atribuite automat și nu pot fi editate",
                "Exportul Excel, CSV și ZIP este doar Pro",
                "Copia de siguranță și restaurarea este doar Pro",
            ]),
            ("p", "Invoice Cove Pro este o singură achiziție unică prin Google Play (nu un abonament) care elimină definitiv toate aceste limite. "
                  "Ciornele, toate șabloanele și limbile, blocarea aplicației, precum și crearea, previzualizarea și partajarea documentelor sunt gratuite pentru toți. "
                  "Vezi <a href=\"terms.html\">Termenii de utilizare</a> pentru detalii complete."),
        ]),
    },
}
