T = {
    "title": "Felhasználói útmutató",
    "subtitle": "Minden, amit az Invoice Cove tud, képernyőről képernyőre.",
    "meta_desc": "Teljes felhasználói útmutató az Invoice Cove - Offline Billing alkalmazáshoz.",
    "lang_label": "Nyelv",
    "brand_alt": "Invoice Cove",
    "toc": "Tartalom",
    "footer_questions": "Kérdése van?",
    "lede": (
        "Az Invoice Cove teljes egészében az eszközén működik: a számlák, árajánlatok, ügyfelek és a vállalkozása adatai helyben tárolódnak, "
        "nem az Invoice Cove egyik szerverén sem. Nem gyűjtünk, nem látunk és nem kapunk semmilyen adatot a számláiról vagy arról, hogyan használja az alkalmazást. "
        "Nincs analitika, nincs követés, a háttérben semmi sem kerül elküldésre. "
        "Az egyetlen alkalom, amikor maga az alkalmazás internetet igényel, az Invoice Cove Pro egyszeri vásárlásának feldolgozása a Google Play-en keresztül. "
        "A részleteket az <a href=\"privacy.html\">Adatvédelmi irányelvekben</a> találja."
    ),
    "warn": (
        "Ne feledje! Mielőtt eltávolítja az alkalmazást vagy törli a tárhelyét: ezeket az adatokat sehol nem mentjük el. "
        "Az Invoice Cove eltávolítása vagy tárhelyének törlése az Android beállításaiban véglegesen töröl minden számlát, árajánlatot, ügyfelet "
        "és beállítást ezen az eszközön — nincs felhőmásolat, amelyből visszaállíthatná. Fájljai védelme érdekében: készítsen biztonsági mentést "
        "az Invoice Cove Pro-val (lásd: <a href=\"#backup\">Mentés és visszaállítás</a>), vagy exportálja, amire szüksége van, Excelbe, CSV-be vagy ZIP-be "
        "(lásd: <a href=\"#export\">Számlák exportálása</a>)."
    ),
    "sections": {
        "home": ("Kezdőképernyő", [
            ("p", "A kezdőképernyő a kiindulópont, minden fő művelethez egy csempével: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} és "
                  "{{common_reports_title}}. Egy csempére koppintva rögtön oda jut."),
            ("p", "Az alsó sáv gyors hozzáférést ad a következőkhöz: {{nav_home}}, {{nav_new}} (új számla), "
                  "{{nav_invoices}}, {{nav_customers}} és {{nav_reports}}."),
            ("p", "A legtöbb képernyő jobb felső sarkában a fogaskerék ikon (⚙️) megnyitja a <a href=\"#settings\">Vállalkozás adatai és beállítások</a> részt."),
        ]),
        "customers": ("Ügyfelek", [
            ("p", "Ügyfél felvételéhez nyissa meg a {{nav_customers}} fület, és koppintson a + ikonra, vagy használja a {{home_new_customer_title}} csempét. "
                  "Számla vagy árajánlat készítése közben is felvehet ügyfelet. Az ügyféladatlap létrehozásához csak a név szükséges. "
                  "A nem kötelező mezők közé tartozik: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, cím, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}}, valamint egy színárnyalat az ügyfél dokumentumaihoz. Minden mező példát mutat, hogy világos legyen, mi kerül bele."),
            ("p", "Az ügyfélre koppintva szerkesztheti ({{common_edit}}), megnyithatja a {{customers_view_history}} részt (számlák, árajánlatok és piszkozatok), "
                  "vagy törölheti ({{common_delete}})."),
            ("p", "A számláin és árajánlatain az ügyfél adatai a neve alatt rögzített sorrendben jelennek meg: ügyfélszám, adószám, közösségi adószám, "
                  "cégjegyzékszám, majd cím, e-mail és telefon. Amit nem tölt ki, az nem kerül nyomtatásra."),
            ("note", "A mentés itt másként működik, mint a számláknál. Az ügyfélnek saját {{customers_form_save_customer}} gombja van "
                     "(szerkesztéskor {{customers_form_save_changes}}), és abban a pillanatban mentődik, amikor megérinti. Ha mentetlen módosításokkal próbálja "
                     "bezárni az űrlapot, az Invoice Cove előbb megerősítést kér."),
            ("note", "Az ügyfél törlése nem törli a számára már kiállított számlákat és árajánlatokat. A befejezetlen <a href=\"#drafts\">piszkozatai</a> "
                     "viszont vele együtt törlődnek; az Invoice Cove előbb megerősítést kér."),
        ]),
        "new-invoice": ("Számla készítése", [
            ("p", "A {{nav_new}} fülön (vagy a {{home_new_invoice_title}} csempével): válasszon ügyfelet (vagy hozzon létre egyet), "
                  "és állítsa be a számla dátumát és a fizetési határidőt, majd adja hozzá a tételeket."),
            ("p", "Koppintson a {{newinvoice_add_item_details_button}} gombra, és töltse ki a leírást, a mennyiséget, az egységárat, szükség esetén a mértékegységet "
                  "(pl. óra, db vagy kg), valamint a dátumot és az időt. A mértékegység a PDF-ben a mennyiség mellett jelenik meg. A tétel melletti ceruzával (✏️) javíthatja, "
                  "a kukával (🗑️) törölheti. A korábban használt leírásokat és árakat gépelés közben felajánlja."),
            ("p", "Ezután szükség esetén adjon hozzá adókulcsot, {{newinvoice_discount_label}} (százalékos vagy fix összegű) és "
                  "{{common_notes_label}} mezőt. A számlaszámot az alkalmazás adja (az Invoice Cove Pro-val szerkeszthető), a pénznemet pedig mellette választhatja ki."),
            ("p", "A {{common_preview_button}} ideiglenes PDF-et készít, hogy lássa, hogyan néz ki — ekkor még semmi sem mentődik. "
                  "A {{common_template_button}} gomb mutatja, melyik sablon lesz használva; koppintással csak erre a dokumentumra választhat másikat."),
            ("note", "A {{newinvoice_generate_button}} egyszerre három dolgot tesz: elmenti a számlát, elkészíti a PDF-et, és megnyitja az eszköz "
                     "megosztás menüjét, hogy elküldhesse. Még nem végzett? Használja a {{newinvoice_save_draft_button}} gombot — lásd: <a href=\"#drafts\">Piszkozatok</a>."),
        ]),
        "drafts": ("Piszkozatok", [
            ("p", "A még készülő számlát nem veszíti el. Amint kiválaszt egy ügyfelet és hozzáad legalább egy tételt vagy megjegyzést, az Invoice Cove "
                  "piszkozatot őriz, és röviddel a gépelés abbahagyása után frissíti, majd még egyszer, amikor elhagyja az alkalmazást. A képernyő elhagyásakor "
                  "nem jelenik meg „elveti a módosításokat?” kérdés; egy rövid üzenet jelzi, hogy a piszkozat mentve lett."),
            ("p", "Koppintson a {{newinvoice_save_draft_button}} gombra (a {{newinvoice_generate_button}} alatt), hogy szándékosan félretegye a számlát: elmentődik, és "
                  "az űrlap kiürül, készen a következő számlára. Ez ügyfél kiválasztása után már működik, tételek hozzáadása előtt is."),
            ("p", "A piszkozatokat itt találja: {{nav_customers}} → ügyfél → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Mindegyik megmutatja, mikor módosították utoljára, hány tétele van és mekkora a végösszege. Rákoppintva "
                  "folytathatja a szerkesztést vagy kiállíthatja a számlát; a kuka törli."),
            ("ul", [
                "A piszkozat sosem használ fel számlaszámot, és nem számít bele az ingyenes havi korlátba. A számot csak a végleges számla kiállításakor kapja meg — "
                "a piszkozat ekkor átadja a helyét.",
                "A piszkozat csak akkor jegyzi meg a számla dátumát és a fizetési határidőt, ha Ön maga választotta ki őket; különben újranyitáskor a mai dátumot használja.",
                "Az ügyfél törlése a piszkozatait is törli (az Invoice Cove előbb rákérdez). A piszkozatok a biztonsági mentés részei.",
                "Piszkozat csak számlához van; árajánlathoz nincs.",
            ]),
        ]),
        "invoices": ("Számlák kezelése", [
            ("p", "Az {{nav_invoices}} fül a számlákat ügyfelenkénti mappákba csoportosítja, amelyeket rendezhet "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> vagy <em>{{invoices_folder_sort_invoice_count}}</em> szerint. "
                  "A mappa megnyitásakor a számlák dátum, érték, szám vagy állapot szerint rendezhetők."),
            ("p", "Minden számlának van állapota: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (lejárt), "
                  "{{invoices_status_partially_paid}} (előleget rögzítettek), {{invoices_status_paid}} vagy "
                  "{{invoices_status_void}}. A számlára koppintva megtekintheti ({{common_view}}), újra elküldheti ({{common_share}}), fizetettnek vagy érvénytelennek jelölheti, vagy törölheti."),
            ("ul", [
                "A {{invoices_action_mark_paid}} rákérdez a fizetés dátumára és módjára (átutalás, készpénz, kártya, PayPal vagy egyéb). "
                "A kifizetett számla nem állítható vissza kifizetetlenre.",
                "A {{deposit_record_title}} előre kapott összeget rögzít. A számla ekkor {{invoices_status_partially_paid}} állapotot kap, és az előleg nem haladhatja meg a végösszeget.",
                "A {{invoices_action_mark_void}} megtartja a számlát a nyilvántartásában, de érvénytelennek jelöli. Ez előnyösebb a törlésnél, mert a törölt számla "
                "nem állítható vissza.",
            ]),
            ("p", "Pro-val az ügyfél mappáját ZIP-ként, PDF-ekkel is elmentheti vagy megoszthatja, a teljes listát pedig exportálhatja a könyvelőjének — lásd: "
                  "<a href=\"#export\">Számlák exportálása</a>."),
        ]),
        "export": ("Számlák exportálása (Excel, CSV, ZIP)", [
            ("p", "Az Invoice Cove Pro-val érhető el. Koppintson az exportálás ikonra (📄) az {{nav_invoices}} fül tetején. A szerepeltetendő számlákat "
                  "az év és hónap választóval adja meg ({{invoices_export_all}}, egy év vagy egy év egy hónapja; csak azok az évek és hónapok "
                  "jelennek meg, amelyekben van számla), majd válassza ki, mit tegyen velük:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — Excel-táblázat (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — ugyanaz a táblázat CSV-fájlként.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — a számlák PDF-jei egyetlen ZIP-ben, ügyfelenként egy mappával.",
                "{{invoices_export_delete}} — két megerősítés után véglegesen törli a kiválasztott számlákat.",
            ]),
            ("p", "A <em>Mentés</em> lehetővé teszi, hogy kiválassza, hová kerüljön a fájl az eszközön; a <em>Megosztás</em> megnyitja az Android megosztás menüjét, hogy "
                  "e-mailben vagy üzenetben elküldhesse."),
            ("p", "Az Excel és a CSV a könyvelője számára készült: alapértelmezés szerint számlánként egy sor, benne a szám és a dátumok, az ügyfél "
                  "neve, száma, adószáma, közösségi adószáma, cégjegyzékszáma és címe, részösszeg, kedvezmény, ÁFA-kulcs, ÁFA-összeg és a számla végösszege, "
                  "pénznem és állapot, a fizetés dátuma és módja. Az oszlopfejlécek és a fix szavak (számla, kifizetett, kifizetetlen, fizetési módok) az "
                  "alkalmazás beállított nyelvén vannak."),
            ("p", "Ha számlatételenként egy sort szeretne, ahol a számla adatai minden sorban ismétlődnek, és minden tétel leírása, mennyisége, "
                  "mértékegysége, egységára és nettó összege is szerepel, kapcsolja be a {{invoices_export_detailed_toggle}} opciót."),
        ]),
        "new-quote": ("Árajánlat készítése", [
            ("p", "A {{home_new_quote_title}} csempe úgy működik, mint az Új számla csempe: ugyanazok a mezők, ugyanazok a {{common_preview_button}} és {{common_template_button}} gombok, ugyanaz a "
                  "{{newquote_generate_button}}, amely egy koppintással ment, PDF-et készít és megnyitja a megosztás menüt, de a számla dátuma és fizetési határideje helyett "
                  "{{newquote_date_label}} és {{newquote_valid_until_label}} dátummal."),
            ("p", "Az árajánlatnak nincsenek piszkozatai."),
        ]),
        "quotes": ("Árajánlatok kezelése és számlává alakítás", [
            ("p", "A {{common_quotes_title}} képernyő (a kezdőképernyő csempéjéről) az árajánlatokat ügyfelenként sorolja fel, mint a számlákat. Nyisson meg egy árajánlatot, hogy "
                  "megtekintse vagy megossza, használja a {{quotes_action_accept}} vagy {{quotes_action_decline}} lehetőséget, amikor az ügyfél válaszol, "
                  "rögzítsen előleget, vagy törölje. Az előleg nem haladhatja meg az árajánlat végösszegét."),
            ("p", "Amikor az ügyfél elfogadja az árajánlatot, használja a {{quotes_action_convert_to_invoice}} lehetőséget, és a kipipált tételek valódi számlává alakulnak, "
                  "amely külön szerkeszthető. A fizetési határidő és a kedvezmény még módosítható, az eredeti árajánlat pedig "
                  "{{quotes_status_converted}} állapotot kap, és megmarad a nyilvántartásában."),
        ]),
        "calendar": ("Naptár és emlékeztetők", [
            ("p", "A {{calendar_title}} képernyő havi nézet a saját jegyzeteinek. Egy napra koppintva megtekintheti vagy hozzáadhatja a jegyzeteket; a jegyzetnek címe és szövege van, és "
                  "a {{calendar_remind_me}} opcióval és egy időponttal értesítést küld a beállított napon és időpontban. A hét első napját a beállításai határozzák meg."),
            ("p", "Külön, az Invoice Cove fizetési emlékeztetőket küld — helyi értesítéseket azokról a számlákról, amelyek hamarosan lejárnak vagy már lejártak. Semmi sem kerül elküldésre szerverre, és semmit sem fogad onnan."),
        ]),
        "reports": ("Jelentések", [
            ("p", "A {{common_reports_title}} gyors áttekintést ad: {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} és {{reports_stat_overdue}} összegek, a számlák száma, "
                  "<em>{{reports_revenue_by_month}}</em>, valamint a <em>{{reports_top_customers}}</em> a számlázott összeg szerint."),
            ("p", "Az {{reports_stat_outstanding}} vagy {{reports_stat_overdue}} kártyára koppintva megnyílik pontosan ezeknek a számláknak a listája."),
        ]),
        "settings": ("Vállalkozás adatai és beállítások", [
            ("p", "A beállításokat a fogaskerék ikonnal nyithatja meg; ennek a képernyőnek a neve {{settings_title}}. A választható preferenciáival kezdődik: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} vagy {{settings_theme_dark}}), az alapértelmezett "
                  "{{settings_invoice_template_label}}, {{settings_tax_label_label}} (ÁFA, GST…), "
                  "{{settings_first_day_of_week_label}} és {{settings_due_date_default_label}}, amely automatikusan kitölti a fizetési határidőt (pl. Net 30). "
                  "Alattuk következik a {{settings_security_label}} (lásd: <a href=\"#app-lock\">Alkalmazászár</a>), "
                  "az {{settings_item_suggestions_label}} és a {{settings_backup_restore_label}} (lásd: <a href=\"#backup\">Mentés és visszaállítás</a>)."),
            ("p", "A {{settings_item_memory_title}} megjegyzi a tételek leírásait és árait, hogy gépelés közben felajánlja őket; a <em>{{common_clear}}</em> elfelejti őket, "
                  "a számláihoz nem nyúl."),
            ("p", "Lejjebb található a vállalkozása profilja, amely minden számlán és árajánlaton megjelenik: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, egy rövid jelmondat ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, a dátumok {{settings_date_format_label}} formátuma, cím, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (cégjegyzékszám, jegyzett tőke és hasonlók), "
                  "{{settings_business_logo_label}} és {{settings_payment_details_label}} (IBAN, PayPal.me hivatkozás). Minden mezőhöz "
                  "van példa, és bármelyik üresen hagyott mező nem jelenik meg a számláin. Ha végzett, koppintson a {{common_done}} gombra; "
                  "ha mentetlen módosításokkal lép ki, az alkalmazás megerősítést kér."),
            ("p", "Legalul jelenik meg ez a {{settings_user_manual}} és a {{settings_share_this_app}}."),
        ]),
        "backup": ("Mentés és visszaállítás", [
            ("p", "Az Invoice Cove Pro-val érhető el, a {{settings_backup_restore_label}} alatt. A {{settings_create_backup_title}} "
                  "mindent elment: számlákat, árajánlatokat, piszkozatokat, ügyfeleket, naptárat, beállításokat, logót és PDF-eket, mindezt egyetlen fájlba. Válassza a "
                  "{{backup_save_button}} lehetőséget, hogy oda mentse, ahová szeretné, vagy a {{backup_share_button}} lehetőséget, hogy biztonságos helyre küldje."),
            ("p", "A {{settings_restore_backup_title}} mindent visszaállít arra az esetre, ha új telefonra kell átköltöznie. Csak friss telepítésen működik, amíg nem adott hozzá "
                  "semmilyen adatot, így soha nem írhatja felül azt, amije már van. Az Invoice Cove ellenőrzi, hogy a fájl sértetlen-e, és figyelmezteti, ha sérült, "
                  "nem Invoice Cove-mentés, vagy az alkalmazás egy újabb verziója készítette (előbb frissítsen)."),
            ("note", "A mentési fájl nincs titkosítva: bárki, akinek megvan, elolvashatja az adatait. Tartsa privát helyen. Az alkalmazászár PIN-kódja soha nem "
                     "kerül bele."),
        ]),
        "app-lock": ("Alkalmazászár", [
            ("p", "A {{settings_security_label}} alatt bekapcsolhatja a {{settings_app_lock_title}} funkciót: az Invoice Cove ekkor PIN-kódot "
                  "(vagy ujjlenyomatot) kér, amikor az alkalmazás elölről nyílik meg, vagy a telefon újraindítása után — nem minden egyes visszatéréskor."),
            ("ul", [
                "{{settings_set_pin}}: válasszon négyjegyű PIN-kódot, és erősítse meg.",
                "Ezután kap egy hatjegyű helyreállítási kódot, amely csak egyszer jelenik meg. Írja fel, és tartsa biztonságos helyen.",
                "Ha a telefonja támogatja, feloldhat ujjlenyomattal ({{security_use_fingerprint}}).",
                "Elfelejtette a PIN-kódot? Használja a {{security_forgot_pin}} lehetőséget, és adja meg a helyreállítási kódot. 5 hibás próbálkozás után 30 másodpercet kell várnia – "
                "a várakozás újabb hibás próbálkozásoknál hosszabbodik.",
            ]),
            ("note", "Ha elveszíti a PIN-kódot és a helyreállítási kódot is, és nincs beállítva ujjlenyomatos feloldás, nem tud visszajutni. Mi nem tudjuk helyette "
                     "visszaállítani."),
        ]),
        "languages": ("Nyelvek", [
            ("p", "Az Invoice Cove 13 nyelven beszél: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands és Svenska. Koppintson a beállítások tetején lévő kerek zászló ikonra, és a nyelv megváltozik — az alkalmazás azonnal átvált."),
            ("p", "A PDF-eiben és az Excel/CSV exportokban a szöveg az alkalmazás beállított nyelvét követi, ez az útmutató pedig ugyanezen a 13 nyelven érhető el "
                  "(használja az oldal tetején lévő nyelvválasztó sávot)."),
        ]),
        "templates": ("PDF-sablonok", [
            ("p", "Az Invoice Cove jelenleg 18 PDF-tervet kínál: Classic, Client Color (az ügyfél színében), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves és Spooky Hollow."),
            ("p", "Az alapértelmezett sablont a Beállítások → {{settings_invoice_template_label}} alatt választhatja ki: koppintson egy tervre, majd a {{common_done}} gombra. Ez "
                  "mindenre érvényes, amit ettől kezdve készít. Egyetlen számlához vagy árajánlathoz használja az űrlapon lévő {{common_template_button}} "
                  "gombot."),
            ("p", "Minden sablon ugyanazokat az információkat nyomtatja: a vállalkozása adatai, az ügyfél adatai, a tételek mértékegységgel és dátummal, az összegek, a megjegyzések és a "
                  "fizetési adatok — de csak azt, amit kitöltött. A hosszú számlák a második oldalon folytatódnak, és a végösszeg az utolsó tétellel együtt marad."),
        ]),
        "free-vs-pro": ("Ingyenes csomag és Invoice Cove Pro", [
            ("p", "Az Invoice Cove ingyenes, néhány ésszerű korláttal:"),
            ("ul", [
                "Naptári havonta legfeljebb 3 kiállított számla",
                "Naptári havonta legfeljebb 3 kiállított árajánlat",
                "Egyszerre legfeljebb 3 ügyfél",
                "A számla- és árajánlatszámok automatikusan generálódnak, és nem szerkeszthetők",
                "Az Excel-, CSV- és ZIP-export csak Pro-val érhető el",
                "A mentés és visszaállítás csak Pro-val érhető el",
            ]),
            ("p", "Az Invoice Cove Pro egyetlen egyszeri vásárlás a Google Play-en keresztül (nem előfizetés), amely mindezeket a korlátokat végleg megszünteti. "
                  "A piszkozatok, az összes sablon és nyelv, az alkalmazászár, valamint a dokumentumok létrehozása, előnézete és megosztása mindenki számára ingyenes. "
                  "Minden részletet megtalál a <a href=\"terms.html\">Felhasználási feltételekben</a>."),
        ]),
    },
}
