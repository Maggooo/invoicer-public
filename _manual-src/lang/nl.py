T = {
    "title": "Gebruikersgids",
    "subtitle": "Alles wat Invoice Cove kan, scherm voor scherm.",
    "meta_desc": "Volledige gebruikersgids voor de app Invoice Cove - Offline Billing.",
    "lang_label": "Taal",
    "brand_alt": "Invoice Cove",
    "toc": "Inhoud",
    "footer_questions": "Vragen?",
    "lede": (
        "Invoice Cove werkt volledig op uw apparaat: uw facturen, offertes, klanten en bedrijfsgegevens worden lokaal opgeslagen, "
        "niet op een server van Invoice Cove. Wij verzamelen, zien of ontvangen geen gegevens over uw facturen of over hoe u de app gebruikt. "
        "Geen analytics, geen tracking, niets wordt op de achtergrond verzonden. "
        "Het enige moment waarop de app zelf internet nodig heeft, is bij de verwerking van de eenmalige aankoop van Invoice Cove Pro via Google Play. "
        "Details vindt u in het <a href=\"privacy.html\">Privacybeleid</a>."
    ),
    "warn": (
        "Denk eraan! Voordat u de app verwijdert of de opslag ervan wist: wij bewaren deze gegevens nergens als back-up. "
        "Als u Invoice Cove verwijdert of de opslag ervan wist in de Android-instellingen, worden alle facturen, offertes, klanten "
        "en instellingen op dit apparaat definitief gewist — er is geen kopie in de cloud om uit te herstellen. Om uw bestanden te beschermen: maak een back-up "
        "met Invoice Cove Pro (zie <a href=\"#backup\">Back-up en herstel</a>) of exporteer wat u nodig hebt naar Excel, CSV of ZIP "
        "(zie <a href=\"#export\">Facturen exporteren</a>)."
    ),
    "sections": {
        "home": ("Startscherm", [
            ("p", "Het startscherm is uw uitgangspunt, met een tegel voor elke hoofdactie: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} en "
                  "{{common_reports_title}}. Tik op een tegel om er direct naartoe te gaan."),
            ("p", "De balk onderaan geeft u snelle toegang tot {{nav_home}}, {{nav_new}} (nieuwe factuur), "
                  "{{nav_invoices}}, {{nav_customers}} en {{nav_reports}}."),
            ("p", "Het tandwielpictogram (⚙️) rechtsboven op de meeste schermen opent <a href=\"#settings\">Bedrijfsgegevens en instellingen</a>."),
        ]),
        "customers": ("Klanten", [
            ("p", "Om een klant toe te voegen, gaat u naar het tabblad {{nav_customers}} en tikt u op het +-pictogram, of gebruikt u de tegel {{home_new_customer_title}}. "
                  "U kunt ook een klant toevoegen tijdens het maken van een factuur of offerte. Voor het aanmaken van een klantkaart is alleen de naam nodig. "
                  "Optionele velden zijn onder meer: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, adres, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} en een kleurtint voor de documenten van de klant. Elk veld toont een voorbeeld, zodat duidelijk is wat erin hoort."),
            ("p", "Tik op een klant om deze te bewerken ({{common_edit}}), de {{customers_view_history}} te openen (facturen, offertes en concepten) "
                  "of de klant te verwijderen ({{common_delete}})."),
            ("p", "Op uw facturen en offertes worden de klantgegevens onder de naam in een vaste volgorde afgedrukt: klantnummer, fiscaal nummer, btw-nummer, "
                  "handelsregisternummer, daarna adres, e-mail en telefoon. Wat u niet invult, wordt niet afgedrukt."),
            ("note", "Opslaan werkt hier anders dan bij facturen. Een klant heeft een eigen knop {{customers_form_save_customer}} "
                     "(bij bewerken {{customers_form_save_changes}}) en de klant wordt opgeslagen op het moment dat u erop tikt. Als u het formulier "
                     "probeert te sluiten met niet-opgeslagen wijzigingen, vraagt Invoice Cove eerst om bevestiging."),
            ("note", "Als u een klant verwijdert, worden de facturen en offertes die u al voor die klant hebt gemaakt niet verwijderd. De onvoltooide <a href=\"#drafts\">concepten</a> "
                     "worden echter wel samen met de klant verwijderd; Invoice Cove vraagt u eerst om bevestiging."),
        ]),
        "new-invoice": ("Een factuur maken", [
            ("p", "Op {{nav_new}} (of via de tegel {{home_new_invoice_title}}): kies een klant (of maak er meteen een aan) "
                  "en stel de factuurdatum en de vervaldatum in en voeg daarna regels toe."),
            ("p", "Tik op {{newinvoice_add_item_details_button}} en vul de omschrijving, het aantal, de prijs per eenheid en eventueel de eenheid in "
                  "(bijv. u, st of kg), plus datum en tijd. De eenheid wordt in de pdf naast het aantal afgedrukt. Met het potlood (✏️) bij een regel corrigeert u die, "
                  "met de prullenbak (🗑️) verwijdert u die. Eerder gebruikte omschrijvingen en prijzen worden tijdens het typen voorgesteld."),
            ("p", "Voeg daarna indien nodig een belastingtarief, {{newinvoice_discount_label}} (percentage of vast bedrag) en "
                  "{{common_notes_label}} toe. Het factuurnummer wordt automatisch toegekend (met Invoice Cove Pro kan het worden aangepast) en de valuta kiest u ernaast."),
            ("p", "{{common_preview_button}} maakt een tijdelijke pdf zodat u kunt zien hoe het eruitziet — er wordt nog niets opgeslagen. "
                  "De knop {{common_template_button}} toont welke sjabloon wordt gebruikt; tik erop om alleen voor dit document een ander te kiezen."),
            ("note", "{{newinvoice_generate_button}} doet drie dingen tegelijk: de factuur opslaan, de pdf maken en het deelmenu van "
                     "uw apparaat openen zodat u de factuur kunt versturen. Nog niet klaar? Gebruik {{newinvoice_save_draft_button}} — zie <a href=\"#drafts\">Concepten</a>."),
        ]),
        "drafts": ("Concepten", [
            ("p", "Een factuur waaraan u nog werkt, raakt u niet kwijt. Zodra u een klant kiest en minstens één regel of notitie toevoegt, bewaart Invoice Cove "
                  "een concept en werkt dat kort nadat u stopt met typen bij, en nog een keer wanneer u de app verlaat. Bij het verlaten van het scherm verschijnt er "
                  "geen vraag „wijzigingen negeren?”; een korte melding laat weten dat het concept is bewaard."),
            ("p", "Tik op {{newinvoice_save_draft_button}} (onder {{newinvoice_generate_button}}) om een factuur bewust opzij te leggen: die wordt bewaard en "
                  "het formulier wordt leeggemaakt, klaar voor de volgende factuur. Dit werkt zodra een klant is gekozen, ook vóór het toevoegen van regels."),
            ("p", "U vindt concepten onder {{nav_customers}} → klant → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Elk concept toont wanneer het voor het laatst is gewijzigd, hoeveel regels het heeft en het totaalbedrag. Tik erop om "
                  "verder te bewerken of de factuur uit te schrijven; de prullenbak verwijdert het."),
            ("ul", [
                "Een concept gebruikt nooit een factuurnummer en telt niet mee voor de gratis maandlimiet. Het nummer wordt pas toegekend wanneer u de definitieve "
                "factuur maakt — het concept maakt dan plaats voor die factuur.",
                "Een concept onthoudt de factuurdatum en de vervaldatum alleen als u die zelf hebt gekozen; anders wordt bij het heropenen de datum van vandaag gebruikt.",
                "Als u een klant verwijdert, worden ook de concepten ervan verwijderd (Invoice Cove vraagt dit eerst). Concepten maken deel uit van de back-up.",
                "Concepten bestaan voor facturen; offertes hebben ze niet.",
            ]),
        ]),
        "invoices": ("Facturen beheren", [
            ("p", "Het tabblad {{nav_invoices}} groepeert facturen in een map per klant, die u kunt sorteren op "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> of <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Open een map om de facturen erin te zien, gesorteerd op datum, waarde, nummer of status."),
            ("p", "Elke factuur heeft een status: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (na de vervaldatum), "
                  "{{invoices_status_partially_paid}} (er is een aanbetaling geregistreerd), {{invoices_status_paid}} of "
                  "{{invoices_status_void}}. Tik op een factuur om die te bekijken ({{common_view}}), opnieuw te versturen ({{common_share}}), als betaald of vervallen te markeren of te verwijderen."),
            ("ul", [
                "{{invoices_action_mark_paid}} vraagt om de betaaldatum en de betaalwijze (overschrijving, contant, kaart, PayPal of anders). "
                "Een betaalde factuur kan niet meer worden teruggezet naar onbetaald.",
                "{{deposit_record_title}} registreert een vooruitbetaling. De factuur wordt dan weergegeven als {{invoices_status_partially_paid}} en de aanbetaling mag het totaal niet overschrijden.",
                "{{invoices_action_mark_void}} houdt de factuur in uw administratie maar markeert die als geannuleerd. Dit is beter dan verwijderen, want een verwijderde factuur "
                "kan niet worden hersteld.",
            ]),
            ("p", "Met Pro kunt u de map van een klant ook opslaan of delen als ZIP met de pdf's, en de volledige lijst exporteren voor uw boekhouder — zie "
                  "<a href=\"#export\">Facturen exporteren</a>."),
        ]),
        "export": ("Facturen exporteren (Excel, CSV, ZIP)", [
            ("p", "Beschikbaar met Invoice Cove Pro. Tik op het exportpictogram (📄) bovenaan het tabblad {{nav_invoices}}. Kies welke facturen worden opgenomen "
                  "met de jaar- en maandkeuze ({{invoices_export_all}}, één jaar of één maand van een jaar; alleen jaren en maanden "
                  "waarin facturen bestaan worden aangeboden) en kies daarna wat u ermee wilt doen:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — een Excel-spreadsheet (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — dezelfde tabel als CSV-bestand.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — de pdf's van de facturen in één ZIP, met een map per klant.",
                "{{invoices_export_delete}} — verwijdert de gekozen facturen definitief na twee bevestigingen.",
            ]),
            ("p", "Met <em>Opslaan</em> kiest u waar op het apparaat het bestand terechtkomt; <em>Delen</em> opent het deelmenu van Android zodat u het "
                  "per e-mail of in een bericht kunt versturen."),
            ("p", "Excel en CSV zijn gemaakt voor uw boekhouder: standaard één rij per factuur, met nummer en data, naam, nummer, fiscaal "
                  "nummer, btw-nummer, handelsregisternummer en adres van de klant, subtotaal, korting, btw-tarief, btw-bedrag en factuurtotaal, valuta en "
                  "status, datum en wijze van betaling. De kolomkoppen en vaste woorden (factuur, betaald, onbetaald, betaalwijzen) staan in de taal waarop "
                  "de app is ingesteld."),
            ("p", "Om één rij per factuurregel te krijgen, met de factuurgegevens op elke rij herhaald en de omschrijving, het aantal, de eenheid, "
                  "de prijs en het nettobedrag van elke regel toegevoegd, zet u {{invoices_export_detailed_toggle}} aan."),
        ]),
        "new-quote": ("Een offerte maken", [
            ("p", "De tegel {{home_new_quote_title}} werkt zoals de tegel Nieuwe factuur: dezelfde velden, dezelfde knoppen {{common_preview_button}} en {{common_template_button}}, dezelfde "
                  "{{newquote_generate_button}}, die met één tik opslaat, de pdf maakt en het deelmenu opent, maar met "
                  "{{newquote_date_label}} en een datum {{newquote_valid_until_label}} in plaats van factuurdatum en vervaldatum."),
            ("p", "Offertes hebben geen concepten."),
        ]),
        "quotes": ("Offertes beheren en omzetten naar een factuur", [
            ("p", "Het scherm {{common_quotes_title}} (via de tegel op het startscherm) toont offertes per klant, net als facturen. Open een offerte om die te "
                  "bekijken of te delen, gebruik {{quotes_action_accept}} of {{quotes_action_decline}} wanneer de klant antwoordt, "
                  "registreer een aanbetaling of verwijder de offerte. Een aanbetaling mag het totaal van de offerte niet overschrijden."),
            ("p", "Wanneer de klant de offerte accepteert, gebruikt u {{quotes_action_convert_to_invoice}} en worden de aangevinkte regels omgezet in een echte factuur, "
                  "die u afzonderlijk kunt aanpassen. De vervaldatum en de korting zijn nog te wijzigen en de oorspronkelijke offerte wordt gemarkeerd als "
                  "{{quotes_status_converted}} en blijft in uw administratie."),
        ]),
        "calendar": ("Agenda en herinneringen", [
            ("p", "Het scherm {{calendar_title}} is een maandoverzicht voor uw eigen notities. Tik op een dag om notities te bekijken of toe te voegen; een notitie heeft een titel en tekst en "
                  "stuurt u met de optie {{calendar_remind_me}} en een tijd op de ingestelde datum en tijd een melding. De eerste dag van de week volgt uw instellingen."),
            ("p", "Los daarvan stuurt Invoice Cove betalingsherinneringen — lokale meldingen over facturen die bijna vervallen of al vervallen zijn. Er wordt niets naar een server verzonden of daarvan ontvangen."),
        ]),
        "reports": ("Rapporten", [
            ("p", "{{common_reports_title}} geeft u een snel overzicht: de bedragen {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} en {{reports_stat_overdue}}, het aantal facturen, "
                  "<em>{{reports_revenue_by_month}}</em> en uw <em>{{reports_top_customers}}</em> op gefactureerd bedrag."),
            ("p", "Tik op de kaart {{reports_stat_outstanding}} of {{reports_stat_overdue}} om precies die facturen in een lijst te openen."),
        ]),
        "settings": ("Bedrijfsgegevens en instellingen", [
            ("p", "Open de instellingen via het tandwielpictogram; dit scherm heet {{settings_title}}. Het begint met uw optionele voorkeuren: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} of {{settings_theme_dark}}), het standaard "
                  "{{settings_invoice_template_label}}, {{settings_tax_label_label}} (btw, GST…), "
                  "{{settings_first_day_of_week_label}} en {{settings_due_date_default_label}}, die de vervaldatum automatisch invult (bijv. Net 30). "
                  "Daaronder vindt u {{settings_security_label}} (zie <a href=\"#app-lock\">App-vergrendeling</a>), "
                  "{{settings_item_suggestions_label}} en {{settings_backup_restore_label}} (zie <a href=\"#backup\">Back-up en herstel</a>)."),
            ("p", "{{settings_item_memory_title}} onthoudt omschrijvingen en prijzen van regels om ze tijdens het typen voor te stellen; <em>{{common_clear}}</em> vergeet ze, "
                  "zonder uw facturen aan te raken."),
            ("p", "Daaronder staat het profiel van uw bedrijf dat op elke factuur en offerte wordt afgedrukt: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, een korte slogan ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, de {{settings_date_format_label}} van datums, adres, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (registratienummer, maatschappelijk kapitaal en dergelijke), "
                  "{{settings_business_logo_label}} en {{settings_payment_details_label}} (IBAN, PayPal.me-link). Elk veld "
                  "heeft een voorbeeld en elk veld dat u leeg laat, verschijnt niet op uw facturen. Tik op {{common_done}} als u klaar bent; "
                  "als u vertrekt met niet-opgeslagen wijzigingen, vraagt de app eerst om bevestiging."),
            ("p", "Helemaal onderaan worden deze {{settings_user_manual}} en {{settings_share_this_app}} weergegeven."),
        ]),
        "backup": ("Back-up en herstel", [
            ("p", "Beschikbaar met Invoice Cove Pro, onder {{settings_backup_restore_label}}. {{settings_create_backup_title}} bewaart "
                  "alles: facturen, offertes, concepten, klanten, agenda, instellingen, logo en pdf's, alles in één bestand. Kies "
                  "{{backup_save_button}} om het op te slaan waar u wilt, of {{backup_share_button}} om het naar een veilige plek te sturen."),
            ("p", "{{settings_restore_backup_title}} zet alles terug, voor het geval u naar een nieuwe telefoon moet overstappen. Het werkt alleen op een verse installatie, zolang u nog "
                  "geen gegevens hebt toegevoegd, zodat het nooit kan overschrijven wat u al hebt. Invoice Cove controleert of het bestand intact is en waarschuwt u als het beschadigd is, "
                  "geen Invoice Cove-back-up is of gemaakt is door een nieuwere versie van de app (werk eerst bij)."),
            ("note", "Het back-upbestand is niet versleuteld: iedereen die het heeft, kan uw gegevens lezen. Bewaar het op een privéplek. De pincode van de app-vergrendeling wordt er nooit "
                     "in opgenomen."),
        ]),
        "app-lock": ("App-vergrendeling", [
            ("p", "Onder {{settings_security_label}} kunt u {{settings_app_lock_title}} inschakelen: Invoice Cove vraagt dan om een pincode "
                  "(of vingerafdruk) wanneer de app helemaal opnieuw wordt geopend of nadat de telefoon is herstart — niet bij elke terugkeer naar de app."),
            ("ul", [
                "{{settings_set_pin}}: kies een pincode van vier cijfers en bevestig die.",
                "Daarna krijgt u een herstelcode van zes cijfers die maar één keer wordt getoond. Schrijf die op en bewaar hem op een veilige plek.",
                "Als uw telefoon dit ondersteunt, ontgrendelt u met uw vingerafdruk ({{security_use_fingerprint}}).",
                "Pincode vergeten? Gebruik {{security_forgot_pin}} en voer de herstelcode in. Na 5 foute pogingen moet u 30 seconden wachten – "
                "de wachttijd wordt langer bij verdere foute pogingen.",
            ]),
            ("note", "Als u zowel de pincode als de herstelcode kwijtraakt en geen ontgrendeling met vingerafdruk hebt ingesteld, kunt u niet meer naar binnen. Wij kunnen die niet voor u "
                     "resetten."),
        ]),
        "languages": ("Talen", [
            ("p", "Invoice Cove spreekt 13 talen: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands en Svenska. Tik bovenaan de instellingen op het ronde vlagpictogram en de taal verandert — de app schakelt direct over."),
            ("p", "De tekst in uw pdf's en in de exports naar Excel/CSV volgt de taal waarop de app is ingesteld, en deze gids is beschikbaar in dezelfde 13 talen "
                  "(gebruik de taalbalk bovenaan de pagina)."),
        ]),
        "templates": ("Pdf-sjablonen", [
            ("p", "Invoice Cove biedt momenteel 18 pdf-ontwerpen: Classic, Client Color (in de kleur van de klant), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves en Spooky Hollow."),
            ("p", "Kies het standaardsjabloon onder Instellingen → {{settings_invoice_template_label}}: tik op een ontwerp en daarna op {{common_done}}. Dit geldt "
                  "voor alles wat u vanaf dat moment maakt. Voor één factuur of offerte gebruikt u de knop {{common_template_button}} "
                  "in het formulier."),
            ("p", "Elk sjabloon drukt dezelfde informatie af: uw bedrijfsgegevens, die van de klant, regels met eenheid en datum, totalen, notities en "
                  "betaalgegevens — maar alleen wat u hebt ingevuld. Lange facturen lopen door op een tweede pagina en het totaal blijft bij de laatste regel staan."),
        ]),
        "free-vs-pro": ("Gratis abonnement en Invoice Cove Pro", [
            ("p", "Invoice Cove is gratis, met een paar redelijke beperkingen:"),
            ("ul", [
                "Maximaal 3 facturen per kalendermaand",
                "Maximaal 3 offertes per kalendermaand",
                "Maximaal 3 klanten tegelijk",
                "Factuur- en offertenummers worden automatisch toegekend en kunnen niet worden aangepast",
                "Export naar Excel, CSV en ZIP is alleen met Pro",
                "Back-up en herstel zijn alleen met Pro",
            ]),
            ("p", "Invoice Cove Pro is één eenmalige aankoop via Google Play (geen abonnement) die al deze beperkingen voorgoed opheft. "
                  "Concepten, alle sjablonen en talen, de app-vergrendeling en het maken, bekijken en delen van documenten zijn voor iedereen gratis. "
                  "Alle details vindt u in de <a href=\"terms.html\">Gebruiksvoorwaarden</a>."),
        ]),
    },
}
