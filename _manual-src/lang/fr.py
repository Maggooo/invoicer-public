T = {
    "title": "Guide d'utilisation",
    "subtitle": "Tout ce que Invoice Cove sait faire, écran par écran.",
    "meta_desc": "Guide d'utilisation complet d'Invoice Cove - Offline Billing.",
    "lang_label": "Langue",
    "brand_alt": "Invoice Cove",
    "toc": "Sommaire",
    "footer_questions": "Des questions ?",
    "lede": (
        "Invoice Cove fonctionne entièrement sur votre appareil — factures, devis, clients et profil de votre entreprise sont stockés localement, "
        "et non sur un serveur d'Invoice Cove. <strong>Nous ne collectons, ne voyons et ne recevons aucune donnée sur vos factures ni sur la façon dont "
        "vous utilisez l'application</strong> — pas d'analyse, pas de suivi, rien n'est envoyé en arrière-plan. "
        "Le seul moment où l'application elle-même a besoin d'Internet, c'est pour traiter l'achat unique d'Invoice Cove Pro via Google Play. "
        "Consultez la <a href=\"privacy.html\">Politique de confidentialité</a> pour les détails."
    ),
    "warn": (
        "<strong>Avant de désinstaller l'application ou d'effacer son stockage :</strong> ces données ne sont sauvegardées nulle part par nos soins. "
        "Désinstaller Invoice Cove ou effacer son stockage depuis les paramètres d'Android supprime définitivement chaque facture, devis, client "
        "et réglage de cet appareil — il n'existe aucune copie dans le cloud pour restaurer. Protégez-vous : créez une sauvegarde "
        "avec Invoice Cove Pro (voir <a href=\"#backup\">Sauvegarde et restauration</a>) ou exportez ce dont vous avez besoin en Excel, CSV ou ZIP "
        "(voir <a href=\"#export\">Exporter les factures</a>)."
    ),
    "sections": {
        "home": ("Écran d'accueil", [
            ("p", "L'écran d'accueil est votre point de départ, avec une tuile pour chaque action principale : <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> et "
                  "<strong>{{common_reports_title}}</strong>. Touchez une tuile pour y accéder directement."),
            ("p", "La barre du bas vous donne toujours un accès rapide à <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (une nouvelle facture), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> et <strong>{{nav_reports}}</strong>."),
            ("p", "L'icône d'engrenage (⚙️) en haut à droite de la plupart des écrans ouvre les <a href=\"#settings\">Informations de l'entreprise et réglages</a>."),
        ]),
        "customers": ("Clients", [
            ("p", "Ajoutez un client depuis l'onglet <strong>{{nav_customers}}</strong> (touchez l'icône +), avec la tuile <strong>{{home_new_customer_title}}</strong> "
                  "ou directement en créant une facture ou un devis. Seul le nom est obligatoire. Champs facultatifs : <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, l'adresse, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} et une couleur qui teinte ses documents. Chaque champ affiche un exemple pour vous indiquer ce qu'il faut y saisir."),
            ("p", "Touchez un client pour le <strong>{{common_edit}}</strong>, ouvrir son <strong>{{customers_view_history}}</strong> (factures, devis et brouillons) "
                  "ou le <strong>{{common_delete}}</strong>."),
            ("p", "Sur vos factures et devis, les informations du client sont imprimées sous son nom dans un ordre fixe : numéro client, numéro fiscal, numéro de TVA, "
                  "numéro du registre du commerce, puis adresse, e-mail et téléphone. Tout ce que vous laissez vide n'est tout simplement pas imprimé."),
            ("note", "<strong>L'enregistrement fonctionne ici différemment des factures.</strong> Un client a son propre bouton <strong>{{customers_form_save_customer}}</strong> "
                     "(ou <strong>{{customers_form_save_changes}}</strong> en modification) — il est enregistré dès que vous le touchez. Si vous essayez de fermer le formulaire "
                     "avec des modifications non enregistrées, Invoice Cove vous demande d'abord de confirmer."),
            ("note", "Supprimer un client ne supprime pas les factures et devis que vous lui avez déjà émis. Ses <a href=\"#drafts\">brouillons</a> inachevés "
                     "sont supprimés avec lui — on vous le demande d'abord."),
        ]),
        "new-invoice": ("Créer une facture", [
            ("p", "Depuis <strong>{{nav_new}}</strong> (ou la tuile <strong>{{home_new_invoice_title}}</strong>) : choisissez un client — ou créez-en un sur place — "
                  "définissez la date de la facture et l'échéance, puis ajoutez vos articles."),
            ("p", "Touchez <strong>{{newinvoice_add_item_details_button}}</strong> et renseignez la description, la quantité, le prix unitaire et, facultativement, une unité "
                  "(par exemple h, pièce ou kg) ainsi qu'une date et une heure. L'unité est imprimée à côté de la quantité dans le PDF. Touchez le crayon (✏️) d'un article pour le corriger "
                  "ou la corbeille (🗑️) pour le supprimer. Les descriptions et prix déjà utilisés vous sont suggérés pendant la saisie."),
            ("p", "Ajoutez ensuite, si besoin, un taux de taxe, une <strong>{{newinvoice_discount_label}}</strong> (pourcentage ou montant fixe) et "
                  "des <strong>{{common_notes_label}}</strong>. Le numéro de facture est attribué pour vous (avec Pro, vous pouvez le modifier) ; la devise se choisit à côté."),
            ("p", "<strong>{{common_preview_button}}</strong> génère un PDF temporaire pour vérifier le rendu — rien n'est encore enregistré. "
                  "Le bouton <strong>{{common_template_button}}</strong> indique le modèle utilisé ; touchez-le pour en choisir un autre pour ce document seulement."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> fait trois choses à la fois : il enregistre la facture, crée le PDF et ouvre le menu de partage "
                     "de votre appareil pour l'envoyer. Pas encore prêt ? Utilisez <strong>{{newinvoice_save_draft_button}}</strong> — voir <a href=\"#drafts\">Brouillons</a>."),
        ]),
        "drafts": ("Brouillons", [
            ("p", "Vous ne perdez pas une facture sur laquelle vous travaillez encore. Dès que vous avez choisi un client et ajouté au moins un article ou une note, Invoice Cove "
                  "conserve un <strong>brouillon</strong> et le met à jour peu après que vous avez arrêté de saisir — et une dernière fois quand vous quittez l'application. "
                  "Il n'y a pas de question « abandonner les modifications ? » quand vous quittez l'écran ; un court message vous indique que le brouillon a été enregistré."),
            ("p", "Touchez <strong>{{newinvoice_save_draft_button}}</strong> (sous {{newinvoice_generate_button}}) pour mettre la facture de côté volontairement : elle est enregistrée et "
                  "le formulaire est vidé, prêt pour la facture suivante. Cela fonctionne dès qu'un client est choisi, même avant d'ajouter des articles."),
            ("p", "Retrouvez vos brouillons dans <strong>{{nav_customers}}</strong> → le client → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Chaque brouillon indique sa dernière modification, son nombre d'articles et son total. Touchez-le pour continuer "
                  "à le modifier ou pour générer la facture ; touchez la corbeille pour le supprimer."),
            ("ul", [
                "Un brouillon n'utilise jamais de numéro de facture et ne compte pas dans la limite mensuelle gratuite. Le numéro n'est attribué que lorsque vous générez la facture "
                "définitive — le brouillon est alors remplacé par elle.",
                "Un brouillon ne conserve la date de facture et l'échéance que si vous les avez choisies vous-même ; sinon, il utilise la date du jour à sa réouverture.",
                "Supprimer un client supprime aussi ses brouillons (on vous le demande d'abord). Les brouillons sont inclus dans une sauvegarde.",
                "Les brouillons existent pour les factures ; les devis n'en ont pas.",
            ]),
        ]),
        "invoices": ("Gérer les factures", [
            ("p", "L'onglet <strong>{{nav_invoices}}</strong> regroupe vos factures dans un dossier par client, que vous pouvez trier par "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> ou <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Ouvrez un dossier pour voir ses factures, triées par date, valeur, numéro ou statut."),
            ("p", "Chaque facture a un statut : <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (échéance dépassée), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (un acompte a été enregistré), <strong>{{invoices_status_paid}}</strong> ou "
                  "<strong>{{invoices_status_void}}</strong>. Touchez une facture pour la consulter ({{common_view}}), la renvoyer ({{common_share}}), la marquer payée ou annulée, ou la supprimer."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> demande la date du paiement et le moyen utilisé (virement, espèces, carte, PayPal ou autre). "
                "Une fois payée, une facture ne peut plus être remise en impayée.",
                "<strong>{{deposit_record_title}}</strong> note un paiement anticipé. La facture apparaît alors comme <strong>{{invoices_status_partially_paid}}</strong>, et l'acompte ne peut pas dépasser le total.",
                "<strong>{{invoices_action_mark_void}}</strong> conserve la facture dans vos dossiers mais la marque comme annulée. Préférez-le à la suppression — une facture supprimée "
                "ne peut pas être récupérée.",
            ]),
            ("p", "Avec Pro, le dossier d'un client peut aussi être enregistré ou partagé en ZIP de PDF, et toute la liste peut être exportée pour votre comptable — voir "
                  "<a href=\"#export\">Exporter les factures</a>."),
        ]),
        "export": ("Exporter les factures (Excel, CSV, ZIP)", [
            ("p", "Disponible avec Invoice Cove Pro. Touchez l'icône d'export (📄) en haut de l'onglet <strong>{{nav_invoices}}</strong>. Choisissez les factures à inclure "
                  "avec les sélecteurs d'année et de mois (<strong>{{invoices_export_all}}</strong>, une année, ou un mois d'une année — seuls les années et mois qui "
                  "contiennent des factures sont proposés), puis choisissez l'action :"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — un tableur Excel (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — le même tableau en fichier CSV.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — les PDF des factures dans un ZIP, un dossier par client.",
                "<strong>{{invoices_export_delete}}</strong> — supprime définitivement les factures sélectionnées, après deux confirmations.",
            ]),
            ("p", "<em>Enregistrer</em> vous laisse choisir où le fichier est placé sur votre appareil ; <em>Partager</em> ouvre le menu de partage d'Android pour l'envoyer "
                  "par e-mail ou dans une discussion."),
            ("p", "Excel et CSV sont conçus pour votre comptable : par défaut, <strong>une ligne par facture</strong> — numéro et dates, nom, numéro, numéro "
                  "fiscal, numéro de TVA, numéro du registre du commerce et adresse du client, sous-total, remise, taux de TVA, montant de TVA et total de la "
                  "facture, devise, ainsi que statut, date et moyen de paiement. Les en-têtes de colonnes et les mots fixes (facture, payé, impayé, moyens de "
                  "paiement) sont écrits dans la langue de l'application."),
            ("p", "Activez <strong>{{invoices_export_detailed_toggle}}</strong> dans le même panneau pour obtenir à la place une ligne par article de facture, "
                  "avec les informations de la facture répétées sur chaque ligne et la description, la quantité, l'unité, le prix et le montant net de chaque "
                  "article ajoutés."),
        ]),
        "new-quote": ("Créer un devis", [
            ("p", "<strong>{{home_new_quote_title}}</strong> fonctionne comme New Invoice — mêmes champs, mêmes boutons <strong>{{common_preview_button}}</strong> et <strong>{{common_template_button}}</strong>, et le même "
                  "<strong>{{newquote_generate_button}}</strong> qui enregistre, crée le PDF et ouvre le menu de partage d'une seule touche — avec une "
                  "<strong>{{newquote_date_label}}</strong> et une date <strong>{{newquote_valid_until_label}}</strong> à la place de la date de facture et de l'échéance. "
                  "Les devis n'ont pas de brouillons."),
        ]),
        "quotes": ("Gérer les devis et les convertir en facture", [
            ("p", "L'écran <strong>{{common_quotes_title}}</strong> (depuis la tuile de l'accueil) liste vos devis par client, comme pour les factures. Ouvrez un devis pour le "
                  "consulter ou le partager, utilisez <strong>{{quotes_action_accept}}</strong> ou <strong>{{quotes_action_decline}}</strong> quand le client répond, "
                  "enregistrez un acompte ou supprimez-le. L'acompte ne peut pas dépasser le total du devis."),
            ("p", "Quand un client accepte un devis, utilisez <strong>{{quotes_action_convert_to_invoice}}</strong> pour transformer les lignes cochées en une vraie facture, "
                  "modifiable indépendamment — l'échéance et la remise restent ajustables, et le devis d'origine est marqué "
                  "<strong>{{quotes_status_converted}}</strong> et conservé dans vos dossiers."),
        ]),
        "calendar": ("Calendrier et rappels", [
            ("p", "L'écran <strong>{{calendar_title}}</strong> est une vue mensuelle pour vos propres notes. Touchez un jour pour voir ou ajouter des notes ; une note a un titre et un texte et, "
                  "avec <strong>{{calendar_remind_me}}</strong> et une heure, vous envoie une notification à ce moment-là. Le premier jour de la semaine suit votre réglage."),
            ("p", "Par ailleurs, Invoice Cove envoie des rappels de paiement — des notifications locales pour les factures bientôt échues ou en retard. Rien n'est envoyé vers un serveur ni reçu d'un serveur."),
        ]),
        "reports": ("Rapports", [
            ("p", "<strong>{{common_reports_title}}</strong> vous donne un aperçu rapide : les montants <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> et <strong>{{reports_stat_overdue}}</strong>, le nombre de factures, "
                  "<em>{{reports_revenue_by_month}}</em> et vos <em>{{reports_top_customers}}</em> selon le total facturé."),
            ("p", "Touchez la carte <strong>{{reports_stat_outstanding}}</strong> ou <strong>{{reports_stat_overdue}}</strong> pour ouvrir la liste de ces factures précisément."),
        ]),
        "settings": ("Informations de l'entreprise et réglages", [
            ("p", "Ouvrez les réglages avec l'icône d'engrenage — l'écran s'appelle <strong>{{settings_title}}</strong>. Il commence par vos préférences : "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} ou {{settings_theme_dark}}), "
                  "<strong>{{settings_invoice_template_label}}</strong> par défaut, <strong>{{settings_tax_label_label}}</strong> (TVA, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> et <strong>{{settings_due_date_default_label}}</strong> (remplit l'échéance automatiquement, par exemple Net 30). "
                  "Viennent ensuite <strong>{{settings_security_label}}</strong> (voir <a href=\"#app-lock\">Verrouillage de l'application</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> et <strong>{{settings_backup_restore_label}}</strong> (voir <a href=\"#backup\">Sauvegarde et restauration</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> retient les descriptions et prix des articles pour vous les suggérer à la saisie ; <em>{{common_clear}}</em> les oublie "
                  "sans toucher à vos factures."),
            ("p", "Plus bas se trouve le profil de votre entreprise, imprimé sur chaque facture et devis : <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, un court slogan (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, le <strong>{{settings_date_format_label}}</strong> des dates, l'adresse, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (numéro d'immatriculation, capital social, etc.), votre "
                  "<strong>{{settings_business_logo_label}}</strong> et vos <strong>{{settings_payment_details_label}}</strong> (IBAN, lien PayPal.me…). Chaque champ "
                  "a un exemple, et <strong>tout champ laissé vide n'apparaît simplement pas sur vos factures</strong>. Touchez <strong>{{common_done}}</strong> quand vous "
                  "avez terminé ; si vous partez avec des modifications non enregistrées, on vous le demande d'abord."),
            ("p", "Tout en bas : ce <strong>{{settings_user_manual}}</strong> et <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Sauvegarde et restauration", [
            ("p", "Disponible avec Invoice Cove Pro. Sous <strong>{{settings_backup_restore_label}}</strong>, <strong>{{settings_create_backup_title}}</strong> enregistre "
                  "tout — factures, devis, brouillons, clients, calendrier, réglages, votre logo et les PDF — dans un seul fichier. Choisissez "
                  "<strong>{{backup_save_button}}</strong> pour le ranger où vous voulez, ou <strong>{{backup_share_button}}</strong> pour l'envoyer en lieu sûr."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> ramène tout — par exemple sur un nouveau téléphone. Cela ne fonctionne que sur une installation neuve, avant que vous "
                  "n'ayez ajouté des données, si bien que rien de ce que vous avez déjà ne peut être écrasé. Invoice Cove vérifie que le fichier est intact et vous prévient s'il est abîmé, "
                  "s'il n'est pas une sauvegarde d'Invoice Cove ou s'il vient d'une version plus récente de l'application (mettez-la d'abord à jour)."),
            ("note", "Un fichier de sauvegarde n'est <strong>pas chiffré</strong> : quiconque le possède peut lire vos données. Conservez-le dans un endroit privé. Le code PIN de verrouillage n'y est "
                     "jamais inclus."),
        ]),
        "app-lock": ("Verrouillage de l'application", [
            ("p", "Sous <strong>{{settings_security_label}}</strong>, vous pouvez activer <strong>{{settings_app_lock_title}}</strong> : Invoice Cove demande alors votre code PIN "
                  "(ou votre empreinte) quand l'application est ouverte à neuf ou après un redémarrage du téléphone — pas à chaque retour dans l'application."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong> : choisissez un code PIN à 4 chiffres et confirmez-le.",
                "Vous recevez ensuite un <strong>code de récupération</strong> à 6 chiffres, affiché une seule fois. Notez-le et gardez-le en lieu sûr.",
                "Si votre téléphone le permet, déverrouillez avec votre empreinte (<strong>{{security_use_fingerprint}}</strong>).",
                "PIN oublié ? Utilisez <strong>{{security_forgot_pin}}</strong> et saisissez le code de récupération. Après 5 essais erronés, vous devez attendre 30 secondes ; "
                "l'attente s'allonge avec les essais erronés suivants.",
            ]),
            ("note", "Si vous perdez à la fois votre code PIN et le code de récupération — et que vous n'avez pas configuré le déverrouillage par empreinte —, il n'y a aucun moyen de revenir. Nous ne pouvons pas le "
                     "réinitialiser pour vous."),
        ]),
        "languages": ("Langues", [
            ("p", "Invoice Cove parle 13 langues : English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands et Svenska. Touchez l'icône ronde au drapeau en haut des réglages pour changer — l'application change immédiatement."),
            ("p", "Le texte de vos PDF et des exports Excel/CSV suit la langue de l'application, et ce guide est disponible dans les mêmes 13 langues "
                  "(utilisez la barre de langues en haut de la page)."),
        ]),
        "templates": ("Modèles PDF", [
            ("p", "Invoice Cove propose 18 modèles PDF : Classic, Client Color (teinté à la couleur du client), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves et Spooky Hollow."),
            ("p", "Choisissez votre modèle par défaut dans Réglages → <strong>{{settings_invoice_template_label}}</strong> : touchez un modèle, puis <strong>{{common_done}}</strong>. Il "
                  "s'applique à tout ce que vous générez ensuite. Pour une seule facture ou un seul devis, utilisez le bouton <strong>{{common_template_button}}</strong> "
                  "du formulaire."),
            ("p", "Chaque modèle imprime les mêmes informations — les données de votre entreprise, celles du client, les articles avec leur unité et leur date, les totaux, les notes et "
                  "les détails de paiement — mais seulement ce que vous avez renseigné. Les longues factures se poursuivent sur une deuxième page, avec le total conservé avec le dernier article."),
        ]),
        "free-vs-pro": ("Offre gratuite ou Invoice Cove Pro", [
            ("p", "Invoice Cove est gratuit, avec quelques limites raisonnables :"),
            ("ul", [
                "Jusqu'à 3 factures et 3 devis générés par mois calendaire",
                "Jusqu'à 3 clients à la fois",
                "Les numéros de facture et de devis sont attribués automatiquement et ne sont pas modifiables",
                "L'export Excel, CSV et ZIP est réservé à Pro",
                "La sauvegarde et la restauration sont réservées à Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> est un achat unique via Google Play — pas un abonnement — qui supprime définitivement toutes ces limites. "
                  "Les brouillons, tous les modèles et toutes les langues, le verrouillage de l'application, ainsi que la création, l'aperçu et le partage de documents sont gratuits pour tous. "
                  "Consultez les <a href=\"terms.html\">Conditions d'utilisation</a> pour tous les détails."),
        ]),
    },
}
