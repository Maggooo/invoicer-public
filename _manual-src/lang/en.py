# English master text. Other languages follow the same sections and blocks.
# {{key}} = the app's own label for that button/screen (see ui/en.json).
T = {
    "title": "User Guide",
    "subtitle": "Everything Invoice Cove can do, screen by screen.",
    "meta_desc": "Complete user guide for Invoice Cove - Offline Billing.",
    "lang_label": "Language",
    "brand_alt": "Invoice Cove",
    "toc": "Contents",
    "footer_questions": "Questions?",
    "lede": (
        "Invoice Cove runs entirely on your device, invoices, quotes, customers and your business profile are stored "
        "locally, not on any Invoice Cove server. We do not collect, see, or receive any data about your invoices "
        "or how you use the app. There are no analytics, no tracking, nothing sent anywhere in the background. "
        "The only time the app itself needs an internet connection is to process a one-time Invoice Cove Pro purchase "
        "through Google Play. See the full <a href=\"privacy.html\">Privacy Policy</a> for details."
    ),
    "warn": (
        "Remember! Before you uninstall the app or clear its storage, that data is not backed up anywhere by us. "
        "Uninstalling Invoice Cove, or clearing its storage from Android Settings, permanently deletes every invoice, "
        "quote, customer and setting on this device — there is no cloud copy to restore from. To protect your files: create a "
        "backup with Invoice Cove Pro (see <a href=\"#backup\">Backup &amp; Restore</a>) or export what you need as "
        "Excel, CSV or ZIP (see <a href=\"#export\">Exporting invoices</a>)."
    ),
    "sections": {
        "home": ("Home screen", [
            ("p", "The Home screen is your starting point, with one tile for each main action: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} and "
                  "{{common_reports_title}}. Tap any tile to jump straight there."),
            ("p", "The bar at the bottom gives you quick access to {{nav_home}}, {{nav_new}} (new invoice), "
                  "{{nav_invoices}}, {{nav_customers}} and {{nav_reports}}."),
            ("p", "The gear icon (⚙️) in the top-right corner of most screens opens <a href=\"#settings\">Business Details &amp; Settings</a>."),
        ]),
        "customers": ("Customers", [
            ("p", "To add a customer, head to the {{nav_customers}} tab and tap the + icon, or use the {{home_new_customer_title}} tile. "
                  "You can also add one while creating an invoice or quote. Only a name is required to create a customer file. Optional fields include: "
                  "{{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, the address, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} and a colour tint for their documents. Every field shows an example so you know what belongs there."),
            ("p", "Tap a customer to {{common_edit}} them, open their {{customers_view_history}} (invoices, quotes and drafts) "
                  "or {{common_delete}} them."),
            ("p", "On your invoices and quotes, the customer's details are printed under their name in a fixed order: customer number, tax ID, VAT number, "
                  "trade register number, then address, email and phone. Anything you leave empty is not printed."),
            ("note", "Saving works differently here than on invoices. A customer has its own {{customers_form_save_customer}} "
                     "button (or {{customers_form_save_changes}} when editing) and is saved the moment you tap it. If you try to close the form "
                     "with unsaved changes, Invoice Cove asks you to confirm first."),
            ("note", "Deleting a customer does not delete the invoices and quotes you already issued to them. However, their unfinished <a href=\"#drafts\">drafts</a> are "
                     "deleted with them, Invoice Cove asks you to confirm first."),
        ]),
        "new-invoice": ("Creating an invoice", [
            ("p", "From {{nav_new}} (or the {{home_new_invoice_title}} tile): choose a customer (or create one on the spot) "
                  "and set the invoice date and due date, then add your items."),
            ("p", "Tap {{newinvoice_add_item_details_button}} and fill in the description, quantity, price per unit, optionally a unit "
                  "(such as h, pcs or kg) and a date and time. The unit is printed next to the quantity on the PDF. Tap the pencil (✏️) on an item to correct it "
                  "or the trash can (🗑️) to remove it. Descriptions and prices you used before are suggested as you type."),
            ("p", "Then add, if necessary, a tax rate, a {{newinvoice_discount_label}} (a percentage or a fixed amount) and "
                  "{{common_notes_label}}. The invoice number is assigned for you (with Invoice Cove Pro, this can be edited) and the currency is chosen next to it."),
            ("p", "{{common_preview_button}} renders a throwaway PDF so you can check how it looks — nothing is saved yet. "
                  "The {{common_template_button}} button shows which template will be used, tap it to pick a different one for this document only."),
            ("note", "{{newinvoice_generate_button}} does three things at once: it saves the invoice, creates the PDF, and opens your device's "
                     "share sheet so you can send it. Not ready yet? Use {{newinvoice_save_draft_button}} — see <a href=\"#drafts\">Drafts</a>."),
        ]),
        "drafts": ("Drafts", [
            ("p", "You do not lose an invoice you are still working on. As soon as you have chosen a customer and added at least one item or a note, Invoice Cove "
                  "keeps a draft and updates it a moment after you stop typing and once more when you leave the app. There is no "
                  "\"discard changes?\" question when you leave the screen; a short message tells you the draft was saved."),
            ("p", "Tap {{newinvoice_save_draft_button}} (under {{newinvoice_generate_button}}) to set the invoice aside on purpose: it is saved and "
                  "the form is cleared, ready for the next invoice. This works as soon as a customer is chosen, even before you add items."),
            ("p", "Find your drafts under {{nav_customers}} → the customer → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Each draft shows when it was last edited, how many items it has and the total. Tap it to keep "
                  "editing or to generate the invoice; tap the trash can to delete it."),
            ("ul", [
                "A draft never uses an invoice number and does not count toward the free monthly limit. The number is only assigned when you generate the final "
                "invoice — the draft is then replaced by it.",
                "A draft keeps the invoice date and due date only if you picked them yourself; otherwise it uses today's date when you reopen it.",
                "Deleting a customer also deletes their drafts (Invoice Cove will ask first). Drafts are included in a backup.",
                "Drafts are available for invoices; quotes do not have them.",
            ]),
        ]),
        "invoices": ("Managing invoices", [
            ("p", "The {{nav_invoices}} tab groups your invoices into a folder per customer, which you can sort by "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> or <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Open a folder to see its invoices, sorted by date, value, number or status."),
            ("p", "Every invoice has a status: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (past its due date), "
                  "{{invoices_status_partially_paid}} (a deposit was recorded), {{invoices_status_paid}} or "
                  "{{invoices_status_void}}. Tap an invoice to {{common_view}} it, {{common_share}} it again, mark it paid or void, or delete it."),
            ("ul", [
                "{{invoices_action_mark_paid}} asks for the payment date and how it was paid (bank transfer, cash, card, PayPal or other). "
                "Once an invoice is paid it cannot be set back to unpaid.",
                "{{deposit_record_title}} notes an advance payment. The invoice then shows as {{invoices_status_partially_paid}}, and the deposit cannot be more than the total.",
                "{{invoices_action_mark_void}} keeps the invoice on record but marks it as cancelled. This is preferred to deleting, a deleted invoice "
                "cannot be recovered.",
            ]),
            ("p", "With Pro, a customer's folder can also be saved or shared as a ZIP of PDFs, the whole list exported for your accountant — see "
                  "<a href=\"#export\">Exporting invoices</a>."),
        ]),
        "export": ("Exporting invoices (Excel, CSV, ZIP)", [
            ("p", "Available with Invoice Cove Pro. Tap the export icon (📄) at the top of the {{nav_invoices}} tab. Choose which invoices to include "
                  "with the year and month pickers ({{invoices_export_all}}, one year, or one month of a year; only years and months that "
                  "have invoices are offered), then pick what to do:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — an Excel spreadsheet (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — the same table as a CSV file.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — the invoice PDFs in one ZIP, one folder per customer.",
                "{{invoices_export_delete}} — permanently deletes the selected invoices after two confirmations.",
            ]),
            ("p", "<em>Save</em> lets you choose where on your device the file goes; <em>Share</em> opens Android's share sheet so you can email it or send it "
                  "in a message."),
            ("p", "Excel and CSV are made for your accountant, the default is: one row per invoice, number and dates, customer's name, number, "
                  "tax ID, VAT number, trade register number and address, the invoice's subtotal, discount, VAT rate, VAT amount and total, the currency, "
                  "payment status, date and method. Column headings and fixed words (invoice, paid, unpaid, payment methods) are written in the language "
                  "the app is set to."),
            ("p", "To get one row per invoice item with the invoice details repeated on every row and each item's description, quantity, unit, price "
                  "and net amount added, turn on {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Creating a quote", [
            ("p", "{{home_new_quote_title}} tile works like New Invoice tile, same fields, same {{common_preview_button}} and {{common_template_button}} buttons, same "
                  "{{newquote_generate_button}} that saves/creates the PDF and opens the share sheet in one tap; with a "
                  "{{newquote_date_label}} and a {{newquote_valid_until_label}} date instead of an invoice date and due date."),
            ("p", "Quotes do not have drafts."),
        ]),
        "quotes": ("Managing quotes & converting to invoice", [
            ("p", "The {{common_quotes_title}} screen (from the Home tile) lists your quotes by customer, the same way Invoices does. Open a quote to "
                  "view or share it, use {{quotes_action_accept}} or {{quotes_action_decline}} when the customer answers, record a deposit, or delete it. "
                  "The deposit cannot be more than the quote's total."),
            ("p", "Once a customer accepts a quote, use {{quotes_action_convert_to_invoice}} to turn the checked line items into a real, "
                  "independently editable invoice. The due date and discount can still be adjusted, the original quote is marked "
                  "{{quotes_status_converted}} and kept for your records."),
        ]),
        "calendar": ("Calendar & reminders", [
            ("p", "The {{calendar_title}} screen is a monthly view for your own notes. Tap a day to see or add notes, notes have titles and text, "
                  "with {{calendar_remind_me}} and a time it sends you a notification at the date and time set. The first day of the week follows your settings."),
            ("p", "Separately, Invoice Cove sends payment reminders — local notifications for invoices that are due soon or overdue. Nothing is sent from or to a server."),
        ]),
        "reports": ("Reports", [
            ("p", "{{common_reports_title}} gives you a quick overview of: {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} and {{reports_stat_overdue}} amounts, how many invoices you have, "
                  "<em>{{reports_revenue_by_month}}</em>, and your <em>{{reports_top_customers}}</em> by billed total."),
            ("p", "Tap the {{reports_stat_outstanding}} or {{reports_stat_overdue}} card to open the list of exactly those invoices."),
        ]),
        "settings": ("Business details & settings", [
            ("p", "Open Settings from the gear icon, this screen is called {{settings_title}}. It starts with your optional preferences: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} or {{settings_theme_dark}}), the default "
                  "{{settings_invoice_template_label}}, the {{settings_tax_label_label}} (VAT, GST…), the "
                  "{{settings_first_day_of_week_label}} and the {{settings_due_date_default_label}}, which fills the due date "
                  "automatically (e.g. Net 30). Below them come {{settings_security_label}} (see <a href=\"#app-lock\">App Lock</a>), "
                  "{{settings_item_suggestions_label}} and {{settings_backup_restore_label}} (see <a href=\"#backup\">Backup &amp; restore</a>)."),
            ("p", "{{settings_item_memory_title}} remembers item descriptions and prices to suggest them as you type – <em>{{common_clear}}</em> forgets "
                  "them without touching your invoices."),
            ("p", "Further down is your business profile, printed on every invoice and quote: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, a short tagline ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, the {{settings_date_format_label}} for dates, the address, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (company number, share capital and the like), your "
                  "{{settings_business_logo_label}} and your {{settings_payment_details_label}} (IBAN, PayPal.me Link). Each field "
                  "has an example, and any field you leave empty does not appear on your invoices. Tap {{common_done}} when "
                  "you have finished, if you leave with unsaved changes you are asked to confirm."),
            ("p", "At the very bottom: this {{settings_user_manual}} and {{settings_share_this_app}} are displayed."),
        ]),
        "backup": ("Backup & restore", [
            ("p", "Available with Invoice Cove Pro, under {{settings_backup_restore_label}}. {{settings_create_backup_title}} saves "
                  "everything: invoices, quotes, drafts, customers, calendar, settings, your logo and the PDFs all into one file. Choose "
                  "{{backup_save_button}} to store it where you want, or {{backup_share_button}} to send it somewhere safe."),
            ("p", "{{settings_restore_backup_title}} brings it all back in case you need to transfer on a new phone. It only works on a fresh install, before you have "
                  "added any data, so it can never overwrite what you already have. Invoice Cove checks that the file is intact and tells you if it is damaged, "
                  "if it is not an Invoice Cove backup, or was made by a newer version of the app (update first)."),
            ("note", "A backup file is not encrypted: anyone who has it can read your data. Keep it somewhere private. Your App Lock PIN is never "
                     "included in it."),
        ]),
        "app-lock": ("App Lock", [
            ("p", "Under {{settings_security_label}} you can turn on {{settings_app_lock_title}}: Invoice Cove then asks for your PIN "
                  "(or fingerprint) when the app is freshly opened, or after the phone restarts — not each time you switch back to it."),
            ("ul", [
                "{{settings_set_pin}}: choose a 4-digit PIN and confirm it.",
                "You then get a 6-digit recovery code, shown only once. Write it down and keep it safe.",
                "If your phone supports it, unlock with your fingerprint instead ({{security_use_fingerprint}}).",
                "Forgot the PIN? Use {{security_forgot_pin}} and enter the recovery code. After 5 wrong attempts you must wait 30 seconds – the wait "
                "grows with more wrong attempts.",
            ]),
            ("note", "If you lose both your PIN and the recovery code and have not set up fingerprint unlock there is no way to get back in. We cannot reset it "
                     "for you."),
        ]),
        "languages": ("Languages", [
            ("p", "Invoice Cove speaks 13 languages: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands and Svenska. Tap the round flag icon at the top of Settings to switch — the app changes immediately."),
            ("p", "The text on your PDFs and on Excel/CSV exports follows the language the app is set to, and this guide is available in the same 13 languages "
                  "(use the language bar at the top of the page)."),
        ]),
        "templates": ("PDF templates", [
            ("p", "Invoice Cove starts with 18 PDF designs: Classic, Client Color (tinted with the customer's colour), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves and Spooky Hollow."),
            ("p", "Pick your default in Settings → {{settings_invoice_template_label}}: tap a design, then {{common_done}}. It "
                  "applies to everything you generate from then on. For a single invoice or quote, use the {{common_template_button}} button on "
                  "the form."),
            ("p", "Every template prints the same information: your business details, the customer's details, items with their unit and date, totals, notes and "
                  "payment details — but only what you filled in. Long invoices continue on a second page, with the totals kept together with the last item."),
        ]),
        "free-vs-pro": ("Free plan vs. Invoice Cove Pro", [
            ("p", "Invoice Cove is free to use, with a few sensible limits:"),
            ("ul", [
                "Up to 3 invoices generated per calendar month",
                "Up to 3 quotes generated per calendar month",
                "Up to 3 customers at a time",
                "Invoice and quote numbers are assigned automatically and cannot be edited",
                "Excel, CSV and ZIP export are Pro-only",
                "Backup &amp; Restore is Pro-only",
            ]),
            ("p", "Invoice Cove Pro is a single one-time purchase through Google Play (not a subscription) that removes every one of those limits "
                  "for good. Drafts, all templates and languages, App Lock, and creating, previewing and sharing documents are free for everyone. See the "
                  "<a href=\"terms.html\">Terms of Use</a> for the full details."),
        ]),
    },
}
