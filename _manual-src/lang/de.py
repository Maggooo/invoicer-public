T = {
    "title": "Bedienungsanleitung",
    "subtitle": "Alles, was Invoice Cove kann, Bildschirm für Bildschirm.",
    "meta_desc": "Vollständige Bedienungsanleitung für Invoice Cove - Offline Billing.",
    "lang_label": "Sprache",
    "brand_alt": "Invoice Cove",
    "toc": "Inhalt",
    "footer_questions": "Fragen?",
    "lede": (
        "Invoice Cove läuft vollständig auf deinem Gerät: Rechnungen, Angebote, Kunden und dein Firmenprofil werden lokal gespeichert, "
        "nicht auf einem Invoice-Cove-Server. Wir erfassen, sehen oder erhalten keine Daten über deine Rechnungen oder darüber, wie du die App "
        "nutzt. Es gibt keine Analyse, kein Tracking, nichts wird im Hintergrund irgendwohin gesendet. "
        "Nur für den einmaligen Kauf von Invoice Cove Pro über Google Play braucht die App selbst eine Internetverbindung. "
        "Einzelheiten findest du in der <a href=\"privacy.html\">Datenschutzerklärung</a>."
    ),
    "warn": (
        "Denk daran! Bevor du die App deinstallierst oder ihren Speicher löschst: Diese Daten werden von uns nirgendwo gesichert. "
        "Wenn du Invoice Cove deinstallierst oder den Speicher in den Android-Einstellungen löschst, werden alle Rechnungen, Angebote, Kunden "
        "und Einstellungen auf diesem Gerät endgültig gelöscht — es gibt keine Cloud-Kopie zum Wiederherstellen. Um deine Daten zu schützen: Erstelle eine Sicherung "
        "mit Invoice Cove Pro (siehe <a href=\"#backup\">Sicherung und Wiederherstellung</a>) oder exportiere, was du brauchst, als Excel, CSV oder ZIP "
        "(siehe <a href=\"#export\">Rechnungen exportieren</a>)."
    ),
    "sections": {
        "home": ("Startbildschirm", [
            ("p", "Der Startbildschirm ist dein Ausgangspunkt, mit einer Kachel für jede Hauptaktion: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} und "
                  "{{common_reports_title}}. Tippe eine Kachel an, um direkt dorthin zu springen."),
            ("p", "Die Leiste unten bietet dir schnellen Zugriff auf {{nav_home}}, {{nav_new}} (neue Rechnung), "
                  "{{nav_invoices}}, {{nav_customers}} und {{nav_reports}}."),
            ("p", "Das Zahnrad-Symbol (⚙️) oben rechts auf den meisten Bildschirmen öffnet die <a href=\"#settings\">Firmendaten und Einstellungen</a>."),
        ]),
        "customers": ("Kunden", [
            ("p", "Um einen Kunden anzulegen, öffne den Reiter {{nav_customers}} und tippe auf das Plus-Symbol, oder nutze die Kachel {{home_new_customer_title}}. "
                  "Du kannst einen Kunden auch beim Erstellen einer Rechnung oder eines Angebots anlegen. Für einen neuen Kunden ist nur der Name nötig. "
                  "Zu den optionalen Feldern gehören: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, die Adresse, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} und ein Farbton für die Dokumente des Kunden. Jedes Feld zeigt ein Beispiel, damit du weißt, was hineingehört."),
            ("p", "Tippe einen Kunden an, um ihn zu {{common_edit}}, seinen {{customers_view_history}} (Rechnungen, Angebote und Entwürfe) zu öffnen "
                  "oder ihn zu {{common_delete}}."),
            ("p", "Auf deinen Rechnungen und Angeboten stehen die Kundendaten unter dem Namen in fester Reihenfolge: Kundennummer, Steuernummer, USt-IdNr., "
                  "Handelsregisternummer, dann Adresse, E-Mail und Telefon. Was du leer lässt, wird nicht gedruckt."),
            ("note", "Das Speichern funktioniert hier anders als bei Rechnungen. Ein Kunde hat seine eigene Schaltfläche {{customers_form_save_customer}} "
                     "(beim Bearbeiten {{customers_form_save_changes}}) und wird gespeichert, sobald du sie antippst. Wenn du das Formular mit "
                     "ungespeicherten Änderungen schließen willst, fragt Invoice Cove zuerst nach."),
            ("note", "Das Löschen eines Kunden löscht nicht die Rechnungen und Angebote, die du ihm bereits ausgestellt hast. Seine unfertigen <a href=\"#drafts\">Entwürfe</a> werden jedoch "
                     "mit ihm gelöscht; Invoice Cove bittet dich vorher um Bestätigung."),
        ]),
        "new-invoice": ("Eine Rechnung erstellen", [
            ("p", "Über {{nav_new}} (oder die Kachel {{home_new_invoice_title}}): Wähle einen Kunden (oder lege ihn direkt an), "
                  "lege Rechnungsdatum und Fälligkeitsdatum fest und füge dann deine Positionen hinzu."),
            ("p", "Tippe {{newinvoice_add_item_details_button}} und gib Beschreibung, Menge, Preis pro Einheit und optional eine Einheit "
                  "(z. B. h, Stk. oder kg) sowie Datum und Uhrzeit ein. Die Einheit steht im PDF neben der Menge. Tippe den Stift (✏️) bei einer Position, um sie zu korrigieren, "
                  "oder den Papierkorb (🗑️), um sie zu entfernen. Bereits verwendete Beschreibungen und Preise werden dir beim Tippen vorgeschlagen."),
            ("p", "Danach kannst du bei Bedarf einen Steuersatz, einen {{newinvoice_discount_label}} (Prozentsatz oder fester Betrag) und "
                  "{{common_notes_label}} hinzufügen. Die Rechnungsnummer wird automatisch vergeben (mit Invoice Cove Pro lässt sie sich ändern), und die Währung wählst du daneben."),
            ("p", "{{common_preview_button}} erzeugt ein temporäres PDF, damit du prüfen kannst, wie es aussieht — es wird noch nichts gespeichert. "
                  "Die Schaltfläche {{common_template_button}} zeigt, welche Vorlage verwendet wird; tippe darauf, um nur für dieses Dokument eine andere zu wählen."),
            ("note", "{{newinvoice_generate_button}} erledigt drei Dinge auf einmal: Es speichert die Rechnung, erstellt das PDF und öffnet das Teilen-Menü "
                     "deines Geräts, damit du sie verschicken kannst. Noch nicht fertig? Nutze {{newinvoice_save_draft_button}} — siehe <a href=\"#drafts\">Entwürfe</a>."),
        ]),
        "drafts": ("Entwürfe", [
            ("p", "Eine Rechnung, an der du noch arbeitest, geht nicht verloren. Sobald du einen Kunden gewählt und mindestens eine Position oder eine Notiz hinzugefügt hast, "
                  "behält Invoice Cove einen Entwurf und aktualisiert ihn kurz, nachdem du aufgehört hast zu tippen, und noch einmal, wenn du die App verlässt. "
                  "Beim Verlassen des Bildschirms gibt es keine Frage „Änderungen verwerfen?“; eine kurze Meldung sagt dir, dass der Entwurf gespeichert wurde."),
            ("p", "Tippe {{newinvoice_save_draft_button}} (unter {{newinvoice_generate_button}}), um die Rechnung bewusst beiseitezulegen: Sie wird gespeichert und "
                  "das Formular geleert, bereit für die nächste Rechnung. Das geht, sobald ein Kunde gewählt ist, auch bevor du Positionen hinzufügst."),
            ("p", "Deine Entwürfe findest du unter {{nav_customers}} → Kunde → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Jeder Entwurf zeigt, wann er zuletzt bearbeitet wurde, wie viele Positionen er hat und die Summe. Tippe ihn an, um "
                  "weiterzuarbeiten oder die Rechnung zu erstellen; tippe den Papierkorb, um ihn zu löschen."),
            ("ul", [
                "Ein Entwurf verbraucht nie eine Rechnungsnummer und zählt nicht zum kostenlosen Monatslimit. Die Nummer wird erst vergeben, wenn du die endgültige "
                "Rechnung erstellst — der Entwurf wird dann durch sie ersetzt.",
                "Ein Entwurf behält Rechnungs- und Fälligkeitsdatum nur, wenn du sie selbst gewählt hast; sonst gilt beim erneuten Öffnen das heutige Datum.",
                "Beim Löschen eines Kunden werden auch seine Entwürfe gelöscht (Invoice Cove fragt vorher nach). Entwürfe sind in einer Sicherung enthalten.",
                "Entwürfe gibt es für Rechnungen; Angebote haben keine.",
            ]),
        ]),
        "invoices": ("Rechnungen verwalten", [
            ("p", "Der Reiter {{nav_invoices}} gruppiert deine Rechnungen in einen Ordner pro Kunde, die du nach "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> oder <em>{{invoices_folder_sort_invoice_count}}</em> sortieren kannst. "
                  "Öffne einen Ordner, um seine Rechnungen zu sehen, sortiert nach Datum, Wert, Nummer oder Status."),
            ("p", "Jede Rechnung hat einen Status: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (Fälligkeit überschritten), "
                  "{{invoices_status_partially_paid}} (eine Anzahlung wurde erfasst), {{invoices_status_paid}} oder "
                  "{{invoices_status_void}}. Tippe eine Rechnung an, um sie anzusehen ({{common_view}}), erneut zu senden ({{common_share}}), als bezahlt oder storniert zu markieren oder zu löschen."),
            ("ul", [
                "{{invoices_action_mark_paid}} fragt nach dem Zahlungsdatum und der Zahlungsart (Überweisung, Bargeld, Karte, PayPal oder sonstige). "
                "Eine bezahlte Rechnung lässt sich nicht mehr auf unbezahlt zurücksetzen.",
                "{{deposit_record_title}} hält eine Anzahlung fest. Die Rechnung erscheint dann als {{invoices_status_partially_paid}}, und die Anzahlung darf die Summe nicht übersteigen.",
                "{{invoices_action_mark_void}} behält die Rechnung in deinen Unterlagen, markiert sie aber als storniert. Das ist dem Löschen vorzuziehen, denn eine gelöschte Rechnung "
                "lässt sich nicht wiederherstellen.",
            ]),
            ("p", "Mit Pro lässt sich der Ordner eines Kunden auch als ZIP mit PDFs speichern oder teilen, und die ganze Liste kann für deinen Steuerberater exportiert werden — siehe "
                  "<a href=\"#export\">Rechnungen exportieren</a>."),
        ]),
        "export": ("Rechnungen exportieren (Excel, CSV, ZIP)", [
            ("p", "Mit Invoice Cove Pro verfügbar. Tippe oben im Reiter {{nav_invoices}} auf das Export-Symbol (📄). Wähle mit den Jahres- und Monatsauswahlen, welche Rechnungen "
                  "enthalten sein sollen ({{invoices_export_all}}, ein Jahr oder ein Monat eines Jahres; angeboten werden nur Jahre und Monate mit "
                  "Rechnungen), und entscheide dann, was passieren soll:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — eine Excel-Tabelle (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — dieselbe Tabelle als CSV-Datei.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — die Rechnungs-PDFs in einem ZIP, ein Ordner pro Kunde.",
                "{{invoices_export_delete}} — löscht die ausgewählten Rechnungen nach zwei Bestätigungen endgültig.",
            ]),
            ("p", "<em>Speichern</em> lässt dich wählen, wo auf deinem Gerät die Datei landet; <em>Teilen</em> öffnet das Android-Teilen-Menü, damit du sie per E-Mail oder "
                  "per Nachricht verschicken kannst."),
            ("p", "Excel und CSV sind für deinen Steuerberater gemacht: standardmäßig eine Zeile pro Rechnung mit Nummer und Daten, Name, Nummer, "
                  "Steuernummer, USt-IdNr., Handelsregisternummer und Adresse des Kunden, Zwischensumme, Rabatt, Steuersatz, Steuerbetrag und Gesamtsumme der "
                  "Rechnung, die Währung sowie Zahlungsstatus, -datum und -art. Spaltenüberschriften und feste Wörter (Rechnung, bezahlt, unbezahlt, Zahlungsarten) "
                  "stehen in der Sprache, auf die die App eingestellt ist."),
            ("p", "Um eine Zeile pro Rechnungsposition zu erhalten, mit den Rechnungsdaten in jeder Zeile sowie Beschreibung, Menge, Einheit, Preis "
                  "und Nettobetrag jeder Position, aktiviere {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Ein Angebot erstellen", [
            ("p", "Die Kachel {{home_new_quote_title}} funktioniert wie die Kachel Neue Rechnung: dieselben Felder, dieselben Schaltflächen {{common_preview_button}} und {{common_template_button}}, dasselbe "
                  "{{newquote_generate_button}}, das mit einem Tipp speichert, das PDF erstellt und das Teilen-Menü öffnet, jedoch mit "
                  "{{newquote_date_label}} und {{newquote_valid_until_label}} statt Rechnungs- und Fälligkeitsdatum."),
            ("p", "Angebote haben keine Entwürfe."),
        ]),
        "quotes": ("Angebote verwalten und in Rechnungen umwandeln", [
            ("p", "Der Bildschirm {{common_quotes_title}} (über die Kachel im Startbildschirm) listet deine Angebote nach Kunden auf, genau wie Rechnungen. Öffne ein Angebot, um es "
                  "anzusehen oder zu teilen, nutze {{quotes_action_accept}} oder {{quotes_action_decline}}, wenn der Kunde antwortet, "
                  "erfasse eine Anzahlung oder lösche es. Die Anzahlung darf die Summe des Angebots nicht übersteigen."),
            ("p", "Sobald ein Kunde ein Angebot annimmt, wandle mit {{quotes_action_convert_to_invoice}} die angehakten Positionen in eine echte, "
                  "unabhängig bearbeitbare Rechnung um. Fälligkeitsdatum und Rabatt lassen sich noch anpassen, das ursprüngliche Angebot wird als "
                  "{{quotes_status_converted}} markiert und bleibt in deinen Unterlagen."),
        ]),
        "calendar": ("Kalender und Erinnerungen", [
            ("p", "Der Bildschirm {{calendar_title}} ist eine Monatsansicht für deine eigenen Notizen. Tippe einen Tag an, um Notizen zu sehen oder hinzuzufügen; eine Notiz hat einen Titel und einen Text und "
                  "sendet dir mit {{calendar_remind_me}} und einer Uhrzeit zum eingestellten Datum und zur eingestellten Uhrzeit eine Benachrichtigung. Der erste Wochentag folgt deinen Einstellungen."),
            ("p", "Unabhängig davon sendet Invoice Cove Zahlungserinnerungen — lokale Benachrichtigungen für bald fällige oder überfällige Rechnungen. Es wird nichts an einen Server gesendet oder von einem empfangen."),
        ]),
        "reports": ("Berichte", [
            ("p", "{{common_reports_title}} gibt dir einen schnellen Überblick: die Beträge {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} und {{reports_stat_overdue}}, wie viele Rechnungen du hast, "
                  "<em>{{reports_revenue_by_month}}</em> und deine <em>{{reports_top_customers}}</em> nach Rechnungssumme."),
            ("p", "Tippe die Karte {{reports_stat_outstanding}} oder {{reports_stat_overdue}} an, um genau diese Rechnungen als Liste zu öffnen."),
        ]),
        "settings": ("Firmendaten und Einstellungen", [
            ("p", "Öffne die Einstellungen über das Zahnrad; dieser Bildschirm heißt {{settings_title}}. Er beginnt mit deinen optionalen Voreinstellungen: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} oder {{settings_theme_dark}}), die Standard-"
                  "{{settings_invoice_template_label}}, {{settings_tax_label_label}} (USt, GST …), "
                  "{{settings_first_day_of_week_label}} und {{settings_due_date_default_label}}, das das Fälligkeitsdatum automatisch ausfüllt (z. B. Net 30). "
                  "Darunter folgen {{settings_security_label}} (siehe <a href=\"#app-lock\">App-Sperre</a>), "
                  "{{settings_item_suggestions_label}} und {{settings_backup_restore_label}} (siehe <a href=\"#backup\">Sicherung und Wiederherstellung</a>)."),
            ("p", "{{settings_item_memory_title}} merkt sich Positionsbeschreibungen und Preise, um sie beim Tippen vorzuschlagen; <em>{{common_clear}}</em> vergisst sie, "
                  "ohne deine Rechnungen anzutasten."),
            ("p", "Weiter unten steht dein Firmenprofil, das auf jeder Rechnung und jedem Angebot gedruckt wird: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, ein kurzer Slogan ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, das {{settings_date_format_label}} für Datumsangaben, die Adresse, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (Handelsregisternummer, Stammkapital und Ähnliches), dein "
                  "{{settings_business_logo_label}} und deine {{settings_payment_details_label}} (IBAN, PayPal.me-Link). Jedes Feld "
                  "hat ein Beispiel, und jedes Feld, das du leer lässt, erscheint nicht auf deinen Rechnungen. Tippe {{common_done}}, wenn du "
                  "fertig bist; wenn du mit ungespeicherten Änderungen gehst, wirst du um Bestätigung gebeten."),
            ("p", "Ganz unten werden diese {{settings_user_manual}} und {{settings_share_this_app}} angezeigt."),
        ]),
        "backup": ("Sicherung und Wiederherstellung", [
            ("p", "Mit Invoice Cove Pro verfügbar, unter {{settings_backup_restore_label}}. {{settings_create_backup_title}} speichert "
                  "alles: Rechnungen, Angebote, Entwürfe, Kunden, Kalender, Einstellungen, dein Logo und die PDFs, alles in einer Datei. Wähle "
                  "{{backup_save_button}}, um sie dort abzulegen, wo du willst, oder {{backup_share_button}}, um sie an einen sicheren Ort zu schicken."),
            ("p", "{{settings_restore_backup_title}} bringt alles zurück, falls du auf ein neues Handy umziehen musst. Es funktioniert nur bei einer frischen Installation, bevor du "
                  "Daten hinzugefügt hast, und kann daher nie überschreiben, was du schon hast. Invoice Cove prüft, ob die Datei unversehrt ist, und sagt dir, wenn sie beschädigt ist, "
                  "keine Invoice-Cove-Sicherung ist oder von einer neueren App-Version stammt (dann zuerst aktualisieren)."),
            ("note", "Eine Sicherungsdatei ist nicht verschlüsselt: Jeder, der sie hat, kann deine Daten lesen. Bewahre sie an einem privaten Ort auf. Deine App-Sperr-PIN ist "
                     "nie darin enthalten."),
        ]),
        "app-lock": ("App-Sperre", [
            ("p", "Unter {{settings_security_label}} kannst du die {{settings_app_lock_title}} einschalten: Invoice Cove fragt dann nach deiner PIN "
                  "(oder deinem Fingerabdruck), wenn die App frisch geöffnet wird oder nach einem Neustart des Handys — nicht bei jedem Zurückwechseln."),
            ("ul", [
                "{{settings_set_pin}}: Wähle eine vierstellige PIN und bestätige sie.",
                "Danach erhältst du einen sechsstelligen Wiederherstellungscode, der nur einmal angezeigt wird. Schreibe ihn auf und bewahre ihn sicher auf.",
                "Wenn dein Handy es unterstützt, entsperre stattdessen mit dem Fingerabdruck ({{security_use_fingerprint}}).",
                "PIN vergessen? Nutze {{security_forgot_pin}} und gib den Wiederherstellungscode ein. Nach 5 falschen Versuchen musst du 30 Sekunden warten – "
                "die Wartezeit wächst mit weiteren Fehlversuchen.",
            ]),
            ("note", "Wenn du sowohl deine PIN als auch den Wiederherstellungscode verlierst und keine Fingerabdruck-Entsperrung eingerichtet hast, gibt es keinen Weg zurück. Wir können sie "
                     "nicht für dich zurücksetzen."),
        ]),
        "languages": ("Sprachen", [
            ("p", "Invoice Cove spricht 13 Sprachen: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands und Svenska. Tippe oben in den Einstellungen auf das runde Flaggen-Symbol, um zu wechseln — die App ändert sich sofort."),
            ("p", "Der Text in deinen PDFs und in Excel-/CSV-Exporten folgt der Sprache, auf die die App eingestellt ist, und diese Bedienungsanleitung gibt es in denselben 13 Sprachen "
                  "(nutze die Sprachleiste oben auf der Seite)."),
        ]),
        "templates": ("PDF-Vorlagen", [
            ("p", "Invoice Cove bietet derzeit 18 PDF-Designs: Classic, Client Color (in der Farbe des Kunden), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves und Spooky Hollow."),
            ("p", "Wähle deinen Standard unter Einstellungen → {{settings_invoice_template_label}}: Tippe ein Design an, dann {{common_done}}. Er "
                  "gilt für alles, was du ab dann erstellst. Für eine einzelne Rechnung oder ein einzelnes Angebot nutze die Schaltfläche {{common_template_button}} "
                  "im Formular."),
            ("p", "Jede Vorlage druckt dieselben Informationen: deine Firmendaten, die Kundendaten, Positionen mit Einheit und Datum, Summen, Notizen und "
                  "Zahlungsdetails —, aber nur, was du ausgefüllt hast. Lange Rechnungen gehen auf einer zweiten Seite weiter, wobei die Summen zusammen mit der letzten Position stehen."),
        ]),
        "free-vs-pro": ("Kostenloser Tarif und Invoice Cove Pro", [
            ("p", "Invoice Cove ist kostenlos nutzbar, mit ein paar vernünftigen Grenzen:"),
            ("ul", [
                "Bis zu 3 erstellte Rechnungen pro Kalendermonat",
                "Bis zu 3 erstellte Angebote pro Kalendermonat",
                "Bis zu 3 Kunden gleichzeitig",
                "Rechnungs- und Angebotsnummern werden automatisch vergeben und sind nicht änderbar",
                "Excel-, CSV- und ZIP-Export sind nur mit Pro möglich",
                "Sicherung und Wiederherstellung sind nur mit Pro möglich",
            ]),
            ("p", "Invoice Cove Pro ist ein einmaliger Kauf über Google Play (kein Abo), der alle diese Grenzen dauerhaft aufhebt. "
                  "Entwürfe, alle Vorlagen und Sprachen, die App-Sperre sowie das Erstellen, Ansehen und Teilen von Dokumenten sind für alle kostenlos. "
                  "Alle Einzelheiten stehen in den <a href=\"terms.html\">Nutzungsbedingungen</a>."),
        ]),
    },
}
