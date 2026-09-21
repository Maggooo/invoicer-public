T = {
    "title": "Manual de utilizare",
    "subtitle": "Tot ce poate face Invoice Cove, ecran cu ecran.",
    "meta_desc": "Manualul complet de utilizare pentru Invoice Cove - Offline Billing.",
    "lang_label": "Limba",
    "brand_alt": "Invoice Cove",
    "toc": "Cuprins",
    "footer_questions": "Întrebări?",
    "lede": (
        "Invoice Cove funcționează în întregime pe dispozitivul tău — facturile, ofertele, clienții și profilul firmei sunt păstrate local, "
        "nu pe vreun server Invoice Cove. <strong>Nu colectăm, nu vedem și nu primim nicio informație despre facturile tale sau despre modul "
        "în care folosești aplicația</strong> — nu există analiză de utilizare, nu există urmărire, nu se trimite nimic în fundal. "
        "Singura dată când aplicația însăși are nevoie de internet este pentru achiziția unică Invoice Cove Pro, procesată prin Google Play. "
        "Detalii găsești în <a href=\"privacy.html\">Politica de confidențialitate</a> (în engleză)."
    ),
    "warn": (
        "<strong>Înainte să dezinstalezi aplicația sau să-i ștergi datele:</strong> nu păstrăm nicăieri o copie a acestor date. "
        "Dezinstalarea Invoice Cove sau ștergerea spațiului de stocare din setările Android șterge definitiv fiecare factură, ofertă, client "
        "și setare de pe acest dispozitiv — nu există o copie în cloud din care să restaurezi. Protejează-te: fă o copie de siguranță cu "
        "Invoice Cove Pro (vezi <a href=\"#backup\">Copie de siguranță și restaurare</a>) sau exportă ce îți trebuie în Excel, CSV sau ZIP "
        "(vezi <a href=\"#export\">Exportul facturilor</a>)."
    ),
    "sections": {
        "home": ("Ecranul principal", [
            ("p", "Ecranul principal este punctul tău de pornire, cu câte o casetă pentru fiecare acțiune importantă: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> și "
                  "<strong>{{common_reports_title}}</strong>. Atinge o casetă ca să ajungi direct acolo."),
            ("p", "Bara de jos îți oferă mereu acces rapid la <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (o factură nouă), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> și <strong>{{nav_reports}}</strong>."),
            ("p", "Pictograma roată (⚙️) din colțul dreapta-sus al majorității ecranelor deschide <a href=\"#settings\">Detaliile firmei și setările</a>."),
        ]),
        "customers": ("Clienți", [
            ("p", "Adaugă un client din fila <strong>{{nav_customers}}</strong> (atinge pictograma +), din caseta <strong>{{home_new_customer_title}}</strong> "
                  "sau direct în timp ce creezi o factură ori o ofertă. Doar numele este obligatoriu. Câmpuri opționale: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, adresa, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} și o culoare care colorează documentele clientului. Fiecare câmp arată un exemplu, ca să știi ce se completează acolo."),
            ("p", "Atinge un client ca să-l <strong>{{common_edit}}</strong>, să deschizi <strong>{{customers_view_history}}</strong> (facturi, oferte și ciorne) "
                  "sau să-l <strong>{{common_delete}}</strong>."),
            ("p", "Pe facturile și ofertele tale, datele clientului sunt tipărite sub numele lui într-o ordine fixă: numărul de client, codul fiscal, numărul de TVA, "
                  "numărul de la registrul comerțului, apoi adresa, emailul și telefonul. Tot ce lași necompletat pur și simplu nu apare."),
            ("note", "<strong>Salvarea funcționează diferit aici față de facturi.</strong> Un client are propriul buton <strong>{{customers_form_save_customer}}</strong> "
                     "(sau <strong>{{customers_form_save_changes}}</strong> la editare) — se salvează în clipa în care îl atingi. Dacă încerci să închizi formularul "
                     "cu modificări nesalvate, Invoice Cove îți cere mai întâi confirmarea."),
            ("note", "Ștergerea unui client nu șterge facturile și ofertele pe care le-ai emis deja pentru el. <a href=\"#drafts\">Ciornele</a> lui nefinalizate "
                     "se șterg odată cu el — ești întrebat mai întâi."),
        ]),
        "new-invoice": ("Crearea unei facturi", [
            ("p", "Din <strong>{{nav_new}}</strong> (sau din caseta <strong>{{home_new_invoice_title}}</strong>): alege un client — sau creează unul pe loc — "
                  "stabilește data facturii și data scadenței, apoi adaugă articolele."),
            ("p", "Atinge <strong>{{newinvoice_add_item_details_button}}</strong> și completează descrierea, cantitatea, prețul unitar și, opțional, o unitate "
                  "(de exemplu h, buc sau kg) și o dată și o oră. Unitatea este tipărită lângă cantitate în PDF. Atinge creionul (✏️) de pe un articol ca să-l corectezi "
                  "sau coșul de gunoi (🗑️) ca să-l ștergi. Descrierile și prețurile folosite înainte îți sunt sugerate pe măsură ce scrii."),
            ("p", "Apoi adaugă, dacă ai nevoie, o cotă de taxă, o <strong>{{newinvoice_discount_label}}</strong> (procent sau sumă fixă) și "
                  "<strong>{{common_notes_label}}</strong>. Numărul facturii este atribuit automat (cu Pro îl poți edita); moneda se alege lângă el."),
            ("p", "<strong>{{common_preview_button}}</strong> generează un PDF temporar ca să vezi cum arată — nu se salvează nimic. "
                  "Butonul <strong>{{common_template_button}}</strong> arată ce șablon va fi folosit; atinge-l ca să alegi altul doar pentru acest document."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> face trei lucruri deodată: salvează factura, creează PDF-ul și deschide meniul de partajare al "
                     "dispozitivului ca să o poți trimite. Nu ești gata? Folosește <strong>{{newinvoice_save_draft_button}}</strong> — vezi <a href=\"#drafts\">Ciorne</a>."),
        ]),
        "drafts": ("Ciorne", [
            ("p", "Nu pierzi o factură la care încă lucrezi. De îndată ce ai ales un client și ai adăugat cel puțin un articol sau o notă, Invoice Cove "
                  "păstrează o <strong>ciornă</strong> și o actualizează la scurt timp după ce nu mai scrii — și încă o dată când părăsești aplicația. Nu există "
                  "întrebarea „renunți la modificări?” când ieși din ecran; un mesaj scurt te anunță că ciorna a fost salvată."),
            ("p", "Atinge <strong>{{newinvoice_save_draft_button}}</strong> (sub {{newinvoice_generate_button}}) ca să pui factura deoparte intenționat: se salvează, iar "
                  "formularul se golește, gata pentru următoarea factură. Funcționează de îndată ce ai ales un client, chiar înainte să adaugi articole."),
            ("p", "Ciornele le găsești la <strong>{{nav_customers}}</strong> → clientul → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Fiecare ciornă arată când a fost modificată ultima dată, câte articole are și totalul. Atinge-o ca să "
                  "continui editarea sau ca să generezi factura; atinge coșul de gunoi ca s-o ștergi."),
            ("ul", [
                "O ciornă nu folosește niciodată un număr de factură și nu se numără în limita lunară gratuită. Numărul se atribuie abia când generezi factura "
                "finală — ciorna este atunci înlocuită de ea.",
                "O ciornă păstrează data facturii și data scadenței doar dacă le-ai ales tu; altfel, la redeschidere folosește data de azi.",
                "Ștergerea unui client șterge și ciornele lui (ești întrebat mai întâi). Ciornele sunt incluse într-o copie de siguranță.",
                "Ciornele există pentru facturi; ofertele nu au.",
            ]),
        ]),
        "invoices": ("Gestionarea facturilor", [
            ("p", "Fila <strong>{{nav_invoices}}</strong> grupează facturile într-un dosar pentru fiecare client, pe care le poți sorta după "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> sau <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Deschide un dosar ca să vezi facturile lui, sortate după dată, valoare, număr sau stare."),
            ("p", "Fiecare factură are o stare: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (a trecut de scadență), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (s-a înregistrat un avans), <strong>{{invoices_status_paid}}</strong> sau "
                  "<strong>{{invoices_status_void}}</strong>. Atinge o factură ca s-o vezi ({{common_view}}), s-o trimiți din nou ({{common_share}}), s-o marchezi plătită sau anulată, sau s-o ștergi."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> cere data plății și modul în care s-a plătit (transfer bancar, numerar, card, PayPal sau altul). "
                "După ce o factură este plătită, nu mai poate fi trecută înapoi la neplătită.",
                "<strong>{{deposit_record_title}}</strong> notează o plată în avans. Factura apare apoi ca <strong>{{invoices_status_partially_paid}}</strong>, iar avansul nu poate depăși totalul.",
                "<strong>{{invoices_action_mark_void}}</strong> păstrează factura în evidență, dar o marchează ca anulată. Preferă asta ștergerii — o factură ștearsă "
                "nu mai poate fi recuperată.",
            ]),
            ("p", "Cu Pro, dosarul unui client poate fi salvat sau partajat și ca ZIP cu PDF-uri, iar toată lista poate fi exportată pentru contabilul tău — vezi "
                  "<a href=\"#export\">Exportul facturilor</a>."),
        ]),
        "export": ("Exportul facturilor (Excel, CSV, ZIP)", [
            ("p", "Disponibil cu Invoice Cove Pro. Atinge pictograma de export (📄) din partea de sus a filei <strong>{{nav_invoices}}</strong>. Alege ce facturi includ "
                  "cu selectoarele de an și lună (<strong>{{invoices_export_all}}</strong>, un an sau o lună dintr-un an — sunt oferiți doar anii și lunile în care "
                  "ai facturi), apoi alege ce faci:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — un tabel Excel (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — același tabel ca fișier CSV.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — PDF-urile facturilor într-un singur ZIP, câte un dosar pentru fiecare client.",
                "<strong>{{invoices_export_delete}}</strong> — șterge definitiv facturile selectate, după două confirmări.",
            ]),
            ("p", "<em>Salvare</em> îți lasă alegerea locului din dispozitiv unde ajunge fișierul; <em>Partajare</em> deschide meniul de partajare Android ca să-l trimiți "
                  "prin email sau într-un chat."),
            ("p", "Excel și CSV sunt făcute pentru contabilul tău: <strong>un rând pentru fiecare articol de pe factură</strong>, cu datele facturii repetate pe fiecare rând — "
                  "numărul și datele, numele, numărul, codul fiscal, numărul de TVA, numărul de la registrul comerțului și adresa clientului, descrierea, cantitatea, unitatea, "
                  "prețul și valoarea netă a articolului, subtotalul, reducerea, cota de TVA, valoarea TVA și totalul facturii, moneda, precum și starea, data și "
                  "metoda plății. Titlurile coloanelor și cuvintele fixe (factură, plătit, neplătit, metode de plată) sunt scrise în limba în care este setată aplicația."),
        ]),
        "new-quote": ("Crearea unei oferte", [
            ("p", "<strong>{{home_new_quote_title}}</strong> funcționează ca New Invoice — aceleași câmpuri, aceleași butoane <strong>{{common_preview_button}}</strong> și <strong>{{common_template_button}}</strong> și același "
                  "<strong>{{newquote_generate_button}}</strong> care salvează, creează PDF-ul și deschide meniul de partajare dintr-o atingere — cu o "
                  "<strong>{{newquote_date_label}}</strong> și o dată <strong>{{newquote_valid_until_label}}</strong> în locul datei facturii și al scadenței. "
                  "Ofertele nu au ciorne."),
        ]),
        "quotes": ("Gestionarea ofertelor și transformarea în factură", [
            ("p", "Ecranul <strong>{{common_quotes_title}}</strong> (din caseta de pe ecranul principal) listează ofertele pe clienți, la fel ca Facturile. Deschide o ofertă ca s-o "
                  "vezi sau s-o partajezi, folosește <strong>{{quotes_action_accept}}</strong> sau <strong>{{quotes_action_decline}}</strong> când clientul răspunde, "
                  "înregistrează un avans sau șterge-o. Avansul nu poate depăși totalul ofertei."),
            ("p", "Când un client acceptă o ofertă, folosește <strong>{{quotes_action_convert_to_invoice}}</strong> ca să transformi articolele bifate într-o factură reală, "
                  "editabilă independent — scadența și reducerea pot fi încă ajustate, iar oferta inițială este marcată "
                  "<strong>{{quotes_status_converted}}</strong> și păstrată în evidența ta."),
        ]),
        "calendar": ("Calendar și mementouri", [
            ("p", "Ecranul <strong>{{calendar_title}}</strong> este o vedere lunară pentru notele tale. Atinge o zi ca să vezi sau să adaugi note; o notă are un titlu și un text și, "
                  "cu <strong>{{calendar_remind_me}}</strong> și o oră, îți trimite o notificare în acel moment. Prima zi a săptămânii urmează setarea ta."),
            ("p", "Separat, Invoice Cove trimite mementouri de plată — notificări locale pentru facturile care se apropie de scadență sau au depășit-o. Nu se trimite nimic către sau de la un server."),
        ]),
        "reports": ("Rapoarte", [
            ("p", "<strong>{{common_reports_title}}</strong> îți dă o privire de ansamblu rapidă: sumele <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> și <strong>{{reports_stat_overdue}}</strong>, câte facturi ai, "
                  "<em>{{reports_revenue_by_month}}</em> și <em>{{reports_top_customers}}</em> după totalul facturat."),
            ("p", "Atinge cardul <strong>{{reports_stat_outstanding}}</strong> sau <strong>{{reports_stat_overdue}}</strong> ca să deschizi lista exact a acelor facturi."),
        ]),
        "settings": ("Detaliile firmei și setări", [
            ("p", "Deschide setările din pictograma roată — ecranul se numește <strong>{{settings_title}}</strong>. Începe cu preferințele tale: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} sau {{settings_theme_dark}}), "
                  "<strong>{{settings_invoice_template_label}}</strong> implicit, <strong>{{settings_tax_label_label}}</strong> (TVA, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> și <strong>{{settings_due_date_default_label}}</strong> (completează automat scadența, de exemplu Net 30). "
                  "Sub ele urmează <strong>{{settings_security_label}}</strong> (vezi <a href=\"#app-lock\">Blocarea aplicației</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> și <strong>{{settings_backup_restore_label}}</strong> (vezi <a href=\"#backup\">Copie de siguranță și restaurare</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> ține minte descrierile și prețurile articolelor ca să ți le sugereze pe măsură ce scrii; <em>{{common_clear}}</em> le uită, "
                  "fără să-ți atingă facturile."),
            ("p", "Mai jos este profilul firmei tale, tipărit pe fiecare factură și ofertă: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, un scurt slogan (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, <strong>{{settings_date_format_label}}</strong> pentru date, adresa, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (numărul de înregistrare, capitalul social și altele asemenea), "
                  "<strong>{{settings_business_logo_label}}</strong> și <strong>{{settings_payment_details_label}}</strong> (IBAN, link PayPal.me…). Fiecare câmp "
                  "are un exemplu, iar <strong>orice câmp pe care îl lași necompletat pur și simplu nu apare pe facturile tale</strong>. Atinge <strong>{{common_done}}</strong> când "
                  "termini; dacă ieși cu modificări nesalvate, ești întrebat mai întâi."),
            ("p", "La final: acest <strong>{{settings_user_manual}}</strong> și <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Copie de siguranță și restaurare", [
            ("p", "Disponibil cu Invoice Cove Pro. La <strong>{{settings_backup_restore_label}}</strong>, <strong>{{settings_create_backup_title}}</strong> salvează "
                  "tot — facturi, oferte, ciorne, clienți, calendar, setări, logo-ul și PDF-urile — într-un singur fișier. Alege "
                  "<strong>{{backup_save_button}}</strong> ca să-l păstrezi unde vrei sau <strong>{{backup_share_button}}</strong> ca să-l trimiți într-un loc sigur."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> readuce totul — de exemplu pe un telefon nou. Funcționează doar pe o instalare proaspătă, înainte să fi "
                  "adăugat date, deci nu poate suprascrie niciodată ce ai deja. Invoice Cove verifică dacă fișierul este intact și îți spune dacă este deteriorat, "
                  "nu este o copie Invoice Cove sau a fost făcut de o versiune mai nouă a aplicației (actualizează mai întâi)."),
            ("note", "Un fișier de backup <strong>nu este criptat</strong>: oricine îl are poate citi datele tale. Păstrează-l într-un loc privat. PIN-ul de blocare a aplicației nu "
                     "este inclus niciodată în el."),
        ]),
        "app-lock": ("Blocarea aplicației", [
            ("p", "La <strong>{{settings_security_label}}</strong> poți activa <strong>{{settings_app_lock_title}}</strong>: Invoice Cove îți cere atunci PIN-ul "
                  "(sau amprenta) când aplicația este deschisă din nou de la zero sau după repornirea telefonului — nu de fiecare dată când revii la ea."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: alege un PIN de 4 cifre și confirmă-l.",
                "Primești apoi un <strong>cod de recuperare</strong> de 6 cifre, afișat o singură dată. Notează-l și păstrează-l într-un loc sigur.",
                "Dacă telefonul permite, deblochează cu amprenta (<strong>{{security_use_fingerprint}}</strong>).",
                "Ai uitat PIN-ul? Folosește <strong>{{security_forgot_pin}}</strong> și introdu codul de recuperare. După 5 încercări greșite trebuie să aștepți 30 de secunde; "
                "așteptarea crește la mai multe încercări greșite.",
            ]),
            ("note", "Dacă pierzi și PIN-ul, și codul de recuperare — și nu ai configurat deblocarea cu amprentă — nu mai există nicio cale de a intra. Nu îl putem reseta "
                     "în locul tău."),
        ]),
        "languages": ("Limbi", [
            ("p", "Invoice Cove vorbește 13 limbi: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands și Svenska. Atinge pictograma rotundă cu steag din partea de sus a setărilor ca să schimbi limba — aplicația se schimbă imediat."),
            ("p", "Textul din PDF-urile tale și din exporturile Excel/CSV urmează limba în care este setată aplicația, iar acest manual este disponibil în aceleași 13 limbi "
                  "(folosește bara de limbi din partea de sus a paginii)."),
        ]),
        "templates": ("Șabloane PDF", [
            ("p", "Invoice Cove vine cu 18 modele PDF: Classic, Client Color (colorat cu culoarea clientului), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves și Spooky Hollow."),
            ("p", "Alege șablonul implicit la Setări → <strong>{{settings_invoice_template_label}}</strong>: atinge un model, apoi <strong>{{common_done}}</strong>. Se "
                  "aplică tuturor documentelor pe care le generezi de atunci înainte. Pentru o singură factură sau ofertă, folosește butonul <strong>{{common_template_button}}</strong> "
                  "din formular."),
            ("p", "Fiecare șablon tipărește aceleași informații — datele firmei tale, datele clientului, articolele cu unitatea și data lor, totalurile, notele și "
                  "detaliile de plată — dar doar ce ai completat. Facturile lungi continuă pe o a doua pagină, cu totalul păstrat împreună cu ultimul articol."),
        ]),
        "free-vs-pro": ("Planul gratuit față de Invoice Cove Pro", [
            ("p", "Invoice Cove este gratuit, cu câteva limite rezonabile:"),
            ("ul", [
                "Până la 3 facturi și 3 oferte generate pe lună calendaristică",
                "Până la 3 clienți simultan",
                "Numerele facturilor și ofertelor sunt atribuite automat și nu pot fi editate",
                "Exportul Excel, CSV și ZIP este doar Pro",
                "Copia de siguranță și restaurarea este doar Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> este o singură achiziție unică prin Google Play — nu un abonament — care elimină definitiv toate aceste limite. "
                  "Ciornele, toate șabloanele și limbile, blocarea aplicației, precum și crearea, previzualizarea și partajarea documentelor sunt gratuite pentru toți. "
                  "Vezi <a href=\"terms.html\">Termenii de utilizare</a> (în engleză) pentru detalii complete."),
        ]),
    },
}
