T = {
    "title": "Používateľská príručka",
    "subtitle": "Všetko, čo Invoice Cove dokáže, obrazovku po obrazovke.",
    "meta_desc": "Kompletná používateľská príručka k aplikácii Invoice Cove - Offline Billing.",
    "lang_label": "Jazyk",
    "brand_alt": "Invoice Cove",
    "toc": "Obsah",
    "footer_questions": "Otázky?",
    "lede": (
        "Invoice Cove funguje celé vo vašom zariadení: faktúry, ponuky, zákazníci aj profil vašej firmy sa ukladajú lokálne, "
        "nie na žiadny server Invoice Cove. Nezhromažďujeme, nevidíme ani neprijímame žiadne údaje o vašich faktúrach ani o tom, ako aplikáciu používate. "
        "Žiadna analytika, žiadne sledovanie, nič sa na pozadí nikam neodosiela. "
        "Jediný okamih, keď samotná aplikácia potrebuje internet, je spracovanie jednorazového nákupu Invoice Cove Pro cez Google Play. "
        "Podrobnosti nájdete v <a href=\"privacy.html\">Zásadách ochrany osobných údajov</a>."
    ),
    "warn": (
        "Nezabudnite! Skôr než aplikáciu odinštalujete alebo vymažete jej úložisko: tieto údaje nikde nezálohujeme. "
        "Odinštalovaním Invoice Cove alebo vymazaním jeho úložiska v nastaveniach Androidu sa natrvalo zmažú všetky faktúry, ponuky, zákazníci "
        "aj nastavenia v tomto zariadení — neexistuje kópia v cloude, z ktorej by sa dalo obnoviť. Aby ste ochránili svoje súbory: vytvorte zálohu "
        "s Invoice Cove Pro (pozri <a href=\"#backup\">Záloha a obnovenie</a>) alebo si potrebné exportujte do Excelu, CSV či ZIP "
        "(pozri <a href=\"#export\">Export faktúr</a>)."
    ),
    "sections": {
        "home": ("Úvodná obrazovka", [
            ("p", "Úvodná obrazovka je váš východiskový bod, s dlaždicou pre každú hlavnú akciu: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} a "
                  "{{common_reports_title}}. Klepnutím na dlaždicu sa tam hneď dostanete."),
            ("p", "Lišta dole vám ponúka rýchly prístup k {{nav_home}}, {{nav_new}} (nová faktúra), "
                  "{{nav_invoices}}, {{nav_customers}} a {{nav_reports}}."),
            ("p", "Ikona ozubeného kolieska (⚙️) v pravom hornom rohu väčšiny obrazoviek otvára <a href=\"#settings\">Údaje o firme a nastavenia</a>."),
        ]),
        "customers": ("Zákazníci", [
            ("p", "Ak chcete pridať zákazníka, prejdite na kartu {{nav_customers}} a klepnite na ikonu +, alebo použite dlaždicu {{home_new_customer_title}}. "
                  "Zákazníka môžete pridať aj pri vytváraní faktúry či ponuky. Na vytvorenie karty zákazníka stačí meno. "
                  "Medzi nepovinné polia patria: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, adresa, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} a farebný odtieň pre dokumenty zákazníka. Každé pole ukazuje príklad, aby bolo jasné, čo tam patrí."),
            ("p", "Klepnutím na zákazníka ho môžete upraviť ({{common_edit}}), otvoriť jeho {{customers_view_history}} (faktúry, ponuky a koncepty) "
                  "alebo ho zmazať ({{common_delete}})."),
            ("p", "Na vašich faktúrach a ponukách sa údaje o zákazníkovi tlačia pod jeho menom v pevnom poradí: číslo zákazníka, daňové číslo, IČ DPH, "
                  "číslo obchodného registra, potom adresa, e-mail a telefón. Čo nevyplníte, sa netlačí."),
            ("note", "Ukladanie tu funguje inak ako pri faktúrach. Zákazník má vlastné tlačidlo {{customers_form_save_customer}} "
                     "(pri úpravách {{customers_form_save_changes}}) a uloží sa v okamihu, keď naň klepnete. Ak sa pokúsite zavrieť formulár "
                     "s neuloženými zmenami, Invoice Cove sa najprv opýta na potvrdenie."),
            ("note", "Zmazanie zákazníka nezmaže faktúry a ponuky, ktoré ste mu už vystavili. Jeho nedokončené <a href=\"#drafts\">koncepty</a> "
                     "sa však zmažú spolu s ním; Invoice Cove vás najprv požiada o potvrdenie."),
        ]),
        "new-invoice": ("Vytvorenie faktúry", [
            ("p", "V {{nav_new}} (alebo na dlaždici {{home_new_invoice_title}}): vyberte zákazníka (alebo ho rovno vytvorte) "
                  "a nastavte dátum faktúry a splatnosť a potom pridajte položky."),
            ("p", "Klepnite na {{newinvoice_add_item_details_button}} a vyplňte popis, množstvo, cenu za jednotku a prípadne jednotku "
                  "(napr. h, ks alebo kg) a dátum a čas. Jednotka sa v PDF tlačí vedľa množstva. Klepnutím na ceruzku (✏️) pri položke ju opravíte, "
                  "kôš (🗑️) ju odstráni. Skôr použité popisy a ceny sa vám ponúkajú pri písaní."),
            ("p", "Potom v prípade potreby pridajte sadzbu dane, {{newinvoice_discount_label}} (percento alebo pevnú sumu) a "
                  "{{common_notes_label}}. Číslo faktúry sa prideľuje samo (s Invoice Cove Pro ho možno upraviť) a menu vyberiete vedľa neho."),
            ("p", "{{common_preview_button}} vytvorí dočasné PDF, aby ste videli, ako vyzerá — zatiaľ sa nič neukladá. "
                  "Tlačidlo {{common_template_button}} ukazuje, ktorá šablóna sa použije; klepnutím vyberiete inú len pre tento dokument."),
            ("note", "{{newinvoice_generate_button}} urobí tri veci naraz: uloží faktúru, vytvorí PDF a otvorí ponuku zdieľania "
                     "vášho zariadenia, aby ste ju mohli odoslať. Ešte nie ste hotoví? Použite {{newinvoice_save_draft_button}} — pozri <a href=\"#drafts\">Koncepty</a>."),
        ]),
        "drafts": ("Koncepty", [
            ("p", "Faktúru, na ktorej ešte pracujete, nestratíte. Akonáhle vyberiete zákazníka a pridáte aspoň jednu položku alebo poznámku, Invoice Cove "
                  "uchová koncept a aktualizuje ho chvíľu po tom, čo prestanete písať, a ešte raz, keď aplikáciu opustíte. Pri opustení obrazovky sa "
                  "neobjaví otázka „zahodiť zmeny?“; krátka správa vám oznámi, že sa koncept uložil."),
            ("p", "Klepnite na {{newinvoice_save_draft_button}} (pod {{newinvoice_generate_button}}), aby ste faktúru zámerne odložili: uloží sa a "
                  "formulár sa vyprázdni, pripravený na ďalšiu faktúru. Funguje to, akonáhle je vybraný zákazník, aj pred pridaním položiek."),
            ("p", "Koncepty nájdete v {{nav_customers}} → zákazník → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Každý koncept ukazuje, kedy bol naposledy upravený, koľko má položiek a jeho celkovú sumu. Klepnutím v úpravách "
                  "pokračujete alebo vystavíte faktúru; kôš ho zmaže."),
            ("ul", [
                "Koncept nikdy nespotrebuje číslo faktúry a nepočíta sa do bezplatného mesačného limitu. Číslo sa pridelí až pri vystavení konečnej "
                "faktúry — koncept ju potom nahradí.",
                "Koncept si pamätá dátum faktúry a splatnosť, iba ak ste ich zvolili sami; inak pri opätovnom otvorení použije dnešný dátum.",
                "Zmazanie zákazníka zmaže aj jeho koncepty (Invoice Cove sa vás najprv opýta). Koncepty sú súčasťou zálohy.",
                "Koncepty existujú pre faktúry; ponuky ich nemajú.",
            ]),
        ]),
        "invoices": ("Správa faktúr", [
            ("p", "Karta {{nav_invoices}} zoskupuje faktúry do priečinka pre každého zákazníka, ktoré môžete zoradiť podľa "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> alebo <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Otvorením priečinka uvidíte jeho faktúry zoradené podľa dátumu, hodnoty, čísla alebo stavu."),
            ("p", "Každá faktúra má stav: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (po splatnosti), "
                  "{{invoices_status_partially_paid}} (bola zaznamenaná záloha), {{invoices_status_paid}} alebo "
                  "{{invoices_status_void}}. Klepnutím na faktúru ju zobrazíte ({{common_view}}), znova odošlete ({{common_share}}), označíte ako zaplatenú alebo stornovanú, prípadne zmažete."),
            ("ul", [
                "{{invoices_action_mark_paid}} sa opýta na dátum platby a spôsob úhrady (prevod, hotovosť, karta, PayPal alebo iný). "
                "Zaplatenú faktúru už nemožno vrátiť späť na nezaplatenú.",
                "{{deposit_record_title}} zaznamená platbu vopred. Faktúra sa potom zobrazí ako {{invoices_status_partially_paid}} a záloha nesmie presiahnuť celkovú sumu.",
                "{{invoices_action_mark_void}} ponechá faktúru v evidencii, ale označí ju ako zrušenú. Je to lepšie ako zmazanie, pretože zmazanú faktúru "
                "nemožno obnoviť.",
            ]),
            ("p", "S Pro možno priečinok zákazníka aj uložiť alebo zdieľať ako ZIP s PDF a celý zoznam exportovať pre vášho účtovníka — pozri "
                  "<a href=\"#export\">Export faktúr</a>."),
        ]),
        "export": ("Export faktúr (Excel, CSV, ZIP)", [
            ("p", "K dispozícii s Invoice Cove Pro. Klepnite na ikonu exportu (📄) hore na karte {{nav_invoices}}. Ktoré faktúry zahrnúť, vyberiete "
                  "pomocou volieb roka a mesiaca ({{invoices_export_all}}, jeden rok alebo jeden mesiac roka; ponúkajú sa len roky a mesiace, "
                  "v ktorých faktúry sú), a potom vyberte, čo s nimi urobiť:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — tabuľka v Exceli (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — tá istá tabuľka ako súbor CSV.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — PDF faktúr v jednom ZIPe, jeden priečinok na zákazníka.",
                "{{invoices_export_delete}} — natrvalo zmaže vybrané faktúry po dvoch potvrdeniach.",
            ]),
            ("p", "<em>Uložiť</em> vám nechá vybrať, kam v zariadení súbor pôjde; <em>Zdieľať</em> otvorí zdieľaciu ponuku Androidu, aby ste ho poslali "
                  "e-mailom alebo v správe."),
            ("p", "Excel a CSV sú vytvorené pre vášho účtovníka: predvolene jeden riadok na faktúru s číslom a dátumami, menom, číslom, daňovým "
                  "číslom, IČ DPH, číslom obchodného registra a adresou zákazníka, medzisúčtom, zľavou, sadzbou DPH, sumou DPH a celkovou sumou faktúry, menou a stavom, dátumom a "
                  "spôsobom platby. Hlavičky stĺpcov a pevné slová (faktúra, zaplatené, nezaplatené, spôsoby platby) sú v jazyku, na ktorý je aplikácia "
                  "nastavená."),
            ("p", "Ak chcete získať jeden riadok na každú položku faktúry, s údajmi o faktúre opakovanými na každom riadku a s pridaným popisom, množstvom, "
                  "jednotkou, cenou a čistou sumou každej položky, zapnite {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Vytvorenie ponuky", [
            ("p", "Dlaždica {{home_new_quote_title}} funguje ako dlaždica Nová faktúra: rovnaké polia, rovnaké tlačidlá {{common_preview_button}} a {{common_template_button}}, rovnaké "
                  "{{newquote_generate_button}}, ktoré jedným klepnutím uloží, vytvorí PDF a otvorí ponuku zdieľania, ale s "
                  "{{newquote_date_label}} a dátumom {{newquote_valid_until_label}} namiesto dátumu faktúry a splatnosti."),
            ("p", "Ponuky nemajú koncepty."),
        ]),
        "quotes": ("Správa ponúk a prevod na faktúru", [
            ("p", "Obrazovka {{common_quotes_title}} (z dlaždice na úvodnej obrazovke) uvádza ponuky podľa zákazníkov, rovnako ako faktúry. Otvorte ponuku, aby ste ju "
                  "zobrazili alebo zdieľali, použite {{quotes_action_accept}} alebo {{quotes_action_decline}}, keď zákazník odpovie, "
                  "zaznamenajte zálohu alebo ju zmažte. Záloha nesmie presiahnuť celkovú sumu ponuky."),
            ("p", "Keď zákazník ponuku prijme, použite {{quotes_action_convert_to_invoice}} a zaškrtnuté položky sa prevedú na skutočnú faktúru, "
                  "samostatne upraviteľnú. Splatnosť a zľavu možno ešte upraviť a pôvodná ponuka sa označí ako "
                  "{{quotes_status_converted}} a zostane vo vašej evidencii."),
        ]),
        "calendar": ("Kalendár a pripomienky", [
            ("p", "Obrazovka {{calendar_title}} je mesačný prehľad pre vaše vlastné poznámky. Klepnutím na deň poznámky zobrazíte alebo pridáte; poznámka má názov a text a "
                  "s voľbou {{calendar_remind_me}} a časom vám v nastavený dátum a čas pošle oznámenie. Prvý deň týždňa sa riadi vašimi nastaveniami."),
            ("p", "Osobitne Invoice Cove posiela pripomienky platieb — miestne oznámenia o faktúrach, ktoré čoskoro budú splatné alebo už splatnosť prekročili. Nič sa neodosiela na server ani z neho neprijíma."),
        ]),
        "reports": ("Prehľady", [
            ("p", "{{common_reports_title}} vám dá rýchly prehľad: sumy {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} a {{reports_stat_overdue}}, počet faktúr, "
                  "<em>{{reports_revenue_by_month}}</em> a vašich <em>{{reports_top_customers}}</em> podľa fakturovanej sumy."),
            ("p", "Klepnutím na kartu {{reports_stat_outstanding}} alebo {{reports_stat_overdue}} otvoríte zoznam presne týchto faktúr."),
        ]),
        "settings": ("Údaje o firme a nastavenia", [
            ("p", "Nastavenia otvoríte ikonou ozubeného kolieska; táto obrazovka sa volá {{settings_title}}. Začína vašimi voliteľnými predvoľbami: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} alebo {{settings_theme_dark}}), predvolená "
                  "{{settings_invoice_template_label}}, {{settings_tax_label_label}} (DPH, GST…), "
                  "{{settings_first_day_of_week_label}} a {{settings_due_date_default_label}}, ktorá automaticky vyplní splatnosť (napr. Net 30). "
                  "Pod nimi nasledujú {{settings_security_label}} (pozri <a href=\"#app-lock\">Zámok aplikácie</a>), "
                  "{{settings_item_suggestions_label}} a {{settings_backup_restore_label}} (pozri <a href=\"#backup\">Záloha a obnovenie</a>)."),
            ("p", "{{settings_item_memory_title}} si pamätá popisy a ceny položiek, aby ich ponúkala pri písaní; <em>{{common_clear}}</em> ich zabudne, "
                  "bez toho aby sa dotkla vašich faktúr."),
            ("p", "Nižšie je profil vašej firmy, ktorý sa tlačí na každej faktúre a ponuke: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, krátke motto ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, {{settings_date_format_label}} dátumov, adresa, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (registračné číslo, základné imanie a podobne), "
                  "{{settings_business_logo_label}} a {{settings_payment_details_label}} (IBAN, odkaz PayPal.me). Každé pole "
                  "má príklad a každé pole, ktoré necháte prázdne, sa na vašich faktúrach neobjaví. Keď skončíte, klepnite na {{common_done}}; "
                  "ak odídete s neuloženými zmenami, budete požiadaní o potvrdenie."),
            ("p", "Úplne dole sa zobrazujú táto {{settings_user_manual}} a {{settings_share_this_app}}."),
        ]),
        "backup": ("Záloha a obnovenie", [
            ("p", "K dispozícii s Invoice Cove Pro, v časti {{settings_backup_restore_label}}. {{settings_create_backup_title}} uloží "
                  "všetko: faktúry, ponuky, koncepty, zákazníkov, kalendár, nastavenia, logo aj PDF, a to všetko do jedného súboru. Zvoľte "
                  "{{backup_save_button}}, aby ste ho uložili, kam chcete, alebo {{backup_share_button}}, aby ste ho poslali na bezpečné miesto."),
            ("p", "{{settings_restore_backup_title}} vráti všetko späť, ak potrebujete údaje preniesť do nového telefónu. Funguje len na čerstvej inštalácii, kým ste nepridali "
                  "žiadne údaje, takže nikdy nemôže prepísať to, čo už máte. Invoice Cove overí, že je súbor neporušený, a upozorní vás, ak je poškodený, "
                  "nie je zálohou Invoice Cove alebo ho vytvorila novšia verzia aplikácie (najprv aktualizujte)."),
            ("note", "Súbor zálohy nie je šifrovaný: ktokoľvek, kto ho má, môže vaše údaje čítať. Uchovajte ho na súkromnom mieste. PIN zámku aplikácie v ňom nie je nikdy "
                     "obsiahnutý."),
        ]),
        "app-lock": ("Zámok aplikácie", [
            ("p", "V {{settings_security_label}} môžete zapnúť {{settings_app_lock_title}}: Invoice Cove potom požiada o PIN "
                  "(alebo odtlačok prsta), keď sa aplikácia otvorí znova od začiatku alebo po reštarte telefónu — nie pri každom návrate do nej."),
            ("ul", [
                "{{settings_set_pin}}: zvoľte štvormiestny PIN a potvrďte ho.",
                "Potom dostanete šesťmiestny obnovovací kód, ktorý sa zobrazí len raz. Zapíšte si ho a uložte na bezpečné miesto.",
                "Ak to váš telefón podporuje, odomykajte odtlačkom prsta ({{security_use_fingerprint}}).",
                "Zabudli ste PIN? Použite {{security_forgot_pin}} a zadajte obnovovací kód. Po 5 chybných pokusoch musíte počkať 30 sekúnd – "
                "čakanie sa s ďalšími chybnými pokusmi predlžuje.",
            ]),
            ("note", "Ak stratíte PIN aj obnovovací kód a nemáte nastavené odomykanie odtlačkom prsta, nemožno sa vrátiť dnu. Nemôžeme ho za vás "
                     "resetovať."),
        ]),
        "languages": ("Jazyky", [
            ("p", "Invoice Cove hovorí 13 jazykmi: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands a Svenska. Klepnite na okrúhlu ikonu s vlajkou hore v nastaveniach a jazyk sa zmení — aplikácia sa prepne okamžite."),
            ("p", "Text vo vašich PDF a v exportoch do Excelu/CSV sa riadi jazykom, na ktorý je aplikácia nastavená, a táto príručka je dostupná v rovnakých 13 jazykoch "
                  "(použite jazykovú lištu hore na stránke)."),
        ]),
        "templates": ("PDF šablóny", [
            ("p", "Invoice Cove zatiaľ ponúka 18 návrhov PDF: Classic, Client Color (vo farbe zákazníka), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves a Spooky Hollow."),
            ("p", "Predvolenú šablónu zvoľte v Nastaveniach → {{settings_invoice_template_label}}: klepnite na návrh a potom na {{common_done}}. Platí "
                  "pre všetko, čo od tej chvíle vytvoríte. Pre jednu faktúru alebo ponuku použite tlačidlo {{common_template_button}} "
                  "vo formulári."),
            ("p", "Každá šablóna tlačí rovnaké informácie: údaje o vašej firme, o zákazníkovi, položky s jednotkou a dátumom, súčty, poznámky a "
                  "platobné údaje — ale len to, čo ste vyplnili. Dlhé faktúry pokračujú na druhej strane a súčet zostáva spolu s poslednou položkou."),
        ]),
        "free-vs-pro": ("Bezplatný plán a Invoice Cove Pro", [
            ("p", "Invoice Cove je zadarmo, s niekoľkými rozumnými obmedzeniami:"),
            ("ul", [
                "Až 3 faktúry vystavené za kalendárny mesiac",
                "Až 3 ponuky vystavené za kalendárny mesiac",
                "Až 3 zákazníci naraz",
                "Čísla faktúr a ponúk sa prideľujú automaticky a nemožno ich upraviť",
                "Export do Excelu, CSV a ZIP je len v Pro",
                "Záloha a obnovenie sú len v Pro",
            ]),
            ("p", "Invoice Cove Pro je jediný jednorazový nákup cez Google Play (nie predplatné), ktorý všetky tieto obmedzenia navždy odstráni. "
                  "Koncepty, všetky šablóny a jazyky, zámok aplikácie aj vytváranie, náhľad a zdieľanie dokumentov sú zadarmo pre všetkých. "
                  "Všetky podrobnosti nájdete v <a href=\"terms.html\">Podmienkach používania</a>."),
        ]),
    },
}
