T = {
    "title": "Przewodnik użytkownika",
    "subtitle": "Wszystko, co potrafi Invoice Cove, ekran po ekranie.",
    "meta_desc": "Pełny przewodnik użytkownika aplikacji Invoice Cove - Offline Billing.",
    "lang_label": "Język",
    "brand_alt": "Invoice Cove",
    "toc": "Spis treści",
    "footer_questions": "Pytania?",
    "lede": (
        "Invoice Cove działa w całości na Twoim urządzeniu: faktury, oferty, klienci i profil Twojej firmy są przechowywane lokalnie, "
        "a nie na żadnym serwerze Invoice Cove. Nie zbieramy, nie widzimy i nie otrzymujemy żadnych danych o Twoich fakturach ani o tym, "
        "jak korzystasz z aplikacji. Nie ma analityki, śledzenia ani niczego wysyłanego w tle. "
        "Jedyny raz, gdy sama aplikacja potrzebuje internetu, to obsługa jednorazowego zakupu Invoice Cove Pro przez Google Play. "
        "Szczegóły znajdziesz w <a href=\"privacy.html\">Polityce prywatności</a>."
    ),
    "warn": (
        "Pamiętaj! Zanim odinstalujesz aplikację lub wyczyścisz jej dane: my nigdzie nie przechowujemy kopii tych danych. "
        "Odinstalowanie Invoice Cove lub wyczyszczenie jego pamięci w ustawieniach Androida trwale usuwa wszystkie faktury, oferty, klientów "
        "i ustawienia z tego urządzenia — nie ma kopii w chmurze, z której można je przywrócić. Aby chronić swoje pliki: utwórz kopię zapasową "
        "w Invoice Cove Pro (zobacz <a href=\"#backup\">Kopia zapasowa i przywracanie</a>) albo wyeksportuj to, czego potrzebujesz, do Excela, CSV lub ZIP "
        "(zobacz <a href=\"#export\">Eksport faktur</a>)."
    ),
    "sections": {
        "home": ("Ekran główny", [
            ("p", "Ekran główny to Twój punkt wyjścia, z kafelkiem dla każdej głównej czynności: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} i "
                  "{{common_reports_title}}. Dotknij kafelka, aby przejść od razu do danej części."),
            ("p", "Pasek na dole daje szybki dostęp do {{nav_home}}, {{nav_new}} (nowa faktura), "
                  "{{nav_invoices}}, {{nav_customers}} i {{nav_reports}}."),
            ("p", "Ikona koła zębatego (⚙️) w prawym górnym rogu większości ekranów otwiera <a href=\"#settings\">Dane firmy i ustawienia</a>."),
        ]),
        "customers": ("Klienci", [
            ("p", "Aby dodać klienta, przejdź do zakładki {{nav_customers}} i dotknij ikony + albo użyj kafelka {{home_new_customer_title}}. "
                  "Klienta możesz też dodać podczas tworzenia faktury lub oferty. Do utworzenia karty klienta wystarczy nazwa. "
                  "Pola opcjonalne obejmują: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, adres, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} oraz odcień koloru dla dokumentów klienta. Każde pole pokazuje przykład, abyś wiedział, co w nim wpisać."),
            ("p", "Dotknij klienta, aby go edytować ({{common_edit}}), otworzyć jego {{customers_view_history}} (faktury, oferty i szkice) "
                  "lub usunąć ({{common_delete}})."),
            ("p", "Na Twoich fakturach i ofertach dane klienta są drukowane pod jego nazwą w stałej kolejności: numer klienta, numer podatkowy, numer VAT, "
                  "numer rejestru handlowego, a potem adres, e-mail i telefon. Czego nie wypełnisz, nie jest drukowane."),
            ("note", "Zapisywanie działa tu inaczej niż przy fakturach. Klient ma własny przycisk {{customers_form_save_customer}} "
                     "(lub {{customers_form_save_changes}} przy edycji) i zapisuje się w chwili dotknięcia. Jeśli spróbujesz zamknąć formularz "
                     "z niezapisanymi zmianami, Invoice Cove najpierw poprosi o potwierdzenie."),
            ("note", "Usunięcie klienta nie usuwa faktur i ofert, które już mu wystawiłeś. Jego niedokończone <a href=\"#drafts\">szkice</a> "
                     "są jednak usuwane razem z nim; Invoice Cove najpierw poprosi o potwierdzenie."),
        ]),
        "new-invoice": ("Tworzenie faktury", [
            ("p", "W {{nav_new}} (lub na kafelku {{home_new_invoice_title}}): wybierz klienta (albo utwórz go na miejscu) "
                  "i ustaw datę faktury i termin płatności, a potem dodaj pozycje."),
            ("p", "Dotknij {{newinvoice_add_item_details_button}} i wpisz opis, ilość, cenę jednostkową oraz opcjonalnie jednostkę "
                  "(np. godz., szt. lub kg) i datę z godziną. Jednostka jest drukowana obok ilości w PDF-ie. Dotknij ołówka (✏️) przy pozycji, aby ją poprawić, "
                  "albo kosza (🗑️), aby ją usunąć. Wcześniej używane opisy i ceny są podpowiadane podczas pisania."),
            ("p", "Potem dodaj, jeśli to konieczne, stawkę podatku, {{newinvoice_discount_label}} (procent lub kwotę stałą) i "
                  "{{common_notes_label}}. Numer faktury nadawany jest automatycznie (w Invoice Cove Pro można go edytować), a walutę wybierasz obok."),
            ("p", "{{common_preview_button}} tworzy tymczasowy PDF, żebyś zobaczył, jak wygląda — nic jeszcze nie jest zapisywane. "
                  "Przycisk {{common_template_button}} pokazuje, który szablon zostanie użyty; dotknij go, aby wybrać inny tylko dla tego dokumentu."),
            ("note", "{{newinvoice_generate_button}} robi trzy rzeczy naraz: zapisuje fakturę, tworzy PDF i otwiera menu udostępniania "
                     "urządzenia, abyś mógł ją wysłać. Nie jesteś jeszcze gotowy? Użyj {{newinvoice_save_draft_button}} — zobacz <a href=\"#drafts\">Szkice</a>."),
        ]),
        "drafts": ("Szkice", [
            ("p", "Nie stracisz faktury, nad którą jeszcze pracujesz. Gdy tylko wybierzesz klienta i dodasz co najmniej jedną pozycję lub notatkę, Invoice Cove "
                  "zachowuje szkic i aktualizuje go chwilę po tym, jak przestaniesz pisać, oraz jeszcze raz, gdy opuścisz aplikację. Przy wychodzeniu z ekranu nie ma "
                  "pytania „odrzucić zmiany?”; krótki komunikat informuje, że szkic został zapisany."),
            ("p", "Dotknij {{newinvoice_save_draft_button}} (pod {{newinvoice_generate_button}}), aby celowo odłożyć fakturę na bok: zostanie zapisana, a "
                  "formularz wyczyszczony, gotowy na następną fakturę. Działa, gdy tylko wybrany jest klient, nawet przed dodaniem pozycji."),
            ("p", "Szkice znajdziesz w {{nav_customers}} → klient → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Każdy szkic pokazuje, kiedy był ostatnio edytowany, ile ma pozycji i jaką ma sumę. Dotknij go, aby kontynuować "
                  "edycję lub wystawić fakturę; dotknij kosza, aby go usunąć."),
            ("ul", [
                "Szkic nigdy nie zajmuje numeru faktury i nie wlicza się do darmowego limitu miesięcznego. Numer jest nadawany dopiero wtedy, gdy wystawiasz ostateczną "
                "fakturę — szkic zostaje wtedy przez nią zastąpiony.",
                "Szkic zachowuje datę faktury i termin płatności tylko wtedy, gdy wybrałeś je sam; w przeciwnym razie po ponownym otwarciu używa dzisiejszej daty.",
                "Usunięcie klienta usuwa też jego szkice (Invoice Cove najpierw zapyta). Szkice są uwzględniane w kopii zapasowej.",
                "Szkice są dostępne dla faktur; oferty ich nie mają.",
            ]),
        ]),
        "invoices": ("Zarządzanie fakturami", [
            ("p", "Zakładka {{nav_invoices}} grupuje faktury w folder dla każdego klienta, który możesz sortować według "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> lub <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Otwórz folder, aby zobaczyć jego faktury, posortowane według daty, wartości, numeru lub statusu."),
            ("p", "Każda faktura ma status: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (po terminie), "
                  "{{invoices_status_partially_paid}} (zapisano zaliczkę), {{invoices_status_paid}} lub "
                  "{{invoices_status_void}}. Dotknij faktury, aby ją zobaczyć ({{common_view}}), ponownie wysłać ({{common_share}}), oznaczyć jako opłaconą lub anulowaną albo usunąć."),
            ("ul", [
                "{{invoices_action_mark_paid}} pyta o datę płatności i sposób zapłaty (przelew, gotówka, karta, PayPal lub inny). "
                "Opłaconej faktury nie można już cofnąć do nieopłaconej.",
                "{{deposit_record_title}} zapisuje wpłatę z góry. Faktura pokazuje się wtedy jako {{invoices_status_partially_paid}}, a zaliczka nie może przekroczyć sumy.",
                "{{invoices_action_mark_void}} zachowuje fakturę w ewidencji, ale oznacza ją jako anulowaną. To lepsze niż usuwanie, bo usuniętej faktury "
                "nie da się odzyskać.",
            ]),
            ("p", "W Pro folder klienta można też zapisać lub udostępnić jako ZIP z plikami PDF, a całą listę wyeksportować dla księgowego — zobacz "
                  "<a href=\"#export\">Eksport faktur</a>."),
        ]),
        "export": ("Eksport faktur (Excel, CSV, ZIP)", [
            ("p", "Dostępne w Invoice Cove Pro. Dotknij ikony eksportu (📄) u góry zakładki {{nav_invoices}}. Wybierz, które faktury uwzględnić, "
                  "za pomocą wyboru roku i miesiąca ({{invoices_export_all}}, jeden rok lub jeden miesiąc danego roku; oferowane są tylko lata i miesiące, "
                  "w których są faktury), a potem wybierz, co zrobić:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — arkusz Excela (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — ta sama tabela jako plik CSV.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — pliki PDF faktur w jednym ZIP-ie, po jednym folderze na klienta.",
                "{{invoices_export_delete}} — trwale usuwa wybrane faktury po dwóch potwierdzeniach.",
            ]),
            ("p", "<em>Zapisz</em> pozwala wybrać, gdzie w urządzeniu trafi plik; <em>Udostępnij</em> otwiera menu udostępniania Androida, aby wysłać go "
                  "e-mailem lub w wiadomości."),
            ("p", "Excel i CSV są przygotowane dla Twojego księgowego: domyślnie jeden wiersz na fakturę, z numerem i datami, nazwą, numerem, numerem "
                  "podatkowym, numerem VAT, numerem rejestru handlowego i adresem klienta, sumą częściową, rabatem, stawką VAT, kwotą VAT i sumą faktury, walutą oraz "
                  "statusem, datą i sposobem płatności. Nagłówki kolumn i stałe słowa (faktura, opłacona, nieopłacona, sposoby płatności) są zapisane w języku "
                  "ustawionym w aplikacji."),
            ("p", "Aby uzyskać jeden wiersz na każdą pozycję faktury, z danymi faktury powtórzonymi w każdym wierszu oraz dodanym opisem, ilością, "
                  "jednostką, ceną i kwotą netto każdej pozycji, włącz {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Tworzenie oferty", [
            ("p", "Kafelek {{home_new_quote_title}} działa jak kafelek Nowa faktura: te same pola, te same przyciski {{common_preview_button}} i {{common_template_button}}, ten sam "
                  "{{newquote_generate_button}}, który jednym dotknięciem zapisuje, tworzy PDF i otwiera menu udostępniania, ale z "
                  "{{newquote_date_label}} i datą {{newquote_valid_until_label}} zamiast daty faktury i terminu płatności."),
            ("p", "Oferty nie mają szkiców."),
        ]),
        "quotes": ("Zarządzanie ofertami i zamiana na fakturę", [
            ("p", "Ekran {{common_quotes_title}} (z kafelka na ekranie głównym) wyświetla oferty pogrupowane według klientów, tak jak faktury. Otwórz ofertę, aby ją "
                  "zobaczyć lub udostępnić, użyj {{quotes_action_accept}} lub {{quotes_action_decline}}, gdy klient odpowie, "
                  "zapisz zaliczkę albo ją usuń. Zaliczka nie może przekroczyć sumy oferty."),
            ("p", "Gdy klient zaakceptuje ofertę, użyj {{quotes_action_convert_to_invoice}}, aby zamienić zaznaczone pozycje w prawdziwą fakturę, "
                  "edytowalną niezależnie. Termin płatności i rabat można jeszcze zmienić, a pierwotna oferta zostaje oznaczona jako "
                  "{{quotes_status_converted}} i zachowana w Twojej ewidencji."),
        ]),
        "calendar": ("Kalendarz i przypomnienia", [
            ("p", "Ekran {{calendar_title}} to widok miesięczny na Twoje własne notatki. Dotknij dnia, aby zobaczyć lub dodać notatki; notatka ma tytuł i treść, a "
                  "z opcją {{calendar_remind_me}} i godziną wyśle Ci powiadomienie w ustawionym dniu i o ustawionej godzinie. Pierwszy dzień tygodnia zależy od Twoich ustawień."),
            ("p", "Osobno Invoice Cove wysyła przypomnienia o płatnościach — lokalne powiadomienia o fakturach, których termin się zbliża lub minął. Nic nie jest wysyłane na serwer ani z niego odbierane."),
        ]),
        "reports": ("Raporty", [
            ("p", "{{common_reports_title}} daje szybki przegląd: kwoty {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} i {{reports_stat_overdue}}, liczbę faktur, "
                  "<em>{{reports_revenue_by_month}}</em> oraz Twoich <em>{{reports_top_customers}}</em> według zafakturowanej sumy."),
            ("p", "Dotknij karty {{reports_stat_outstanding}} lub {{reports_stat_overdue}}, aby otworzyć listę dokładnie tych faktur."),
        ]),
        "settings": ("Dane firmy i ustawienia", [
            ("p", "Otwórz ustawienia ikoną koła zębatego; ten ekran nazywa się {{settings_title}}. Zaczyna się od Twoich opcjonalnych preferencji: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} lub {{settings_theme_dark}}), domyślny "
                  "{{settings_invoice_template_label}}, {{settings_tax_label_label}} (VAT, GST…), "
                  "{{settings_first_day_of_week_label}} i {{settings_due_date_default_label}}, który automatycznie uzupełnia termin płatności (np. Net 30). "
                  "Poniżej znajdują się {{settings_security_label}} (zobacz <a href=\"#app-lock\">Blokada aplikacji</a>), "
                  "{{settings_item_suggestions_label}} i {{settings_backup_restore_label}} (zobacz <a href=\"#backup\">Kopia zapasowa i przywracanie</a>)."),
            ("p", "{{settings_item_memory_title}} zapamiętuje opisy i ceny pozycji, aby podpowiadać je podczas pisania; <em>{{common_clear}}</em> je zapomina, "
                  "nie ruszając Twoich faktur."),
            ("p", "Niżej jest profil Twojej firmy, drukowany na każdej fakturze i ofercie: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, krótkie hasło ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, {{settings_date_format_label}} dat, adres, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (numer rejestrowy, kapitał zakładowy itp.), "
                  "{{settings_business_logo_label}} i {{settings_payment_details_label}} (IBAN, link PayPal.me). Każde pole "
                  "ma przykład, a każde pole, które zostawisz puste, nie pojawia się na Twoich fakturach. Dotknij {{common_done}}, gdy "
                  "skończysz; jeśli wyjdziesz z niezapisanymi zmianami, zostaniesz poproszony o potwierdzenie."),
            ("p", "Na samym dole wyświetlane są ten {{settings_user_manual}} i {{settings_share_this_app}}."),
        ]),
        "backup": ("Kopia zapasowa i przywracanie", [
            ("p", "Dostępne w Invoice Cove Pro, w sekcji {{settings_backup_restore_label}}. Opcja {{settings_create_backup_title}} zapisuje "
                  "wszystko: faktury, oferty, szkice, klientów, kalendarz, ustawienia, logo i pliki PDF, całość w jednym pliku. Wybierz "
                  "{{backup_save_button}}, aby zapisać go, gdzie chcesz, lub {{backup_share_button}}, aby wysłać go w bezpieczne miejsce."),
            ("p", "{{settings_restore_backup_title}} przywraca wszystko, gdybyś musiał przenieść dane na nowy telefon. Działa tylko na świeżej instalacji, zanim dodasz "
                  "jakiekolwiek dane, więc nigdy nie może nadpisać tego, co już masz. Invoice Cove sprawdza, czy plik jest nienaruszony, i informuje, jeśli jest uszkodzony, "
                  "nie jest kopią Invoice Cove albo został utworzony przez nowszą wersję aplikacji (najpierw zaktualizuj)."),
            ("note", "Plik kopii zapasowej nie jest zaszyfrowany: każdy, kto go ma, może odczytać Twoje dane. Trzymaj go w prywatnym miejscu. PIN blokady aplikacji nigdy "
                     "w nim nie jest zawarty."),
        ]),
        "app-lock": ("Blokada aplikacji", [
            ("p", "W {{settings_security_label}} możesz włączyć {{settings_app_lock_title}}: Invoice Cove poprosi wtedy o PIN "
                  "(lub odcisk palca) przy świeżym uruchomieniu aplikacji lub po ponownym uruchomieniu telefonu — a nie za każdym razem, gdy do niej wracasz."),
            ("ul", [
                "{{settings_set_pin}}: wybierz 4-cyfrowy PIN i potwierdź go.",
                "Następnie dostaniesz 6-cyfrowy kod odzyskiwania, pokazany tylko raz. Zapisz go i przechowuj w bezpiecznym miejscu.",
                "Jeśli telefon to obsługuje, odblokowuj odciskiem palca ({{security_use_fingerprint}}).",
                "Zapomniałeś PIN-u? Użyj {{security_forgot_pin}} i wpisz kod odzyskiwania. Po 5 błędnych próbach musisz poczekać 30 sekund – "
                "czas oczekiwania rośnie przy kolejnych błędnych próbach.",
            ]),
            ("note", "Jeśli stracisz zarówno PIN, jak i kod odzyskiwania i nie masz skonfigurowanego odblokowywania odciskiem palca, nie ma sposobu, by wrócić do aplikacji. Nie możemy go "
                     "zresetować za Ciebie."),
        ]),
        "languages": ("Języki", [
            ("p", "Invoice Cove mówi w 13 językach: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands i Svenska. Dotknij okrągłej ikony z flagą u góry ustawień, aby zmienić język — aplikacja zmienia się od razu."),
            ("p", "Tekst w Twoich plikach PDF i eksportach Excel/CSV podąża za językiem ustawionym w aplikacji, a ten przewodnik jest dostępny w tych samych 13 językach "
                  "(użyj paska języków u góry strony)."),
        ]),
        "templates": ("Szablony PDF", [
            ("p", "Invoice Cove oferuje na razie 18 wzorów PDF: Classic, Client Color (w kolorze klienta), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves i Spooky Hollow."),
            ("p", "Wybierz domyślny szablon w Ustawienia → {{settings_invoice_template_label}}: dotknij wzoru, a potem {{common_done}}. Obowiązuje "
                  "wszystko, co od tej pory wystawisz. Dla pojedynczej faktury lub oferty użyj przycisku {{common_template_button}} "
                  "w formularzu."),
            ("p", "Każdy szablon drukuje te same informacje: dane Twojej firmy, dane klienta, pozycje z jednostką i datą, sumy, notatki i "
                  "dane do płatności — ale tylko to, co wypełniłeś. Długie faktury przechodzą na drugą stronę, a suma pozostaje razem z ostatnią pozycją."),
        ]),
        "free-vs-pro": ("Plan darmowy a Invoice Cove Pro", [
            ("p", "Invoice Cove jest darmowy, z kilkoma rozsądnymi ograniczeniami:"),
            ("ul", [
                "Do 3 faktur wystawionych w miesiącu kalendarzowym",
                "Do 3 ofert wystawionych w miesiącu kalendarzowym",
                "Do 3 klientów jednocześnie",
                "Numery faktur i ofert nadawane są automatycznie i nie można ich edytować",
                "Eksport do Excela, CSV i ZIP jest tylko w Pro",
                "Kopia zapasowa i przywracanie są tylko w Pro",
            ]),
            ("p", "Invoice Cove Pro to jednorazowy zakup przez Google Play (nie subskrypcja), który na stałe znosi wszystkie te ograniczenia. "
                  "Szkice, wszystkie szablony i języki, blokada aplikacji oraz tworzenie, podgląd i udostępnianie dokumentów są darmowe dla wszystkich. "
                  "Pełne szczegóły znajdziesz w <a href=\"terms.html\">Warunkach korzystania</a>."),
        ]),
    },
}
