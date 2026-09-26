T = {
    "title": "Guide d'utilisation",
    "subtitle": "Tout ce que Invoice Cove sait faire, écran par écran.",
    "meta_desc": "Guide d'utilisation complet d'Invoice Cove - Offline Billing.",
    "lang_label": "Langue",
    "brand_alt": "Invoice Cove",
    "toc": "Sommaire",
    "footer_questions": "Des questions ?",
    "lede": (
        "Invoice Cove fonctionne entièrement sur votre appareil : factures, devis, clients et profil de votre entreprise sont stockés localement, "
        "et non sur un serveur d'Invoice Cove. Nous ne collectons, ne voyons et ne recevons aucune donnée sur vos factures ni sur la façon dont "
        "vous utilisez l'application. Pas d'analyse, pas de suivi, rien n'est envoyé en arrière-plan. "
        "Le seul moment où l'application elle-même a besoin d'Internet, c'est pour traiter l'achat unique d'Invoice Cove Pro via Google Play. "
        "Consultez la <a href=\"privacy.html\">Politique de confidentialité</a> pour les détails."
    ),
    "warn": (
        "N'oubliez pas ! Avant de désinstaller l'application ou d'effacer son stockage : ces données ne sont sauvegardées nulle part par nos soins. "
        "Désinstaller Invoice Cove ou effacer son stockage depuis les paramètres d'Android supprime définitivement chaque facture, devis, client "
        "et réglage de cet appareil — il n'existe aucune copie dans le cloud pour restaurer. Pour protéger vos fichiers : créez une sauvegarde "
        "avec Invoice Cove Pro (voir <a href=\"#backup\">Sauvegarde et restauration</a>) ou exportez ce dont vous avez besoin en Excel, CSV ou ZIP "
        "(voir <a href=\"#export\">Exporter les factures</a>)."
    ),
    "sections": {
        "home": ("Écran d'accueil", [
            ("p", "L'écran d'accueil est votre point de départ, avec une tuile pour chaque action principale : {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} et "
                  "{{common_reports_title}}. Touchez une tuile pour y accéder directement."),
            ("p", "La barre du bas vous donne un accès rapide à {{nav_home}}, {{nav_new}} (nouvelle facture), "
                  "{{nav_invoices}}, {{nav_customers}} et {{nav_reports}}."),
            ("p", "L'icône d'engrenage (⚙️) en haut à droite de la plupart des écrans ouvre les <a href=\"#settings\">Informations de l'entreprise et réglages</a>."),
        ]),
        "customers": ("Clients", [
            ("p", "Pour ajouter un client, allez dans l'onglet {{nav_customers}} et touchez l'icône +, ou utilisez la tuile {{home_new_customer_title}}. "
                  "Vous pouvez aussi en ajouter un en créant une facture ou un devis. Seul le nom est nécessaire pour créer une fiche client. "
                  "Les champs facultatifs comprennent : {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, l'adresse, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} et une teinte de couleur pour ses documents. Chaque champ affiche un exemple pour vous indiquer ce qu'il faut y saisir."),
            ("p", "Touchez un client pour le {{common_edit}}, ouvrir son {{customers_view_history}} (factures, devis et brouillons) "
                  "ou le {{common_delete}}."),
            ("p", "Sur vos factures et devis, les informations du client sont imprimées sous son nom dans un ordre fixe : numéro client, numéro fiscal, numéro de TVA, "
                  "numéro du registre du commerce, puis adresse, e-mail et téléphone. Tout ce que vous laissez vide n'est pas imprimé."),
            ("note", "L'enregistrement fonctionne ici différemment des factures. Un client a son propre bouton {{customers_form_save_customer}} "
                     "(ou {{customers_form_save_changes}} en modification) et il est enregistré dès que vous le touchez. Si vous essayez de fermer le formulaire "
                     "avec des modifications non enregistrées, Invoice Cove vous demande d'abord de confirmer."),
            ("note", "Supprimer un client ne supprime pas les factures et devis que vous lui avez déjà émis. En revanche, ses <a href=\"#drafts\">brouillons</a> inachevés "
                     "sont supprimés avec lui ; Invoice Cove vous demande d'abord de confirmer."),
        ]),
        "new-invoice": ("Créer une facture", [
            ("p", "Depuis {{nav_new}} (ou la tuile {{home_new_invoice_title}}) : choisissez un client (ou créez-en un sur place) "
                  "et définissez la date de la facture et l'échéance, puis ajoutez vos articles."),
            ("p", "Touchez {{newinvoice_add_item_details_button}} et renseignez la description, la quantité, le prix unitaire et, facultativement, une unité "
                  "(par exemple h, pièce ou kg) ainsi qu'une date et une heure. L'unité est imprimée à côté de la quantité dans le PDF. Touchez le crayon (✏️) d'un article pour le corriger "
                  "ou la corbeille (🗑️) pour le supprimer. Les descriptions et prix déjà utilisés vous sont suggérés pendant la saisie."),
            ("p", "Ajoutez ensuite, si besoin, un taux de taxe, une {{newinvoice_discount_label}} (pourcentage ou montant fixe) et "
                  "des {{common_notes_label}}. Le numéro de facture est attribué pour vous (avec Invoice Cove Pro, il peut être modifié), et la devise se choisit à côté."),
            ("p", "{{common_preview_button}} génère un PDF temporaire pour vérifier le rendu — rien n'est encore enregistré. "
                  "Le bouton {{common_template_button}} indique le modèle utilisé ; touchez-le pour en choisir un autre pour ce document seulement."),
            ("note", "{{newinvoice_generate_button}} fait trois choses à la fois : il enregistre la facture, crée le PDF et ouvre le menu de partage "
                     "de votre appareil pour l'envoyer. Pas encore prêt ? Utilisez {{newinvoice_save_draft_button}} — voir <a href=\"#drafts\">Brouillons</a>."),
        ]),
        "drafts": ("Brouillons", [
            ("p", "Vous ne perdez pas une facture sur laquelle vous travaillez encore. Dès que vous avez choisi un client et ajouté au moins un article ou une note, Invoice Cove "
                  "conserve un brouillon et le met à jour peu après que vous avez arrêté de saisir, et une dernière fois quand vous quittez l'application. "
                  "Il n'y a pas de question « abandonner les modifications ? » quand vous quittez l'écran ; un court message vous indique que le brouillon a été enregistré."),
            ("p", "Touchez {{newinvoice_save_draft_button}} (sous {{newinvoice_generate_button}}) pour mettre la facture de côté volontairement : elle est enregistrée et "
                  "le formulaire est vidé, prêt pour la facture suivante. Cela fonctionne dès qu'un client est choisi, même avant d'ajouter des articles."),
            ("p", "Retrouvez vos brouillons dans {{nav_customers}} → le client → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Chaque brouillon indique sa dernière modification, son nombre d'articles et son total. Touchez-le pour continuer "
                  "à le modifier ou pour générer la facture ; touchez la corbeille pour le supprimer."),
            ("ul", [
                "Un brouillon n'utilise jamais de numéro de facture et ne compte pas dans la limite mensuelle gratuite. Le numéro n'est attribué que lorsque vous générez la facture "
                "définitive — le brouillon est alors remplacé par elle.",
                "Un brouillon ne conserve la date de facture et l'échéance que si vous les avez choisies vous-même ; sinon, il utilise la date du jour à sa réouverture.",
                "Supprimer un client supprime aussi ses brouillons (Invoice Cove vous le demande d'abord). Les brouillons sont inclus dans une sauvegarde.",
                "Les brouillons existent pour les factures ; les devis n'en ont pas.",
            ]),
        ]),
        "invoices": ("Gérer les factures", [
            ("p", "L'onglet {{nav_invoices}} regroupe vos factures dans un dossier par client, que vous pouvez trier par "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> ou <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Ouvrez un dossier pour voir ses factures, triées par date, valeur, numéro ou statut."),
            ("p", "Chaque facture a un statut : {{invoices_status_unpaid}}, {{invoices_status_overdue}} (échéance dépassée), "
                  "{{invoices_status_partially_paid}} (un acompte a été enregistré), {{invoices_status_paid}} ou "
                  "{{invoices_status_void}}. Touchez une facture pour la consulter ({{common_view}}), la renvoyer ({{common_share}}), la marquer payée ou annulée, ou la supprimer."),
            ("ul", [
                "{{invoices_action_mark_paid}} demande la date du paiement et le moyen utilisé (virement, espèces, carte, PayPal ou autre). "
                "Une fois payée, une facture ne peut plus être remise en impayée.",
                "{{deposit_record_title}} note un paiement anticipé. La facture apparaît alors comme {{invoices_status_partially_paid}}, et l'acompte ne peut pas dépasser le total.",
                "{{invoices_action_mark_void}} conserve la facture dans vos dossiers mais la marque comme annulée. C'est préférable à la suppression, car une facture supprimée "
                "ne peut pas être récupérée.",
            ]),
            ("p", "Avec Pro, le dossier d'un client peut aussi être enregistré ou partagé en ZIP de PDF, et toute la liste peut être exportée pour votre comptable — voir "
                  "<a href=\"#export\">Exporter les factures</a>."),
        ]),
        "export": ("Exporter les factures (Excel, CSV, ZIP)", [
            ("p", "Disponible avec Invoice Cove Pro. Touchez l'icône d'export (📄) en haut de l'onglet {{nav_invoices}}. Choisissez les factures à inclure "
                  "avec les sélecteurs d'année et de mois ({{invoices_export_all}}, une année, ou un mois d'une année ; seuls les années et mois qui "
                  "contiennent des factures sont proposés), puis choisissez l'action :"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — un tableur Excel (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — le même tableau en fichier CSV.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — les PDF des factures dans un ZIP, un dossier par client.",
                "{{invoices_export_delete}} — supprime définitivement les factures sélectionnées après deux confirmations.",
            ]),
            ("p", "<em>Enregistrer</em> vous laisse choisir où le fichier est placé sur votre appareil ; <em>Partager</em> ouvre le menu de partage d'Android pour l'envoyer "
                  "par e-mail ou dans un message."),
            ("p", "Excel et CSV sont conçus pour votre comptable : par défaut, une ligne par facture, avec numéro et dates, nom, numéro, numéro "
                  "fiscal, numéro de TVA, numéro du registre du commerce et adresse du client, sous-total, remise, taux de TVA, montant de TVA et total de la "
                  "facture, devise, ainsi que statut, date et moyen de paiement. Les en-têtes de colonnes et les mots fixes (facture, payé, impayé, moyens de "
                  "paiement) sont écrits dans la langue de l'application."),
            ("p", "Pour obtenir une ligne par article de facture, avec les informations de la facture répétées sur chaque ligne et la description, "
                  "la quantité, l'unité, le prix et le montant net de chaque article ajoutés, activez {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Créer un devis", [
            ("p", "La tuile {{home_new_quote_title}} fonctionne comme la tuile Nouvelle facture : mêmes champs, mêmes boutons {{common_preview_button}} et {{common_template_button}}, même "
                  "{{newquote_generate_button}} qui enregistre, crée le PDF et ouvre le menu de partage d'une seule touche, mais avec une "
                  "{{newquote_date_label}} et une date {{newquote_valid_until_label}} à la place de la date de facture et de l'échéance."),
            ("p", "Les devis n'ont pas de brouillons."),
        ]),
        "quotes": ("Gérer les devis et les convertir en facture", [
            ("p", "L'écran {{common_quotes_title}} (depuis la tuile de l'accueil) liste vos devis par client, comme pour les factures. Ouvrez un devis pour le "
                  "consulter ou le partager, utilisez {{quotes_action_accept}} ou {{quotes_action_decline}} quand le client répond, "
                  "enregistrez un acompte ou supprimez-le. L'acompte ne peut pas dépasser le total du devis."),
            ("p", "Quand un client accepte un devis, utilisez {{quotes_action_convert_to_invoice}} pour transformer les lignes cochées en une vraie facture, "
                  "modifiable indépendamment. L'échéance et la remise restent ajustables, et le devis d'origine est marqué "
                  "{{quotes_status_converted}} et conservé dans vos dossiers."),
        ]),
        "calendar": ("Calendrier et rappels", [
            ("p", "L'écran {{calendar_title}} est une vue mensuelle pour vos propres notes. Touchez un jour pour voir ou ajouter des notes ; une note a un titre et un texte et, "
                  "avec {{calendar_remind_me}} et une heure, vous envoie une notification à la date et à l'heure choisies. Le premier jour de la semaine suit vos réglages."),
            ("p", "Par ailleurs, Invoice Cove envoie des rappels de paiement — des notifications locales pour les factures bientôt échues ou en retard. Rien n'est envoyé vers un serveur ni reçu d'un serveur."),
        ]),
        "reports": ("Rapports", [
            ("p", "{{common_reports_title}} vous donne un aperçu rapide : les montants {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} et {{reports_stat_overdue}}, le nombre de factures, "
                  "<em>{{reports_revenue_by_month}}</em> et vos <em>{{reports_top_customers}}</em> selon le total facturé."),
            ("p", "Touchez la carte {{reports_stat_outstanding}} ou {{reports_stat_overdue}} pour ouvrir la liste de ces factures précisément."),
        ]),
        "settings": ("Informations de l'entreprise et réglages", [
            ("p", "Ouvrez les réglages avec l'icône d'engrenage ; cet écran s'appelle {{settings_title}}. Il commence par vos préférences facultatives : "
                  "{{settings_appearance_label}} ({{settings_theme_light}} ou {{settings_theme_dark}}), "
                  "{{settings_invoice_template_label}} par défaut, {{settings_tax_label_label}} (TVA, GST…), "
                  "{{settings_first_day_of_week_label}} et {{settings_due_date_default_label}}, qui remplit l'échéance automatiquement (par exemple Net 30). "
                  "Viennent ensuite {{settings_security_label}} (voir <a href=\"#app-lock\">Verrouillage de l'application</a>), "
                  "{{settings_item_suggestions_label}} et {{settings_backup_restore_label}} (voir <a href=\"#backup\">Sauvegarde et restauration</a>)."),
            ("p", "{{settings_item_memory_title}} retient les descriptions et prix des articles pour vous les suggérer à la saisie ; <em>{{common_clear}}</em> les oublie "
                  "sans toucher à vos factures."),
            ("p", "Plus bas se trouve le profil de votre entreprise, imprimé sur chaque facture et devis : {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, un court slogan ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, le {{settings_date_format_label}} des dates, l'adresse, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (numéro d'immatriculation, capital social, etc.), votre "
                  "{{settings_business_logo_label}} et vos {{settings_payment_details_label}} (IBAN, lien PayPal.me). Chaque champ "
                  "a un exemple, et tout champ laissé vide n'apparaît pas sur vos factures. Touchez {{common_done}} quand vous "
                  "avez terminé ; si vous partez avec des modifications non enregistrées, on vous demande de confirmer."),
            ("p", "Tout en bas s'affichent ce {{settings_user_manual}} et {{settings_share_this_app}}."),
        ]),
        "backup": ("Sauvegarde et restauration", [
            ("p", "Disponible avec Invoice Cove Pro, sous {{settings_backup_restore_label}}. {{settings_create_backup_title}} enregistre "
                  "tout : factures, devis, brouillons, clients, calendrier, réglages, votre logo et les PDF, le tout dans un seul fichier. Choisissez "
                  "{{backup_save_button}} pour le ranger où vous voulez, ou {{backup_share_button}} pour l'envoyer en lieu sûr."),
            ("p", "{{settings_restore_backup_title}} ramène tout, au cas où vous devriez passer à un nouveau téléphone. Cela ne fonctionne que sur une installation neuve, avant que vous "
                  "n'ayez ajouté des données, si bien que rien de ce que vous avez déjà ne peut être écrasé. Invoice Cove vérifie que le fichier est intact et vous prévient s'il est abîmé, "
                  "s'il n'est pas une sauvegarde d'Invoice Cove ou s'il vient d'une version plus récente de l'application (mettez-la d'abord à jour)."),
            ("note", "Un fichier de sauvegarde n'est pas chiffré : quiconque le possède peut lire vos données. Conservez-le dans un endroit privé. Le code PIN de verrouillage n'y est "
                     "jamais inclus."),
        ]),
        "app-lock": ("Verrouillage de l'application", [
            ("p", "Sous {{settings_security_label}}, vous pouvez activer {{settings_app_lock_title}} : Invoice Cove demande alors votre code PIN "
                  "(ou votre empreinte) quand l'application est ouverte à neuf ou après un redémarrage du téléphone — pas à chaque retour dans l'application."),
            ("ul", [
                "{{settings_set_pin}} : choisissez un code PIN à 4 chiffres et confirmez-le.",
                "Vous recevez ensuite un code de récupération à 6 chiffres, affiché une seule fois. Notez-le et gardez-le en lieu sûr.",
                "Si votre téléphone le permet, déverrouillez avec votre empreinte ({{security_use_fingerprint}}).",
                "PIN oublié ? Utilisez {{security_forgot_pin}} et saisissez le code de récupération. Après 5 essais erronés, vous devez attendre 30 secondes – "
                "l'attente s'allonge avec les essais erronés suivants.",
            ]),
            ("note", "Si vous perdez à la fois votre code PIN et le code de récupération et que vous n'avez pas configuré le déverrouillage par empreinte, il n'y a aucun moyen de revenir. Nous ne pouvons pas le "
                     "réinitialiser pour vous."),
        ]),
        "languages": ("Langues", [
            ("p", "Invoice Cove parle 13 langues : English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands et Svenska. Touchez l'icône ronde au drapeau en haut des réglages pour changer — l'application change immédiatement."),
            ("p", "Le texte de vos PDF et des exports Excel/CSV suit la langue de l'application, et ce guide est disponible dans les mêmes 13 langues "
                  "(utilisez la barre de langues en haut de la page)."),
        ]),
        "templates": ("Modèles PDF", [
            ("p", "Invoice Cove propose pour l'instant 18 modèles PDF : Classic, Client Color (teinté à la couleur du client), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves et Spooky Hollow."),
            ("p", "Choisissez votre modèle par défaut dans Réglages → {{settings_invoice_template_label}} : touchez un modèle, puis {{common_done}}. Il "
                  "s'applique à tout ce que vous générez ensuite. Pour une seule facture ou un seul devis, utilisez le bouton {{common_template_button}} "
                  "du formulaire."),
            ("p", "Chaque modèle imprime les mêmes informations : les données de votre entreprise, celles du client, les articles avec leur unité et leur date, les totaux, les notes et "
                  "les détails de paiement — mais seulement ce que vous avez renseigné. Les longues factures se poursuivent sur une deuxième page, avec le total conservé avec le dernier article."),
        ]),
        "free-vs-pro": ("Offre gratuite ou Invoice Cove Pro", [
            ("p", "Invoice Cove est gratuit, avec quelques limites raisonnables :"),
            ("ul", [
                "Jusqu'à 3 factures générées par mois calendaire",
                "Jusqu'à 3 devis générés par mois calendaire",
                "Jusqu'à 3 clients à la fois",
                "Les numéros de facture et de devis sont attribués automatiquement et ne sont pas modifiables",
                "L'export Excel, CSV et ZIP est réservé à Pro",
                "La sauvegarde et la restauration sont réservées à Pro",
            ]),
            ("p", "Invoice Cove Pro est un achat unique via Google Play (pas un abonnement) qui supprime définitivement toutes ces limites. "
                  "Les brouillons, tous les modèles et toutes les langues, le verrouillage de l'application, ainsi que la création, l'aperçu et le partage de documents sont gratuits pour tous. "
                  "Consultez les <a href=\"terms.html\">Conditions d'utilisation</a> pour tous les détails."),
        ]),
    },
}
