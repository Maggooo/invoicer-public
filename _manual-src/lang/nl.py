T = {
    "title": "Gebruikershandleiding",
    "subtitle": "Alles wat Invoice Cove kan, scherm voor scherm.",
    "meta_desc": "Volledige gebruikershandleiding voor de app Invoice Cove - Offline Billing.",
    "lang_label": "Taal",
    "brand_alt": "Invoice Cove",
    "toc": "Inhoud",
    "footer_questions": "Vragen?",
    "lede": (
        "Invoice Cove werkt volledig op uw apparaat — uw facturen, offertes, klanten en bedrijfsgegevens worden lokaal opgeslagen, "
        "niet op een server van Invoice Cove. <strong>Wij verzamelen, zien of ontvangen geen gegevens over uw facturen of over hoe u de app gebruikt</strong> "
        "— geen analytics, geen tracking, niets wordt op de achtergrond verzonden. "
        "Het enige moment waarop de app zelf internet nodig heeft, is bij de verwerking van de eenmalige aankoop van Invoice Cove Pro via Google Play. "
        "Details vindt u in het <a href=\"privacy.html\">Privacybeleid</a>."
    ),
    "warn": (
        "<strong>Voordat u de app verwijdert of de opslag ervan wist:</strong> wij bewaren deze gegevens nergens als back-up. "
        "Als u Invoice Cove verwijdert of de opslag ervan wist in de Android-instellingen, worden alle facturen, offertes, klanten "
        "en instellingen op dit apparaat definitief gewist — er is geen kopie in de cloud om uit te herstellen. Bescherm uzelf: maak een back-up "
        "met Invoice Cove Pro (zie <a href=\"#backup\">Back-up en herstel</a>) of exporteer wat u nodig hebt naar Excel, CSV of ZIP "
        "(zie <a href=\"#export\">Facturen exporteren</a>)."
    ),
    "sections": {
        "home": ("Startscherm", [
            ("p", "Het startscherm is uw uitgangspunt, met een tegel voor elke hoofdactie: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> en "
                  "<strong>{{common_reports_title}}</strong>. Tik op een tegel om er direct naartoe te gaan."),
            ("p", "De balk onderaan geeft u altijd snelle toegang tot <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (nieuwe factuur), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> en <strong>{{nav_reports}}</strong>."),
            ("p", "Het tandwielpictogram (⚙️) rechtsboven op de meeste schermen opent <a href=\"#settings\">Bedrijfsgegevens en instellingen</a>."),
        ]),
        "customers": ("Klanten", [
            ("p", "Voeg een klant toe via het tabblad <strong>{{nav_customers}}</strong> (tik op het +-pictogram), via de tegel <strong>{{home_new_customer_title}}</strong> "
                  "of direct tijdens het maken van een factuur of offerte. Alleen de naam is verplicht. Optionele velden: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, adres, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} en een kleur waarmee de documenten van de klant worden ingekleurd. Elk veld toont een voorbeeld, zodat duidelijk is wat erin hoort."),
            ("p", "Tik op een klant om deze te bewerken (<strong>{{common_edit}}</strong>), de <strong>{{customers_view_history}}</strong> te openen (facturen, offertes en concepten) "
                  "of de klant te verwijderen (<strong>{{common_delete}}</strong>)."),
            ("p", "Op uw facturen en offertes worden de klantgegevens onder de naam in een vaste volgorde afgedrukt: klantnummer, fiscaal nummer, btw-nummer, "
                  "handelsregisternummer, daarna adres, e-mail en telefoon. Wat u niet invult, wordt gewoon niet afgedrukt."),
            ("note", "<strong>Opslaan werkt hier anders dan bij facturen.</strong> Een klant heeft een eigen knop <strong>{{customers_form_save_customer}}</strong> "
                     "(bij bewerken <strong>{{customers_form_save_changes}}</strong>) — de klant wordt opgeslagen op het moment dat u erop tikt. Als u het formulier "
                     "probeert te sluiten met niet-opgeslagen wijzigingen, vraagt Invoice Cove eerst om bevestiging."),
            ("note", "Als u een klant verwijdert, worden de facturen en offertes die u al voor die klant hebt gemaakt niet verwijderd. De onvoltooide <a href=\"#drafts\">concepten</a> "
                     "worden wel samen met de klant verwijderd — de app vraagt dit eerst."),
        ]),
        "new-invoice": ("Een factuur maken", [
            ("p", "Op <strong>{{nav_new}}</strong> (of via de tegel <strong>{{home_new_invoice_title}}</strong>): kies een klant — of maak er meteen een aan — "
                  "stel de factuurdatum en de vervaldatum in en voeg daarna regels toe."),
            ("p", "Tik op <strong>{{newinvoice_add_item_details_button}}</strong> en vul de omschrijving, het aantal, de prijs per eenheid en eventueel de eenheid in "
                  "(bijv. u, st of kg), plus datum en tijd. De eenheid wordt in de pdf naast het aantal afgedrukt. Met het potlood (✏️) bij een regel corrigeert u die, "
                  "met de prullenbak (🗑️) verwijdert u die. Eerder gebruikte omschrijvingen en prijzen worden tijdens het typen voorgesteld."),
            ("p", "Voeg daarna naar wens een belastingtarief, <strong>{{newinvoice_discount_label}}</strong> (percentage of vast bedrag) en "
                  "<strong>{{common_notes_label}}</strong> toe. Het factuurnummer wordt automatisch toegekend (met Pro kunt u het aanpassen); de valuta kiest u ernaast."),
            ("p", "<strong>{{common_preview_button}}</strong> maakt een tijdelijke pdf zodat u kunt zien hoe het eruitziet — er wordt nog niets opgeslagen. "
                  "De knop <strong>{{common_template_button}}</strong> toont welke sjabloon wordt gebruikt; tik erop om alleen voor dit document een ander te kiezen."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> doet drie dingen tegelijk: de factuur opslaan, de pdf maken en het deelmenu van "
                     "uw apparaat openen zodat u de factuur kunt versturen. Nog niet klaar? Gebruik <strong>{{newinvoice_save_draft_button}}</strong> — zie <a href=\"#drafts\">Concepten</a>."),
        ]),
        "drafts": ("Concepten", [
            ("p", "Een factuur waaraan u nog werkt, raakt u niet kwijt. Zodra u een klant kiest en minstens één regel of notitie toevoegt, bewaart Invoice Cove "
                  "een <strong>concept</strong> en werkt dat kort nadat u stopt met typen bij — en nog een keer wanneer u de app verlaat. Bij het verlaten van het scherm verschijnt er "
                  "geen vraag „wijzigingen negeren?”; een korte melding laat weten dat het concept is bewaard."),
            ("p", "Tik op <strong>{{newinvoice_save_draft_button}}</strong> (onder {{newinvoice_generate_button}}) om een factuur bewust opzij te leggen: die wordt bewaard en "
                  "het formulier wordt leeggemaakt, klaar voor de volgende factuur. Dit werkt zodra een klant is gekozen, ook vóór het toevoegen van regels."),
            ("p", "U vindt concepten onder <strong>{{nav_customers}}</strong> → klant → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Elk concept toont wanneer het voor het laatst is gewijzigd, hoeveel regels het heeft en het totaalbedrag. Tik erop om "
                  "verder te bewerken of de factuur uit te schrijven; de prullenbak verwijdert het."),
            ("ul", [
                "Een concept gebruikt nooit een factuurnummer en telt niet mee voor de gratis maandlimiet. Het nummer wordt pas toegekend wanneer u de definitieve "
                "factuur maakt — het concept maakt dan plaats voor die factuur.",
                "Een concept onthoudt de factuurdatum en de vervaldatum alleen als u die zelf hebt gekozen; anders wordt bij het heropenen de datum van vandaag gebruikt.",
                "Als u een klant verwijdert, worden ook de concepten ervan verwijderd (de app vraagt dit eerst). Concepten maken deel uit van de back-up.",
                "Concepten bestaan voor facturen; offertes hebben ze niet.",
            ]),
        ]),
        "invoices": ("Facturen beheren", [
            ("p", "Het tabblad <strong>{{nav_invoices}}</strong> groepeert facturen in een map per klant, die u kunt sorteren op "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> of <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Open een map om de facturen erin te zien, gesorteerd op datum, waarde, nummer of status."),
            ("p", "Elke factuur heeft een status: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (na de vervaldatum), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (er is een aanbetaling geregistreerd), <strong>{{invoices_status_paid}}</strong> of "
                  "<strong>{{invoices_status_void}}</strong>. Tik op een factuur om die te bekijken ({{common_view}}), opnieuw te versturen ({{common_share}}), als betaald of vervallen te markeren of te verwijderen."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> vraagt om de betaaldatum en de betaalwijze (overschrijving, contant, kaart, PayPal of anders). "
                "Een betaalde factuur kan niet meer worden teruggezet naar onbetaald.",
                "<strong>{{deposit_record_title}}</strong> registreert een vooruitbetaling. De factuur wordt dan weergegeven als <strong>{{invoices_status_partially_paid}}</strong> en de aanbetaling mag het totaal niet overschrijden.",
                "<strong>{{invoices_action_mark_void}}</strong> houdt de factuur in uw administratie maar markeert die als geannuleerd. Kies dit liever dan verwijderen — een verwijderde factuur "
                "kan niet worden hersteld.",
            ]),
            ("p", "Met Pro kunt u de map van een klant ook opslaan of delen als ZIP met de pdf's, en de volledige lijst exporteren voor uw boekhouder — zie "
                  "<a href=\"#export\">Facturen exporteren</a>."),
        ]),
        "export": ("Facturen exporteren (Excel, CSV, ZIP)", [
            ("p", "Beschikbaar met Invoice Cove Pro. Tik op het exportpictogram (📄) bovenaan het tabblad <strong>{{nav_invoices}}</strong>. Kies welke facturen worden opgenomen "
                  "met de jaar- en maandkeuze (<strong>{{invoices_export_all}}</strong>, één jaar of één maand van een jaar — alleen jaren en maanden "
                  "waarin facturen bestaan worden aangeboden) en kies daarna wat u ermee wilt doen:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — een Excel-spreadsheet (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — dezelfde tabel als CSV-bestand.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — de pdf's van de facturen in één ZIP, met een map per klant.",
                "<strong>{{invoices_export_delete}}</strong> — verwijdert de gekozen facturen definitief na twee bevestigingen.",
            ]),
            ("p", "Met <em>Opslaan</em> kiest u waar op het apparaat het bestand terechtkomt; <em>Delen</em> opent het deelmenu van Android zodat u het "
                  "per e-mail of in een chat kunt versturen."),
            ("p", "Excel en CSV zijn gemaakt voor uw boekhouder: standaard <strong>één rij per factuur</strong> — nummer en data, naam, nummer, fiscaal "
                  "nummer, btw-nummer, handelsregisternummer en adres van de klant, subtotaal, korting, btw-tarief, btw-bedrag en factuurtotaal, valuta en "
                  "status, datum en wijze van betaling. De kolomkoppen en vaste woorden (factuur, betaald, onbetaald, betaalwijzen) staan in de taal waarop "
                  "de app is ingesteld."),
            ("p", "Zet <strong>{{invoices_export_detailed_toggle}}</strong> aan in hetzelfde blad om in plaats daarvan één rij per factuurregel te krijgen, "
                  "waarbij de factuurgegevens op elke rij worden herhaald en de omschrijving, het aantal, de eenheid, de prijs en het nettobedrag van elke "
                  "regel worden toegevoegd."),
        ]),
        "new-quote": ("Een offerte maken", [
            ("p", "<strong>{{home_new_quote_title}}</strong> werkt zoals New Invoice — dezelfde velden, dezelfde knoppen <strong>{{common_preview_button}}</strong> en <strong>{{common_template_button}}</strong> en dezelfde "
                  "<strong>{{newquote_generate_button}}</strong>, die met één tik opslaat, de pdf maakt en het deelmenu opent — met "
                  "<strong>{{newquote_date_label}}</strong> en een datum <strong>{{newquote_valid_until_label}}</strong> in plaats van factuurdatum en vervaldatum. "
                  "Offertes hebben geen concepten."),
        ]),
        "quotes": ("Offertes beheren en omzetten naar een factuur", [
            ("p", "Het scherm <strong>{{common_quotes_title}}</strong> (via de tegel op het startscherm) toont offertes per klant, net als facturen. Open een offerte om die te "
                  "bekijken of te delen, gebruik <strong>{{quotes_action_accept}}</strong> of <strong>{{quotes_action_decline}}</strong> wanneer de klant antwoordt, "
                  "registreer een aanbetaling of verwijder de offerte. Een aanbetaling mag het totaal van de offerte niet overschrijden."),
            ("p", "Wanneer de klant de offerte accepteert, gebruikt u <strong>{{quotes_action_convert_to_invoice}}</strong> en worden de aangevinkte regels omgezet in een echte factuur, "
                  "die u afzonderlijk kunt aanpassen — de vervaldatum en de korting zijn nog te wijzigen en de oorspronkelijke offerte wordt gemarkeerd als "
                  "<strong>{{quotes_status_converted}}</strong> en blijft in uw administratie."),
        ]),
        "calendar": ("Agenda en herinneringen", [
            ("p", "Het scherm <strong>{{calendar_title}}</strong> is een maandoverzicht voor uw eigen notities. Tik op een dag om notities te bekijken of toe te voegen; een notitie heeft een titel en tekst en "
                  "stuurt u met de optie <strong>{{calendar_remind_me}}</strong> en een tijd op dat moment een melding. De eerste dag van de week volgt uw instelling."),
            ("p", "Los daarvan stuurt Invoice Cove betalingsherinneringen — lokale meldingen over facturen die bijna vervallen of al vervallen zijn. Er wordt niets naar een server verzonden of daarvan ontvangen."),
        ]),
        "reports": ("Rapporten", [
            ("p", "<strong>{{common_reports_title}}</strong> geeft u een snel overzicht: de bedragen <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> en <strong>{{reports_stat_overdue}}</strong>, het aantal facturen, "
                  "<em>{{reports_revenue_by_month}}</em> en uw <em>{{reports_top_customers}}</em> op gefactureerd bedrag."),
            ("p", "Tik op de kaart <strong>{{reports_stat_outstanding}}</strong> of <strong>{{reports_stat_overdue}}</strong> om precies die facturen in een lijst te openen."),
        ]),
        "settings": ("Bedrijfsgegevens en instellingen", [
            ("p", "Open de instellingen via het tandwielpictogram — het scherm heet <strong>{{settings_title}}</strong>. Het begint met uw voorkeuren: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} of {{settings_theme_dark}}), het standaard "
                  "<strong>{{settings_invoice_template_label}}</strong>, <strong>{{settings_tax_label_label}}</strong> (btw, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> en <strong>{{settings_due_date_default_label}}</strong> (vult de vervaldatum automatisch in, bijv. Net 30). "
                  "Daaronder vindt u <strong>{{settings_security_label}}</strong> (zie <a href=\"#app-lock\">App-vergrendeling</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> en <strong>{{settings_backup_restore_label}}</strong> (zie <a href=\"#backup\">Back-up en herstel</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> onthoudt omschrijvingen en prijzen van regels om ze tijdens het typen voor te stellen; <em>{{common_clear}}</em> vergeet ze, "
                  "zonder uw facturen aan te raken."),
            ("p", "Daaronder staat het profiel van uw bedrijf dat op elke factuur en offerte wordt afgedrukt: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, een korte slogan (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, de <strong>{{settings_date_format_label}}</strong> van datums, adres, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (registratienummer, maatschappelijk kapitaal en dergelijke), "
                  "<strong>{{settings_business_logo_label}}</strong> en <strong>{{settings_payment_details_label}}</strong> (IBAN, PayPal.me-link…). Elk veld "
                  "heeft een voorbeeld en <strong>elk veld dat u leeg laat, verschijnt gewoon niet op uw facturen</strong>. Tik op <strong>{{common_done}}</strong> als u klaar bent; "
                  "als u vertrekt met niet-opgeslagen wijzigingen, vraagt de app eerst om bevestiging."),
            ("p", "Helemaal onderaan: deze <strong>{{settings_user_manual}}</strong> en <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Back-up en herstel", [
            ("p", "Beschikbaar met Invoice Cove Pro. Onder <strong>{{settings_backup_restore_label}}</strong> bewaart <strong>{{settings_create_backup_title}}</strong> "
                  "alles — facturen, offertes, concepten, klanten, agenda, instellingen, logo en pdf's — in één bestand. Kies "
                  "<strong>{{backup_save_button}}</strong> om het op te slaan waar u wilt, of <strong>{{backup_share_button}}</strong> om het naar een veilige plek te sturen."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> zet alles terug — bijvoorbeeld op een nieuwe telefoon. Het werkt alleen op een verse installatie, zolang u nog "
                  "geen gegevens hebt toegevoegd, zodat het nooit kan overschrijven wat u al hebt. Invoice Cove controleert of het bestand intact is en waarschuwt u als het beschadigd is, "
                  "geen Invoice Cove-back-up is of gemaakt is door een nieuwere versie van de app (werk eerst bij)."),
            ("note", "Het back-upbestand is <strong>niet versleuteld</strong>: iedereen die het heeft, kan uw gegevens lezen. Bewaar het op een privéplek. De pincode van de app-vergrendeling wordt er nooit "
                     "in opgenomen."),
        ]),
        "app-lock": ("App-vergrendeling", [
            ("p", "Onder <strong>{{settings_security_label}}</strong> kunt u <strong>{{settings_app_lock_title}}</strong> inschakelen: Invoice Cove vraagt dan om een pincode "
                  "(of vingerafdruk) wanneer de app helemaal opnieuw wordt geopend of nadat de telefoon is herstart — niet bij elke terugkeer naar de app."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: kies een pincode van vier cijfers en bevestig die.",
                "Daarna krijgt u een <strong>herstelcode</strong> van zes cijfers die maar één keer wordt getoond. Schrijf die op en bewaar hem op een veilige plek.",
                "Als uw telefoon dit ondersteunt, ontgrendelt u met uw vingerafdruk (<strong>{{security_use_fingerprint}}</strong>).",
                "Pincode vergeten? Gebruik <strong>{{security_forgot_pin}}</strong> en voer de herstelcode in. Na 5 foute pogingen moet u 30 seconden wachten; "
                "de wachttijd wordt langer bij verdere foute pogingen.",
            ]),
            ("note", "Als u zowel de pincode als de herstelcode kwijtraakt — en geen ontgrendeling met vingerafdruk hebt ingesteld — kunt u niet meer naar binnen. Wij kunnen die niet voor u "
                     "resetten."),
        ]),
        "languages": ("Talen", [
            ("p", "Invoice Cove spreekt 13 talen: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands en Svenska. Tik bovenaan de instellingen op het ronde vlagpictogram en de taal verandert — de app schakelt direct over."),
            ("p", "De tekst in uw pdf's en in de exports naar Excel/CSV volgt de taal waarop de app is ingesteld, en deze handleiding is beschikbaar in dezelfde 13 talen "
                  "(gebruik de taalbalk bovenaan de pagina)."),
        ]),
        "templates": ("Pdf-sjablonen", [
            ("p", "Invoice Cove bevat 18 pdf-ontwerpen: Classic, Client Color (in de kleur van de klant), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves en Spooky Hollow."),
            ("p", "Kies het standaardsjabloon onder Instellingen → <strong>{{settings_invoice_template_label}}</strong>: tik op een ontwerp en daarna op <strong>{{common_done}}</strong>. Dit geldt "
                  "voor alles wat u vanaf dat moment maakt. Voor één factuur of offerte gebruikt u de knop <strong>{{common_template_button}}</strong> "
                  "in het formulier."),
            ("p", "Elk sjabloon drukt dezelfde informatie af — uw bedrijfsgegevens, die van de klant, regels met eenheid en datum, totalen, notities en "
                  "betaalgegevens — maar alleen wat u hebt ingevuld. Lange facturen lopen door op een tweede pagina en het totaal blijft bij de laatste regel staan."),
        ]),
        "free-vs-pro": ("Gratis abonnement en Invoice Cove Pro", [
            ("p", "Invoice Cove is gratis, met een paar redelijke beperkingen:"),
            ("ul", [
                "Maximaal 3 facturen en 3 offertes per kalendermaand",
                "Maximaal 3 klanten tegelijk",
                "Factuur- en offertenummers worden automatisch toegekend en kunnen niet worden aangepast",
                "Export naar Excel, CSV en ZIP is alleen met Pro",
                "Back-up en herstel zijn alleen met Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> is één eenmalige aankoop via Google Play — geen abonnement — die al deze beperkingen voorgoed opheft. "
                  "Concepten, alle sjablonen en talen, de app-vergrendeling en het maken, bekijken en delen van documenten zijn voor iedereen gratis. "
                  "Alle details vindt u in de <a href=\"terms.html\">Gebruiksvoorwaarden</a>."),
        ]),
    },
}
