T = {
    "title": "Användarguide",
    "subtitle": "Allt Invoice Cove kan göra, skärm för skärm.",
    "meta_desc": "Komplett användarguide för appen Invoice Cove - Offline Billing.",
    "lang_label": "Språk",
    "brand_alt": "Invoice Cove",
    "toc": "Innehåll",
    "footer_questions": "Frågor?",
    "lede": (
        "Invoice Cove fungerar helt på din enhet: dina fakturor, offerter, kunder och företagsuppgifter lagras lokalt, "
        "inte på någon Invoice Cove-server. Vi samlar inte in, ser eller tar emot några uppgifter om dina fakturor eller om hur du använder appen. "
        "Ingen analys, ingen spårning, inget skickas i bakgrunden. "
        "Den enda gången själva appen behöver internet är när engångsköpet av Invoice Cove Pro behandlas via Google Play. "
        "Detaljer finns i <a href=\"privacy.html\">Integritetspolicyn</a>."
    ),
    "warn": (
        "Kom ihåg! Innan du avinstallerar appen eller rensar dess lagring: vi säkerhetskopierar inte dessa uppgifter någonstans. "
        "Om du avinstallerar Invoice Cove eller rensar dess lagring i Androids inställningar raderas alla fakturor, offerter, kunder "
        "och inställningar på den här enheten permanent — det finns ingen molnkopia att återställa från. För att skydda dina filer: skapa en säkerhetskopia "
        "med Invoice Cove Pro (se <a href=\"#backup\">Säkerhetskopiering och återställning</a>) eller exportera det du behöver till Excel, CSV eller ZIP "
        "(se <a href=\"#export\">Exportera fakturor</a>)."
    ),
    "sections": {
        "home": ("Startskärm", [
            ("p", "Startskärmen är din utgångspunkt, med en ruta för varje huvudåtgärd: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} och "
                  "{{common_reports_title}}. Tryck på en ruta för att gå dit direkt."),
            ("p", "Fältet längst ned ger dig snabb åtkomst till {{nav_home}}, {{nav_new}} (ny faktura), "
                  "{{nav_invoices}}, {{nav_customers}} och {{nav_reports}}."),
            ("p", "Kugghjulsikonen (⚙️) uppe till höger på de flesta skärmar öppnar <a href=\"#settings\">Företagsuppgifter och inställningar</a>."),
        ]),
        "customers": ("Kunder", [
            ("p", "För att lägga till en kund går du till fliken {{nav_customers}} och trycker på +-ikonen, eller använder rutan {{home_new_customer_title}}. "
                  "Du kan också lägga till en kund när du skapar en faktura eller offert. Det enda som krävs för att skapa ett kundkort är namnet. "
                  "De valfria fälten omfattar: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, adress, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} och en färgton för kundens dokument. Varje fält visar ett exempel så att det är tydligt vad som ska stå där."),
            ("p", "Tryck på en kund för att redigera den ({{common_edit}}), öppna dess {{customers_view_history}} (fakturor, offerter och utkast) "
                  "eller ta bort den ({{common_delete}})."),
            ("p", "På dina fakturor och offerter skrivs kunduppgifterna ut under namnet i en fast ordning: kundnummer, skatte-ID, momsregistreringsnummer, "
                  "handelsregisternummer, därefter adress, e-post och telefon. Det du inte fyller i skrivs inte ut."),
            ("note", "Sparandet fungerar annorlunda här än för fakturor. En kund har en egen knapp {{customers_form_save_customer}} "
                     "(vid redigering {{customers_form_save_changes}}) och sparas i samma stund som du trycker på den. Om du försöker stänga formuläret "
                     "med osparade ändringar ber Invoice Cove först om bekräftelse."),
            ("note", "Att ta bort en kund tar inte bort de fakturor och offerter du redan har skapat åt kunden. Kundens ofärdiga <a href=\"#drafts\">utkast</a> "
                     "tas däremot bort tillsammans med kunden; Invoice Cove ber dig först bekräfta."),
        ]),
        "new-invoice": ("Skapa en faktura", [
            ("p", "På {{nav_new}} (eller via rutan {{home_new_invoice_title}}): välj en kund (eller skapa en direkt) "
                  "och ange fakturadatum och förfallodatum och lägg sedan till rader."),
            ("p", "Tryck på {{newinvoice_add_item_details_button}} och fyll i beskrivning, antal, pris per enhet och vid behov enhet "
                  "(t.ex. tim, st eller kg) samt datum och tid. Enheten skrivs ut bredvid antalet i PDF:en. Med pennan (✏️) vid en rad rättar du den, "
                  "med papperskorgen (🗑️) tar du bort den. Tidigare använda beskrivningar och priser föreslås medan du skriver."),
            ("p", "Lägg sedan vid behov till en skattesats, {{newinvoice_discount_label}} (procent eller fast belopp) och "
                  "{{common_notes_label}}. Fakturanumret tilldelas automatiskt (med Invoice Cove Pro kan det ändras), och valutan väljer du bredvid."),
            ("p", "{{common_preview_button}} skapar en tillfällig PDF så att du ser hur den ser ut — ingenting sparas ännu. "
                  "Knappen {{common_template_button}} visar vilken mall som används; tryck på den för att välja en annan bara för det här dokumentet."),
            ("note", "{{newinvoice_generate_button}} gör tre saker på en gång: sparar fakturan, skapar PDF:en och öppnar enhetens "
                     "delningsmeny så att du kan skicka den. Inte klar än? Använd {{newinvoice_save_draft_button}} — se <a href=\"#drafts\">Utkast</a>."),
        ]),
        "drafts": ("Utkast", [
            ("p", "En faktura du fortfarande arbetar på försvinner inte. Så snart du väljer en kund och lägger till minst en rad eller anteckning behåller Invoice Cove "
                  "ett utkast och uppdaterar det en stund efter att du slutat skriva, och en gång till när du lämnar appen. När du lämnar skärmen visas "
                  "ingen fråga om att ”kasta ändringar?”; ett kort meddelande talar om att utkastet har sparats."),
            ("p", "Tryck på {{newinvoice_save_draft_button}} (under {{newinvoice_generate_button}}) för att medvetet lägga en faktura åt sidan: den sparas och "
                  "formuläret töms, redo för nästa faktura. Det fungerar så snart en kund är vald, även innan du lagt till rader."),
            ("p", "Du hittar utkasten under {{nav_customers}} → kund → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Varje utkast visar när det senast ändrades, hur många rader det har och totalbeloppet. Tryck på det för att "
                  "fortsätta redigera eller skapa fakturan; papperskorgen tar bort det."),
            ("ul", [
                "Ett utkast använder aldrig ett fakturanummer och räknas inte mot den kostnadsfria månadsgränsen. Numret tilldelas först när du skapar den slutliga "
                "fakturan — utkastet ersätts då av den.",
                "Ett utkast minns fakturadatum och förfallodatum bara om du själv valt dem; annars används dagens datum när du öppnar det igen.",
                "Om du tar bort en kund tas även dess utkast bort (Invoice Cove frågar dig först). Utkast ingår i säkerhetskopian.",
                "Utkast finns för fakturor; offerter har inga.",
            ]),
        ]),
        "invoices": ("Hantera fakturor", [
            ("p", "Fliken {{nav_invoices}} grupperar fakturor i en mapp per kund, som du kan sortera efter "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> eller <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Öppna en mapp för att se dess fakturor, sorterade efter datum, värde, nummer eller status."),
            ("p", "Varje faktura har en status: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (efter förfallodatum), "
                  "{{invoices_status_partially_paid}} (en handpenning har registrerats), {{invoices_status_paid}} eller "
                  "{{invoices_status_void}}. Tryck på en faktura för att visa den ({{common_view}}), skicka den igen ({{common_share}}), markera den som betald eller makulerad eller ta bort den."),
            ("ul", [
                "{{invoices_action_mark_paid}} frågar efter betalningsdatum och betalsätt (överföring, kontant, kort, PayPal eller annat). "
                "En betald faktura kan inte sättas tillbaka till obetald.",
                "{{deposit_record_title}} registrerar en förskottsbetalning. Fakturan visas då som {{invoices_status_partially_paid}} och handpenningen får inte överstiga totalen.",
                "{{invoices_action_mark_void}} behåller fakturan i din bokföring men markerar den som annullerad. Det är att föredra framför att ta bort, eftersom en borttagen faktura "
                "kan inte återställas.",
            ]),
            ("p", "Med Pro kan du också spara eller dela en kunds mapp som ZIP med PDF:erna och exportera hela listan till din revisor — se "
                  "<a href=\"#export\">Exportera fakturor</a>."),
        ]),
        "export": ("Exportera fakturor (Excel, CSV, ZIP)", [
            ("p", "Tillgängligt med Invoice Cove Pro. Tryck på exportikonen (📄) högst upp på fliken {{nav_invoices}}. Välj vilka fakturor som ska tas med "
                  "med år- och månadsväljaren ({{invoices_export_all}}, ett år eller en månad i ett år; bara år och månader "
                  "där det finns fakturor erbjuds) och välj sedan vad du vill göra med dem:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — ett Excel-kalkylblad (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — samma tabell som en CSV-fil.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — fakturornas PDF:er i en ZIP, med en mapp per kund.",
                "{{invoices_export_delete}} — tar permanent bort de valda fakturorna efter två bekräftelser.",
            ]),
            ("p", "Med <em>Spara</em> väljer du var på enheten filen hamnar; <em>Dela</em> öppnar Androids delningsmeny så att du kan skicka den "
                  "via e-post eller i ett meddelande."),
            ("p", "Excel och CSV är gjorda för din revisor: som standard en rad per faktura, med nummer och datum, kundens namn, nummer, "
                  "skatte-ID, momsregistreringsnummer, handelsregisternummer och adress, delsumma, rabatt, momssats, momsbelopp och fakturans totalbelopp, "
                  "valuta och status, betalningsdatum och betalsätt. Kolumnrubrikerna och de fasta orden (faktura, betald, obetald, betalsätt) står på det "
                  "språk som appen är inställd på."),
            ("p", "För att få en rad per fakturarad, där fakturauppgifterna upprepas på varje rad och beskrivning, antal, enhet, pris och "
                  "nettobelopp för varje rad läggs till, slår du på {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Skapa en offert", [
            ("p", "Rutan {{home_new_quote_title}} fungerar som rutan Ny faktura: samma fält, samma knappar {{common_preview_button}} och {{common_template_button}}, samma "
                  "{{newquote_generate_button}}, som med ett tryck sparar, skapar PDF:en och öppnar delningsmenyn, men med "
                  "{{newquote_date_label}} och ett datum {{newquote_valid_until_label}} i stället för fakturadatum och förfallodatum."),
            ("p", "Offerter har inga utkast."),
        ]),
        "quotes": ("Hantera offerter och omvandla till faktura", [
            ("p", "Skärmen {{common_quotes_title}} (via rutan på startskärmen) listar offerter per kund, precis som fakturor. Öppna en offert för att "
                  "visa eller dela den, använd {{quotes_action_accept}} eller {{quotes_action_decline}} när kunden svarar, "
                  "registrera en handpenning eller ta bort den. En handpenning får inte överstiga offertens totalbelopp."),
            ("p", "När kunden godkänner offerten använder du {{quotes_action_convert_to_invoice}} och de ikryssade raderna omvandlas till en riktig faktura, "
                  "som du kan redigera separat. Förfallodatum och rabatt kan fortfarande ändras, och den ursprungliga offerten markeras som "
                  "{{quotes_status_converted}} och finns kvar i din bokföring."),
        ]),
        "calendar": ("Kalender och påminnelser", [
            ("p", "Skärmen {{calendar_title}} är en månadsvy för dina egna anteckningar. Tryck på en dag för att se eller lägga till anteckningar; en anteckning har en titel och text och "
                  "skickar dig med alternativet {{calendar_remind_me}} och en tid en avisering vid det inställda datumet och klockslaget. Veckans första dag följer dina inställningar."),
            ("p", "Separat skickar Invoice Cove betalningspåminnelser — lokala aviseringar om fakturor som snart förfaller eller redan har förfallit. Ingenting skickas till eller tas emot från en server."),
        ]),
        "reports": ("Rapporter", [
            ("p", "{{common_reports_title}} ger dig en snabb överblick: beloppen {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} och {{reports_stat_overdue}}, antalet fakturor, "
                  "<em>{{reports_revenue_by_month}}</em> och dina <em>{{reports_top_customers}}</em> efter fakturerat belopp."),
            ("p", "Tryck på kortet {{reports_stat_outstanding}} eller {{reports_stat_overdue}} för att öppna en lista över exakt de fakturorna."),
        ]),
        "settings": ("Företagsuppgifter och inställningar", [
            ("p", "Öppna inställningarna med kugghjulsikonen; den här skärmen heter {{settings_title}}. Den börjar med dina valfria preferenser: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} eller {{settings_theme_dark}}), standard-"
                  "{{settings_invoice_template_label}}, {{settings_tax_label_label}} (moms, GST…), "
                  "{{settings_first_day_of_week_label}} och {{settings_due_date_default_label}}, som fyller i förfallodatum automatiskt (t.ex. Net 30). "
                  "Under dem följer {{settings_security_label}} (se <a href=\"#app-lock\">Applås</a>), "
                  "{{settings_item_suggestions_label}} och {{settings_backup_restore_label}} (se <a href=\"#backup\">Säkerhetskopiering och återställning</a>)."),
            ("p", "{{settings_item_memory_title}} minns radernas beskrivningar och priser för att föreslå dem medan du skriver; <em>{{common_clear}}</em> glömmer dem, "
                  "utan att röra dina fakturor."),
            ("p", "Längre ned finns ditt företags profil som skrivs ut på varje faktura och offert: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, en kort slogan ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, {{settings_date_format_label}} för datum, adress, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (registreringsnummer, aktiekapital och liknande), "
                  "{{settings_business_logo_label}} och {{settings_payment_details_label}} (IBAN, PayPal.me-länk). Varje fält "
                  "har ett exempel och varje fält du lämnar tomt visas inte på dina fakturor. Tryck på {{common_done}} när du är klar; "
                  "om du lämnar med osparade ändringar ombeds du bekräfta."),
            ("p", "Allra längst ned visas den här {{settings_user_manual}} och {{settings_share_this_app}}."),
        ]),
        "backup": ("Säkerhetskopiering och återställning", [
            ("p", "Tillgängligt med Invoice Cove Pro, under {{settings_backup_restore_label}}. {{settings_create_backup_title}} sparar "
                  "allt: fakturor, offerter, utkast, kunder, kalender, inställningar, logotyp och PDF:er, allt i en enda fil. Välj "
                  "{{backup_save_button}} för att spara den var du vill, eller {{backup_share_button}} för att skicka den till en säker plats."),
            ("p", "{{settings_restore_backup_title}} lägger tillbaka allt, ifall du behöver flytta till en ny telefon. Det fungerar bara på en nyinstallation, så länge du inte lagt till "
                  "några uppgifter, så det kan aldrig skriva över det du redan har. Invoice Cove kontrollerar att filen är hel och varnar dig om den är skadad, "
                  "inte är en Invoice Cove-säkerhetskopia eller skapades av en nyare version av appen (uppdatera först)."),
            ("note", "Säkerhetskopian är inte krypterad: den som har den kan läsa dina uppgifter. Förvara den på en privat plats. Applåsets PIN-kod ingår aldrig "
                     "i den."),
        ]),
        "app-lock": ("Applås", [
            ("p", "Under {{settings_security_label}} kan du slå på {{settings_app_lock_title}}: Invoice Cove ber då om en PIN-kod "
                  "(eller fingeravtryck) när appen öppnas från början eller efter att telefonen startats om — inte vid varje återkomst till den."),
            ("ul", [
                "{{settings_set_pin}}: välj en fyrsiffrig PIN-kod och bekräfta den.",
                "Därefter får du en sexsiffrig återställningskod som bara visas en gång. Skriv ned den och förvara den på en säker plats.",
                "Om din telefon stöder det kan du låsa upp med fingeravtryck ({{security_use_fingerprint}}).",
                "Glömt PIN-koden? Använd {{security_forgot_pin}} och ange återställningskoden. Efter 5 felaktiga försök måste du vänta 30 sekunder – "
                "väntetiden förlängs vid fler felaktiga försök.",
            ]),
            ("note", "Om du tappar både PIN-koden och återställningskoden och inte har ställt in fingeravtrycksupplåsning, går det inte att komma in igen. Vi kan inte återställa den åt "
                     "dig."),
        ]),
        "languages": ("Språk", [
            ("p", "Invoice Cove talar 13 språk: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands och Svenska. Tryck på den runda flaggikonen högst upp i inställningarna så byts språket — appen växlar direkt."),
            ("p", "Texten i dina PDF:er och i exporterna till Excel/CSV följer det språk som appen är inställd på, och den här guiden finns på samma 13 språk "
                  "(använd språkfältet högst upp på sidan)."),
        ]),
        "templates": ("PDF-mallar", [
            ("p", "Invoice Cove erbjuder för närvarande 18 PDF-design: Classic, Client Color (i kundens färg), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves och Spooky Hollow."),
            ("p", "Välj standardmall under Inställningar → {{settings_invoice_template_label}}: tryck på en design och sedan på {{common_done}}. Den gäller "
                  "för allt du skapar från och med då. För en enskild faktura eller offert använder du knappen {{common_template_button}} "
                  "i formuläret."),
            ("p", "Varje mall skriver ut samma information: dina företagsuppgifter, kundens, rader med enhet och datum, summor, anteckningar och "
                  "betalningsuppgifter — men bara det du har fyllt i. Långa fakturor fortsätter på en andra sida och totalen följer med den sista raden."),
        ]),
        "free-vs-pro": ("Gratisversion och Invoice Cove Pro", [
            ("p", "Invoice Cove är gratis, med några rimliga begränsningar:"),
            ("ul", [
                "Upp till 3 fakturor per kalendermånad",
                "Upp till 3 offerter per kalendermånad",
                "Upp till 3 kunder åt gången",
                "Faktura- och offertnummer tilldelas automatiskt och kan inte ändras",
                "Export till Excel, CSV och ZIP finns bara med Pro",
                "Säkerhetskopiering och återställning finns bara med Pro",
            ]),
            ("p", "Invoice Cove Pro är ett enda engångsköp via Google Play (inte en prenumeration) som tar bort alla dessa begränsningar för alltid. "
                  "Utkast, alla mallar och språk, applåset samt att skapa, förhandsvisa och dela dokument är gratis för alla. "
                  "Alla detaljer finns i <a href=\"terms.html\">Användarvillkoren</a>."),
        ]),
    },
}
