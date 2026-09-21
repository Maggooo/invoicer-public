T = {
    "title": "Instrukcja obsługi",
    "subtitle": "Wszystko, co potrafi Invoice Cove, ekran po ekranie.",
    "meta_desc": "Pełna instrukcja obsługi aplikacji Invoice Cove - Offline Billing.",
    "lang_label": "Język",
    "brand_alt": "Invoice Cove",
    "toc": "Spis treści",
    "footer_questions": "Pytania?",
    "lede": (
        "Invoice Cove działa w całości na Twoim urządzeniu — faktury, oferty, klienci i profil Twojej firmy są przechowywane lokalnie, "
        "a nie na żadnym serwerze Invoice Cove. <strong>Nie zbieramy, nie widzimy i nie otrzymujemy żadnych danych o Twoich fakturach ani o tym, "
        "jak korzystasz z aplikacji</strong> — nie ma analityki, śledzenia ani niczego wysyłanego w tle. "
        "Jedyny raz, gdy sama aplikacja potrzebuje internetu, to obsługa jednorazowego zakupu Invoice Cove Pro przez Google Play. "
        "Szczegóły znajdziesz w <a href=\"privacy.html\">Polityce prywatności</a>."
    ),
    "warn": (
        "<strong>Zanim odinstalujesz aplikację lub wyczyścisz jej dane:</strong> my nigdzie nie przechowujemy kopii tych danych. "
        "Odinstalowanie Invoice Cove lub wyczyszczenie jego pamięci w ustawieniach Androida trwale usuwa wszystkie faktury, oferty, klientów "
        "i ustawienia z tego urządzenia — nie ma kopii w chmurze, z której można je przywrócić. Zabezpiecz się: utwórz kopię zapasową "
        "w Invoice Cove Pro (zobacz <a href=\"#backup\">Kopia zapasowa i przywracanie</a>) albo wyeksportuj to, czego potrzebujesz, do Excela, CSV lub ZIP "
        "(zobacz <a href=\"#export\">Eksport faktur</a>)."
    ),
    "sections": {
        "home": ("Ekran główny", [
            ("p", "Ekran główny to Twój punkt wyjścia, z kafelkiem dla każdej głównej czynności: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> i "
                  "<strong>{{common_reports_title}}</strong>. Dotknij kafelka, aby przejść od razu do danej części."),
            ("p", "Pasek na dole zawsze daje szybki dostęp do <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (nowa faktura), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> i <strong>{{nav_reports}}</strong>."),
            ("p", "Ikona koła zębatego (⚙️) w prawym górnym rogu większości ekranów otwiera <a href=\"#settings\">Dane firmy i ustawienia</a>."),
        ]),
        "customers": ("Klienci", [
            ("p", "Dodaj klienta z zakładki <strong>{{nav_customers}}</strong> (dotknij ikony +), za pomocą kafelka <strong>{{home_new_customer_title}}</strong> "
                  "albo od razu podczas tworzenia faktury lub oferty. Obowiązkowa jest tylko nazwa. Pola opcjonalne: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, adres, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} oraz kolor, który nadaje odcień dokumentom klienta. Każde pole pokazuje przykład, abyś wiedział, co w nim wpisać."),
            ("p", "Dotknij klienta, aby go edytować (<strong>{{common_edit}}</strong>), otworzyć jego <strong>{{customers_view_history}}</strong> (faktury, oferty i szkice) "
                  "lub usunąć (<strong>{{common_delete}}</strong>)."),
            ("p", "Na Twoich fakturach i ofertach dane klienta są drukowane pod jego nazwą w stałej kolejności: numer klienta, numer podatkowy, numer VAT, "
                  "numer rejestru handlowego, a potem adres, e-mail i telefon. Czego nie wypełnisz, po prostu się nie drukuje."),
            ("note", "<strong>Zapisywanie działa tu inaczej niż przy fakturach.</strong> Klient ma własny przycisk <strong>{{customers_form_save_customer}}</strong> "
                     "(lub <strong>{{customers_form_save_changes}}</strong> przy edycji) — zapisuje się w chwili dotknięcia. Jeśli spróbujesz zamknąć formularz "
                     "z niezapisanymi zmianami, Invoice Cove najpierw poprosi o potwierdzenie."),
            ("note", "Usunięcie klienta nie usuwa faktur i ofert, które już mu wystawiłeś. Jego niedokończone <a href=\"#drafts\">szkice</a> "
                     "są usuwane razem z nim — najpierw zostaniesz zapytany."),
        ]),
        "new-invoice": ("Tworzenie faktury", [
            ("p", "W <strong>{{nav_new}}</strong> (lub na kafelku <strong>{{home_new_invoice_title}}</strong>): wybierz klienta — albo utwórz go na miejscu — "
                  "ustaw datę faktury i termin płatności, a potem dodaj pozycje."),
            ("p", "Dotknij <strong>{{newinvoice_add_item_details_button}}</strong> i wpisz opis, ilość, cenę jednostkową oraz opcjonalnie jednostkę "
                  "(np. godz., szt. lub kg) i datę z godziną. Jednostka jest drukowana obok ilości w PDF-ie. Dotknij ołówka (✏️) przy pozycji, aby ją poprawić, "
                  "albo kosza (🗑️), aby ją usunąć. Wcześniej używane opisy i ceny są podpowiadane podczas pisania."),
            ("p", "Potem dodaj, jeśli potrzebujesz, stawkę podatku, <strong>{{newinvoice_discount_label}}</strong> (procent lub kwotę stałą) i "
                  "<strong>{{common_notes_label}}</strong>. Numer faktury nadawany jest automatycznie (w Pro możesz go edytować); walutę wybierasz obok."),
            ("p", "<strong>{{common_preview_button}}</strong> tworzy tymczasowy PDF, żebyś zobaczył, jak wygląda — nic jeszcze nie jest zapisywane. "
                  "Przycisk <strong>{{common_template_button}}</strong> pokazuje, który szablon zostanie użyty; dotknij go, aby wybrać inny tylko dla tego dokumentu."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> robi trzy rzeczy naraz: zapisuje fakturę, tworzy PDF i otwiera menu udostępniania "
                     "urządzenia, abyś mógł ją wysłać. Nie jesteś jeszcze gotowy? Użyj <strong>{{newinvoice_save_draft_button}}</strong> — zobacz <a href=\"#drafts\">Szkice</a>."),
        ]),
        "drafts": ("Szkice", [
            ("p", "Nie stracisz faktury, nad którą jeszcze pracujesz. Gdy tylko wybierzesz klienta i dodasz co najmniej jedną pozycję lub notatkę, Invoice Cove "
                  "zachowuje <strong>szkic</strong> i aktualizuje go chwilę po tym, jak przestaniesz pisać — oraz jeszcze raz, gdy opuścisz aplikację. Przy wychodzeniu z ekranu nie ma "
                  "pytania „odrzucić zmiany?”; krótki komunikat informuje, że szkic został zapisany."),
            ("p", "Dotknij <strong>{{newinvoice_save_draft_button}}</strong> (pod {{newinvoice_generate_button}}), aby celowo odłożyć fakturę na bok: zostanie zapisana, a "
                  "formularz wyczyszczony, gotowy na następną fakturę. Działa, gdy tylko wybrany jest klient, nawet przed dodaniem pozycji."),
            ("p", "Szkice znajdziesz w <strong>{{nav_customers}}</strong> → klient → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Każdy szkic pokazuje, kiedy był ostatnio edytowany, ile ma pozycji i jaką ma sumę. Dotknij go, aby kontynuować "
                  "edycję lub wystawić fakturę; dotknij kosza, aby go usunąć."),
            ("ul", [
                "Szkic nigdy nie zajmuje numeru faktury i nie wlicza się do darmowego limitu miesięcznego. Numer jest nadawany dopiero wtedy, gdy wystawiasz ostateczną "
                "fakturę — szkic zostaje wtedy przez nią zastąpiony.",
                "Szkic zachowuje datę faktury i termin płatności tylko wtedy, gdy wybrałeś je sam; w przeciwnym razie po ponownym otwarciu używa dzisiejszej daty.",
                "Usunięcie klienta usuwa też jego szkice (najpierw zostaniesz zapytany). Szkice są uwzględniane w kopii zapasowej.",
                "Szkice są dostępne dla faktur; oferty ich nie mają.",
            ]),
        ]),
        "invoices": ("Zarządzanie fakturami", [
            ("p", "Zakładka <strong>{{nav_invoices}}</strong> grupuje faktury w folder dla każdego klienta, który możesz sortować według "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> lub <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Otwórz folder, aby zobaczyć jego faktury, posortowane według daty, wartości, numeru lub statusu."),
            ("p", "Każda faktura ma status: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (po terminie), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (zapisano zaliczkę), <strong>{{invoices_status_paid}}</strong> lub "
                  "<strong>{{invoices_status_void}}</strong>. Dotknij faktury, aby ją zobaczyć ({{common_view}}), ponownie wysłać ({{common_share}}), oznaczyć jako opłaconą lub anulowaną albo usunąć."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> pyta o datę płatności i sposób zapłaty (przelew, gotówka, karta, PayPal lub inny). "
                "Opłaconej faktury nie można już cofnąć do nieopłaconej.",
                "<strong>{{deposit_record_title}}</strong> zapisuje wpłatę z góry. Faktura pokazuje się wtedy jako <strong>{{invoices_status_partially_paid}}</strong>, a zaliczka nie może przekroczyć sumy.",
                "<strong>{{invoices_action_mark_void}}</strong> zachowuje fakturę w ewidencji, ale oznacza ją jako anulowaną. Wybieraj to zamiast usuwania — usuniętej faktury "
                "nie da się odzyskać.",
            ]),
            ("p", "W Pro folder klienta można też zapisać lub udostępnić jako ZIP z plikami PDF, a całą listę wyeksportować dla księgowego — zobacz "
                  "<a href=\"#export\">Eksport faktur</a>."),
        ]),
        "export": ("Eksport faktur (Excel, CSV, ZIP)", [
            ("p", "Dostępne w Invoice Cove Pro. Dotknij ikony eksportu (📄) u góry zakładki <strong>{{nav_invoices}}</strong>. Wybierz, które faktury uwzględnić, "
                  "za pomocą wyboru roku i miesiąca (<strong>{{invoices_export_all}}</strong>, jeden rok lub jeden miesiąc danego roku — oferowane są tylko lata i miesiące, "
                  "w których są faktury), a potem wybierz, co zrobić:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — arkusz Excela (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — ta sama tabela jako plik CSV.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — pliki PDF faktur w jednym ZIP-ie, po jednym folderze na klienta.",
                "<strong>{{invoices_export_delete}}</strong> — trwale usuwa wybrane faktury, po dwóch potwierdzeniach.",
            ]),
            ("p", "<em>Zapisz</em> pozwala wybrać, gdzie w urządzeniu trafi plik; <em>Udostępnij</em> otwiera menu udostępniania Androida, aby wysłać go "
                  "e-mailem lub w czacie."),
            ("p", "Excel i CSV są przygotowane dla Twojego księgowego: <strong>jeden wiersz na każdą pozycję faktury</strong>, z danymi faktury powtórzonymi w każdym wierszu — "
                  "numer i daty, nazwa, numer, numer podatkowy, numer VAT, numer rejestru handlowego i adres klienta, opis, ilość, jednostka, "
                  "cena i kwota netto pozycji, suma częściowa, rabat, stawka VAT, kwota VAT i suma faktury, waluta oraz status, data i "
                  "sposób płatności. Nagłówki kolumn i stałe słowa (faktura, opłacona, nieopłacona, sposoby płatności) są zapisane w języku ustawionym w aplikacji."),
        ]),
        "new-quote": ("Tworzenie oferty", [
            ("p", "<strong>{{home_new_quote_title}}</strong> działa jak New Invoice — te same pola, te same przyciski <strong>{{common_preview_button}}</strong> i <strong>{{common_template_button}}</strong> oraz ten sam "
                  "<strong>{{newquote_generate_button}}</strong>, który jednym dotknięciem zapisuje, tworzy PDF i otwiera menu udostępniania — z "
                  "<strong>{{newquote_date_label}}</strong> i datą <strong>{{newquote_valid_until_label}}</strong> zamiast daty faktury i terminu płatności. "
                  "Oferty nie mają szkiców."),
        ]),
        "quotes": ("Zarządzanie ofertami i zamiana na fakturę", [
            ("p", "Ekran <strong>{{common_quotes_title}}</strong> (z kafelka na ekranie głównym) wyświetla oferty pogrupowane według klientów, tak jak faktury. Otwórz ofertę, aby ją "
                  "zobaczyć lub udostępnić, użyj <strong>{{quotes_action_accept}}</strong> lub <strong>{{quotes_action_decline}}</strong>, gdy klient odpowie, "
                  "zapisz zaliczkę albo ją usuń. Zaliczka nie może przekroczyć sumy oferty."),
            ("p", "Gdy klient zaakceptuje ofertę, użyj <strong>{{quotes_action_convert_to_invoice}}</strong>, aby zamienić zaznaczone pozycje w prawdziwą fakturę, "
                  "edytowalną niezależnie — termin płatności i rabat można jeszcze zmienić, a pierwotna oferta zostaje oznaczona jako "
                  "<strong>{{quotes_status_converted}}</strong> i zachowana w Twojej ewidencji."),
        ]),
        "calendar": ("Kalendarz i przypomnienia", [
            ("p", "Ekran <strong>{{calendar_title}}</strong> to widok miesiąca na Twoje własne notatki. Dotknij dnia, aby zobaczyć lub dodać notatki; notatka ma tytuł i treść, a "
                  "z opcją <strong>{{calendar_remind_me}}</strong> i godziną wyśle Ci powiadomienie w tej chwili. Pierwszy dzień tygodnia zależy od Twojego ustawienia."),
            ("p", "Osobno Invoice Cove wysyła przypomnienia o płatnościach — lokalne powiadomienia o fakturach, których termin się zbliża lub minął. Nic nie jest wysyłane na serwer ani z niego odbierane."),
        ]),
        "reports": ("Raporty", [
            ("p", "<strong>{{common_reports_title}}</strong> daje szybki przegląd: kwoty <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> i <strong>{{reports_stat_overdue}}</strong>, liczbę faktur, "
                  "<em>{{reports_revenue_by_month}}</em> oraz Twoich <em>{{reports_top_customers}}</em> według zafakturowanej sumy."),
            ("p", "Dotknij karty <strong>{{reports_stat_outstanding}}</strong> lub <strong>{{reports_stat_overdue}}</strong>, aby otworzyć listę dokładnie tych faktur."),
        ]),
        "settings": ("Dane firmy i ustawienia", [
            ("p", "Otwórz ustawienia ikoną koła zębatego — ekran nazywa się <strong>{{settings_title}}</strong>. Zaczyna się od Twoich preferencji: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} lub {{settings_theme_dark}}), domyślny "
                  "<strong>{{settings_invoice_template_label}}</strong>, <strong>{{settings_tax_label_label}}</strong> (VAT, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> i <strong>{{settings_due_date_default_label}}</strong> (automatycznie uzupełnia termin płatności, np. Net 30). "
                  "Poniżej znajdują się <strong>{{settings_security_label}}</strong> (zobacz <a href=\"#app-lock\">Blokada aplikacji</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> i <strong>{{settings_backup_restore_label}}</strong> (zobacz <a href=\"#backup\">Kopia zapasowa i przywracanie</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> zapamiętuje opisy i ceny pozycji, aby podpowiadać je podczas pisania; <em>{{common_clear}}</em> je zapomina, "
                  "nie ruszając Twoich faktur."),
            ("p", "Niżej jest profil Twojej firmy, drukowany na każdej fakturze i ofercie: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, krótkie hasło (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, <strong>{{settings_date_format_label}}</strong> dat, adres, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (numer rejestrowy, kapitał zakładowy itp.), "
                  "<strong>{{settings_business_logo_label}}</strong> i <strong>{{settings_payment_details_label}}</strong> (IBAN, link PayPal.me…). Każde pole "
                  "ma przykład, a <strong>każde pole, które zostawisz puste, po prostu nie pojawia się na Twoich fakturach</strong>. Dotknij <strong>{{common_done}}</strong>, gdy "
                  "skończysz; jeśli wyjdziesz z niezapisanymi zmianami, najpierw zostaniesz zapytany."),
            ("p", "Na samym dole: ta <strong>{{settings_user_manual}}</strong> i <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Kopia zapasowa i przywracanie", [
            ("p", "Dostępne w Invoice Cove Pro. W <strong>{{settings_backup_restore_label}}</strong> opcja <strong>{{settings_create_backup_title}}</strong> zapisuje "
                  "wszystko — faktury, oferty, szkice, klientów, kalendarz, ustawienia, logo i pliki PDF — w jednym pliku. Wybierz "
                  "<strong>{{backup_save_button}}</strong>, aby zapisać go, gdzie chcesz, lub <strong>{{backup_share_button}}</strong>, aby wysłać go w bezpieczne miejsce."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> przywraca wszystko — na przykład na nowym telefonie. Działa tylko na świeżej instalacji, zanim dodasz "
                  "jakiekolwiek dane, więc nigdy nie może nadpisać tego, co już masz. Invoice Cove sprawdza, czy plik jest nienaruszony, i informuje, jeśli jest uszkodzony, "
                  "nie jest kopią Invoice Cove albo został utworzony przez nowszą wersję aplikacji (najpierw zaktualizuj)."),
            ("note", "Plik kopii zapasowej <strong>nie jest zaszyfrowany</strong>: każdy, kto go ma, może odczytać Twoje dane. Trzymaj go w prywatnym miejscu. PIN blokady aplikacji nigdy "
                     "w nim nie jest zawarty."),
        ]),
        "app-lock": ("Blokada aplikacji", [
            ("p", "W <strong>{{settings_security_label}}</strong> możesz włączyć <strong>{{settings_app_lock_title}}</strong>: Invoice Cove poprosi wtedy o PIN "
                  "(lub odcisk palca) przy świeżym uruchomieniu aplikacji lub po ponownym uruchomieniu telefonu — a nie za każdym razem, gdy do niej wracasz."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: wybierz 4-cyfrowy PIN i potwierdź go.",
                "Następnie dostaniesz 6-cyfrowy <strong>kod odzyskiwania</strong>, pokazany tylko raz. Zapisz go i przechowuj w bezpiecznym miejscu.",
                "Jeśli telefon to obsługuje, odblokowuj odciskiem palca (<strong>{{security_use_fingerprint}}</strong>).",
                "Zapomniałeś PIN-u? Użyj <strong>{{security_forgot_pin}}</strong> i wpisz kod odzyskiwania. Po 5 błędnych próbach musisz poczekać 30 sekund; "
                "czas oczekiwania rośnie przy kolejnych błędnych próbach.",
            ]),
            ("note", "Jeśli stracisz zarówno PIN, jak i kod odzyskiwania — a nie masz skonfigurowanego odblokowywania odciskiem palca — nie ma sposobu, by wrócić do aplikacji. Nie możemy go "
                     "zresetować za Ciebie."),
        ]),
        "languages": ("Języki", [
            ("p", "Invoice Cove mówi w 13 językach: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands i Svenska. Dotknij okrągłej ikony z flagą u góry ustawień, aby zmienić język — aplikacja zmienia się od razu."),
            ("p", "Tekst w Twoich plikach PDF i eksportach Excel/CSV podąża za językiem ustawionym w aplikacji, a ta instrukcja jest dostępna w tych samych 13 językach "
                  "(użyj paska języków u góry strony)."),
        ]),
        "templates": ("Szablony PDF", [
            ("p", "Invoice Cove ma 18 wzorów PDF: Classic, Client Color (w kolorze klienta), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves i Spooky Hollow."),
            ("p", "Wybierz domyślny szablon w Ustawienia → <strong>{{settings_invoice_template_label}}</strong>: dotknij wzoru, a potem <strong>{{common_done}}</strong>. Obowiązuje "
                  "wszystko, co od tej pory wystawisz. Dla pojedynczej faktury lub oferty użyj przycisku <strong>{{common_template_button}}</strong> "
                  "w formularzu."),
            ("p", "Każdy szablon drukuje te same informacje — dane Twojej firmy, dane klienta, pozycje z jednostką i datą, sumy, notatki i "
                  "dane do płatności — ale tylko to, co wypełniłeś. Długie faktury przechodzą na drugą stronę, a suma pozostaje razem z ostatnią pozycją."),
        ]),
        "free-vs-pro": ("Plan darmowy a Invoice Cove Pro", [
            ("p", "Invoice Cove jest darmowy, z kilkoma rozsądnymi ograniczeniami:"),
            ("ul", [
                "Do 3 faktur i 3 ofert wystawionych w miesiącu kalendarzowym",
                "Do 3 klientów jednocześnie",
                "Numery faktur i ofert nadawane są automatycznie i nie można ich edytować",
                "Eksport do Excela, CSV i ZIP jest tylko w Pro",
                "Kopia zapasowa i przywracanie są tylko w Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> to jednorazowy zakup przez Google Play — nie subskrypcja — który na stałe znosi wszystkie te ograniczenia. "
                  "Szkice, wszystkie szablony i języki, blokada aplikacji oraz tworzenie, podgląd i udostępnianie dokumentów są darmowe dla wszystkich. "
                  "Pełne szczegóły znajdziesz w <a href=\"terms.html\">Warunkach korzystania</a>."),
        ]),
    },
}
