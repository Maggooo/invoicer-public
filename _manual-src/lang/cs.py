T = {
    "title": "Uživatelská příručka",
    "subtitle": "Vše, co Invoice Cove umí, obrazovku po obrazovce.",
    "meta_desc": "Kompletní uživatelská příručka k aplikaci Invoice Cove - Offline Billing.",
    "lang_label": "Jazyk",
    "brand_alt": "Invoice Cove",
    "toc": "Obsah",
    "footer_questions": "Otázky?",
    "lede": (
        "Invoice Cove funguje celé na vašem zařízení — faktury, nabídky, zákazníci i profil vaší firmy se ukládají lokálně, "
        "ne na žádný server Invoice Cove. <strong>Neshromažďujeme, nevidíme ani nepřijímáme žádná data o vašich fakturách ani o tom, jak aplikaci používáte</strong> "
        "— žádná analytika, žádné sledování, nic se v pozadí nikam neodesílá. "
        "Jediný okamžik, kdy samotná aplikace potřebuje internet, je zpracování jednorázového nákupu Invoice Cove Pro přes Google Play. "
        "Podrobnosti najdete v <a href=\"privacy.html\">Zásadách ochrany osobních údajů</a>."
    ),
    "warn": (
        "<strong>Než aplikaci odinstalujete nebo vymažete její úložiště:</strong> tato data my nikde nezálohujeme. "
        "Odinstalováním Invoice Cove nebo vymazáním jeho úložiště v nastavení Androidu se trvale smažou všechny faktury, nabídky, zákazníci "
        "i nastavení v tomto zařízení — neexistuje kopie v cloudu, ze které by šlo obnovit. Chraňte se: vytvořte zálohu "
        "s Invoice Cove Pro (viz <a href=\"#backup\">Záloha a obnovení</a>) nebo si potřebné exportujte do Excelu, CSV či ZIP "
        "(viz <a href=\"#export\">Export faktur</a>)."
    ),
    "sections": {
        "home": ("Úvodní obrazovka", [
            ("p", "Úvodní obrazovka je váš výchozí bod, s dlaždicí pro každou hlavní akci: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> a "
                  "<strong>{{common_reports_title}}</strong>. Klepnutím na dlaždici se tam hned dostanete."),
            ("p", "Lišta dole vám vždy nabízí rychlý přístup k <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (nová faktura), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> a <strong>{{nav_reports}}</strong>."),
            ("p", "Ikona ozubeného kola (⚙️) v pravém horním rohu většiny obrazovek otevírá <a href=\"#settings\">Údaje o firmě a nastavení</a>."),
        ]),
        "customers": ("Zákazníci", [
            ("p", "Zákazníka přidáte na kartě <strong>{{nav_customers}}</strong> (klepněte na ikonu +), dlaždicí <strong>{{home_new_customer_title}}</strong> "
                  "nebo rovnou při vytváření faktury či nabídky. Povinné je pouze jméno. Nepovinná pole: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, adresa, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} a barva, která dokumenty zákazníka zabarví. Každé pole ukazuje příklad, aby bylo jasné, co tam patří."),
            ("p", "Klepnutím na zákazníka ho můžete upravit (<strong>{{common_edit}}</strong>), otevřít jeho <strong>{{customers_view_history}}</strong> (faktury, nabídky a koncepty) "
                  "nebo ho smazat (<strong>{{common_delete}}</strong>)."),
            ("p", "Na vašich fakturách a nabídkách se údaje o zákazníkovi tisknou pod jeho jménem v pevném pořadí: číslo zákazníka, daňové číslo, DIČ, "
                  "číslo obchodního rejstříku, poté adresa, e-mail a telefon. Co nevyplníte, se prostě netiskne."),
            ("note", "<strong>Ukládání tu funguje jinak než u faktur.</strong> Zákazník má vlastní tlačítko <strong>{{customers_form_save_customer}}</strong> "
                     "(při úpravách <strong>{{customers_form_save_changes}}</strong>) — uloží se ve chvíli, kdy na něj klepnete. Pokud se pokusíte zavřít formulář "
                     "s neuloženými změnami, Invoice Cove se nejprve zeptá na potvrzení."),
            ("note", "Smazání zákazníka nesmaže faktury a nabídky, které jste mu už vystavili. Jeho nedokončené <a href=\"#drafts\">koncepty</a> "
                     "se smažou spolu s ním — předtím se vás aplikace zeptá."),
        ]),
        "new-invoice": ("Vytvoření faktury", [
            ("p", "V <strong>{{nav_new}}</strong> (nebo na dlaždici <strong>{{home_new_invoice_title}}</strong>): vyberte zákazníka — nebo ho rovnou vytvořte — "
                  "nastavte datum faktury a splatnost a poté přidejte položky."),
            ("p", "Klepněte na <strong>{{newinvoice_add_item_details_button}}</strong> a vyplňte popis, množství, cenu za jednotku a případně jednotku "
                  "(např. h, ks nebo kg) a datum a čas. Jednotka se v PDF tiskne vedle množství. Klepnutím na tužku (✏️) u položky ji opravíte, "
                  "koš (🗑️) ji odstraní. Dříve použité popisy a ceny se vám nabízejí při psaní."),
            ("p", "Poté podle potřeby přidejte sazbu daně, <strong>{{newinvoice_discount_label}}</strong> (procento nebo pevnou částku) a "
                  "<strong>{{common_notes_label}}</strong>. Číslo faktury se přiděluje samo (s Pro ho můžete upravit); měnu vyberete vedle něj."),
            ("p", "<strong>{{common_preview_button}}</strong> vytvoří dočasné PDF, abyste viděli, jak vypadá — zatím se nic neukládá. "
                  "Tlačítko <strong>{{common_template_button}}</strong> ukazuje, která šablona se použije; klepnutím vyberete jinou jen pro tento dokument."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> udělá tři věci najednou: uloží fakturu, vytvoří PDF a otevře nabídku sdílení "
                     "vašeho zařízení, abyste ji mohli odeslat. Ještě nejste hotovi? Použijte <strong>{{newinvoice_save_draft_button}}</strong> — viz <a href=\"#drafts\">Koncepty</a>."),
        ]),
        "drafts": ("Koncepty", [
            ("p", "Fakturu, na které ještě pracujete, neztratíte. Jakmile vyberete zákazníka a přidáte alespoň jednu položku nebo poznámku, Invoice Cove "
                  "uchová <strong>koncept</strong> a aktualizuje ho chvíli poté, co přestanete psát — a ještě jednou, když aplikaci opustíte. Při opuštění obrazovky se "
                  "neobjeví otázka „zahodit změny?“; krátká zpráva vám oznámí, že se koncept uložil."),
            ("p", "Klepněte na <strong>{{newinvoice_save_draft_button}}</strong> (pod {{newinvoice_generate_button}}), abyste fakturu záměrně odložili: uloží se a "
                  "formulář se vyprázdní, připravený na další fakturu. Funguje to, jakmile je vybrán zákazník, i před přidáním položek."),
            ("p", "Koncepty najdete v <strong>{{nav_customers}}</strong> → zákazník → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Každý koncept ukazuje, kdy byl naposledy upraven, kolik má položek a jeho celkovou částku. Klepnutím v úpravách "
                  "pokračujete nebo vystavíte fakturu; koš ho smaže."),
            ("ul", [
                "Koncept nikdy nespotřebuje číslo faktury a nepočítá se do bezplatného měsíčního limitu. Číslo se přidělí až při vystavení konečné "
                "faktury — koncept ji pak nahradí.",
                "Koncept si pamatuje datum faktury a splatnost, jen pokud jste je zvolili sami; jinak při znovuotevření použije dnešní datum.",
                "Smazání zákazníka smaže i jeho koncepty (předtím se vás aplikace zeptá). Koncepty jsou součástí zálohy.",
                "Koncepty existují pro faktury; nabídky je nemají.",
            ]),
        ]),
        "invoices": ("Správa faktur", [
            ("p", "Karta <strong>{{nav_invoices}}</strong> seskupuje faktury do složky pro každého zákazníka, které můžete řadit podle "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> nebo <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Otevřením složky uvidíte její faktury seřazené podle data, hodnoty, čísla nebo stavu."),
            ("p", "Každá faktura má stav: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (po splatnosti), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (byla zaznamenána záloha), <strong>{{invoices_status_paid}}</strong> nebo "
                  "<strong>{{invoices_status_void}}</strong>. Klepnutím na fakturu ji zobrazíte ({{common_view}}), znovu odešlete ({{common_share}}), označíte jako zaplacenou nebo stornovanou, případně smažete."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> se zeptá na datum platby a způsob úhrady (převod, hotovost, karta, PayPal nebo jiný). "
                "Zaplacenou fakturu už nelze vrátit zpět na nezaplacenou.",
                "<strong>{{deposit_record_title}}</strong> zaznamená platbu předem. Faktura se pak zobrazí jako <strong>{{invoices_status_partially_paid}}</strong> a záloha nesmí přesáhnout celkovou částku.",
                "<strong>{{invoices_action_mark_void}}</strong> ponechá fakturu v evidenci, ale označí ji jako zrušenou. Dejte tomu přednost před smazáním — smazanou fakturu "
                "nelze obnovit.",
            ]),
            ("p", "S Pro lze složku zákazníka také uložit nebo sdílet jako ZIP s PDF a celý seznam exportovat pro vašeho účetního — viz "
                  "<a href=\"#export\">Export faktur</a>."),
        ]),
        "export": ("Export faktur (Excel, CSV, ZIP)", [
            ("p", "K dispozici s Invoice Cove Pro. Klepněte na ikonu exportu (📄) nahoře na kartě <strong>{{nav_invoices}}</strong>. Které faktury zahrnout, vyberete "
                  "pomocí voleb roku a měsíce (<strong>{{invoices_export_all}}</strong>, jeden rok nebo jeden měsíc roku — nabízejí se jen roky a měsíce, "
                  "ve kterých faktury jsou), a poté vyberte, co s nimi udělat:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — tabulka v Excelu (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — táž tabulka jako soubor CSV.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — PDF faktur v jednom ZIPu, jedna složka na zákazníka.",
                "<strong>{{invoices_export_delete}}</strong> — trvale smaže vybrané faktury po dvou potvrzeních.",
            ]),
            ("p", "<em>Uložit</em> vám nechá vybrat, kam v zařízení soubor půjde; <em>Sdílet</em> otevře sdílecí nabídku Androidu, abyste ho poslali "
                  "e-mailem nebo v chatu."),
            ("p", "Excel a CSV jsou vytvořeny pro vašeho účetního: <strong>jeden řádek na každou položku faktury</strong>, přičemž údaje o faktuře se opakují na každém řádku — "
                  "číslo a data, jméno, číslo, daňové číslo, DIČ, číslo obchodního rejstříku a adresa zákazníka, popis, množství, jednotka, "
                  "cena a čistá částka položky, mezisoučet, sleva, sazba DPH, částka DPH a celkem faktury, měna a stav, datum a "
                  "způsob platby. Záhlaví sloupců a pevná slova (faktura, zaplaceno, nezaplaceno, způsoby platby) jsou v jazyce, na který je aplikace nastavena."),
        ]),
        "new-quote": ("Vytvoření nabídky", [
            ("p", "<strong>{{home_new_quote_title}}</strong> funguje jako New Invoice — stejná pole, stejná tlačítka <strong>{{common_preview_button}}</strong> a <strong>{{common_template_button}}</strong> a stejné "
                  "<strong>{{newquote_generate_button}}</strong>, které jedním klepnutím uloží, vytvoří PDF a otevře nabídku sdílení — s "
                  "<strong>{{newquote_date_label}}</strong> a datem <strong>{{newquote_valid_until_label}}</strong> místo data faktury a splatnosti. "
                  "Nabídky nemají koncepty."),
        ]),
        "quotes": ("Správa nabídek a převod na fakturu", [
            ("p", "Obrazovka <strong>{{common_quotes_title}}</strong> (z dlaždice na úvodní obrazovce) uvádí nabídky podle zákazníků, stejně jako faktury. Otevřete nabídku, abyste ji "
                  "zobrazili nebo sdíleli, použijte <strong>{{quotes_action_accept}}</strong> nebo <strong>{{quotes_action_decline}}</strong>, když zákazník odpoví, "
                  "zaznamenejte zálohu nebo ji smažte. Záloha nesmí přesáhnout celkovou částku nabídky."),
            ("p", "Když zákazník nabídku přijme, použijte <strong>{{quotes_action_convert_to_invoice}}</strong> a zaškrtnuté položky se převedou na skutečnou fakturu, "
                  "samostatně upravitelnou — splatnost a slevu lze ještě upravit a původní nabídka se označí jako "
                  "<strong>{{quotes_status_converted}}</strong> a zůstane ve vaší evidenci."),
        ]),
        "calendar": ("Kalendář a připomínky", [
            ("p", "Obrazovka <strong>{{calendar_title}}</strong> je měsíční přehled pro vaše vlastní poznámky. Klepnutím na den poznámky zobrazíte nebo přidáte; poznámka má název a text a "
                  "s volbou <strong>{{calendar_remind_me}}</strong> a časem vám v daný okamžik pošle oznámení. První den týdne se řídí vaším nastavením."),
            ("p", "Zvlášť Invoice Cove posílá připomínky plateb — místní oznámení o fakturách, které brzy splatnost nebo ji už překročily. Nic se neodesílá na server ani z něj nepřijímá."),
        ]),
        "reports": ("Přehledy", [
            ("p", "<strong>{{common_reports_title}}</strong> vám dá rychlý přehled: částky <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> a <strong>{{reports_stat_overdue}}</strong>, počet faktur, "
                  "<em>{{reports_revenue_by_month}}</em> a vaše <em>{{reports_top_customers}}</em> podle fakturované částky."),
            ("p", "Klepnutím na kartu <strong>{{reports_stat_outstanding}}</strong> nebo <strong>{{reports_stat_overdue}}</strong> otevřete seznam přesně těchto faktur."),
        ]),
        "settings": ("Údaje o firmě a nastavení", [
            ("p", "Nastavení otevřete ikonou ozubeného kola — obrazovka se jmenuje <strong>{{settings_title}}</strong>. Začíná vašimi předvolbami: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} nebo {{settings_theme_dark}}), výchozí "
                  "<strong>{{settings_invoice_template_label}}</strong>, <strong>{{settings_tax_label_label}}</strong> (DPH, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> a <strong>{{settings_due_date_default_label}}</strong> (automaticky vyplní splatnost, např. Net 30). "
                  "Pod nimi následují <strong>{{settings_security_label}}</strong> (viz <a href=\"#app-lock\">Zámek aplikace</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> a <strong>{{settings_backup_restore_label}}</strong> (viz <a href=\"#backup\">Záloha a obnovení</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> si pamatuje popisy a ceny položek, aby je nabízela při psaní; <em>{{common_clear}}</em> je zapomene, "
                  "aniž by se dotkla vašich faktur."),
            ("p", "Níže je profil vaší firmy, který se tiskne na každé faktuře a nabídce: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, krátké motto (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, <strong>{{settings_date_format_label}}</strong> dat, adresa, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (registrační číslo, základní kapitál a podobně), "
                  "<strong>{{settings_business_logo_label}}</strong> a <strong>{{settings_payment_details_label}}</strong> (IBAN, odkaz PayPal.me…). Každé pole "
                  "má příklad a <strong>každé pole, které necháte prázdné, se na vašich fakturách prostě neobjeví</strong>. Až skončíte, klepněte na <strong>{{common_done}}</strong>; "
                  "pokud odejdete s neuloženými změnami, aplikace se nejprve zeptá."),
            ("p", "Úplně dole: tato <strong>{{settings_user_manual}}</strong> a <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Záloha a obnovení", [
            ("p", "K dispozici s Invoice Cove Pro. V <strong>{{settings_backup_restore_label}}</strong> uloží <strong>{{settings_create_backup_title}}</strong> "
                  "vše — faktury, nabídky, koncepty, zákazníky, kalendář, nastavení, logo i PDF — do jednoho souboru. Zvolte "
                  "<strong>{{backup_save_button}}</strong>, abyste ho uložili, kam chcete, nebo <strong>{{backup_share_button}}</strong>, abyste ho poslali na bezpečné místo."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> vrátí vše zpět — například v novém telefonu. Funguje jen na čerstvé instalaci, dokud jste nepřidali "
                  "žádná data, takže nikdy nemůže přepsat to, co už máte. Invoice Cove ověří, že je soubor neporušený, a upozorní vás, je-li poškozený, "
                  "není zálohou Invoice Cove nebo ho vytvořila novější verze aplikace (nejprve aktualizujte)."),
            ("note", "Soubor zálohy <strong>není šifrovaný</strong>: kdokoli, kdo ho má, může vaše data číst. Uchovejte ho na soukromém místě. PIN zámku aplikace v něm není nikdy "
                     "obsažen."),
        ]),
        "app-lock": ("Zámek aplikace", [
            ("p", "V <strong>{{settings_security_label}}</strong> můžete zapnout <strong>{{settings_app_lock_title}}</strong>: Invoice Cove pak požádá o PIN "
                  "(nebo otisk prstu), když se aplikace otevře znovu od začátku nebo po restartu telefonu — ne při každém návratu do ní."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: zvolte čtyřmístný PIN a potvrďte ho.",
                "Poté dostanete šestimístný <strong>obnovovací kód</strong>, který se zobrazí jen jednou. Zapište si ho a uložte na bezpečné místo.",
                "Pokud to váš telefon podporuje, odemykejte otiskem prstu (<strong>{{security_use_fingerprint}}</strong>).",
                "Zapomněli jste PIN? Použijte <strong>{{security_forgot_pin}}</strong> a zadejte obnovovací kód. Po 5 chybných pokusech musíte počkat 30 sekund; "
                "čekání se s dalšími chybnými pokusy prodlužuje.",
            ]),
            ("note", "Pokud ztratíte PIN i obnovovací kód — a nemáte nastavené odemykání otiskem prstu — nelze se dovnitř vrátit. Nemůžeme ho za vás "
                     "resetovat."),
        ]),
        "languages": ("Jazyky", [
            ("p", "Invoice Cove mluví 13 jazyky: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands a Svenska. Klepněte na kulatou ikonu s vlajkou nahoře v nastavení a jazyk se změní — aplikace se přepne okamžitě."),
            ("p", "Text ve vašich PDF a v exportech do Excelu/CSV se řídí jazykem, na který je aplikace nastavena, a tato příručka je dostupná ve stejných 13 jazycích "
                  "(použijte jazykovou lištu nahoře na stránce)."),
        ]),
        "templates": ("PDF šablony", [
            ("p", "Invoice Cove obsahuje 18 návrhů PDF: Classic, Client Color (v barvě zákazníka), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves a Spooky Hollow."),
            ("p", "Výchozí šablonu zvolte v Nastavení → <strong>{{settings_invoice_template_label}}</strong>: klepněte na návrh a poté na <strong>{{common_done}}</strong>. Platí "
                  "pro vše, co od té chvíle vytvoříte. Pro jednu fakturu nebo nabídku použijte tlačítko <strong>{{common_template_button}}</strong> "
                  "ve formuláři."),
            ("p", "Každá šablona tiskne stejné informace — údaje o vaší firmě, o zákazníkovi, položky s jednotkou a datem, součty, poznámky a "
                  "platební údaje — ale jen to, co jste vyplnili. Dlouhé faktury pokračují na druhé straně a součet zůstává společně s poslední položkou."),
        ]),
        "free-vs-pro": ("Bezplatný plán a Invoice Cove Pro", [
            ("p", "Invoice Cove je zdarma, s několika rozumnými omezeními:"),
            ("ul", [
                "Až 3 faktury a 3 nabídky vystavené za kalendářní měsíc",
                "Až 3 zákazníci najednou",
                "Čísla faktur a nabídek se přidělují automaticky a nelze je upravit",
                "Export do Excelu, CSV a ZIP je jen v Pro",
                "Záloha a obnovení jsou jen v Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> je jediný jednorázový nákup přes Google Play — ne předplatné — který všechna tato omezení navždy odstraní. "
                  "Koncepty, všechny šablony a jazyky, zámek aplikace i vytváření, náhled a sdílení dokumentů jsou zdarma pro všechny. "
                  "Všechny podrobnosti najdete v <a href=\"terms.html\">Podmínkách užívání</a>."),
        ]),
    },
}
