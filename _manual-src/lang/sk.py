T = {
    "title": "Používateľská príručka",
    "subtitle": "Všetko, čo Invoice Cove dokáže, obrazovku po obrazovke.",
    "meta_desc": "Kompletná používateľská príručka k aplikácii Invoice Cove - Offline Billing.",
    "lang_label": "Jazyk",
    "brand_alt": "Invoice Cove",
    "toc": "Obsah",
    "footer_questions": "Otázky?",
    "lede": (
        "Invoice Cove funguje celé vo vašom zariadení — faktúry, ponuky, zákazníci aj profil vašej firmy sa ukladajú lokálne, "
        "nie na žiadny server Invoice Cove. <strong>Nezhromažďujeme, nevidíme ani neprijímame žiadne údaje o vašich faktúrach ani o tom, ako aplikáciu používate</strong> "
        "— žiadna analytika, žiadne sledovanie, nič sa na pozadí nikam neodosiela. "
        "Jediný okamih, keď samotná aplikácia potrebuje internet, je spracovanie jednorazového nákupu Invoice Cove Pro cez Google Play. "
        "Podrobnosti nájdete v <a href=\"privacy.html\">Zásadách ochrany osobných údajov</a> (po anglicky)."
    ),
    "warn": (
        "<strong>Skôr než aplikáciu odinštalujete alebo vymažete jej úložisko:</strong> tieto údaje nikde nezálohujeme. "
        "Odinštalovaním Invoice Cove alebo vymazaním jeho úložiska v nastaveniach Androidu sa natrvalo zmažú všetky faktúry, ponuky, zákazníci "
        "aj nastavenia v tomto zariadení — neexistuje kópia v cloude, z ktorej by sa dalo obnoviť. Chráňte sa: vytvorte zálohu "
        "s Invoice Cove Pro (pozri <a href=\"#backup\">Záloha a obnovenie</a>) alebo si potrebné exportujte do Excelu, CSV či ZIP "
        "(pozri <a href=\"#export\">Export faktúr</a>)."
    ),
    "sections": {
        "home": ("Úvodná obrazovka", [
            ("p", "Úvodná obrazovka je váš východiskový bod, s dlaždicou pre každú hlavnú akciu: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> a "
                  "<strong>{{common_reports_title}}</strong>. Klepnutím na dlaždicu sa tam hneď dostanete."),
            ("p", "Lišta dole vám vždy ponúka rýchly prístup k <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (nová faktúra), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> a <strong>{{nav_reports}}</strong>."),
            ("p", "Ikona ozubeného kolieska (⚙️) v pravom hornom rohu väčšiny obrazoviek otvára <a href=\"#settings\">Údaje o firme a nastavenia</a>."),
        ]),
        "customers": ("Zákazníci", [
            ("p", "Zákazníka pridáte na karte <strong>{{nav_customers}}</strong> (klepnite na ikonu +), dlaždicou <strong>{{home_new_customer_title}}</strong> "
                  "alebo priamo pri vytváraní faktúry či ponuky. Povinné je iba meno. Nepovinné polia: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, adresa, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} a farba, ktorá zafarbí dokumenty zákazníka. Každé pole ukazuje príklad, aby bolo jasné, čo tam patrí."),
            ("p", "Klepnutím na zákazníka ho môžete upraviť (<strong>{{common_edit}}</strong>), otvoriť jeho <strong>{{customers_view_history}}</strong> (faktúry, ponuky a koncepty) "
                  "alebo ho zmazať (<strong>{{common_delete}}</strong>)."),
            ("p", "Na vašich faktúrach a ponukách sa údaje o zákazníkovi tlačia pod jeho menom v pevnom poradí: číslo zákazníka, daňové číslo, IČ DPH, "
                  "číslo obchodného registra, potom adresa, e-mail a telefón. Čo nevyplníte, sa jednoducho netlačí."),
            ("note", "<strong>Ukladanie tu funguje inak ako pri faktúrach.</strong> Zákazník má vlastné tlačidlo <strong>{{customers_form_save_customer}}</strong> "
                     "(pri úpravách <strong>{{customers_form_save_changes}}</strong>) — uloží sa v okamihu, keď naň klepnete. Ak sa pokúsite zavrieť formulár "
                     "s neuloženými zmenami, Invoice Cove sa najprv opýta na potvrdenie."),
            ("note", "Zmazanie zákazníka nezmaže faktúry a ponuky, ktoré ste mu už vystavili. Jeho nedokončené <a href=\"#drafts\">koncepty</a> "
                     "sa zmažú spolu s ním — predtým sa vás aplikácia opýta."),
        ]),
        "new-invoice": ("Vytvorenie faktúry", [
            ("p", "V <strong>{{nav_new}}</strong> (alebo na dlaždici <strong>{{home_new_invoice_title}}</strong>): vyberte zákazníka — alebo ho rovno vytvorte — "
                  "nastavte dátum faktúry a splatnosť a potom pridajte položky."),
            ("p", "Klepnite na <strong>{{newinvoice_add_item_details_button}}</strong> a vyplňte popis, množstvo, cenu za jednotku a prípadne jednotku "
                  "(napr. h, ks alebo kg) a dátum a čas. Jednotka sa v PDF tlačí vedľa množstva. Klepnutím na ceruzku (✏️) pri položke ju opravíte, "
                  "kôš (🗑️) ju odstráni. Skôr použité popisy a ceny sa vám ponúkajú pri písaní."),
            ("p", "Potom podľa potreby pridajte sadzbu dane, <strong>{{newinvoice_discount_label}}</strong> (percento alebo pevnú sumu) a "
                  "<strong>{{common_notes_label}}</strong>. Číslo faktúry sa prideľuje samo (s Pro ho môžete upraviť); menu vyberiete vedľa neho."),
            ("p", "<strong>{{common_preview_button}}</strong> vytvorí dočasné PDF, aby ste videli, ako vyzerá — zatiaľ sa nič neukladá. "
                  "Tlačidlo <strong>{{common_template_button}}</strong> ukazuje, ktorá šablóna sa použije; klepnutím vyberiete inú len pre tento dokument."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> urobí tri veci naraz: uloží faktúru, vytvorí PDF a otvorí ponuku zdieľania "
                     "vášho zariadenia, aby ste ju mohli odoslať. Ešte nie ste hotoví? Použite <strong>{{newinvoice_save_draft_button}}</strong> — pozri <a href=\"#drafts\">Koncepty</a>."),
        ]),
        "drafts": ("Koncepty", [
            ("p", "Faktúru, na ktorej ešte pracujete, nestratíte. Akonáhle vyberiete zákazníka a pridáte aspoň jednu položku alebo poznámku, Invoice Cove "
                  "uchová <strong>koncept</strong> a aktualizuje ho chvíľu po tom, čo prestanete písať — a ešte raz, keď aplikáciu opustíte. Pri opustení obrazovky sa "
                  "neobjaví otázka „zahodiť zmeny?“; krátka správa vám oznámi, že sa koncept uložil."),
            ("p", "Klepnite na <strong>{{newinvoice_save_draft_button}}</strong> (pod {{newinvoice_generate_button}}), aby ste faktúru zámerne odložili: uloží sa a "
                  "formulár sa vyprázdni, pripravený na ďalšiu faktúru. Funguje to, akonáhle je vybraný zákazník, aj pred pridaním položiek."),
            ("p", "Koncepty nájdete v <strong>{{nav_customers}}</strong> → zákazník → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Každý koncept ukazuje, kedy bol naposledy upravený, koľko má položiek a jeho celkovú sumu. Klepnutím v úpravách "
                  "pokračujete alebo vystavíte faktúru; kôš ho zmaže."),
            ("ul", [
                "Koncept nikdy nespotrebuje číslo faktúry a nepočíta sa do bezplatného mesačného limitu. Číslo sa pridelí až pri vystavení konečnej "
                "faktúry — koncept ju potom nahradí.",
                "Koncept si pamätá dátum faktúry a splatnosť, iba ak ste ich zvolili sami; inak pri opätovnom otvorení použije dnešný dátum.",
                "Zmazanie zákazníka zmaže aj jeho koncepty (predtým sa vás aplikácia opýta). Koncepty sú súčasťou zálohy.",
                "Koncepty existujú pre faktúry; ponuky ich nemajú.",
            ]),
        ]),
        "invoices": ("Správa faktúr", [
            ("p", "Karta <strong>{{nav_invoices}}</strong> zoskupuje faktúry do priečinka pre každého zákazníka, ktoré môžete zoradiť podľa "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> alebo <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Otvorením priečinka uvidíte jeho faktúry zoradené podľa dátumu, hodnoty, čísla alebo stavu."),
            ("p", "Každá faktúra má stav: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (po splatnosti), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (bola zaznamenaná záloha), <strong>{{invoices_status_paid}}</strong> alebo "
                  "<strong>{{invoices_status_void}}</strong>. Klepnutím na faktúru ju zobrazíte ({{common_view}}), znova odošlete ({{common_share}}), označíte ako zaplatenú alebo stornovanú, prípadne zmažete."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> sa opýta na dátum platby a spôsob úhrady (prevod, hotovosť, karta, PayPal alebo iný). "
                "Zaplatenú faktúru už nemožno vrátiť späť na nezaplatenú.",
                "<strong>{{deposit_record_title}}</strong> zaznamená platbu vopred. Faktúra sa potom zobrazí ako <strong>{{invoices_status_partially_paid}}</strong> a záloha nesmie presiahnuť celkovú sumu.",
                "<strong>{{invoices_action_mark_void}}</strong> ponechá faktúru v evidencii, ale označí ju ako zrušenú. Dajte tomu prednosť pred zmazaním — zmazanú faktúru "
                "nemožno obnoviť.",
            ]),
            ("p", "S Pro možno priečinok zákazníka aj uložiť alebo zdieľať ako ZIP s PDF a celý zoznam exportovať pre vášho účtovníka — pozri "
                  "<a href=\"#export\">Export faktúr</a>."),
        ]),
        "export": ("Export faktúr (Excel, CSV, ZIP)", [
            ("p", "K dispozícii s Invoice Cove Pro. Klepnite na ikonu exportu (📄) hore na karte <strong>{{nav_invoices}}</strong>. Ktoré faktúry zahrnúť, vyberiete "
                  "pomocou volieb roka a mesiaca (<strong>{{invoices_export_all}}</strong>, jeden rok alebo jeden mesiac roka — ponúkajú sa len roky a mesiace, "
                  "v ktorých faktúry sú), a potom vyberte, čo s nimi urobiť:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — tabuľka v Exceli (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — tá istá tabuľka ako súbor CSV.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — PDF faktúr v jednom ZIPe, jeden priečinok na zákazníka.",
                "<strong>{{invoices_export_delete}}</strong> — natrvalo zmaže vybrané faktúry po dvoch potvrdeniach.",
            ]),
            ("p", "<em>Uložiť</em> vám nechá vybrať, kam v zariadení súbor pôjde; <em>Zdieľať</em> otvorí zdieľaciu ponuku Androidu, aby ste ho poslali "
                  "e-mailom alebo v chate."),
            ("p", "Excel a CSV sú vytvorené pre vášho účtovníka: <strong>jeden riadok na každú položku faktúry</strong>, pričom údaje o faktúre sa opakujú na každom riadku — "
                  "číslo a dátumy, meno, číslo, daňové číslo, IČ DPH, číslo obchodného registra a adresa zákazníka, popis, množstvo, jednotka, "
                  "cena a čistá suma položky, medzisúčet, zľava, sadzba DPH, suma DPH a spolu faktúry, mena a stav, dátum a "
                  "spôsob platby. Hlavičky stĺpcov a pevné slová (faktúra, zaplatené, nezaplatené, spôsoby platby) sú v jazyku, na ktorý je aplikácia nastavená."),
        ]),
        "new-quote": ("Vytvorenie ponuky", [
            ("p", "<strong>{{home_new_quote_title}}</strong> funguje ako New Invoice — rovnaké polia, rovnaké tlačidlá <strong>{{common_preview_button}}</strong> a <strong>{{common_template_button}}</strong> a rovnaké "
                  "<strong>{{newquote_generate_button}}</strong>, ktoré jedným klepnutím uloží, vytvorí PDF a otvorí ponuku zdieľania — s "
                  "<strong>{{newquote_date_label}}</strong> a dátumom <strong>{{newquote_valid_until_label}}</strong> namiesto dátumu faktúry a splatnosti. "
                  "Ponuky nemajú koncepty."),
        ]),
        "quotes": ("Správa ponúk a prevod na faktúru", [
            ("p", "Obrazovka <strong>{{common_quotes_title}}</strong> (z dlaždice na úvodnej obrazovke) uvádza ponuky podľa zákazníkov, rovnako ako faktúry. Otvorte ponuku, aby ste ju "
                  "zobrazili alebo zdieľali, použite <strong>{{quotes_action_accept}}</strong> alebo <strong>{{quotes_action_decline}}</strong>, keď zákazník odpovie, "
                  "zaznamenajte zálohu alebo ju zmažte. Záloha nesmie presiahnuť celkovú sumu ponuky."),
            ("p", "Keď zákazník ponuku prijme, použite <strong>{{quotes_action_convert_to_invoice}}</strong> a zaškrtnuté položky sa prevedú na skutočnú faktúru, "
                  "samostatne upraviteľnú — splatnosť a zľavu možno ešte upraviť a pôvodná ponuka sa označí ako "
                  "<strong>{{quotes_status_converted}}</strong> a zostane vo vašej evidencii."),
        ]),
        "calendar": ("Kalendár a pripomienky", [
            ("p", "Obrazovka <strong>{{calendar_title}}</strong> je mesačný prehľad pre vaše vlastné poznámky. Klepnutím na deň poznámky zobrazíte alebo pridáte; poznámka má názov a text a "
                  "s voľbou <strong>{{calendar_remind_me}}</strong> a časom vám v daný okamih pošle oznámenie. Prvý deň týždňa sa riadi vaším nastavením."),
            ("p", "Osobitne Invoice Cove posiela pripomienky platieb — miestne oznámenia o faktúrach, ktoré čoskoro budú splatné alebo už splatnosť prekročili. Nič sa neodosiela na server ani z neho neprijíma."),
        ]),
        "reports": ("Prehľady", [
            ("p", "<strong>{{common_reports_title}}</strong> vám dá rýchly prehľad: sumy <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> a <strong>{{reports_stat_overdue}}</strong>, počet faktúr, "
                  "<em>{{reports_revenue_by_month}}</em> a vašich <em>{{reports_top_customers}}</em> podľa fakturovanej sumy."),
            ("p", "Klepnutím na kartu <strong>{{reports_stat_outstanding}}</strong> alebo <strong>{{reports_stat_overdue}}</strong> otvoríte zoznam presne týchto faktúr."),
        ]),
        "settings": ("Údaje o firme a nastavenia", [
            ("p", "Nastavenia otvoríte ikonou ozubeného kolieska — obrazovka sa volá <strong>{{settings_title}}</strong>. Začína vašimi predvoľbami: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} alebo {{settings_theme_dark}}), predvolená "
                  "<strong>{{settings_invoice_template_label}}</strong>, <strong>{{settings_tax_label_label}}</strong> (DPH, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> a <strong>{{settings_due_date_default_label}}</strong> (automaticky vyplní splatnosť, napr. Net 30). "
                  "Pod nimi nasledujú <strong>{{settings_security_label}}</strong> (pozri <a href=\"#app-lock\">Zámok aplikácie</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> a <strong>{{settings_backup_restore_label}}</strong> (pozri <a href=\"#backup\">Záloha a obnovenie</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> si pamätá popisy a ceny položiek, aby ich ponúkala pri písaní; <em>{{common_clear}}</em> ich zabudne, "
                  "bez toho aby sa dotkla vašich faktúr."),
            ("p", "Nižšie je profil vašej firmy, ktorý sa tlačí na každej faktúre a ponuke: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, krátke motto (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, <strong>{{settings_date_format_label}}</strong> dátumov, adresa, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (registračné číslo, základné imanie a podobne), "
                  "<strong>{{settings_business_logo_label}}</strong> a <strong>{{settings_payment_details_label}}</strong> (IBAN, odkaz PayPal.me…). Každé pole "
                  "má príklad a <strong>každé pole, ktoré necháte prázdne, sa na vašich faktúrach jednoducho neobjaví</strong>. Keď skončíte, klepnite na <strong>{{common_done}}</strong>; "
                  "ak odídete s neuloženými zmenami, aplikácia sa najprv opýta."),
            ("p", "Úplne dole: táto <strong>{{settings_user_manual}}</strong> a <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Záloha a obnovenie", [
            ("p", "K dispozícii s Invoice Cove Pro. V <strong>{{settings_backup_restore_label}}</strong> uloží <strong>{{settings_create_backup_title}}</strong> "
                  "všetko — faktúry, ponuky, koncepty, zákazníkov, kalendár, nastavenia, logo aj PDF — do jedného súboru. Zvoľte "
                  "<strong>{{backup_save_button}}</strong>, aby ste ho uložili, kam chcete, alebo <strong>{{backup_share_button}}</strong>, aby ste ho poslali na bezpečné miesto."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> vráti všetko späť — napríklad v novom telefóne. Funguje len na čerstvej inštalácii, kým ste nepridali "
                  "žiadne údaje, takže nikdy nemôže prepísať to, čo už máte. Invoice Cove overí, že je súbor neporušený, a upozorní vás, ak je poškodený, "
                  "nie je zálohou Invoice Cove alebo ho vytvorila novšia verzia aplikácie (najprv aktualizujte)."),
            ("note", "Súbor zálohy <strong>nie je šifrovaný</strong>: ktokoľvek, kto ho má, môže vaše údaje čítať. Uchovajte ho na súkromnom mieste. PIN zámku aplikácie v ňom nie je nikdy "
                     "obsiahnutý."),
        ]),
        "app-lock": ("Zámok aplikácie", [
            ("p", "V <strong>{{settings_security_label}}</strong> môžete zapnúť <strong>{{settings_app_lock_title}}</strong>: Invoice Cove potom požiada o PIN "
                  "(alebo odtlačok prsta), keď sa aplikácia otvorí znova od začiatku alebo po reštarte telefónu — nie pri každom návrate do nej."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: zvoľte štvormiestny PIN a potvrďte ho.",
                "Potom dostanete šesťmiestny <strong>obnovovací kód</strong>, ktorý sa zobrazí len raz. Zapíšte si ho a uložte na bezpečné miesto.",
                "Ak to váš telefón podporuje, odomykajte odtlačkom prsta (<strong>{{security_use_fingerprint}}</strong>).",
                "Zabudli ste PIN? Použite <strong>{{security_forgot_pin}}</strong> a zadajte obnovovací kód. Po 5 chybných pokusoch musíte počkať 30 sekúnd; "
                "čakanie sa s ďalšími chybnými pokusmi predlžuje.",
            ]),
            ("note", "Ak stratíte PIN aj obnovovací kód — a nemáte nastavené odomykanie odtlačkom prsta — nemožno sa vrátiť dnu. Nemôžeme ho za vás "
                     "resetovať."),
        ]),
        "languages": ("Jazyky", [
            ("p", "Invoice Cove hovorí 13 jazykmi: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands a Svenska. Klepnite na okrúhlu ikonu s vlajkou hore v nastaveniach a jazyk sa zmení — aplikácia sa prepne okamžite."),
            ("p", "Text vo vašich PDF a v exportoch do Excelu/CSV sa riadi jazykom, na ktorý je aplikácia nastavená, a táto príručka je dostupná v rovnakých 13 jazykoch "
                  "(použite jazykovú lištu hore na stránke)."),
        ]),
        "templates": ("PDF šablóny", [
            ("p", "Invoice Cove obsahuje 18 návrhov PDF: Classic, Client Color (vo farbe zákazníka), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves a Spooky Hollow."),
            ("p", "Predvolenú šablónu zvoľte v Nastaveniach → <strong>{{settings_invoice_template_label}}</strong>: klepnite na návrh a potom na <strong>{{common_done}}</strong>. Platí "
                  "pre všetko, čo od tej chvíle vytvoríte. Pre jednu faktúru alebo ponuku použite tlačidlo <strong>{{common_template_button}}</strong> "
                  "vo formulári."),
            ("p", "Každá šablóna tlačí rovnaké informácie — údaje o vašej firme, o zákazníkovi, položky s jednotkou a dátumom, súčty, poznámky a "
                  "platobné údaje — ale len to, čo ste vyplnili. Dlhé faktúry pokračujú na druhej strane a súčet zostáva spolu s poslednou položkou."),
        ]),
        "free-vs-pro": ("Bezplatný plán a Invoice Cove Pro", [
            ("p", "Invoice Cove je zadarmo, s niekoľkými rozumnými obmedzeniami:"),
            ("ul", [
                "Až 3 faktúry a 3 ponuky vystavené za kalendárny mesiac",
                "Až 3 zákazníci naraz",
                "Čísla faktúr a ponúk sa prideľujú automaticky a nemožno ich upraviť",
                "Export do Excelu, CSV a ZIP je len v Pro",
                "Záloha a obnovenie sú len v Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> je jediný jednorazový nákup cez Google Play — nie predplatné — ktorý všetky tieto obmedzenia navždy odstráni. "
                  "Koncepty, všetky šablóny a jazyky, zámok aplikácie aj vytváranie, náhľad a zdieľanie dokumentov sú zadarmo pre všetkých. "
                  "Všetky podrobnosti nájdete v <a href=\"terms.html\">Podmienkach používania</a> (po anglicky)."),
        ]),
    },
}
