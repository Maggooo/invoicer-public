T = {
    "title": "Benutzerhandbuch",
    "subtitle": "Alles, was Invoice Cove kann, Bildschirm für Bildschirm.",
    "meta_desc": "Vollständiges Benutzerhandbuch für Invoice Cove - Offline Billing.",
    "lang_label": "Sprache",
    "brand_alt": "Invoice Cove",
    "toc": "Inhalt",
    "footer_questions": "Fragen?",
    "lede": (
        "Invoice Cove läuft vollständig auf deinem Gerät — Rechnungen, Angebote, Kunden und dein Firmenprofil werden lokal gespeichert, "
        "nicht auf einem Invoice-Cove-Server. <strong>Wir erfassen, sehen oder erhalten keine Daten über deine Rechnungen oder darüber, wie du die App "
        "nutzt</strong> — es gibt keine Analyse, kein Tracking, nichts wird im Hintergrund irgendwohin gesendet. "
        "Nur für den einmaligen Kauf von Invoice Cove Pro über Google Play braucht die App selbst eine Internetverbindung. "
        "Einzelheiten findest du in der <a href=\"privacy.html\">Datenschutzerklärung</a>."
    ),
    "warn": (
        "<strong>Bevor du die App deinstallierst oder ihren Speicher löschst:</strong> Diese Daten werden von uns nirgendwo gesichert. "
        "Wenn du Invoice Cove deinstallierst oder den Speicher in den Android-Einstellungen löschst, werden alle Rechnungen, Angebote, Kunden "
        "und Einstellungen auf diesem Gerät endgültig gelöscht — es gibt keine Cloud-Kopie zum Wiederherstellen. Schütze dich: Erstelle eine Sicherung "
        "mit Invoice Cove Pro (siehe <a href=\"#backup\">Sicherung und Wiederherstellung</a>) oder exportiere, was du brauchst, als Excel, CSV oder ZIP "
        "(siehe <a href=\"#export\">Rechnungen exportieren</a>)."
    ),
    "sections": {
        "home": ("Startbildschirm", [
            ("p", "Der Startbildschirm ist dein Ausgangspunkt, mit einer Kachel für jede Hauptaktion: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> und "
                  "<strong>{{common_reports_title}}</strong>. Tippe eine Kachel an, um direkt dorthin zu springen."),
            ("p", "Die Leiste unten bietet dir immer schnellen Zugriff auf <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (eine neue Rechnung), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> und <strong>{{nav_reports}}</strong>."),
            ("p", "Das Zahnrad-Symbol (⚙️) oben rechts auf den meisten Bildschirmen öffnet die <a href=\"#settings\">Firmendaten und Einstellungen</a>."),
        ]),
        "customers": ("Kunden", [
            ("p", "Lege einen Kunden über den Reiter <strong>{{nav_customers}}</strong> an (Plus-Symbol antippen), über die Kachel <strong>{{home_new_customer_title}}</strong> "
                  "oder direkt beim Erstellen einer Rechnung oder eines Angebots. Nur der Name ist Pflicht. Optionale Felder: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, die Adresse, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} und eine Farbe, die die Dokumente des Kunden einfärbt. Jedes Feld zeigt ein Beispiel, damit du weißt, was hineingehört."),
            ("p", "Tippe einen Kunden an, um ihn zu <strong>{{common_edit}}</strong>, seinen <strong>{{customers_view_history}}</strong> (Rechnungen, Angebote und Entwürfe) zu öffnen "
                  "oder ihn zu <strong>{{common_delete}}</strong>."),
            ("p", "Auf deinen Rechnungen und Angeboten stehen die Kundendaten unter dem Namen in fester Reihenfolge: Kundennummer, Steuernummer, USt-IdNr., "
                  "Handelsregisternummer, dann Adresse, E-Mail und Telefon. Was du leer lässt, wird einfach nicht gedruckt."),
            ("note", "<strong>Das Speichern funktioniert hier anders als bei Rechnungen.</strong> Ein Kunde hat seine eigene Schaltfläche <strong>{{customers_form_save_customer}}</strong> "
                     "(beim Bearbeiten <strong>{{customers_form_save_changes}}</strong>) — er wird gespeichert, sobald du sie antippst. Wenn du das Formular mit "
                     "ungespeicherten Änderungen schließen willst, fragt Invoice Cove zuerst nach."),
            ("note", "Das Löschen eines Kunden löscht nicht die Rechnungen und Angebote, die du ihm bereits ausgestellt hast. Seine unfertigen <a href=\"#drafts\">Entwürfe</a> "
                     "werden mit ihm gelöscht — du wirst vorher gefragt."),
        ]),
        "new-invoice": ("Eine Rechnung erstellen", [
            ("p", "Über <strong>{{nav_new}}</strong> (oder die Kachel <strong>{{home_new_invoice_title}}</strong>): Wähle einen Kunden — oder lege ihn direkt an — "
                  "lege Rechnungsdatum und Fälligkeitsdatum fest und füge dann deine Positionen hinzu."),
            ("p", "Tippe <strong>{{newinvoice_add_item_details_button}}</strong> und gib Beschreibung, Menge, Preis pro Einheit und optional eine Einheit "
                  "(z. B. h, Stk. oder kg) sowie Datum und Uhrzeit ein. Die Einheit steht im PDF neben der Menge. Tippe den Stift (✏️) bei einer Position, um sie zu korrigieren, "
                  "oder den Papierkorb (🗑️), um sie zu entfernen. Bereits verwendete Beschreibungen und Preise werden dir beim Tippen vorgeschlagen."),
            ("p", "Danach kannst du bei Bedarf einen Steuersatz, einen <strong>{{newinvoice_discount_label}}</strong> (Prozentsatz oder fester Betrag) und "
                  "<strong>{{common_notes_label}}</strong> hinzufügen. Die Rechnungsnummer wird automatisch vergeben (mit Pro kannst du sie ändern); die Währung wählst du daneben."),
            ("p", "<strong>{{common_preview_button}}</strong> erzeugt ein temporäres PDF, damit du prüfen kannst, wie es aussieht — es wird noch nichts gespeichert. "
                  "Die Schaltfläche <strong>{{common_template_button}}</strong> zeigt, welche Vorlage verwendet wird; tippe darauf, um nur für dieses Dokument eine andere zu wählen."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> erledigt drei Dinge auf einmal: Es speichert die Rechnung, erstellt das PDF und öffnet das Teilen-Menü "
                     "deines Geräts, damit du sie verschicken kannst. Noch nicht fertig? Nutze <strong>{{newinvoice_save_draft_button}}</strong> — siehe <a href=\"#drafts\">Entwürfe</a>."),
        ]),
        "drafts": ("Entwürfe", [
            ("p", "Eine Rechnung, an der du noch arbeitest, geht nicht verloren. Sobald du einen Kunden gewählt und mindestens eine Position oder eine Notiz hinzugefügt hast, "
                  "behält Invoice Cove einen <strong>Entwurf</strong> und aktualisiert ihn kurz, nachdem du aufgehört hast zu tippen — und noch einmal, wenn du die App verlässt. "
                  "Beim Verlassen des Bildschirms gibt es keine Frage „Änderungen verwerfen?“; eine kurze Meldung sagt dir, dass der Entwurf gespeichert wurde."),
            ("p", "Tippe <strong>{{newinvoice_save_draft_button}}</strong> (unter {{newinvoice_generate_button}}), um die Rechnung bewusst beiseitezulegen: Sie wird gespeichert und "
                  "das Formular geleert, bereit für die nächste Rechnung. Das geht, sobald ein Kunde gewählt ist, auch bevor du Positionen hinzufügst."),
            ("p", "Deine Entwürfe findest du unter <strong>{{nav_customers}}</strong> → Kunde → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Jeder Entwurf zeigt, wann er zuletzt bearbeitet wurde, wie viele Positionen er hat und die Summe. Tippe ihn an, um "
                  "weiterzuarbeiten oder die Rechnung zu erstellen; tippe den Papierkorb, um ihn zu löschen."),
            ("ul", [
                "Ein Entwurf verbraucht nie eine Rechnungsnummer und zählt nicht zum kostenlosen Monatslimit. Die Nummer wird erst vergeben, wenn du die endgültige "
                "Rechnung erstellst — der Entwurf wird dann durch sie ersetzt.",
                "Ein Entwurf behält Rechnungs- und Fälligkeitsdatum nur, wenn du sie selbst gewählt hast; sonst gilt beim erneuten Öffnen das heutige Datum.",
                "Beim Löschen eines Kunden werden auch seine Entwürfe gelöscht (du wirst vorher gefragt). Entwürfe sind in einer Sicherung enthalten.",
                "Entwürfe gibt es für Rechnungen; Angebote haben keine.",
            ]),
        ]),
        "invoices": ("Rechnungen verwalten", [
            ("p", "Der Reiter <strong>{{nav_invoices}}</strong> gruppiert deine Rechnungen in einen Ordner pro Kunde, die du nach "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> oder <em>{{invoices_folder_sort_invoice_count}}</em> sortieren kannst. "
                  "Öffne einen Ordner, um seine Rechnungen zu sehen, sortiert nach Datum, Wert, Nummer oder Status."),
            ("p", "Jede Rechnung hat einen Status: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (Fälligkeit überschritten), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (eine Anzahlung wurde erfasst), <strong>{{invoices_status_paid}}</strong> oder "
                  "<strong>{{invoices_status_void}}</strong>. Tippe eine Rechnung an, um sie anzusehen ({{common_view}}), erneut zu senden ({{common_share}}), als bezahlt oder storniert zu markieren oder zu löschen."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> fragt nach dem Zahlungsdatum und der Zahlungsart (Überweisung, Bargeld, Karte, PayPal oder sonstige). "
                "Eine bezahlte Rechnung lässt sich nicht mehr auf unbezahlt zurücksetzen.",
                "<strong>{{deposit_record_title}}</strong> hält eine Anzahlung fest. Die Rechnung erscheint dann als <strong>{{invoices_status_partially_paid}}</strong>, und die Anzahlung darf die Summe nicht übersteigen.",
                "<strong>{{invoices_action_mark_void}}</strong> behält die Rechnung in deinen Unterlagen, markiert sie aber als storniert. Nimm das lieber statt zu löschen — eine gelöschte Rechnung "
                "lässt sich nicht wiederherstellen.",
            ]),
            ("p", "Mit Pro lässt sich der Ordner eines Kunden auch als ZIP mit PDFs speichern oder teilen, und die ganze Liste kann für deinen Steuerberater exportiert werden — siehe "
                  "<a href=\"#export\">Rechnungen exportieren</a>."),
        ]),
        "export": ("Rechnungen exportieren (Excel, CSV, ZIP)", [
            ("p", "Mit Invoice Cove Pro verfügbar. Tippe oben im Reiter <strong>{{nav_invoices}}</strong> auf das Export-Symbol (📄). Wähle mit den Jahres- und Monatsauswahlen, welche Rechnungen "
                  "enthalten sein sollen (<strong>{{invoices_export_all}}</strong>, ein Jahr oder ein Monat eines Jahres — angeboten werden nur Jahre und Monate mit "
                  "Rechnungen), und entscheide dann, was passieren soll:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — eine Excel-Tabelle (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — dieselbe Tabelle als CSV-Datei.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — die Rechnungs-PDFs in einem ZIP, ein Ordner pro Kunde.",
                "<strong>{{invoices_export_delete}}</strong> — löscht die ausgewählten Rechnungen endgültig, nach zwei Bestätigungen.",
            ]),
            ("p", "<em>Speichern</em> lässt dich wählen, wo auf deinem Gerät die Datei landet; <em>Teilen</em> öffnet das Android-Teilen-Menü, damit du sie per E-Mail oder "
                  "im Chat verschicken kannst."),
            ("p", "Excel und CSV sind für deinen Steuerberater gemacht: <strong>eine Zeile pro Rechnungsposition</strong>, wobei die Rechnungsdaten in jeder Zeile wiederholt werden — "
                  "Nummer und Daten, Name, Nummer, Steuernummer, USt-IdNr., Handelsregisternummer und Adresse des Kunden, Beschreibung, Menge, Einheit, "
                  "Preis und Nettobetrag der Position, Zwischensumme, Rabatt, Steuersatz, Steuerbetrag und Gesamtsumme der Rechnung, die Währung sowie Zahlungsstatus, -datum und "
                  "-art. Spaltenüberschriften und feste Wörter (Rechnung, bezahlt, unbezahlt, Zahlungsarten) stehen in der Sprache, auf die die App eingestellt ist."),
        ]),
        "new-quote": ("Ein Angebot erstellen", [
            ("p", "<strong>{{home_new_quote_title}}</strong> funktioniert wie New Invoice — dieselben Felder, dieselben Schaltflächen <strong>{{common_preview_button}}</strong> und <strong>{{common_template_button}}</strong> und dasselbe "
                  "<strong>{{newquote_generate_button}}</strong>, das mit einem Tipp speichert, das PDF erstellt und das Teilen-Menü öffnet — mit "
                  "<strong>{{newquote_date_label}}</strong> und <strong>{{newquote_valid_until_label}}</strong> statt Rechnungs- und Fälligkeitsdatum. "
                  "Angebote haben keine Entwürfe."),
        ]),
        "quotes": ("Angebote verwalten und in Rechnungen umwandeln", [
            ("p", "Der Bildschirm <strong>{{common_quotes_title}}</strong> (über die Kachel im Startbildschirm) listet deine Angebote nach Kunden auf, genau wie Rechnungen. Öffne ein Angebot, um es "
                  "anzusehen oder zu teilen, nutze <strong>{{quotes_action_accept}}</strong> oder <strong>{{quotes_action_decline}}</strong>, wenn der Kunde antwortet, "
                  "erfasse eine Anzahlung oder lösche es. Die Anzahlung darf die Summe des Angebots nicht übersteigen."),
            ("p", "Sobald ein Kunde ein Angebot annimmt, wandle mit <strong>{{quotes_action_convert_to_invoice}}</strong> die angehakten Positionen in eine echte, "
                  "unabhängig bearbeitbare Rechnung um — Fälligkeitsdatum und Rabatt lassen sich noch anpassen, das ursprüngliche Angebot wird als "
                  "<strong>{{quotes_status_converted}}</strong> markiert und bleibt in deinen Unterlagen."),
        ]),
        "calendar": ("Kalender und Erinnerungen", [
            ("p", "Der Bildschirm <strong>{{calendar_title}}</strong> ist eine Monatsansicht für deine eigenen Notizen. Tippe einen Tag an, um Notizen zu sehen oder hinzuzufügen; eine Notiz hat einen Titel und einen Text und "
                  "sendet dir mit <strong>{{calendar_remind_me}}</strong> und einer Uhrzeit zu diesem Zeitpunkt eine Benachrichtigung. Der erste Wochentag folgt deiner Einstellung."),
            ("p", "Unabhängig davon sendet Invoice Cove Zahlungserinnerungen — lokale Benachrichtigungen für bald fällige oder überfällige Rechnungen. Es wird nichts an einen Server gesendet oder von einem empfangen."),
        ]),
        "reports": ("Berichte", [
            ("p", "<strong>{{common_reports_title}}</strong> gibt dir einen schnellen Überblick: die Beträge <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> und <strong>{{reports_stat_overdue}}</strong>, wie viele Rechnungen du hast, "
                  "<em>{{reports_revenue_by_month}}</em> und deine <em>{{reports_top_customers}}</em> nach Rechnungssumme."),
            ("p", "Tippe die Karte <strong>{{reports_stat_outstanding}}</strong> oder <strong>{{reports_stat_overdue}}</strong> an, um genau diese Rechnungen als Liste zu öffnen."),
        ]),
        "settings": ("Firmendaten und Einstellungen", [
            ("p", "Öffne die Einstellungen über das Zahnrad — der Bildschirm heißt <strong>{{settings_title}}</strong>. Er beginnt mit deinen Voreinstellungen: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} oder {{settings_theme_dark}}), die Standard-"
                  "<strong>{{settings_invoice_template_label}}</strong>, <strong>{{settings_tax_label_label}}</strong> (USt, GST …), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> und <strong>{{settings_due_date_default_label}}</strong> (füllt das Fälligkeitsdatum automatisch aus, z. B. Net 30). "
                  "Darunter folgen <strong>{{settings_security_label}}</strong> (siehe <a href=\"#app-lock\">App-Sperre</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> und <strong>{{settings_backup_restore_label}}</strong> (siehe <a href=\"#backup\">Sicherung und Wiederherstellung</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> merkt sich Positionsbeschreibungen und Preise, um sie beim Tippen vorzuschlagen; <em>{{common_clear}}</em> vergisst sie, "
                  "ohne deine Rechnungen anzutasten."),
            ("p", "Weiter unten steht dein Firmenprofil, das auf jeder Rechnung und jedem Angebot gedruckt wird: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, ein kurzer Slogan (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, das <strong>{{settings_date_format_label}}</strong> für Datumsangaben, die Adresse, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (Handelsregisternummer, Stammkapital und Ähnliches), dein "
                  "<strong>{{settings_business_logo_label}}</strong> und deine <strong>{{settings_payment_details_label}}</strong> (IBAN, PayPal.me-Link …). Jedes Feld "
                  "hat ein Beispiel, und <strong>jedes Feld, das du leer lässt, erscheint einfach nicht auf deinen Rechnungen</strong>. Tippe <strong>{{common_done}}</strong>, wenn du "
                  "fertig bist; wenn du mit ungespeicherten Änderungen gehst, wirst du zuerst gefragt."),
            ("p", "Ganz unten: dieses <strong>{{settings_user_manual}}</strong> und <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Sicherung und Wiederherstellung", [
            ("p", "Mit Invoice Cove Pro verfügbar. Unter <strong>{{settings_backup_restore_label}}</strong> speichert <strong>{{settings_create_backup_title}}</strong> "
                  "alles — Rechnungen, Angebote, Entwürfe, Kunden, Kalender, Einstellungen, dein Logo und die PDFs — in einer Datei. Wähle "
                  "<strong>{{backup_save_button}}</strong>, um sie dort abzulegen, wo du willst, oder <strong>{{backup_share_button}}</strong>, um sie an einen sicheren Ort zu schicken."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> bringt alles zurück — zum Beispiel auf einem neuen Handy. Es funktioniert nur bei einer frischen Installation, bevor du "
                  "Daten hinzugefügt hast, und kann daher nie überschreiben, was du schon hast. Invoice Cove prüft, ob die Datei unversehrt ist, und sagt dir, wenn sie beschädigt ist, "
                  "keine Invoice-Cove-Sicherung ist oder von einer neueren App-Version stammt (dann zuerst aktualisieren)."),
            ("note", "Eine Sicherungsdatei ist <strong>nicht verschlüsselt</strong>: Jeder, der sie hat, kann deine Daten lesen. Bewahre sie an einem privaten Ort auf. Deine App-Sperr-PIN ist "
                     "nie darin enthalten."),
        ]),
        "app-lock": ("App-Sperre", [
            ("p", "Unter <strong>{{settings_security_label}}</strong> kannst du die <strong>{{settings_app_lock_title}}</strong> einschalten: Invoice Cove fragt dann nach deiner PIN "
                  "(oder deinem Fingerabdruck), wenn die App frisch geöffnet wird oder nach einem Neustart des Handys — nicht bei jedem Zurückwechseln."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: Wähle eine vierstellige PIN und bestätige sie.",
                "Danach erhältst du einen sechsstelligen <strong>Wiederherstellungscode</strong>, der nur einmal angezeigt wird. Schreibe ihn auf und bewahre ihn sicher auf.",
                "Wenn dein Handy es unterstützt, entsperre stattdessen mit dem Fingerabdruck (<strong>{{security_use_fingerprint}}</strong>).",
                "PIN vergessen? Nutze <strong>{{security_forgot_pin}}</strong> und gib den Wiederherstellungscode ein. Nach 5 falschen Versuchen musst du 30 Sekunden warten; "
                "die Wartezeit wächst mit weiteren Fehlversuchen.",
            ]),
            ("note", "Wenn du sowohl deine PIN als auch den Wiederherstellungscode verlierst — und keine Fingerabdruck-Entsperrung eingerichtet hast —, gibt es keinen Weg zurück. Wir können sie "
                     "nicht für dich zurücksetzen."),
        ]),
        "languages": ("Sprachen", [
            ("p", "Invoice Cove spricht 13 Sprachen: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands und Svenska. Tippe oben in den Einstellungen auf das runde Flaggen-Symbol, um zu wechseln — die App ändert sich sofort."),
            ("p", "Der Text in deinen PDFs und in Excel-/CSV-Exporten folgt der Sprache, auf die die App eingestellt ist, und dieses Handbuch gibt es in denselben 13 Sprachen "
                  "(nutze die Sprachleiste oben auf der Seite)."),
        ]),
        "templates": ("PDF-Vorlagen", [
            ("p", "Invoice Cove bringt 18 PDF-Designs mit: Classic, Client Color (in der Farbe des Kunden), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves und Spooky Hollow."),
            ("p", "Wähle deinen Standard unter Einstellungen → <strong>{{settings_invoice_template_label}}</strong>: Tippe ein Design an, dann <strong>{{common_done}}</strong>. Er "
                  "gilt für alles, was du ab dann erstellst. Für eine einzelne Rechnung oder ein einzelnes Angebot nutze die Schaltfläche <strong>{{common_template_button}}</strong> "
                  "im Formular."),
            ("p", "Jede Vorlage druckt dieselben Informationen — deine Firmendaten, die Kundendaten, Positionen mit Einheit und Datum, Summen, Notizen und "
                  "Zahlungsdetails —, aber nur, was du ausgefüllt hast. Lange Rechnungen gehen auf einer zweiten Seite weiter, wobei die Summen zusammen mit der letzten Position stehen."),
        ]),
        "free-vs-pro": ("Kostenloser Tarif und Invoice Cove Pro", [
            ("p", "Invoice Cove ist kostenlos nutzbar, mit ein paar vernünftigen Grenzen:"),
            ("ul", [
                "Bis zu 3 erstellte Rechnungen und 3 Angebote pro Kalendermonat",
                "Bis zu 3 Kunden gleichzeitig",
                "Rechnungs- und Angebotsnummern werden automatisch vergeben und sind nicht änderbar",
                "Excel-, CSV- und ZIP-Export sind nur mit Pro möglich",
                "Sicherung und Wiederherstellung sind nur mit Pro möglich",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> ist ein einmaliger Kauf über Google Play — kein Abo —, der alle diese Grenzen dauerhaft aufhebt. "
                  "Entwürfe, alle Vorlagen und Sprachen, die App-Sperre sowie das Erstellen, Ansehen und Teilen von Dokumenten sind für alle kostenlos. "
                  "Alle Einzelheiten stehen in den <a href=\"terms.html\">Nutzungsbedingungen</a>."),
        ]),
    },
}
