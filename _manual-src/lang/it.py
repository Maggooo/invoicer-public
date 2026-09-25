T = {
    "title": "Guida utente",
    "subtitle": "Tutto ciò che Invoice Cove sa fare, schermata per schermata.",
    "meta_desc": "Guida utente completa di Invoice Cove - Offline Billing.",
    "lang_label": "Lingua",
    "brand_alt": "Invoice Cove",
    "toc": "Indice",
    "footer_questions": "Domande?",
    "lede": (
        "Invoice Cove funziona interamente sul tuo dispositivo: fatture, preventivi, clienti e profilo della tua attività sono salvati in locale, "
        "non su un server di Invoice Cove. <strong>Non raccogliamo, non vediamo e non riceviamo alcun dato sulle tue fatture né su come usi l'app</strong> "
        "— nessuna analisi, nessun tracciamento, niente viene inviato in background. "
        "L'unico momento in cui l'app stessa ha bisogno di una connessione a internet è per elaborare l'acquisto una tantum di Invoice Cove Pro tramite Google Play. "
        "Per i dettagli consulta l'<a href=\"privacy.html\">Informativa sulla privacy</a>."
    ),
    "warn": (
        "<strong>Prima di disinstallare l'app o cancellarne i dati:</strong> questi dati non sono salvati da noi in nessun luogo. "
        "Disinstallare Invoice Cove, o cancellarne i dati dalle impostazioni di Android, elimina definitivamente ogni fattura, preventivo, cliente "
        "e impostazione su questo dispositivo: non esiste una copia nel cloud da cui ripristinare. Proteggiti: crea un backup "
        "con Invoice Cove Pro (vedi <a href=\"#backup\">Backup e ripristino</a>) oppure esporta ciò che ti serve in Excel, CSV o ZIP "
        "(vedi <a href=\"#export\">Esportare le fatture</a>)."
    ),
    "sections": {
        "home": ("Schermata principale", [
            ("p", "La schermata principale è il tuo punto di partenza, con un riquadro per ogni azione principale: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> e "
                  "<strong>{{common_reports_title}}</strong>. Tocca un riquadro per andare direttamente lì."),
            ("p", "La barra in basso ti dà sempre accesso rapido a <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (una nuova fattura), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> e <strong>{{nav_reports}}</strong>."),
            ("p", "L'icona a forma di ingranaggio (⚙️) nell'angolo in alto a destra della maggior parte delle schermate apre i <a href=\"#settings\">Dati dell'attività e impostazioni</a>."),
        ]),
        "customers": ("Clienti", [
            ("p", "Aggiungi un cliente dalla scheda <strong>{{nav_customers}}</strong> (tocca l'icona +), con il riquadro <strong>{{home_new_customer_title}}</strong> "
                  "oppure direttamente mentre crei una fattura o un preventivo. Solo il nome è obbligatorio. Campi facoltativi: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, l'indirizzo, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} e un colore che tinge i suoi documenti. Ogni campo mostra un esempio, così sai cosa inserire."),
            ("p", "Tocca un cliente per modificarlo (<strong>{{common_edit}}</strong>), aprire la sua <strong>{{customers_view_history}}</strong> (fatture, preventivi e bozze) "
                  "o eliminarlo (<strong>{{common_delete}}</strong>)."),
            ("p", "Sulle tue fatture e sui preventivi, i dati del cliente sono stampati sotto il suo nome in un ordine fisso: numero cliente, codice fiscale, partita IVA, "
                  "numero del registro delle imprese, poi indirizzo, email e telefono. Ciò che lasci vuoto semplicemente non viene stampato."),
            ("note", "<strong>Qui il salvataggio funziona in modo diverso rispetto alle fatture.</strong> Un cliente ha il suo pulsante <strong>{{customers_form_save_customer}}</strong> "
                     "(oppure <strong>{{customers_form_save_changes}}</strong> in modifica): viene salvato non appena lo tocchi. Se provi a chiudere il modulo "
                     "con modifiche non salvate, Invoice Cove ti chiede prima conferma."),
            ("note", "Eliminare un cliente non elimina le fatture e i preventivi che gli hai già emesso. Le sue <a href=\"#drafts\">bozze</a> non completate "
                     "vengono eliminate insieme a lui: ti viene chiesto prima."),
        ]),
        "new-invoice": ("Creare una fattura", [
            ("p", "Da <strong>{{nav_new}}</strong> (o dal riquadro <strong>{{home_new_invoice_title}}</strong>): scegli un cliente — o creane uno al volo — "
                  "imposta la data della fattura e la scadenza, poi aggiungi le voci."),
            ("p", "Tocca <strong>{{newinvoice_add_item_details_button}}</strong> e compila descrizione, quantità, prezzo unitario e, facoltativamente, un'unità "
                  "(come h, pz o kg) e una data e un'ora. L'unità è stampata accanto alla quantità nel PDF. Tocca la matita (✏️) su una voce per correggerla "
                  "o il cestino (🗑️) per rimuoverla. Le descrizioni e i prezzi usati in precedenza ti vengono suggeriti mentre scrivi."),
            ("p", "Poi aggiungi, se ti servono, un'aliquota, uno <strong>{{newinvoice_discount_label}}</strong> (percentuale o importo fisso) e "
                  "<strong>{{common_notes_label}}</strong>. Il numero della fattura è assegnato per te (con Pro puoi modificarlo); la valuta si sceglie accanto."),
            ("p", "<strong>{{common_preview_button}}</strong> genera un PDF temporaneo per vedere come viene: non si salva ancora nulla. "
                  "Il pulsante <strong>{{common_template_button}}</strong> mostra quale modello verrà usato; toccalo per sceglierne un altro solo per questo documento."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> fa tre cose insieme: salva la fattura, crea il PDF e apre il menu di condivisione "
                     "del dispositivo per inviarla. Non sei ancora pronto? Usa <strong>{{newinvoice_save_draft_button}}</strong> — vedi <a href=\"#drafts\">Bozze</a>."),
        ]),
        "drafts": ("Bozze", [
            ("p", "Non perdi una fattura a cui stai ancora lavorando. Appena hai scelto un cliente e aggiunto almeno una voce o una nota, Invoice Cove "
                  "conserva una <strong>bozza</strong> e la aggiorna poco dopo che hai smesso di scrivere — e ancora una volta quando esci dall'app. Non c'è "
                  "la domanda «scartare le modifiche?» quando lasci la schermata; un breve messaggio ti avvisa che la bozza è stata salvata."),
            ("p", "Tocca <strong>{{newinvoice_save_draft_button}}</strong> (sotto {{newinvoice_generate_button}}) per mettere da parte la fattura di proposito: viene salvata e "
                  "il modulo si svuota, pronto per la fattura successiva. Funziona appena è stato scelto un cliente, anche prima di aggiungere voci."),
            ("p", "Trovi le tue bozze in <strong>{{nav_customers}}</strong> → il cliente → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Ogni bozza mostra quando è stata modificata l'ultima volta, quante voci ha e il totale. Toccala per continuare "
                  "a modificarla o per generare la fattura; tocca il cestino per eliminarla."),
            ("ul", [
                "Una bozza non usa mai un numero di fattura e non conta nel limite mensile gratuito. Il numero viene assegnato solo quando generi la fattura "
                "definitiva — la bozza viene poi sostituita da essa.",
                "Una bozza conserva la data della fattura e la scadenza solo se le hai scelte tu; altrimenti, quando la riapri, usa la data di oggi.",
                "Eliminare un cliente elimina anche le sue bozze (ti viene chiesto prima). Le bozze sono incluse in un backup.",
                "Le bozze esistono per le fatture; i preventivi non le hanno.",
            ]),
        ]),
        "invoices": ("Gestire le fatture", [
            ("p", "La scheda <strong>{{nav_invoices}}</strong> raggruppa le tue fatture in una cartella per cliente, che puoi ordinare per "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> o <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Apri una cartella per vederne le fatture, ordinate per data, valore, numero o stato."),
            ("p", "Ogni fattura ha uno stato: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (scadenza superata), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (è stato registrato un acconto), <strong>{{invoices_status_paid}}</strong> o "
                  "<strong>{{invoices_status_void}}</strong>. Tocca una fattura per vederla ({{common_view}}), reinviarla ({{common_share}}), segnarla come pagata o annullata, oppure eliminarla."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> chiede la data del pagamento e come è stato pagato (bonifico, contanti, carta, PayPal o altro). "
                "Una fattura pagata non può più essere riportata a non pagata.",
                "<strong>{{deposit_record_title}}</strong> annota un pagamento anticipato. La fattura risulta poi <strong>{{invoices_status_partially_paid}}</strong>, e l'acconto non può superare il totale.",
                "<strong>{{invoices_action_mark_void}}</strong> conserva la fattura nei tuoi registri ma la segna come annullata. Preferiscilo all'eliminazione: una fattura eliminata "
                "non si può recuperare.",
            ]),
            ("p", "Con Pro, la cartella di un cliente può anche essere salvata o condivisa come ZIP di PDF, e l'intero elenco può essere esportato per il tuo commercialista — vedi "
                  "<a href=\"#export\">Esportare le fatture</a>."),
        ]),
        "export": ("Esportare le fatture (Excel, CSV, ZIP)", [
            ("p", "Disponibile con Invoice Cove Pro. Tocca l'icona di esportazione (📄) in alto nella scheda <strong>{{nav_invoices}}</strong>. Scegli quali fatture includere "
                  "con i selettori di anno e mese (<strong>{{invoices_export_all}}</strong>, un anno o un mese di un anno — vengono proposti solo gli anni e i mesi che "
                  "hanno fatture), poi scegli cosa fare:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — un foglio di calcolo Excel (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — la stessa tabella come file CSV.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — i PDF delle fatture in un unico ZIP, una cartella per cliente.",
                "<strong>{{invoices_export_delete}}</strong> — elimina definitivamente le fatture selezionate, dopo due conferme.",
            ]),
            ("p", "<em>Salva</em> ti lascia scegliere dove sul dispositivo va il file; <em>Condividi</em> apre il menu di condivisione di Android per inviarlo "
                  "via email o in una chat."),
            ("p", "Excel e CSV sono pensati per il tuo commercialista: per impostazione predefinita, <strong>una riga per ogni fattura</strong> — numero e date, "
                  "nome, numero, codice fiscale, partita IVA, numero del registro delle imprese e indirizzo del cliente, subtotale, sconto, aliquota IVA, "
                  "importo IVA e totale della fattura, la valuta, e stato, data e metodo di pagamento. Le intestazioni delle colonne e le parole fisse "
                  "(fattura, pagata, non pagata, metodi di pagamento) sono scritte nella lingua impostata nell'app."),
            ("p", "Attiva <strong>{{invoices_export_detailed_toggle}}</strong> nello stesso foglio per ottenere invece una riga per ogni voce di fattura, con i "
                  "dati della fattura ripetuti su ogni riga e descrizione, quantità, unità, prezzo e importo netto di ogni voce aggiunti."),
        ]),
        "new-quote": ("Creare un preventivo", [
            ("p", "<strong>{{home_new_quote_title}}</strong> funziona come New Invoice — stessi campi, stessi pulsanti <strong>{{common_preview_button}}</strong> e <strong>{{common_template_button}}</strong> e lo stesso "
                  "<strong>{{newquote_generate_button}}</strong> che salva, crea il PDF e apre il menu di condivisione con un tocco — con una "
                  "<strong>{{newquote_date_label}}</strong> e una data <strong>{{newquote_valid_until_label}}</strong> al posto di data della fattura e scadenza. "
                  "I preventivi non hanno bozze."),
        ]),
        "quotes": ("Gestire i preventivi e convertirli in fattura", [
            ("p", "La schermata <strong>{{common_quotes_title}}</strong> (dal riquadro nella schermata principale) elenca i preventivi per cliente, come per le fatture. Apri un preventivo per "
                  "vederlo o condividerlo, usa <strong>{{quotes_action_accept}}</strong> o <strong>{{quotes_action_decline}}</strong> quando il cliente risponde, "
                  "registra un acconto oppure eliminalo. L'acconto non può superare il totale del preventivo."),
            ("p", "Quando un cliente accetta un preventivo, usa <strong>{{quotes_action_convert_to_invoice}}</strong> per trasformare le righe selezionate in una vera fattura, "
                  "modificabile in modo indipendente — scadenza e sconto si possono ancora regolare, e il preventivo originale viene segnato come "
                  "<strong>{{quotes_status_converted}}</strong> e conservato nei tuoi registri."),
        ]),
        "calendar": ("Calendario e promemoria", [
            ("p", "La schermata <strong>{{calendar_title}}</strong> è una vista mensile per le tue note. Tocca un giorno per vedere o aggiungere note; una nota ha un titolo e un testo e, "
                  "con <strong>{{calendar_remind_me}}</strong> e un orario, ti invia una notifica in quel momento. Il primo giorno della settimana segue la tua impostazione."),
            ("p", "Separatamente, Invoice Cove invia promemoria di pagamento — notifiche locali per le fatture in scadenza o scadute. Non viene inviato nulla a un server né ricevuto da esso."),
        ]),
        "reports": ("Report", [
            ("p", "<strong>{{common_reports_title}}</strong> ti dà una panoramica rapida: gli importi <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> e <strong>{{reports_stat_overdue}}</strong>, quante fatture hai, "
                  "<em>{{reports_revenue_by_month}}</em> e i tuoi <em>{{reports_top_customers}}</em> per totale fatturato."),
            ("p", "Tocca la scheda <strong>{{reports_stat_outstanding}}</strong> o <strong>{{reports_stat_overdue}}</strong> per aprire l'elenco esatto di quelle fatture."),
        ]),
        "settings": ("Dati dell'attività e impostazioni", [
            ("p", "Apri le impostazioni dall'icona a forma di ingranaggio — la schermata si chiama <strong>{{settings_title}}</strong>. Inizia con le tue preferenze: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} o {{settings_theme_dark}}), "
                  "<strong>{{settings_invoice_template_label}}</strong> predefinito, <strong>{{settings_tax_label_label}}</strong> (IVA, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> e <strong>{{settings_due_date_default_label}}</strong> (compila la scadenza automaticamente, ad esempio Net 30). "
                  "Sotto seguono <strong>{{settings_security_label}}</strong> (vedi <a href=\"#app-lock\">Blocco dell'app</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> e <strong>{{settings_backup_restore_label}}</strong> (vedi <a href=\"#backup\">Backup e ripristino</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> ricorda descrizioni e prezzi delle voci per suggerirli mentre scrivi; <em>{{common_clear}}</em> li dimentica "
                  "senza toccare le tue fatture."),
            ("p", "Più in basso c'è il profilo della tua attività, stampato su ogni fattura e preventivo: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, un breve slogan (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, il <strong>{{settings_date_format_label}}</strong> delle date, l'indirizzo, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (numero di registrazione, capitale sociale e simili), il tuo "
                  "<strong>{{settings_business_logo_label}}</strong> e i tuoi <strong>{{settings_payment_details_label}}</strong> (IBAN, link PayPal.me…). Ogni campo "
                  "ha un esempio, e <strong>qualsiasi campo lasci vuoto semplicemente non compare sulle tue fatture</strong>. Tocca <strong>{{common_done}}</strong> quando "
                  "hai finito; se esci con modifiche non salvate, ti viene chiesto prima."),
            ("p", "In fondo: questa <strong>{{settings_user_manual}}</strong> e <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Backup e ripristino", [
            ("p", "Disponibile con Invoice Cove Pro. In <strong>{{settings_backup_restore_label}}</strong>, <strong>{{settings_create_backup_title}}</strong> salva "
                  "tutto — fatture, preventivi, bozze, clienti, calendario, impostazioni, il tuo logo e i PDF — in un solo file. Scegli "
                  "<strong>{{backup_save_button}}</strong> per conservarlo dove vuoi, oppure <strong>{{backup_share_button}}</strong> per inviarlo in un luogo sicuro."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> riporta tutto — per esempio su un telefono nuovo. Funziona solo su un'installazione nuova, prima di aver "
                  "aggiunto dati, quindi non può mai sovrascrivere ciò che hai già. Invoice Cove verifica che il file sia integro e ti avvisa se è danneggiato, "
                  "se non è un backup di Invoice Cove o se è stato creato da una versione più recente dell'app (aggiorna prima)."),
            ("note", "Un file di backup <strong>non è cifrato</strong>: chiunque lo abbia può leggere i tuoi dati. Conservalo in un luogo privato. Il PIN di blocco dell'app non "
                     "è mai incluso."),
        ]),
        "app-lock": ("Blocco dell'app", [
            ("p", "In <strong>{{settings_security_label}}</strong> puoi attivare <strong>{{settings_app_lock_title}}</strong>: Invoice Cove ti chiede allora il PIN "
                  "(o l'impronta) quando l'app viene aperta da zero o dopo il riavvio del telefono — non ogni volta che ci torni."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: scegli un PIN di 4 cifre e confermalo.",
                "Ricevi poi un <strong>codice di recupero</strong> di 6 cifre, mostrato una sola volta. Annotalo e conservalo in un luogo sicuro.",
                "Se il tuo telefono lo supporta, sblocca con l'impronta (<strong>{{security_use_fingerprint}}</strong>).",
                "Hai dimenticato il PIN? Usa <strong>{{security_forgot_pin}}</strong> e inserisci il codice di recupero. Dopo 5 tentativi errati devi attendere 30 secondi; "
                "l'attesa aumenta con altri tentativi errati.",
            ]),
            ("note", "Se perdi sia il PIN sia il codice di recupero — e non hai configurato lo sblocco con impronta — non c'è modo di rientrare. Non possiamo reimpostarlo "
                     "per te."),
        ]),
        "languages": ("Lingue", [
            ("p", "Invoice Cove parla 13 lingue: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands e Svenska. Tocca l'icona rotonda con la bandiera in alto nelle impostazioni per cambiare — l'app cambia subito."),
            ("p", "Il testo dei tuoi PDF e delle esportazioni Excel/CSV segue la lingua impostata nell'app, e questa guida è disponibile nelle stesse 13 lingue "
                  "(usa la barra delle lingue in alto nella pagina)."),
        ]),
        "templates": ("Modelli PDF", [
            ("p", "Invoice Cove include 18 modelli PDF: Classic, Client Color (tinto con il colore del cliente), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves e Spooky Hollow."),
            ("p", "Scegli il modello predefinito in Impostazioni → <strong>{{settings_invoice_template_label}}</strong>: tocca un modello, poi <strong>{{common_done}}</strong>. Vale "
                  "per tutto ciò che generi da quel momento. Per una singola fattura o un singolo preventivo, usa il pulsante <strong>{{common_template_button}}</strong> "
                  "nel modulo."),
            ("p", "Ogni modello stampa le stesse informazioni — i dati della tua attività, quelli del cliente, le voci con unità e data, i totali, le note e "
                  "i dati di pagamento — ma solo ciò che hai compilato. Le fatture lunghe continuano su una seconda pagina, con i totali insieme all'ultima voce."),
        ]),
        "free-vs-pro": ("Piano gratuito e Invoice Cove Pro", [
            ("p", "Invoice Cove è gratuito, con alcuni limiti ragionevoli:"),
            ("ul", [
                "Fino a 3 fatture e 3 preventivi generati per mese di calendario",
                "Fino a 3 clienti alla volta",
                "I numeri di fatture e preventivi sono assegnati automaticamente e non si possono modificare",
                "L'esportazione in Excel, CSV e ZIP è solo Pro",
                "Backup e ripristino sono solo Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> è un unico acquisto tramite Google Play — non un abbonamento — che elimina per sempre tutti questi limiti. "
                  "Bozze, tutti i modelli e le lingue, il blocco dell'app e la creazione, l'anteprima e la condivisione dei documenti sono gratuiti per tutti. "
                  "Consulta le <a href=\"terms.html\">Condizioni d'uso</a> per tutti i dettagli."),
        ]),
    },
}
