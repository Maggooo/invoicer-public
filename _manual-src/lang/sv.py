T = {
    "title": "Användarhandbok",
    "subtitle": "Allt Invoice Cove kan göra, skärm för skärm.",
    "meta_desc": "Komplett användarhandbok för appen Invoice Cove - Offline Billing.",
    "lang_label": "Språk",
    "brand_alt": "Invoice Cove",
    "toc": "Innehåll",
    "footer_questions": "Frågor?",
    "lede": (
        "Invoice Cove fungerar helt på din enhet — dina fakturor, offerter, kunder och företagsuppgifter lagras lokalt, "
        "inte på någon Invoice Cove-server. <strong>Vi samlar inte in, ser eller tar emot några uppgifter om dina fakturor eller om hur du använder appen</strong> "
        "— ingen analys, ingen spårning, inget skickas i bakgrunden. "
        "Den enda gången själva appen behöver internet är när engångsköpet av Invoice Cove Pro behandlas via Google Play. "
        "Detaljer finns i <a href=\"privacy.html\">Integritetspolicyn</a> (på engelska)."
    ),
    "warn": (
        "<strong>Innan du avinstallerar appen eller rensar dess lagring:</strong> vi säkerhetskopierar inte dessa uppgifter någonstans. "
        "Om du avinstallerar Invoice Cove eller rensar dess lagring i Androids inställningar raderas alla fakturor, offerter, kunder "
        "och inställningar på den här enheten permanent — det finns ingen molnkopia att återställa från. Skydda dig: skapa en säkerhetskopia "
        "med Invoice Cove Pro (se <a href=\"#backup\">Säkerhetskopiering och återställning</a>) eller exportera det du behöver till Excel, CSV eller ZIP "
        "(se <a href=\"#export\">Exportera fakturor</a>)."
    ),
    "sections": {
        "home": ("Startskärm", [
            ("p", "Startskärmen är din utgångspunkt, med en ruta för varje huvudåtgärd: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> och "
                  "<strong>{{common_reports_title}}</strong>. Tryck på en ruta för att gå dit direkt."),
            ("p", "Fältet längst ned ger dig alltid snabb åtkomst till <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (ny faktura), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> och <strong>{{nav_reports}}</strong>."),
            ("p", "Kugghjulsikonen (⚙️) uppe till höger på de flesta skärmar öppnar <a href=\"#settings\">Företagsuppgifter och inställningar</a>."),
        ]),
        "customers": ("Kunder", [
            ("p", "Lägg till en kund på fliken <strong>{{nav_customers}}</strong> (tryck på +-ikonen), med rutan <strong>{{home_new_customer_title}}</strong> "
                  "eller direkt när du skapar en faktura eller offert. Bara namnet är obligatoriskt. Valfria fält: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, adress, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} och en färg som färgsätter kundens dokument. Varje fält visar ett exempel så att det är tydligt vad som ska stå där."),
            ("p", "Tryck på en kund för att redigera den (<strong>{{common_edit}}</strong>), öppna dess <strong>{{customers_view_history}}</strong> (fakturor, offerter och utkast) "
                  "eller ta bort den (<strong>{{common_delete}}</strong>)."),
            ("p", "På dina fakturor och offerter skrivs kunduppgifterna ut under namnet i en fast ordning: kundnummer, skatte-ID, momsregistreringsnummer, "
                  "handelsregisternummer, därefter adress, e-post och telefon. Det du inte fyller i skrivs helt enkelt inte ut."),
            ("note", "<strong>Sparandet fungerar annorlunda här än för fakturor.</strong> En kund har en egen knapp <strong>{{customers_form_save_customer}}</strong> "
                     "(vid redigering <strong>{{customers_form_save_changes}}</strong>) — den sparas i samma stund som du trycker på den. Om du försöker stänga formuläret "
                     "med osparade ändringar ber Invoice Cove först om bekräftelse."),
            ("note", "Att ta bort en kund tar inte bort de fakturor och offerter du redan har skapat åt kunden. Kundens ofärdiga <a href=\"#drafts\">utkast</a> "
                     "tas däremot bort tillsammans med kunden — appen frågar dig först."),
        ]),
        "new-invoice": ("Skapa en faktura", [
            ("p", "På <strong>{{nav_new}}</strong> (eller via rutan <strong>{{home_new_invoice_title}}</strong>): välj en kund — eller skapa en direkt — "
                  "ange fakturadatum och förfallodatum och lägg sedan till rader."),
            ("p", "Tryck på <strong>{{newinvoice_add_item_details_button}}</strong> och fyll i beskrivning, antal, pris per enhet och vid behov enhet "
                  "(t.ex. tim, st eller kg) samt datum och tid. Enheten skrivs ut bredvid antalet i PDF:en. Med pennan (✏️) vid en rad rättar du den, "
                  "med papperskorgen (🗑️) tar du bort den. Tidigare använda beskrivningar och priser föreslås medan du skriver."),
            ("p", "Lägg sedan efter behov till en skattesats, <strong>{{newinvoice_discount_label}}</strong> (procent eller fast belopp) och "
                  "<strong>{{common_notes_label}}</strong>. Fakturanumret tilldelas automatiskt (med Pro kan du ändra det); välj valuta bredvid."),
            ("p", "<strong>{{common_preview_button}}</strong> skapar en tillfällig PDF så att du ser hur den ser ut — ingenting sparas ännu. "
                  "Knappen <strong>{{common_template_button}}</strong> visar vilken mall som används; tryck på den för att välja en annan bara för det här dokumentet."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> gör tre saker på en gång: sparar fakturan, skapar PDF:en och öppnar enhetens "
                     "delningsmeny så att du kan skicka den. Inte klar än? Använd <strong>{{newinvoice_save_draft_button}}</strong> — se <a href=\"#drafts\">Utkast</a>."),
        ]),
        "drafts": ("Utkast", [
            ("p", "En faktura du fortfarande arbetar på försvinner inte. Så snart du väljer en kund och lägger till minst en rad eller anteckning behåller Invoice Cove "
                  "ett <strong>utkast</strong> och uppdaterar det en stund efter att du slutat skriva — och en gång till när du lämnar appen. När du lämnar skärmen visas "
                  "ingen fråga om att ”kasta ändringar?”; ett kort meddelande talar om att utkastet har sparats."),
            ("p", "Tryck på <strong>{{newinvoice_save_draft_button}}</strong> (under {{newinvoice_generate_button}}) för att medvetet lägga en faktura åt sidan: den sparas och "
                  "formuläret töms, redo för nästa faktura. Det fungerar så snart en kund är vald, även innan du lagt till rader."),
            ("p", "Du hittar utkasten under <strong>{{nav_customers}}</strong> → kund → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Varje utkast visar när det senast ändrades, hur många rader det har och totalbeloppet. Tryck på det för att "
                  "fortsätta redigera eller skapa fakturan; papperskorgen tar bort det."),
            ("ul", [
                "Ett utkast använder aldrig ett fakturanummer och räknas inte mot den kostnadsfria månadsgränsen. Numret tilldelas först när du skapar den slutliga "
                "fakturan — utkastet ersätts då av den.",
                "Ett utkast minns fakturadatum och förfallodatum bara om du själv valt dem; annars används dagens datum när du öppnar det igen.",
                "Om du tar bort en kund tas även dess utkast bort (appen frågar dig först). Utkast ingår i säkerhetskopian.",
                "Utkast finns för fakturor; offerter har inga.",
            ]),
        ]),
        "invoices": ("Hantera fakturor", [
            ("p", "Fliken <strong>{{nav_invoices}}</strong> grupperar fakturor i en mapp per kund, som du kan sortera efter "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> eller <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Öppna en mapp för att se dess fakturor, sorterade efter datum, värde, nummer eller status."),
            ("p", "Varje faktura har en status: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (efter förfallodatum), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (en handpenning har registrerats), <strong>{{invoices_status_paid}}</strong> eller "
                  "<strong>{{invoices_status_void}}</strong>. Tryck på en faktura för att visa den ({{common_view}}), skicka den igen ({{common_share}}), markera den som betald eller makulerad eller ta bort den."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> frågar efter betalningsdatum och betalsätt (överföring, kontant, kort, PayPal eller annat). "
                "En betald faktura kan inte sättas tillbaka till obetald.",
                "<strong>{{deposit_record_title}}</strong> registrerar en förskottsbetalning. Fakturan visas då som <strong>{{invoices_status_partially_paid}}</strong> och handpenningen får inte överstiga totalen.",
                "<strong>{{invoices_action_mark_void}}</strong> behåller fakturan i din bokföring men markerar den som annullerad. Välj hellre detta än att ta bort — en borttagen faktura "
                "kan inte återställas.",
            ]),
            ("p", "Med Pro kan du också spara eller dela en kunds mapp som ZIP med PDF:erna och exportera hela listan till din revisor — se "
                  "<a href=\"#export\">Exportera fakturor</a>."),
        ]),
        "export": ("Exportera fakturor (Excel, CSV, ZIP)", [
            ("p", "Tillgängligt med Invoice Cove Pro. Tryck på exportikonen (📄) högst upp på fliken <strong>{{nav_invoices}}</strong>. Välj vilka fakturor som ska tas med "
                  "med år- och månadsväljaren (<strong>{{invoices_export_all}}</strong>, ett år eller en månad i ett år — bara år och månader "
                  "där det finns fakturor erbjuds) och välj sedan vad du vill göra med dem:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — ett Excel-kalkylblad (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — samma tabell som en CSV-fil.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — fakturornas PDF:er i en ZIP, med en mapp per kund.",
                "<strong>{{invoices_export_delete}}</strong> — tar permanent bort de valda fakturorna efter två bekräftelser.",
            ]),
            ("p", "Med <em>Spara</em> väljer du var på enheten filen hamnar; <em>Dela</em> öppnar Androids delningsmeny så att du kan skicka den "
                  "via e-post eller i en chatt."),
            ("p", "Excel och CSV är gjorda för din revisor: <strong>en rad per fakturarad</strong>, där fakturauppgifterna upprepas på varje rad — "
                  "nummer och datum, kundens namn, nummer, skatte-ID, momsregistreringsnummer, handelsregisternummer och adress, beskrivning, antal, enhet, "
                  "radens pris och nettobelopp, delsumma, rabatt, momssats, momsbelopp och fakturans totalbelopp, valuta och status, betalningsdatum och "
                  "betalsätt. Kolumnrubrikerna och de fasta orden (faktura, betald, obetald, betalsätt) står på det språk som appen är inställd på."),
        ]),
        "new-quote": ("Skapa en offert", [
            ("p", "<strong>{{home_new_quote_title}}</strong> fungerar som New Invoice — samma fält, samma knappar <strong>{{common_preview_button}}</strong> och <strong>{{common_template_button}}</strong> och samma "
                  "<strong>{{newquote_generate_button}}</strong>, som med ett tryck sparar, skapar PDF:en och öppnar delningsmenyn — med "
                  "<strong>{{newquote_date_label}}</strong> och ett datum <strong>{{newquote_valid_until_label}}</strong> i stället för fakturadatum och förfallodatum. "
                  "Offerter har inga utkast."),
        ]),
        "quotes": ("Hantera offerter och omvandla till faktura", [
            ("p", "Skärmen <strong>{{common_quotes_title}}</strong> (via rutan på startskärmen) listar offerter per kund, precis som fakturor. Öppna en offert för att "
                  "visa eller dela den, använd <strong>{{quotes_action_accept}}</strong> eller <strong>{{quotes_action_decline}}</strong> när kunden svarar, "
                  "registrera en handpenning eller ta bort den. En handpenning får inte överstiga offertens totalbelopp."),
            ("p", "När kunden godkänner offerten använder du <strong>{{quotes_action_convert_to_invoice}}</strong> och de ikryssade raderna omvandlas till en riktig faktura, "
                  "som du kan redigera separat — förfallodatum och rabatt kan fortfarande ändras, och den ursprungliga offerten markeras som "
                  "<strong>{{quotes_status_converted}}</strong> och finns kvar i din bokföring."),
        ]),
        "calendar": ("Kalender och påminnelser", [
            ("p", "Skärmen <strong>{{calendar_title}}</strong> är en månadsvy för dina egna anteckningar. Tryck på en dag för att se eller lägga till anteckningar; en anteckning har en titel och text och "
                  "skickar dig med alternativet <strong>{{calendar_remind_me}}</strong> och en tid en avisering vid just det tillfället. Veckans första dag följer din inställning."),
            ("p", "Separat skickar Invoice Cove betalningspåminnelser — lokala aviseringar om fakturor som snart förfaller eller redan har förfallit. Ingenting skickas till eller tas emot från en server."),
        ]),
        "reports": ("Rapporter", [
            ("p", "<strong>{{common_reports_title}}</strong> ger dig en snabb överblick: beloppen <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> och <strong>{{reports_stat_overdue}}</strong>, antalet fakturor, "
                  "<em>{{reports_revenue_by_month}}</em> och dina <em>{{reports_top_customers}}</em> efter fakturerat belopp."),
            ("p", "Tryck på kortet <strong>{{reports_stat_outstanding}}</strong> eller <strong>{{reports_stat_overdue}}</strong> för att öppna en lista över exakt de fakturorna."),
        ]),
        "settings": ("Företagsuppgifter och inställningar", [
            ("p", "Öppna inställningarna med kugghjulsikonen — skärmen heter <strong>{{settings_title}}</strong>. Den börjar med dina preferenser: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} eller {{settings_theme_dark}}), standard-"
                  "<strong>{{settings_invoice_template_label}}</strong>, <strong>{{settings_tax_label_label}}</strong> (moms, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> och <strong>{{settings_due_date_default_label}}</strong> (fyller i förfallodatum automatiskt, t.ex. Net 30). "
                  "Under dem följer <strong>{{settings_security_label}}</strong> (se <a href=\"#app-lock\">Applås</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> och <strong>{{settings_backup_restore_label}}</strong> (se <a href=\"#backup\">Säkerhetskopiering och återställning</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> minns radernas beskrivningar och priser för att föreslå dem medan du skriver; <em>{{common_clear}}</em> glömmer dem, "
                  "utan att röra dina fakturor."),
            ("p", "Längre ned finns ditt företags profil som skrivs ut på varje faktura och offert: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, en kort slogan (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, <strong>{{settings_date_format_label}}</strong> för datum, adress, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (registreringsnummer, aktiekapital och liknande), "
                  "<strong>{{settings_business_logo_label}}</strong> och <strong>{{settings_payment_details_label}}</strong> (IBAN, PayPal.me-länk…). Varje fält "
                  "har ett exempel och <strong>varje fält du lämnar tomt visas helt enkelt inte på dina fakturor</strong>. Tryck på <strong>{{common_done}}</strong> när du är klar; "
                  "om du lämnar med osparade ändringar frågar appen först."),
            ("p", "Allra längst ned: den här <strong>{{settings_user_manual}}</strong> och <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Säkerhetskopiering och återställning", [
            ("p", "Tillgängligt med Invoice Cove Pro. Under <strong>{{settings_backup_restore_label}}</strong> sparar <strong>{{settings_create_backup_title}}</strong> "
                  "allt — fakturor, offerter, utkast, kunder, kalender, inställningar, logotyp och PDF:er — i en enda fil. Välj "
                  "<strong>{{backup_save_button}}</strong> för att spara den var du vill, eller <strong>{{backup_share_button}}</strong> för att skicka den till en säker plats."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> lägger tillbaka allt — till exempel på en ny telefon. Det fungerar bara på en nyinstallation, så länge du inte lagt till "
                  "några uppgifter, så det kan aldrig skriva över det du redan har. Invoice Cove kontrollerar att filen är hel och varnar dig om den är skadad, "
                  "inte är en Invoice Cove-säkerhetskopia eller skapades av en nyare version av appen (uppdatera först)."),
            ("note", "Säkerhetskopian är <strong>inte krypterad</strong>: den som har den kan läsa dina uppgifter. Förvara den på en privat plats. Applåsets PIN-kod ingår aldrig "
                     "i den."),
        ]),
        "app-lock": ("Applås", [
            ("p", "Under <strong>{{settings_security_label}}</strong> kan du slå på <strong>{{settings_app_lock_title}}</strong>: Invoice Cove ber då om en PIN-kod "
                  "(eller fingeravtryck) när appen öppnas från början eller efter att telefonen startats om — inte vid varje återkomst till den."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: välj en fyrsiffrig PIN-kod och bekräfta den.",
                "Därefter får du en sexsiffrig <strong>återställningskod</strong> som bara visas en gång. Skriv ned den och förvara den på en säker plats.",
                "Om din telefon stöder det kan du låsa upp med fingeravtryck (<strong>{{security_use_fingerprint}}</strong>).",
                "Glömt PIN-koden? Använd <strong>{{security_forgot_pin}}</strong> och ange återställningskoden. Efter 5 felaktiga försök måste du vänta 30 sekunder; "
                "väntetiden förlängs vid fler felaktiga försök.",
            ]),
            ("note", "Om du tappar både PIN-koden och återställningskoden — och inte har ställt in fingeravtrycksupplåsning — går det inte att komma in igen. Vi kan inte återställa den åt "
                     "dig."),
        ]),
        "languages": ("Språk", [
            ("p", "Invoice Cove talar 13 språk: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands och Svenska. Tryck på den runda flaggikonen högst upp i inställningarna så byts språket — appen växlar direkt."),
            ("p", "Texten i dina PDF:er och i exporterna till Excel/CSV följer det språk som appen är inställd på, och den här handboken finns på samma 13 språk "
                  "(använd språkfältet högst upp på sidan)."),
        ]),
        "templates": ("PDF-mallar", [
            ("p", "Invoice Cove innehåller 18 PDF-design: Classic, Client Color (i kundens färg), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves och Spooky Hollow."),
            ("p", "Välj standardmall under Inställningar → <strong>{{settings_invoice_template_label}}</strong>: tryck på en design och sedan på <strong>{{common_done}}</strong>. Den gäller "
                  "för allt du skapar från och med då. För en enskild faktura eller offert använder du knappen <strong>{{common_template_button}}</strong> "
                  "i formuläret."),
            ("p", "Varje mall skriver ut samma information — dina företagsuppgifter, kundens, rader med enhet och datum, summor, anteckningar och "
                  "betalningsuppgifter — men bara det du har fyllt i. Långa fakturor fortsätter på en andra sida och totalen följer med den sista raden."),
        ]),
        "free-vs-pro": ("Gratisversion och Invoice Cove Pro", [
            ("p", "Invoice Cove är gratis, med några rimliga begränsningar:"),
            ("ul", [
                "Upp till 3 fakturor och 3 offerter per kalendermånad",
                "Upp till 3 kunder åt gången",
                "Faktura- och offertnummer tilldelas automatiskt och kan inte ändras",
                "Export till Excel, CSV och ZIP finns bara med Pro",
                "Säkerhetskopiering och återställning finns bara med Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> är ett enda engångsköp via Google Play — inte en prenumeration — som tar bort alla dessa begränsningar för alltid. "
                  "Utkast, alla mallar och språk, applåset samt att skapa, förhandsvisa och dela dokument är gratis för alla. "
                  "Alla detaljer finns i <a href=\"terms.html\">Användarvillkoren</a> (på engelska)."),
        ]),
    },
}
