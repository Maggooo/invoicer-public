T = {
    "title": "Uživatelská příručka",
    "subtitle": "Vše, co Invoice Cove umí, obrazovku po obrazovce.",
    "meta_desc": "Kompletní uživatelská příručka k aplikaci Invoice Cove - Offline Billing.",
    "lang_label": "Jazyk",
    "brand_alt": "Invoice Cove",
    "toc": "Obsah",
    "footer_questions": "Otázky?",
    "lede": (
        "Invoice Cove funguje celé na vašem zařízení: faktury, nabídky, zákazníci i profil vaší firmy se ukládají lokálně, "
        "ne na žádný server Invoice Cove. Neshromažďujeme, nevidíme ani nepřijímáme žádná data o vašich fakturách ani o tom, jak aplikaci používáte. "
        "Žádná analytika, žádné sledování, nic se v pozadí nikam neodesílá. "
        "Jediný okamžik, kdy samotná aplikace potřebuje internet, je zpracování jednorázového nákupu Invoice Cove Pro přes Google Play. "
        "Podrobnosti najdete v <a href=\"privacy.html\">Zásadách ochrany osobních údajů</a>."
    ),
    "warn": (
        "Nezapomeňte! Než aplikaci odinstalujete nebo vymažete její úložiště: tato data my nikde nezálohujeme. "
        "Odinstalováním Invoice Cove nebo vymazáním jeho úložiště v nastavení Androidu se trvale smažou všechny faktury, nabídky, zákazníci "
        "i nastavení v tomto zařízení — neexistuje kopie v cloudu, ze které by šlo obnovit. Abyste ochránili své soubory: vytvořte zálohu "
        "s Invoice Cove Pro (viz <a href=\"#backup\">Záloha a obnovení</a>) nebo si potřebné exportujte do Excelu, CSV či ZIP "
        "(viz <a href=\"#export\">Export faktur</a>)."
    ),
    "sections": {
        "home": ("Úvodní obrazovka", [
            ("p", "Úvodní obrazovka je váš výchozí bod, s dlaždicí pro každou hlavní akci: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} a "
                  "{{common_reports_title}}. Klepnutím na dlaždici se tam hned dostanete."),
            ("p", "Lišta dole vám nabízí rychlý přístup k {{nav_home}}, {{nav_new}} (nová faktura), "
                  "{{nav_invoices}}, {{nav_customers}} a {{nav_reports}}."),
            ("p", "Ikona ozubeného kola (⚙️) v pravém horním rohu většiny obrazovek otevírá <a href=\"#settings\">Údaje o firmě a nastavení</a>."),
        ]),
        "customers": ("Zákazníci", [
            ("p", "Chcete-li přidat zákazníka, přejděte na kartu {{nav_customers}} a klepněte na ikonu +, nebo použijte dlaždici {{home_new_customer_title}}. "
                  "Zákazníka můžete přidat i při vytváření faktury či nabídky. K vytvoření karty zákazníka stačí jméno. "
                  "Mezi nepovinná pole patří: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, adresa, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} a barevný odstín pro dokumenty zákazníka. Každé pole ukazuje příklad, aby bylo jasné, co tam patří."),
            ("p", "Klepnutím na zákazníka ho můžete upravit ({{common_edit}}), otevřít jeho {{customers_view_history}} (faktury, nabídky a koncepty) "
                  "nebo ho smazat ({{common_delete}})."),
            ("p", "Na vašich fakturách a nabídkách se údaje o zákazníkovi tisknou pod jeho jménem v pevném pořadí: číslo zákazníka, daňové číslo, DIČ, "
                  "číslo obchodního rejstříku, poté adresa, e-mail a telefon. Co nevyplníte, se netiskne."),
            ("note", "Ukládání tu funguje jinak než u faktur. Zákazník má vlastní tlačítko {{customers_form_save_customer}} "
                     "(při úpravách {{customers_form_save_changes}}) a uloží se ve chvíli, kdy na něj klepnete. Pokud se pokusíte zavřít formulář "
                     "s neuloženými změnami, Invoice Cove se nejprve zeptá na potvrzení."),
            ("note", "Smazání zákazníka nesmaže faktury a nabídky, které jste mu už vystavili. Jeho nedokončené <a href=\"#drafts\">koncepty</a> "
                     "se však smažou spolu s ním; Invoice Cove vás nejprve požádá o potvrzení."),
        ]),
        "new-invoice": ("Vytvoření faktury", [
            ("p", "V {{nav_new}} (nebo na dlaždici {{home_new_invoice_title}}): vyberte zákazníka (nebo ho rovnou vytvořte) "
                  "a nastavte datum faktury a splatnost a poté přidejte položky."),
            ("p", "Klepněte na {{newinvoice_add_item_details_button}} a vyplňte popis, množství, cenu za jednotku a případně jednotku "
                  "(např. h, ks nebo kg) a datum a čas. Jednotka se v PDF tiskne vedle množství. Klepnutím na tužku (✏️) u položky ji opravíte, "
                  "koš (🗑️) ji odstraní. Dříve použité popisy a ceny se vám nabízejí při psaní."),
            ("p", "Poté v případě potřeby přidejte sazbu daně, {{newinvoice_discount_label}} (procento nebo pevnou částku) a "
                  "{{common_notes_label}}. Číslo faktury se přiděluje samo (s Invoice Cove Pro ho lze upravit) a měnu vyberete vedle něj."),
            ("p", "{{common_preview_button}} vytvoří dočasné PDF, abyste viděli, jak vypadá — zatím se nic neukládá. "
                  "Tlačítko {{common_template_button}} ukazuje, která šablona se použije; klepnutím vyberete jinou jen pro tento dokument."),
            ("note", "{{newinvoice_generate_button}} udělá tři věci najednou: uloží fakturu, vytvoří PDF a otevře nabídku sdílení "
                     "vašeho zařízení, abyste ji mohli odeslat. Ještě nejste hotovi? Použijte {{newinvoice_save_draft_button}} — viz <a href=\"#drafts\">Koncepty</a>."),
        ]),
        "drafts": ("Koncepty", [
            ("p", "Fakturu, na které ještě pracujete, neztratíte. Jakmile vyberete zákazníka a přidáte alespoň jednu položku nebo poznámku, Invoice Cove "
                  "uchová koncept a aktualizuje ho chvíli poté, co přestanete psát, a ještě jednou, když aplikaci opustíte. Při opuštění obrazovky se "
                  "neobjeví otázka „zahodit změny?“; krátká zpráva vám oznámí, že se koncept uložil."),
            ("p", "Klepněte na {{newinvoice_save_draft_button}} (pod {{newinvoice_generate_button}}), abyste fakturu záměrně odložili: uloží se a "
                  "formulář se vyprázdní, připravený na další fakturu. Funguje to, jakmile je vybrán zákazník, i před přidáním položek."),
            ("p", "Koncepty najdete v {{nav_customers}} → zákazník → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Každý koncept ukazuje, kdy byl naposledy upraven, kolik má položek a jeho celkovou částku. Klepnutím v úpravách "
                  "pokračujete nebo vystavíte fakturu; koš ho smaže."),
            ("ul", [
                "Koncept nikdy nespotřebuje číslo faktury a nepočítá se do bezplatného měsíčního limitu. Číslo se přidělí až při vystavení konečné "
                "faktury — koncept ji pak nahradí.",
                "Koncept si pamatuje datum faktury a splatnost, jen pokud jste je zvolili sami; jinak při znovuotevření použije dnešní datum.",
                "Smazání zákazníka smaže i jeho koncepty (Invoice Cove se vás nejprve zeptá). Koncepty jsou součástí zálohy.",
                "Koncepty existují pro faktury; nabídky je nemají.",
            ]),
        ]),
        "invoices": ("Správa faktur", [
            ("p", "Karta {{nav_invoices}} seskupuje faktury do složky pro každého zákazníka, které můžete řadit podle "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> nebo <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Otevřením složky uvidíte její faktury seřazené podle data, hodnoty, čísla nebo stavu."),
            ("p", "Každá faktura má stav: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (po splatnosti), "
                  "{{invoices_status_partially_paid}} (byla zaznamenána záloha), {{invoices_status_paid}} nebo "
                  "{{invoices_status_void}}. Klepnutím na fakturu ji zobrazíte ({{common_view}}), znovu odešlete ({{common_share}}), označíte jako zaplacenou nebo stornovanou, případně smažete."),
            ("ul", [
                "{{invoices_action_mark_paid}} se zeptá na datum platby a způsob úhrady (převod, hotovost, karta, PayPal nebo jiný). "
                "Zaplacenou fakturu už nelze vrátit zpět na nezaplacenou.",
                "{{deposit_record_title}} zaznamená platbu předem. Faktura se pak zobrazí jako {{invoices_status_partially_paid}} a záloha nesmí přesáhnout celkovou částku.",
                "{{invoices_action_mark_void}} ponechá fakturu v evidenci, ale označí ji jako zrušenou. Je to lepší než smazání, protože smazanou fakturu "
                "nelze obnovit.",
            ]),
            ("p", "S Pro lze složku zákazníka také uložit nebo sdílet jako ZIP s PDF a celý seznam exportovat pro vašeho účetního — viz "
                  "<a href=\"#export\">Export faktur</a>."),
        ]),
        "export": ("Export faktur (Excel, CSV, ZIP)", [
            ("p", "K dispozici s Invoice Cove Pro. Klepněte na ikonu exportu (📄) nahoře na kartě {{nav_invoices}}. Které faktury zahrnout, vyberete "
                  "pomocí voleb roku a měsíce ({{invoices_export_all}}, jeden rok nebo jeden měsíc roku; nabízejí se jen roky a měsíce, "
                  "ve kterých faktury jsou), a poté vyberte, co s nimi udělat:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — tabulka v Excelu (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — táž tabulka jako soubor CSV.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — PDF faktur v jednom ZIPu, jedna složka na zákazníka.",
                "{{invoices_export_delete}} — trvale smaže vybrané faktury po dvou potvrzeních.",
            ]),
            ("p", "<em>Uložit</em> vám nechá vybrat, kam v zařízení soubor půjde; <em>Sdílet</em> otevře sdílecí nabídku Androidu, abyste ho poslali "
                  "e-mailem nebo ve zprávě."),
            ("p", "Excel a CSV jsou vytvořeny pro vašeho účetního: ve výchozím nastavení jeden řádek na fakturu s číslem a daty, jménem, číslem, "
                  "daňovým číslem, DIČ, číslem obchodního rejstříku a adresou zákazníka, mezisoučtem, slevou, sazbou DPH, částkou DPH a celkovou částkou faktury, měnou a stavem, "
                  "datem a způsobem platby. Záhlaví sloupců a pevná slova (faktura, zaplaceno, nezaplaceno, způsoby platby) jsou v jazyce, na který je aplikace "
                  "nastavena."),
            ("p", "Chcete-li získat jeden řádek na každou položku faktury, s údaji o faktuře opakovanými na každém řádku a s přidaným popisem, množstvím, "
                  "jednotkou, cenou a čistou částkou každé položky, zapněte {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Vytvoření nabídky", [
            ("p", "Dlaždice {{home_new_quote_title}} funguje jako dlaždice Nová faktura: stejná pole, stejná tlačítka {{common_preview_button}} a {{common_template_button}}, stejné "
                  "{{newquote_generate_button}}, které jedním klepnutím uloží, vytvoří PDF a otevře nabídku sdílení, ale s "
                  "{{newquote_date_label}} a datem {{newquote_valid_until_label}} místo data faktury a splatnosti."),
            ("p", "Nabídky nemají koncepty."),
        ]),
        "quotes": ("Správa nabídek a převod na fakturu", [
            ("p", "Obrazovka {{common_quotes_title}} (z dlaždice na úvodní obrazovce) uvádí nabídky podle zákazníků, stejně jako faktury. Otevřete nabídku, abyste ji "
                  "zobrazili nebo sdíleli, použijte {{quotes_action_accept}} nebo {{quotes_action_decline}}, když zákazník odpoví, "
                  "zaznamenejte zálohu nebo ji smažte. Záloha nesmí přesáhnout celkovou částku nabídky."),
            ("p", "Když zákazník nabídku přijme, použijte {{quotes_action_convert_to_invoice}} a zaškrtnuté položky se převedou na skutečnou fakturu, "
                  "samostatně upravitelnou. Splatnost a slevu lze ještě upravit a původní nabídka se označí jako "
                  "{{quotes_status_converted}} a zůstane ve vaší evidenci."),
        ]),
        "calendar": ("Kalendář a připomínky", [
            ("p", "Obrazovka {{calendar_title}} je měsíční přehled pro vaše vlastní poznámky. Klepnutím na den poznámky zobrazíte nebo přidáte; poznámka má název a text a "
                  "s volbou {{calendar_remind_me}} a časem vám v nastavené datum a čas pošle oznámení. První den týdne se řídí vaším nastavením."),
            ("p", "Zvlášť Invoice Cove posílá připomínky plateb — místní oznámení o fakturách, které brzy splatnost nebo ji už překročily. Nic se neodesílá na server ani z něj nepřijímá."),
        ]),
        "reports": ("Přehledy", [
            ("p", "{{common_reports_title}} vám dá rychlý přehled: částky {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} a {{reports_stat_overdue}}, počet faktur, "
                  "<em>{{reports_revenue_by_month}}</em> a vaše <em>{{reports_top_customers}}</em> podle fakturované částky."),
            ("p", "Klepnutím na kartu {{reports_stat_outstanding}} nebo {{reports_stat_overdue}} otevřete seznam přesně těchto faktur."),
        ]),
        "settings": ("Údaje o firmě a nastavení", [
            ("p", "Nastavení otevřete ikonou ozubeného kola; tato obrazovka se jmenuje {{settings_title}}. Začíná vašimi volitelnými předvolbami: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} nebo {{settings_theme_dark}}), výchozí "
                  "{{settings_invoice_template_label}}, {{settings_tax_label_label}} (DPH, GST…), "
                  "{{settings_first_day_of_week_label}} a {{settings_due_date_default_label}}, která automaticky vyplní splatnost (např. Net 30). "
                  "Pod nimi následují {{settings_security_label}} (viz <a href=\"#app-lock\">Zámek aplikace</a>), "
                  "{{settings_item_suggestions_label}} a {{settings_backup_restore_label}} (viz <a href=\"#backup\">Záloha a obnovení</a>)."),
            ("p", "{{settings_item_memory_title}} si pamatuje popisy a ceny položek, aby je nabízela při psaní; <em>{{common_clear}}</em> je zapomene, "
                  "aniž by se dotkla vašich faktur."),
            ("p", "Níže je profil vaší firmy, který se tiskne na každé faktuře a nabídce: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, krátké motto ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, {{settings_date_format_label}} dat, adresa, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (registrační číslo, základní kapitál a podobně), "
                  "{{settings_business_logo_label}} a {{settings_payment_details_label}} (IBAN, odkaz PayPal.me). Každé pole "
                  "má příklad a každé pole, které necháte prázdné, se na vašich fakturách neobjeví. Až skončíte, klepněte na {{common_done}}; "
                  "pokud odejdete s neuloženými změnami, budete požádáni o potvrzení."),
            ("p", "Úplně dole se zobrazují tato {{settings_user_manual}} a {{settings_share_this_app}}."),
        ]),
        "backup": ("Záloha a obnovení", [
            ("p", "K dispozici s Invoice Cove Pro, v části {{settings_backup_restore_label}}. {{settings_create_backup_title}} uloží "
                  "vše: faktury, nabídky, koncepty, zákazníky, kalendář, nastavení, logo i PDF, a to vše do jednoho souboru. Zvolte "
                  "{{backup_save_button}}, abyste ho uložili, kam chcete, nebo {{backup_share_button}}, abyste ho poslali na bezpečné místo."),
            ("p", "{{settings_restore_backup_title}} vrátí vše zpět, pokud potřebujete data přenést do nového telefonu. Funguje jen na čerstvé instalaci, dokud jste nepřidali "
                  "žádná data, takže nikdy nemůže přepsat to, co už máte. Invoice Cove ověří, že je soubor neporušený, a upozorní vás, je-li poškozený, "
                  "není zálohou Invoice Cove nebo ho vytvořila novější verze aplikace (nejprve aktualizujte)."),
            ("note", "Soubor zálohy není šifrovaný: kdokoli, kdo ho má, může vaše data číst. Uchovejte ho na soukromém místě. PIN zámku aplikace v něm není nikdy "
                     "obsažen."),
        ]),
        "app-lock": ("Zámek aplikace", [
            ("p", "V {{settings_security_label}} můžete zapnout {{settings_app_lock_title}}: Invoice Cove pak požádá o PIN "
                  "(nebo otisk prstu), když se aplikace otevře znovu od začátku nebo po restartu telefonu — ne při každém návratu do ní."),
            ("ul", [
                "{{settings_set_pin}}: zvolte čtyřmístný PIN a potvrďte ho.",
                "Poté dostanete šestimístný obnovovací kód, který se zobrazí jen jednou. Zapište si ho a uložte na bezpečné místo.",
                "Pokud to váš telefon podporuje, odemykejte otiskem prstu ({{security_use_fingerprint}}).",
                "Zapomněli jste PIN? Použijte {{security_forgot_pin}} a zadejte obnovovací kód. Po 5 chybných pokusech musíte počkat 30 sekund – "
                "čekání se s dalšími chybnými pokusy prodlužuje.",
            ]),
            ("note", "Pokud ztratíte PIN i obnovovací kód a nemáte nastavené odemykání otiskem prstu, nelze se dovnitř vrátit. Nemůžeme ho za vás "
                     "resetovat."),
        ]),
        "languages": ("Jazyky", [
            ("p", "Invoice Cove mluví 13 jazyky: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands a Svenska. Klepněte na kulatou ikonu s vlajkou nahoře v nastavení a jazyk se změní — aplikace se přepne okamžitě."),
            ("p", "Text ve vašich PDF a v exportech do Excelu/CSV se řídí jazykem, na který je aplikace nastavena, a tato příručka je dostupná ve stejných 13 jazycích "
                  "(použijte jazykovou lištu nahoře na stránce)."),
        ]),
        "templates": ("PDF šablony", [
            ("p", "Invoice Cove zatím nabízí 18 návrhů PDF: Classic, Client Color (v barvě zákazníka), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves a Spooky Hollow."),
            ("p", "Výchozí šablonu zvolte v Nastavení → {{settings_invoice_template_label}}: klepněte na návrh a poté na {{common_done}}. Platí "
                  "pro vše, co od té chvíle vytvoříte. Pro jednu fakturu nebo nabídku použijte tlačítko {{common_template_button}} "
                  "ve formuláři."),
            ("p", "Každá šablona tiskne stejné informace: údaje o vaší firmě, o zákazníkovi, položky s jednotkou a datem, součty, poznámky a "
                  "platební údaje — ale jen to, co jste vyplnili. Dlouhé faktury pokračují na druhé straně a součet zůstává společně s poslední položkou."),
        ]),
        "free-vs-pro": ("Bezplatný plán a Invoice Cove Pro", [
            ("p", "Invoice Cove je zdarma, s několika rozumnými omezeními:"),
            ("ul", [
                "Až 3 faktury vystavené za kalendářní měsíc",
                "Až 3 nabídky vystavené za kalendářní měsíc",
                "Až 3 zákazníci najednou",
                "Čísla faktur a nabídek se přidělují automaticky a nelze je upravit",
                "Export do Excelu, CSV a ZIP je jen v Pro",
                "Záloha a obnovení jsou jen v Pro",
            ]),
            ("p", "Invoice Cove Pro je jediný jednorázový nákup přes Google Play (ne předplatné), který všechna tato omezení navždy odstraní. "
                  "Koncepty, všechny šablony a jazyky, zámek aplikace i vytváření, náhled a sdílení dokumentů jsou zdarma pro všechny. "
                  "Všechny podrobnosti najdete v <a href=\"terms.html\">Podmínkách užívání</a>."),
        ]),
    },
}
