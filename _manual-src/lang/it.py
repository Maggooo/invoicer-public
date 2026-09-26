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
        "non su un server di Invoice Cove. Non raccogliamo, non vediamo e non riceviamo alcun dato sulle tue fatture né su come usi l'app. "
        "Nessuna analisi, nessun tracciamento, niente viene inviato in background. "
        "L'unico momento in cui l'app stessa ha bisogno di una connessione a internet è per elaborare l'acquisto una tantum di Invoice Cove Pro tramite Google Play. "
        "Per i dettagli consulta l'<a href=\"privacy.html\">Informativa sulla privacy</a>."
    ),
    "warn": (
        "Ricorda! Prima di disinstallare l'app o cancellarne i dati: questi dati non sono salvati da noi in nessun luogo. "
        "Disinstallare Invoice Cove, o cancellarne i dati dalle impostazioni di Android, elimina definitivamente ogni fattura, preventivo, cliente "
        "e impostazione su questo dispositivo: non esiste una copia nel cloud da cui ripristinare. Per proteggere i tuoi file: crea un backup "
        "con Invoice Cove Pro (vedi <a href=\"#backup\">Backup e ripristino</a>) oppure esporta ciò che ti serve in Excel, CSV o ZIP "
        "(vedi <a href=\"#export\">Esportare le fatture</a>)."
    ),
    "sections": {
        "home": ("Schermata principale", [
            ("p", "La schermata principale è il tuo punto di partenza, con un riquadro per ogni azione principale: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} e "
                  "{{common_reports_title}}. Tocca un riquadro per andare direttamente lì."),
            ("p", "La barra in basso ti dà accesso rapido a {{nav_home}}, {{nav_new}} (nuova fattura), "
                  "{{nav_invoices}}, {{nav_customers}} e {{nav_reports}}."),
            ("p", "L'icona a forma di ingranaggio (⚙️) nell'angolo in alto a destra della maggior parte delle schermate apre i <a href=\"#settings\">Dati dell'attività e impostazioni</a>."),
        ]),
        "customers": ("Clienti", [
            ("p", "Per aggiungere un cliente, vai alla scheda {{nav_customers}} e tocca l'icona +, oppure usa il riquadro {{home_new_customer_title}}. "
                  "Puoi aggiungerne uno anche mentre crei una fattura o un preventivo. Per creare la scheda di un cliente basta il nome. "
                  "I campi facoltativi includono: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, l'indirizzo, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} e una tinta di colore per i suoi documenti. Ogni campo mostra un esempio, così sai cosa inserire."),
            ("p", "Tocca un cliente per modificarlo ({{common_edit}}), aprire la sua {{customers_view_history}} (fatture, preventivi e bozze) "
                  "o eliminarlo ({{common_delete}})."),
            ("p", "Sulle tue fatture e sui preventivi, i dati del cliente sono stampati sotto il suo nome in un ordine fisso: numero cliente, codice fiscale, partita IVA, "
                  "numero del registro delle imprese, poi indirizzo, email e telefono. Ciò che lasci vuoto non viene stampato."),
            ("note", "Qui il salvataggio funziona in modo diverso rispetto alle fatture. Un cliente ha il suo pulsante {{customers_form_save_customer}} "
                     "(oppure {{customers_form_save_changes}} in modifica) e viene salvato non appena lo tocchi. Se provi a chiudere il modulo "
                     "con modifiche non salvate, Invoice Cove ti chiede prima conferma."),
            ("note", "Eliminare un cliente non elimina le fatture e i preventivi che gli hai già emesso. Tuttavia, le sue <a href=\"#drafts\">bozze</a> non completate "
                     "vengono eliminate insieme a lui; Invoice Cove ti chiede prima conferma."),
        ]),
        "new-invoice": ("Creare una fattura", [
            ("p", "Da {{nav_new}} (o dal riquadro {{home_new_invoice_title}}): scegli un cliente (o creane uno al volo) "
                  "e imposta la data della fattura e la scadenza, poi aggiungi le voci."),
            ("p", "Tocca {{newinvoice_add_item_details_button}} e compila descrizione, quantità, prezzo unitario e, facoltativamente, un'unità "
                  "(come h, pz o kg) e una data e un'ora. L'unità è stampata accanto alla quantità nel PDF. Tocca la matita (✏️) su una voce per correggerla "
                  "o il cestino (🗑️) per rimuoverla. Le descrizioni e i prezzi usati in precedenza ti vengono suggeriti mentre scrivi."),
            ("p", "Poi aggiungi, se necessario, un'aliquota, uno {{newinvoice_discount_label}} (percentuale o importo fisso) e "
                  "{{common_notes_label}}. Il numero della fattura è assegnato per te (con Invoice Cove Pro si può modificare), e la valuta si sceglie accanto."),
            ("p", "{{common_preview_button}} genera un PDF temporaneo per vedere come viene: non si salva ancora nulla. "
                  "Il pulsante {{common_template_button}} mostra quale modello verrà usato; toccalo per sceglierne un altro solo per questo documento."),
            ("note", "{{newinvoice_generate_button}} fa tre cose insieme: salva la fattura, crea il PDF e apre il menu di condivisione "
                     "del dispositivo per inviarla. Non sei ancora pronto? Usa {{newinvoice_save_draft_button}} — vedi <a href=\"#drafts\">Bozze</a>."),
        ]),
        "drafts": ("Bozze", [
            ("p", "Non perdi una fattura a cui stai ancora lavorando. Appena hai scelto un cliente e aggiunto almeno una voce o una nota, Invoice Cove "
                  "conserva una bozza e la aggiorna poco dopo che hai smesso di scrivere, e ancora una volta quando esci dall'app. Non c'è "
                  "la domanda «scartare le modifiche?» quando lasci la schermata; un breve messaggio ti avvisa che la bozza è stata salvata."),
            ("p", "Tocca {{newinvoice_save_draft_button}} (sotto {{newinvoice_generate_button}}) per mettere da parte la fattura di proposito: viene salvata e "
                  "il modulo si svuota, pronto per la fattura successiva. Funziona appena è stato scelto un cliente, anche prima di aggiungere voci."),
            ("p", "Trovi le tue bozze in {{nav_customers}} → il cliente → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Ogni bozza mostra quando è stata modificata l'ultima volta, quante voci ha e il totale. Toccala per continuare "
                  "a modificarla o per generare la fattura; tocca il cestino per eliminarla."),
            ("ul", [
                "Una bozza non usa mai un numero di fattura e non conta nel limite mensile gratuito. Il numero viene assegnato solo quando generi la fattura "
                "definitiva — la bozza viene poi sostituita da essa.",
                "Una bozza conserva la data della fattura e la scadenza solo se le hai scelte tu; altrimenti, quando la riapri, usa la data di oggi.",
                "Eliminare un cliente elimina anche le sue bozze (Invoice Cove te lo chiede prima). Le bozze sono incluse in un backup.",
                "Le bozze esistono per le fatture; i preventivi non le hanno.",
            ]),
        ]),
        "invoices": ("Gestire le fatture", [
            ("p", "La scheda {{nav_invoices}} raggruppa le tue fatture in una cartella per cliente, che puoi ordinare per "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> o <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Apri una cartella per vederne le fatture, ordinate per data, valore, numero o stato."),
            ("p", "Ogni fattura ha uno stato: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (scadenza superata), "
                  "{{invoices_status_partially_paid}} (è stato registrato un acconto), {{invoices_status_paid}} o "
                  "{{invoices_status_void}}. Tocca una fattura per vederla ({{common_view}}), reinviarla ({{common_share}}), segnarla come pagata o annullata, oppure eliminarla."),
            ("ul", [
                "{{invoices_action_mark_paid}} chiede la data del pagamento e come è stato pagato (bonifico, contanti, carta, PayPal o altro). "
                "Una fattura pagata non può più essere riportata a non pagata.",
                "{{deposit_record_title}} annota un pagamento anticipato. La fattura risulta poi {{invoices_status_partially_paid}}, e l'acconto non può superare il totale.",
                "{{invoices_action_mark_void}} conserva la fattura nei tuoi registri ma la segna come annullata. È preferibile all'eliminazione, perché una fattura eliminata "
                "non si può recuperare.",
            ]),
            ("p", "Con Pro, la cartella di un cliente può anche essere salvata o condivisa come ZIP di PDF, e l'intero elenco può essere esportato per il tuo commercialista — vedi "
                  "<a href=\"#export\">Esportare le fatture</a>."),
        ]),
        "export": ("Esportare le fatture (Excel, CSV, ZIP)", [
            ("p", "Disponibile con Invoice Cove Pro. Tocca l'icona di esportazione (📄) in alto nella scheda {{nav_invoices}}. Scegli quali fatture includere "
                  "con i selettori di anno e mese ({{invoices_export_all}}, un anno o un mese di un anno; vengono proposti solo gli anni e i mesi che "
                  "hanno fatture), poi scegli cosa fare:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — un foglio di calcolo Excel (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — la stessa tabella come file CSV.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — i PDF delle fatture in un unico ZIP, una cartella per cliente.",
                "{{invoices_export_delete}} — elimina definitivamente le fatture selezionate dopo due conferme.",
            ]),
            ("p", "<em>Salva</em> ti lascia scegliere dove sul dispositivo va il file; <em>Condividi</em> apre il menu di condivisione di Android per inviarlo "
                  "via email o in un messaggio."),
            ("p", "Excel e CSV sono pensati per il tuo commercialista: per impostazione predefinita, una riga per ogni fattura, con numero e date, "
                  "nome, numero, codice fiscale, partita IVA, numero del registro delle imprese e indirizzo del cliente, subtotale, sconto, aliquota IVA, "
                  "importo IVA e totale della fattura, la valuta, e stato, data e metodo di pagamento. Le intestazioni delle colonne e le parole fisse "
                  "(fattura, pagata, non pagata, metodi di pagamento) sono scritte nella lingua impostata nell'app."),
            ("p", "Per ottenere una riga per ogni voce di fattura, con i dati della fattura ripetuti su ogni riga e descrizione, quantità, unità, "
                  "prezzo e importo netto di ogni voce aggiunti, attiva {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Creare un preventivo", [
            ("p", "Il riquadro {{home_new_quote_title}} funziona come il riquadro Nuova fattura: stessi campi, stessi pulsanti {{common_preview_button}} e {{common_template_button}}, stesso "
                  "{{newquote_generate_button}} che salva, crea il PDF e apre il menu di condivisione con un tocco, ma con una "
                  "{{newquote_date_label}} e una data {{newquote_valid_until_label}} al posto di data della fattura e scadenza."),
            ("p", "I preventivi non hanno bozze."),
        ]),
        "quotes": ("Gestire i preventivi e convertirli in fattura", [
            ("p", "La schermata {{common_quotes_title}} (dal riquadro nella schermata principale) elenca i preventivi per cliente, come per le fatture. Apri un preventivo per "
                  "vederlo o condividerlo, usa {{quotes_action_accept}} o {{quotes_action_decline}} quando il cliente risponde, "
                  "registra un acconto oppure eliminalo. L'acconto non può superare il totale del preventivo."),
            ("p", "Quando un cliente accetta un preventivo, usa {{quotes_action_convert_to_invoice}} per trasformare le righe selezionate in una vera fattura, "
                  "modificabile in modo indipendente. Scadenza e sconto si possono ancora regolare, e il preventivo originale viene segnato come "
                  "{{quotes_status_converted}} e conservato nei tuoi registri."),
        ]),
        "calendar": ("Calendario e promemoria", [
            ("p", "La schermata {{calendar_title}} è una vista mensile per le tue note. Tocca un giorno per vedere o aggiungere note; una nota ha un titolo e un testo e, "
                  "con {{calendar_remind_me}} e un orario, ti invia una notifica alla data e all'ora impostate. Il primo giorno della settimana segue le tue impostazioni."),
            ("p", "Separatamente, Invoice Cove invia promemoria di pagamento — notifiche locali per le fatture in scadenza o scadute. Non viene inviato nulla a un server né ricevuto da esso."),
        ]),
        "reports": ("Report", [
            ("p", "{{common_reports_title}} ti dà una panoramica rapida: gli importi {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} e {{reports_stat_overdue}}, quante fatture hai, "
                  "<em>{{reports_revenue_by_month}}</em> e i tuoi <em>{{reports_top_customers}}</em> per totale fatturato."),
            ("p", "Tocca la scheda {{reports_stat_outstanding}} o {{reports_stat_overdue}} per aprire l'elenco esatto di quelle fatture."),
        ]),
        "settings": ("Dati dell'attività e impostazioni", [
            ("p", "Apri le impostazioni dall'icona a forma di ingranaggio; questa schermata si chiama {{settings_title}}. Inizia con le tue preferenze facoltative: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} o {{settings_theme_dark}}), "
                  "{{settings_invoice_template_label}} predefinito, {{settings_tax_label_label}} (IVA, GST…), "
                  "{{settings_first_day_of_week_label}} e {{settings_due_date_default_label}}, che compila la scadenza automaticamente (ad esempio Net 30). "
                  "Sotto seguono {{settings_security_label}} (vedi <a href=\"#app-lock\">Blocco dell'app</a>), "
                  "{{settings_item_suggestions_label}} e {{settings_backup_restore_label}} (vedi <a href=\"#backup\">Backup e ripristino</a>)."),
            ("p", "{{settings_item_memory_title}} ricorda descrizioni e prezzi delle voci per suggerirli mentre scrivi; <em>{{common_clear}}</em> li dimentica "
                  "senza toccare le tue fatture."),
            ("p", "Più in basso c'è il profilo della tua attività, stampato su ogni fattura e preventivo: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, un breve slogan ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, il {{settings_date_format_label}} delle date, l'indirizzo, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (numero di registrazione, capitale sociale e simili), il tuo "
                  "{{settings_business_logo_label}} e i tuoi {{settings_payment_details_label}} (IBAN, link PayPal.me). Ogni campo "
                  "ha un esempio, e qualsiasi campo lasci vuoto non compare sulle tue fatture. Tocca {{common_done}} quando "
                  "hai finito; se esci con modifiche non salvate, ti viene chiesta conferma."),
            ("p", "In fondo vengono mostrati questa {{settings_user_manual}} e {{settings_share_this_app}}."),
        ]),
        "backup": ("Backup e ripristino", [
            ("p", "Disponibile con Invoice Cove Pro, in {{settings_backup_restore_label}}. {{settings_create_backup_title}} salva "
                  "tutto: fatture, preventivi, bozze, clienti, calendario, impostazioni, il tuo logo e i PDF, tutto in un solo file. Scegli "
                  "{{backup_save_button}} per conservarlo dove vuoi, oppure {{backup_share_button}} per inviarlo in un luogo sicuro."),
            ("p", "{{settings_restore_backup_title}} riporta tutto, nel caso tu debba passare a un telefono nuovo. Funziona solo su un'installazione nuova, prima di aver "
                  "aggiunto dati, quindi non può mai sovrascrivere ciò che hai già. Invoice Cove verifica che il file sia integro e ti avvisa se è danneggiato, "
                  "se non è un backup di Invoice Cove o se è stato creato da una versione più recente dell'app (aggiorna prima)."),
            ("note", "Un file di backup non è cifrato: chiunque lo abbia può leggere i tuoi dati. Conservalo in un luogo privato. Il PIN di blocco dell'app non "
                     "è mai incluso."),
        ]),
        "app-lock": ("Blocco dell'app", [
            ("p", "In {{settings_security_label}} puoi attivare {{settings_app_lock_title}}: Invoice Cove ti chiede allora il PIN "
                  "(o l'impronta) quando l'app viene aperta da zero o dopo il riavvio del telefono — non ogni volta che ci torni."),
            ("ul", [
                "{{settings_set_pin}}: scegli un PIN di 4 cifre e confermalo.",
                "Ricevi poi un codice di recupero di 6 cifre, mostrato una sola volta. Annotalo e conservalo in un luogo sicuro.",
                "Se il tuo telefono lo supporta, sblocca con l'impronta ({{security_use_fingerprint}}).",
                "Hai dimenticato il PIN? Usa {{security_forgot_pin}} e inserisci il codice di recupero. Dopo 5 tentativi errati devi attendere 30 secondi – "
                "l'attesa aumenta con altri tentativi errati.",
            ]),
            ("note", "Se perdi sia il PIN sia il codice di recupero e non hai configurato lo sblocco con impronta, non c'è modo di rientrare. Non possiamo reimpostarlo "
                     "per te."),
        ]),
        "languages": ("Lingue", [
            ("p", "Invoice Cove parla 13 lingue: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands e Svenska. Tocca l'icona rotonda con la bandiera in alto nelle impostazioni per cambiare — l'app cambia subito."),
            ("p", "Il testo dei tuoi PDF e delle esportazioni Excel/CSV segue la lingua impostata nell'app, e questa guida è disponibile nelle stesse 13 lingue "
                  "(usa la barra delle lingue in alto nella pagina)."),
        ]),
        "templates": ("Modelli PDF", [
            ("p", "Invoice Cove offre per ora 18 modelli PDF: Classic, Client Color (tinto con il colore del cliente), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves e Spooky Hollow."),
            ("p", "Scegli il modello predefinito in Impostazioni → {{settings_invoice_template_label}}: tocca un modello, poi {{common_done}}. Vale "
                  "per tutto ciò che generi da quel momento. Per una singola fattura o un singolo preventivo, usa il pulsante {{common_template_button}} "
                  "nel modulo."),
            ("p", "Ogni modello stampa le stesse informazioni: i dati della tua attività, quelli del cliente, le voci con unità e data, i totali, le note e "
                  "i dati di pagamento — ma solo ciò che hai compilato. Le fatture lunghe continuano su una seconda pagina, con i totali insieme all'ultima voce."),
        ]),
        "free-vs-pro": ("Piano gratuito e Invoice Cove Pro", [
            ("p", "Invoice Cove è gratuito, con alcuni limiti ragionevoli:"),
            ("ul", [
                "Fino a 3 fatture generate per mese di calendario",
                "Fino a 3 preventivi generati per mese di calendario",
                "Fino a 3 clienti alla volta",
                "I numeri di fatture e preventivi sono assegnati automaticamente e non si possono modificare",
                "L'esportazione in Excel, CSV e ZIP è solo Pro",
                "Backup e ripristino sono solo Pro",
            ]),
            ("p", "Invoice Cove Pro è un unico acquisto tramite Google Play (non un abbonamento) che elimina per sempre tutti questi limiti. "
                  "Bozze, tutti i modelli e le lingue, il blocco dell'app e la creazione, l'anteprima e la condivisione dei documenti sono gratuiti per tutti. "
                  "Consulta le <a href=\"terms.html\">Condizioni d'uso</a> per tutti i dettagli."),
        ]),
    },
}
