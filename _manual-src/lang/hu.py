T = {
    "title": "Felhasználói kézikönyv",
    "subtitle": "Minden, amit az Invoice Cove tud, képernyőről képernyőre.",
    "meta_desc": "Teljes felhasználói kézikönyv az Invoice Cove - Offline Billing alkalmazáshoz.",
    "lang_label": "Nyelv",
    "brand_alt": "Invoice Cove",
    "toc": "Tartalom",
    "footer_questions": "Kérdése van?",
    "lede": (
        "Az Invoice Cove teljes egészében az eszközén működik — a számlák, árajánlatok, ügyfelek és a vállalkozása adatai helyben tárolódnak, "
        "nem az Invoice Cove egyik szerverén sem. <strong>Nem gyűjtünk, nem látunk és nem kapunk semmilyen adatot a számláiról vagy arról, hogyan használja az alkalmazást</strong> "
        "— nincs analitika, nincs követés, a háttérben semmi sem kerül elküldésre. "
        "Az egyetlen alkalom, amikor maga az alkalmazás internetet igényel, az Invoice Cove Pro egyszeri vásárlásának feldolgozása a Google Play-en keresztül. "
        "A részleteket az <a href=\"privacy.html\">Adatvédelmi irányelvekben</a> találja."
    ),
    "warn": (
        "<strong>Mielőtt eltávolítja az alkalmazást vagy törli a tárhelyét:</strong> ezeket az adatokat sehol nem mentjük el. "
        "Az Invoice Cove eltávolítása vagy tárhelyének törlése az Android beállításaiban véglegesen töröl minden számlát, árajánlatot, ügyfelet "
        "és beállítást ezen az eszközön — nincs felhőmásolat, amelyből visszaállíthatná. Védekezzen: készítsen biztonsági mentést "
        "az Invoice Cove Pro-val (lásd: <a href=\"#backup\">Mentés és visszaállítás</a>), vagy exportálja, amire szüksége van, Excelbe, CSV-be vagy ZIP-be "
        "(lásd: <a href=\"#export\">Számlák exportálása</a>)."
    ),
    "sections": {
        "home": ("Kezdőképernyő", [
            ("p", "A kezdőképernyő a kiindulópont, minden fő művelethez egy csempével: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> és "
                  "<strong>{{common_reports_title}}</strong>. Egy csempére koppintva rögtön oda jut."),
            ("p", "Az alsó sáv mindig gyors hozzáférést ad a következőkhöz: <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (új számla), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> és <strong>{{nav_reports}}</strong>."),
            ("p", "A legtöbb képernyő jobb felső sarkában a fogaskerék ikon (⚙️) megnyitja a <a href=\"#settings\">Vállalkozás adatai és beállítások</a> részt."),
        ]),
        "customers": ("Ügyfelek", [
            ("p", "Ügyfelet a <strong>{{nav_customers}}</strong> fülön vehet fel (koppintson a + ikonra), a <strong>{{home_new_customer_title}}</strong> csempével, "
                  "vagy közvetlenül számla vagy árajánlat készítése közben. Csak a név kötelező. Nem kötelező mezők: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, cím, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}}, valamint egy szín, amely az ügyfél dokumentumait színezi. Minden mező példát mutat, hogy világos legyen, mi kerül bele."),
            ("p", "Az ügyfélre koppintva szerkesztheti (<strong>{{common_edit}}</strong>), megnyithatja a <strong>{{customers_view_history}}</strong> részt (számlák, árajánlatok és piszkozatok), "
                  "vagy törölheti (<strong>{{common_delete}}</strong>)."),
            ("p", "A számláin és árajánlatain az ügyfél adatai a neve alatt rögzített sorrendben jelennek meg: ügyfélszám, adószám, közösségi adószám, "
                  "cégjegyzékszám, majd cím, e-mail és telefon. Amit nem tölt ki, az egyszerűen nem kerül nyomtatásra."),
            ("note", "<strong>A mentés itt másként működik, mint a számláknál.</strong> Az ügyfélnek saját <strong>{{customers_form_save_customer}}</strong> gombja van "
                     "(szerkesztéskor <strong>{{customers_form_save_changes}}</strong>) — abban a pillanatban mentődik, amikor megérinti. Ha mentetlen módosításokkal próbálja "
                     "bezárni az űrlapot, az Invoice Cove előbb megerősítést kér."),
            ("note", "Az ügyfél törlése nem törli a számára már kiállított számlákat és árajánlatokat. A befejezetlen <a href=\"#drafts\">piszkozatai</a> "
                     "viszont vele együtt törlődnek — az alkalmazás előtte rákérdez."),
        ]),
        "new-invoice": ("Számla készítése", [
            ("p", "A <strong>{{nav_new}}</strong> fülön (vagy a <strong>{{home_new_invoice_title}}</strong> csempével): válasszon ügyfelet — vagy hozzon létre egyet — "
                  "állítsa be a számla dátumát és a fizetési határidőt, majd adja hozzá a tételeket."),
            ("p", "Koppintson a <strong>{{newinvoice_add_item_details_button}}</strong> gombra, és töltse ki a leírást, a mennyiséget, az egységárat, szükség esetén a mértékegységet "
                  "(pl. óra, db vagy kg), valamint a dátumot és az időt. A mértékegység a PDF-ben a mennyiség mellett jelenik meg. A tétel melletti ceruzával (✏️) javíthatja, "
                  "a kukával (🗑️) törölheti. A korábban használt leírásokat és árakat gépelés közben felajánlja."),
            ("p", "Ezután szükség szerint adjon hozzá adókulcsot, <strong>{{newinvoice_discount_label}}</strong> (százalékos vagy fix összegű) és "
                  "<strong>{{common_notes_label}}</strong> mezőt. A számlaszámot az alkalmazás adja (Pro-val szerkeszthető); a pénznemet mellette választhatja ki."),
            ("p", "A <strong>{{common_preview_button}}</strong> ideiglenes PDF-et készít, hogy lássa, hogyan néz ki — ekkor még semmi sem mentődik. "
                  "A <strong>{{common_template_button}}</strong> gomb mutatja, melyik sablon lesz használva; koppintással csak erre a dokumentumra választhat másikat."),
            ("note", "A <strong>{{newinvoice_generate_button}}</strong> egyszerre három dolgot tesz: elmenti a számlát, elkészíti a PDF-et, és megnyitja az eszköz "
                     "megosztás menüjét, hogy elküldhesse. Még nem végzett? Használja a <strong>{{newinvoice_save_draft_button}}</strong> gombot — lásd: <a href=\"#drafts\">Piszkozatok</a>."),
        ]),
        "drafts": ("Piszkozatok", [
            ("p", "A még készülő számlát nem veszíti el. Amint kiválaszt egy ügyfelet és hozzáad legalább egy tételt vagy megjegyzést, az Invoice Cove "
                  "<strong>piszkozatot</strong> őriz, és röviddel a gépelés abbahagyása után frissíti — majd még egyszer, amikor elhagyja az alkalmazást. A képernyő elhagyásakor "
                  "nem jelenik meg „elveti a módosításokat?” kérdés; egy rövid üzenet jelzi, hogy a piszkozat mentve lett."),
            ("p", "Koppintson a <strong>{{newinvoice_save_draft_button}}</strong> gombra (a {{newinvoice_generate_button}} alatt), hogy szándékosan félretegye a számlát: elmentődik, és "
                  "az űrlap kiürül, készen a következő számlára. Ez ügyfél kiválasztása után már működik, tételek hozzáadása előtt is."),
            ("p", "A piszkozatokat itt találja: <strong>{{nav_customers}}</strong> → ügyfél → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Mindegyik megmutatja, mikor módosították utoljára, hány tétele van és mekkora a végösszege. Rákoppintva "
                  "folytathatja a szerkesztést vagy kiállíthatja a számlát; a kuka törli."),
            ("ul", [
                "A piszkozat sosem használ fel számlaszámot, és nem számít bele az ingyenes havi korlátba. A számot csak a végleges számla kiállításakor kapja meg — "
                "a piszkozat ekkor átadja a helyét.",
                "A piszkozat csak akkor jegyzi meg a számla dátumát és a fizetési határidőt, ha Ön maga választotta ki őket; különben újranyitáskor a mai dátumot használja.",
                "Az ügyfél törlése a piszkozatait is törli (az alkalmazás előtte rákérdez). A piszkozatok a biztonsági mentés részei.",
                "Piszkozat csak számlához van; árajánlathoz nincs.",
            ]),
        ]),
        "invoices": ("Számlák kezelése", [
            ("p", "Az <strong>{{nav_invoices}}</strong> fül a számlákat ügyfelenkénti mappákba csoportosítja, amelyeket rendezhet "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> vagy <em>{{invoices_folder_sort_invoice_count}}</em> szerint. "
                  "A mappa megnyitásakor a számlák dátum, érték, szám vagy állapot szerint rendezhetők."),
            ("p", "Minden számlának van állapota: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (lejárt), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (előleget rögzítettek), <strong>{{invoices_status_paid}}</strong> vagy "
                  "<strong>{{invoices_status_void}}</strong>. A számlára koppintva megtekintheti ({{common_view}}), újra elküldheti ({{common_share}}), fizetettnek vagy érvénytelennek jelölheti, vagy törölheti."),
            ("ul", [
                "A <strong>{{invoices_action_mark_paid}}</strong> rákérdez a fizetés dátumára és módjára (átutalás, készpénz, kártya, PayPal vagy egyéb). "
                "A kifizetett számla nem állítható vissza kifizetetlenre.",
                "A <strong>{{deposit_record_title}}</strong> előre kapott összeget rögzít. A számla ekkor <strong>{{invoices_status_partially_paid}}</strong> állapotot kap, és az előleg nem haladhatja meg a végösszeget.",
                "A <strong>{{invoices_action_mark_void}}</strong> megtartja a számlát a nyilvántartásában, de érvénytelennek jelöli. Törlés helyett inkább ezt válassza — a törölt számla "
                "nem állítható vissza.",
            ]),
            ("p", "Pro-val az ügyfél mappáját ZIP-ként, PDF-ekkel is elmentheti vagy megoszthatja, a teljes listát pedig exportálhatja a könyvelőjének — lásd: "
                  "<a href=\"#export\">Számlák exportálása</a>."),
        ]),
        "export": ("Számlák exportálása (Excel, CSV, ZIP)", [
            ("p", "Az Invoice Cove Pro-val érhető el. Koppintson az exportálás ikonra (📄) az <strong>{{nav_invoices}}</strong> fül tetején. A szerepeltetendő számlákat "
                  "az év és hónap választóval adja meg (<strong>{{invoices_export_all}}</strong>, egy év vagy egy év egy hónapja — csak azok az évek és hónapok "
                  "jelennek meg, amelyekben van számla), majd válassza ki, mit tegyen velük:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — Excel-táblázat (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — ugyanaz a táblázat CSV-fájlként.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — a számlák PDF-jei egyetlen ZIP-ben, ügyfelenként egy mappával.",
                "<strong>{{invoices_export_delete}}</strong> — két megerősítés után véglegesen törli a kiválasztott számlákat.",
            ]),
            ("p", "A <em>Mentés</em> lehetővé teszi, hogy kiválassza, hová kerüljön a fájl az eszközön; a <em>Megosztás</em> megnyitja az Android megosztás menüjét, hogy "
                  "e-mailben vagy csevegésben elküldhesse."),
            ("p", "Az Excel és a CSV a könyvelője számára készült: <strong>számlatételenként egy sor</strong>, a számla adatai minden sorban ismétlődnek — "
                  "szám és dátumok, az ügyfél neve, száma, adószáma, közösségi adószáma, cégjegyzékszáma és címe, leírás, mennyiség, mértékegység, "
                  "a tétel egységára és nettó összege, részösszeg, kedvezmény, ÁFA-kulcs, ÁFA-összeg és a számla végösszege, pénznem és állapot, a fizetés dátuma és "
                  "módja. Az oszlopfejlécek és a fix szavak (számla, kifizetett, kifizetetlen, fizetési módok) az alkalmazás beállított nyelvén vannak."),
        ]),
        "new-quote": ("Árajánlat készítése", [
            ("p", "A <strong>{{home_new_quote_title}}</strong> úgy működik, mint a New Invoice — ugyanazok a mezők, ugyanazok a <strong>{{common_preview_button}}</strong> és <strong>{{common_template_button}}</strong> gombok, és ugyanaz a "
                  "<strong>{{newquote_generate_button}}</strong>, amely egy koppintással ment, PDF-et készít és megnyitja a megosztás menüt — a számla dátuma és fizetési határideje helyett "
                  "<strong>{{newquote_date_label}}</strong> és <strong>{{newquote_valid_until_label}}</strong> dátummal. "
                  "Az árajánlatnak nincsenek piszkozatai."),
        ]),
        "quotes": ("Árajánlatok kezelése és számlává alakítás", [
            ("p", "A <strong>{{common_quotes_title}}</strong> képernyő (a kezdőképernyő csempéjéről) az árajánlatokat ügyfelenként sorolja fel, mint a számlákat. Nyisson meg egy árajánlatot, hogy "
                  "megtekintse vagy megossza, használja a <strong>{{quotes_action_accept}}</strong> vagy <strong>{{quotes_action_decline}}</strong> lehetőséget, amikor az ügyfél válaszol, "
                  "rögzítsen előleget, vagy törölje. Az előleg nem haladhatja meg az árajánlat végösszegét."),
            ("p", "Amikor az ügyfél elfogadja az árajánlatot, használja a <strong>{{quotes_action_convert_to_invoice}}</strong> lehetőséget, és a kipipált tételek valódi számlává alakulnak, "
                  "amely külön szerkeszthető — a fizetési határidő és a kedvezmény még módosítható, az eredeti árajánlat pedig "
                  "<strong>{{quotes_status_converted}}</strong> állapotot kap, és megmarad a nyilvántartásában."),
        ]),
        "calendar": ("Naptár és emlékeztetők", [
            ("p", "A <strong>{{calendar_title}}</strong> képernyő havi nézet a saját jegyzeteinek. Egy napra koppintva megtekintheti vagy hozzáadhatja a jegyzeteket; a jegyzetnek címe és szövege van, és "
                  "a <strong>{{calendar_remind_me}}</strong> opcióval és egy időponttal értesítést küld a kiválasztott pillanatban. A hét első napját a beállítása határozza meg."),
            ("p", "Külön, az Invoice Cove fizetési emlékeztetőket küld — helyi értesítéseket azokról a számlákról, amelyek hamarosan lejárnak vagy már lejártak. Semmi sem kerül elküldésre szerverre, és semmit sem fogad onnan."),
        ]),
        "reports": ("Jelentések", [
            ("p", "A <strong>{{common_reports_title}}</strong> gyors áttekintést ad: <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> és <strong>{{reports_stat_overdue}}</strong> összegek, a számlák száma, "
                  "<em>{{reports_revenue_by_month}}</em>, valamint a <em>{{reports_top_customers}}</em> a számlázott összeg szerint."),
            ("p", "Az <strong>{{reports_stat_outstanding}}</strong> vagy <strong>{{reports_stat_overdue}}</strong> kártyára koppintva megnyílik pontosan ezeknek a számláknak a listája."),
        ]),
        "settings": ("Vállalkozás adatai és beállítások", [
            ("p", "A beállításokat a fogaskerék ikonnal nyithatja meg — a képernyő neve <strong>{{settings_title}}</strong>. A saját preferenciáival kezdődik: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} vagy {{settings_theme_dark}}), az alapértelmezett "
                  "<strong>{{settings_invoice_template_label}}</strong>, <strong>{{settings_tax_label_label}}</strong> (ÁFA, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> és <strong>{{settings_due_date_default_label}}</strong> (automatikusan kitölti a fizetési határidőt, pl. Net 30). "
                  "Alattuk következik a <strong>{{settings_security_label}}</strong> (lásd: <a href=\"#app-lock\">Alkalmazászár</a>), "
                  "az <strong>{{settings_item_suggestions_label}}</strong> és a <strong>{{settings_backup_restore_label}}</strong> (lásd: <a href=\"#backup\">Mentés és visszaállítás</a>)."),
            ("p", "A <strong>{{settings_item_memory_title}}</strong> megjegyzi a tételek leírásait és árait, hogy gépelés közben felajánlja őket; a <em>{{common_clear}}</em> elfelejti őket, "
                  "a számláihoz nem nyúl."),
            ("p", "Lejjebb található a vállalkozása profilja, amely minden számlán és árajánlaton megjelenik: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, egy rövid jelmondat (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, a dátumok <strong>{{settings_date_format_label}}</strong> formátuma, cím, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (cégjegyzékszám, jegyzett tőke és hasonlók), "
                  "<strong>{{settings_business_logo_label}}</strong> és <strong>{{settings_payment_details_label}}</strong> (IBAN, PayPal.me hivatkozás…). Minden mezőhöz "
                  "van példa, és <strong>bármelyik üresen hagyott mező egyszerűen nem jelenik meg a számláin</strong>. Ha végzett, koppintson a <strong>{{common_done}}</strong> gombra; "
                  "ha mentetlen módosításokkal lép ki, az alkalmazás előbb rákérdez."),
            ("p", "Legalul: ez a <strong>{{settings_user_manual}}</strong> és a <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Mentés és visszaállítás", [
            ("p", "Az Invoice Cove Pro-val érhető el. A <strong>{{settings_backup_restore_label}}</strong> alatt a <strong>{{settings_create_backup_title}}</strong> "
                  "mindent — számlákat, árajánlatokat, piszkozatokat, ügyfeleket, naptárat, beállításokat, logót és PDF-eket — egyetlen fájlba ment. Válassza a "
                  "<strong>{{backup_save_button}}</strong> lehetőséget, hogy oda mentse, ahová szeretné, vagy a <strong>{{backup_share_button}}</strong> lehetőséget, hogy biztonságos helyre küldje."),
            ("p", "A <strong>{{settings_restore_backup_title}}</strong> mindent visszaállít — például egy új telefonon. Csak friss telepítésen működik, amíg nem adott hozzá "
                  "semmilyen adatot, így soha nem írhatja felül azt, amije már van. Az Invoice Cove ellenőrzi, hogy a fájl sértetlen-e, és figyelmezteti, ha sérült, "
                  "nem Invoice Cove-mentés, vagy az alkalmazás egy újabb verziója készítette (előbb frissítsen)."),
            ("note", "A mentési fájl <strong>nincs titkosítva</strong>: bárki, akinek megvan, elolvashatja az adatait. Tartsa privát helyen. Az alkalmazászár PIN-kódja soha nem "
                     "kerül bele."),
        ]),
        "app-lock": ("Alkalmazászár", [
            ("p", "A <strong>{{settings_security_label}}</strong> alatt bekapcsolhatja a <strong>{{settings_app_lock_title}}</strong> funkciót: az Invoice Cove ekkor PIN-kódot "
                  "(vagy ujjlenyomatot) kér, amikor az alkalmazás elölről nyílik meg, vagy a telefon újraindítása után — nem minden egyes visszatéréskor."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: válasszon négyjegyű PIN-kódot, és erősítse meg.",
                "Ezután kap egy hatjegyű <strong>helyreállítási kódot</strong>, amely csak egyszer jelenik meg. Írja fel, és tartsa biztonságos helyen.",
                "Ha a telefonja támogatja, feloldhat ujjlenyomattal (<strong>{{security_use_fingerprint}}</strong>).",
                "Elfelejtette a PIN-kódot? Használja a <strong>{{security_forgot_pin}}</strong> lehetőséget, és adja meg a helyreállítási kódot. 5 hibás próbálkozás után 30 másodpercet kell várnia; "
                "a várakozás újabb hibás próbálkozásoknál hosszabbodik.",
            ]),
            ("note", "Ha elveszíti a PIN-kódot és a helyreállítási kódot is — és nincs beállítva ujjlenyomatos feloldás —, nem tud visszajutni. Mi nem tudjuk helyette "
                     "visszaállítani."),
        ]),
        "languages": ("Nyelvek", [
            ("p", "Az Invoice Cove 13 nyelven beszél: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands és Svenska. Koppintson a beállítások tetején lévő kerek zászló ikonra, és a nyelv megváltozik — az alkalmazás azonnal átvált."),
            ("p", "A PDF-eiben és az Excel/CSV exportokban a szöveg az alkalmazás beállított nyelvét követi, ez a kézikönyv pedig ugyanezen a 13 nyelven érhető el "
                  "(használja az oldal tetején lévő nyelvválasztó sávot)."),
        ]),
        "templates": ("PDF-sablonok", [
            ("p", "Az Invoice Cove 18 PDF-tervet tartalmaz: Classic, Client Color (az ügyfél színében), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves és Spooky Hollow."),
            ("p", "Az alapértelmezett sablont a Beállítások → <strong>{{settings_invoice_template_label}}</strong> alatt választhatja ki: koppintson egy tervre, majd a <strong>{{common_done}}</strong> gombra. Ez "
                  "mindenre érvényes, amit ettől kezdve készít. Egyetlen számlához vagy árajánlathoz használja az űrlapon lévő <strong>{{common_template_button}}</strong> "
                  "gombot."),
            ("p", "Minden sablon ugyanazokat az információkat nyomtatja — a vállalkozása adatai, az ügyfél adatai, a tételek mértékegységgel és dátummal, az összegek, a megjegyzések és a "
                  "fizetési adatok — de csak azt, amit kitöltött. A hosszú számlák a második oldalon folytatódnak, és a végösszeg az utolsó tétellel együtt marad."),
        ]),
        "free-vs-pro": ("Ingyenes csomag és Invoice Cove Pro", [
            ("p", "Az Invoice Cove ingyenes, néhány ésszerű korláttal:"),
            ("ul", [
                "Naptári havonta legfeljebb 3 kiállított számla és 3 árajánlat",
                "Egyszerre legfeljebb 3 ügyfél",
                "A számla- és árajánlatszámok automatikusan generálódnak, és nem szerkeszthetők",
                "Az Excel-, CSV- és ZIP-export csak Pro-val érhető el",
                "A mentés és visszaállítás csak Pro-val érhető el",
            ]),
            ("p", "Az <strong>Invoice Cove Pro</strong> egyetlen egyszeri vásárlás a Google Play-en keresztül — nem előfizetés —, amely mindezeket a korlátokat végleg megszünteti. "
                  "A piszkozatok, az összes sablon és nyelv, az alkalmazászár, valamint a dokumentumok létrehozása, előnézete és megosztása mindenki számára ingyenes. "
                  "Minden részletet megtalál a <a href=\"terms.html\">Felhasználási feltételekben</a>."),
        ]),
    },
}
