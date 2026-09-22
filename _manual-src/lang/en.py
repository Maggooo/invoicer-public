# English master text. Other languages follow the same sections and blocks.
# {{key}} = the app's own label for that button/screen (see ui/en.json).
T = {
    "title": "User Manual",
    "subtitle": "Everything Invoice Cove can do, screen by screen.",
    "meta_desc": "Complete user manual for Invoice Cove - Offline Billing.",
    "lang_label": "Language",
    "brand_alt": "Invoice Cove",
    "toc": "Contents",
    "footer_questions": "Questions?",
    "lede": (
        "Invoice Cove runs entirely on your device — invoices, quotes, customers and your business profile are stored "
        "locally, not on any Invoice Cove server. <strong>We don't collect, see, or receive any data about your invoices "
        "or how you use the app</strong> — there's no analytics, no tracking, nothing sent anywhere in the background. "
        "The only time the app itself needs an internet connection is to process a one-time Invoice Cove Pro purchase "
        "through Google Play. See the full <a href=\"privacy.html\">Privacy Policy</a> for details."
    ),
    "warn": (
        "<strong>Before you uninstall the app or clear its storage:</strong> that data is not backed up anywhere by us. "
        "Uninstalling Invoice Cove, or clearing its storage from Android Settings, permanently deletes every invoice, "
        "quote, customer and setting on this device — there's no cloud copy to restore from. Protect yourself: create a "
        "backup with Invoice Cove Pro (see <a href=\"#backup\">Backup &amp; Restore</a>) or export what you need as "
        "Excel, CSV or ZIP (see <a href=\"#export\">Exporting invoices</a>)."
    ),
    "sections": {
        "home": ("Home screen", [
            ("p", "The Home screen is your starting point, with one tile for each main action: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> and "
                  "<strong>{{common_reports_title}}</strong>. Tap any tile to jump straight there."),
            ("p", "The bar at the bottom always gives you quick access to <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (a new invoice), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> and <strong>{{nav_reports}}</strong>."),
            ("p", "The gear icon (⚙️) in the top-right corner of most screens opens <a href=\"#settings\">Business Details &amp; Settings</a>."),
        ]),
        "customers": ("Customers", [
            ("p", "Add a customer from the <strong>{{nav_customers}}</strong> tab (tap the + icon), with the <strong>{{home_new_customer_title}}</strong> tile, "
                  "or inline while creating an invoice or quote. Only the name is required. Optional fields: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, the address, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} and a color that tints their documents. Every field shows an example so you know what belongs there."),
            ("p", "Tap a customer to <strong>{{common_edit}}</strong> them, open their <strong>{{customers_view_history}}</strong> (invoices, quotes and drafts) "
                  "or <strong>{{common_delete}}</strong> them."),
            ("p", "On your invoices and quotes, the customer's details are printed under their name in a fixed order: customer number, tax ID, VAT number, "
                  "trade register number, then address, email and phone. Anything you leave empty is simply not printed."),
            ("note", "<strong>Saving works differently here than on invoices.</strong> A customer has its own <strong>{{customers_form_save_customer}}</strong> "
                     "(or <strong>{{customers_form_save_changes}}</strong> when editing) button — it's saved the moment you tap it. If you try to close the form "
                     "with unsaved changes, Invoice Cove asks you to confirm first."),
            ("note", "Deleting a customer does not delete the invoices and quotes you already issued to them. Their unfinished <a href=\"#drafts\">drafts</a> are "
                     "deleted with them — you're asked first."),
        ]),
        "new-invoice": ("Creating an invoice", [
            ("p", "From <strong>{{nav_new}}</strong> (or the <strong>{{home_new_invoice_title}}</strong> tile): choose a customer — or create one on the spot — "
                  "set the invoice date and due date, then add your items."),
            ("p", "Tap <strong>{{newinvoice_add_item_details_button}}</strong> and fill in the description, quantity, price per unit, and optionally a unit "
                  "(such as h, pcs or kg) and a date and time. The unit is printed next to the quantity on the PDF. Tap the pencil (✏️) on an item to correct it "
                  "or the trash can (🗑️) to remove it. Descriptions and prices you used before are suggested as you type."),
            ("p", "Then add, if you need them, a tax rate, a <strong>{{newinvoice_discount_label}}</strong> (a percentage or a fixed amount) and "
                  "<strong>{{common_notes_label}}</strong>. The invoice number is assigned for you (with Pro you can edit it); the currency is chosen next to it."),
            ("p", "<strong>{{common_preview_button}}</strong> renders a throwaway PDF so you can check how it looks — nothing is saved yet. "
                  "The <strong>{{common_template_button}}</strong> button shows which template will be used; tap it to pick a different one for this document only."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> does three things at once: it saves the invoice, creates the PDF, and opens your device's "
                     "share sheet so you can send it. Not ready yet? Use <strong>{{newinvoice_save_draft_button}}</strong> — see <a href=\"#drafts\">Drafts</a>."),
        ]),
        "drafts": ("Drafts", [
            ("p", "You don't lose an invoice you're still working on. As soon as you've chosen a customer and added at least one item or a note, Invoice Cove "
                  "keeps a <strong>draft</strong> and updates it a moment after you stop typing — and once more when you leave the app. There is no "
                  "\"discard changes?\" question when you leave the screen; a short message tells you the draft was saved."),
            ("p", "Tap <strong>{{newinvoice_save_draft_button}}</strong> (under {{newinvoice_generate_button}}) to set the invoice aside on purpose: it is saved and "
                  "the form is cleared, ready for the next invoice. This works as soon as a customer is chosen, even before you add items."),
            ("p", "Find your drafts under <strong>{{nav_customers}}</strong> → the customer → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Each draft shows when it was last edited, how many items it has and its total. Tap it to keep "
                  "editing or to generate the invoice; tap the trash can to delete it."),
            ("ul", [
                "A draft never uses an invoice number and doesn't count toward the free monthly limit. The number is only assigned when you generate the final "
                "invoice — the draft is then replaced by it.",
                "A draft keeps the invoice date and due date only if you picked them yourself; otherwise it uses today's date when you reopen it.",
                "Deleting a customer also deletes their drafts (you're asked first). Drafts are included in a backup.",
                "Drafts are available for invoices; quotes don't have them.",
            ]),
        ]),
        "invoices": ("Managing invoices", [
            ("p", "The <strong>{{nav_invoices}}</strong> tab groups your invoices into a folder per customer, which you can sort by "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> or <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Open a folder to see its invoices, sorted by date, value, number or status."),
            ("p", "Every invoice has a status: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (past its due date), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (a deposit was recorded), <strong>{{invoices_status_paid}}</strong> or "
                  "<strong>{{invoices_status_void}}</strong>. Tap an invoice to {{common_view}} it, {{common_share}} it again, mark it paid or void, or delete it."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> asks for the payment date and how it was paid (bank transfer, cash, card, PayPal or other). "
                "Once an invoice is paid it can't be set back to unpaid.",
                "<strong>{{deposit_record_title}}</strong> notes an advance payment. The invoice then shows as <strong>{{invoices_status_partially_paid}}</strong>, and the deposit can't be more than the total.",
                "<strong>{{invoices_action_mark_void}}</strong> keeps the invoice on record but marks it as cancelled. Prefer it to deleting — a deleted invoice "
                "can't be recovered.",
            ]),
            ("p", "With Pro, a customer's folder can also be saved or shared as a ZIP of PDFs, and the whole list exported for your accountant — see "
                  "<a href=\"#export\">Exporting invoices</a>."),
        ]),
        "export": ("Exporting invoices (Excel, CSV, ZIP)", [
            ("p", "Available with Invoice Cove Pro. Tap the export icon (📄) at the top of the <strong>{{nav_invoices}}</strong> tab. Choose which invoices to include "
                  "with the year and month pickers (<strong>{{invoices_export_all}}</strong>, one year, or one month of a year — only years and months that "
                  "have invoices are offered), then pick what to do:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — an Excel spreadsheet (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — the same table as a CSV file.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — the invoice PDFs in one ZIP, one folder per customer.",
                "<strong>{{invoices_export_delete}}</strong> — permanently deletes the selected invoices, after two confirmations.",
            ]),
            ("p", "<em>Save</em> lets you choose where on your device the file goes; <em>Share</em> opens Android's share sheet so you can email it or send it "
                  "in a chat."),
            ("p", "Excel and CSV are made for your accountant: by default, <strong>one row per invoice</strong> — number and dates, the customer's name, number, "
                  "tax ID, VAT number, trade register number and address, the invoice's subtotal, discount, VAT rate, VAT amount and total, the currency, and "
                  "the payment status, date and method. Column headings and fixed words (invoice, paid, unpaid, payment methods) are written in the language "
                  "the app is set to."),
            ("p", "Turn on <strong>{{invoices_export_detailed_toggle}}</strong> in the same sheet to get one row per invoice item instead, with the invoice "
                  "details repeated on every row and each item's description, quantity, unit, price and net amount added."),
        ]),
        "new-quote": ("Creating a quote", [
            ("p", "<strong>{{home_new_quote_title}}</strong> works like New Invoice — same fields, the same <strong>{{common_preview_button}}</strong> and <strong>{{common_template_button}}</strong> buttons, and the same "
                  "<strong>{{newquote_generate_button}}</strong> that saves, creates the PDF and opens the share sheet in one tap — with a "
                  "<strong>{{newquote_date_label}}</strong> and a <strong>{{newquote_valid_until_label}}</strong> date instead of an invoice date and due date. "
                  "Quotes don't have drafts."),
        ]),
        "quotes": ("Managing quotes & converting to invoice", [
            ("p", "The <strong>{{common_quotes_title}}</strong> screen (from the Home tile) lists your quotes by customer, the same way Invoices does. Open a quote to "
                  "view or share it, use <strong>{{quotes_action_accept}}</strong> or <strong>{{quotes_action_decline}}</strong> when the customer answers, record a deposit, or delete it. "
                  "The deposit can't be more than the quote's total."),
            ("p", "Once a customer accepts a quote, use <strong>{{quotes_action_convert_to_invoice}}</strong> to turn the checked line items into a real, "
                  "independently editable invoice — the due date and discount can still be adjusted, the original quote is marked "
                  "<strong>{{quotes_status_converted}}</strong> and kept for your records."),
        ]),
        "calendar": ("Calendar & reminders", [
            ("p", "The <strong>{{calendar_title}}</strong> screen is a month view for your own notes. Tap a day to see or add notes; a note has a title and text, and "
                  "with <strong>{{calendar_remind_me}}</strong> and a time it sends you a notification at that moment. The first day of the week follows your setting."),
            ("p", "Separately, Invoice Cove sends payment reminders — local notifications for invoices that are due soon or overdue. Nothing is sent from or to a server."),
        ]),
        "reports": ("Reports", [
            ("p", "<strong>{{common_reports_title}}</strong> gives you a quick overview: <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> and <strong>{{reports_stat_overdue}}</strong> amounts, how many invoices you have, "
                  "<em>{{reports_revenue_by_month}}</em>, and your <em>{{reports_top_customers}}</em> by billed total."),
            ("p", "Tap the <strong>{{reports_stat_outstanding}}</strong> or <strong>{{reports_stat_overdue}}</strong> card to open the list of exactly those invoices."),
        ]),
        "settings": ("Business details & settings", [
            ("p", "Open Settings from the gear icon — the screen is called <strong>{{settings_title}}</strong>. It starts with your preferences: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} or {{settings_theme_dark}}), the default "
                  "<strong>{{settings_invoice_template_label}}</strong>, the <strong>{{settings_tax_label_label}}</strong> (VAT, GST…), the "
                  "<strong>{{settings_first_day_of_week_label}}</strong> and the <strong>{{settings_due_date_default_label}}</strong> (fills the due date "
                  "automatically, e.g. Net 30). Below them come <strong>{{settings_security_label}}</strong> (see <a href=\"#app-lock\">App Lock</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> and <strong>{{settings_backup_restore_label}}</strong> (see <a href=\"#backup\">Backup &amp; restore</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> remembers item descriptions and prices to suggest them as you type; <em>{{common_clear}}</em> forgets "
                  "them without touching your invoices."),
            ("p", "Further down is your business profile, printed on every invoice and quote: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, a short tagline (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, the <strong>{{settings_date_format_label}}</strong> for dates, the address, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (company number, share capital and the like), your "
                  "<strong>{{settings_business_logo_label}}</strong> and your <strong>{{settings_payment_details_label}}</strong> (IBAN, PayPal.me link…). Each field "
                  "has an example, and <strong>any field you leave empty simply doesn't appear on your invoices</strong>. Tap <strong>{{common_done}}</strong> when "
                  "you finish; if you leave with unsaved changes you're asked first."),
            ("p", "At the very bottom: this <strong>{{settings_user_manual}}</strong> and <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Backup & restore", [
            ("p", "Available with Invoice Cove Pro. Under <strong>{{settings_backup_restore_label}}</strong>, <strong>{{settings_create_backup_title}}</strong> saves "
                  "everything — invoices, quotes, drafts, customers, calendar, settings, your logo and the PDFs — into one file. Choose "
                  "<strong>{{backup_save_button}}</strong> to store it where you want, or <strong>{{backup_share_button}}</strong> to send it somewhere safe."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> brings it all back — for example on a new phone. It only works on a fresh install, before you've "
                  "added any data, so it can never overwrite what you already have. Invoice Cove checks that the file is intact and tells you if it is damaged, "
                  "isn't an Invoice Cove backup, or was made by a newer version of the app (update first)."),
            ("note", "A backup file is <strong>not encrypted</strong>: anyone who has it can read your data. Keep it somewhere private. Your App Lock PIN is never "
                     "included in it."),
        ]),
        "app-lock": ("App Lock", [
            ("p", "Under <strong>{{settings_security_label}}</strong> you can turn on <strong>{{settings_app_lock_title}}</strong>: Invoice Cove then asks for your PIN "
                  "(or fingerprint) when the app is freshly opened, or after the phone restarts — not each time you switch back to it."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: choose a 4-digit PIN and confirm it.",
                "You then get a 6-digit <strong>recovery code</strong>, shown only once. Write it down and keep it safe.",
                "If your phone supports it, unlock with your fingerprint instead (<strong>{{security_use_fingerprint}}</strong>).",
                "Forgot the PIN? Use <strong>{{security_forgot_pin}}</strong> and enter the recovery code. After 5 wrong attempts you must wait 30 seconds; the wait "
                "grows with more wrong attempts.",
            ]),
            ("note", "If you lose both your PIN and the recovery code — and haven't set up fingerprint unlock — there is no way to get back in. We cannot reset it "
                     "for you."),
        ]),
        "languages": ("Languages", [
            ("p", "Invoice Cove speaks 13 languages: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands and Svenska. Tap the round flag icon at the top of Settings to switch — the app changes immediately."),
            ("p", "The text on your PDFs and on Excel/CSV exports follows the language the app is set to, and this manual is available in the same 13 languages "
                  "(use the language bar at the top of the page)."),
        ]),
        "templates": ("PDF templates", [
            ("p", "Invoice Cove ships with 18 PDF designs: Classic, Client Color (tinted with the customer's color), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves and Spooky Hollow."),
            ("p", "Pick your default in Settings → <strong>{{settings_invoice_template_label}}</strong>: tap a design, then <strong>{{common_done}}</strong>. It "
                  "applies to everything you generate from then on. For a single invoice or quote, use the <strong>{{common_template_button}}</strong> button on "
                  "the form."),
            ("p", "Every template prints the same information — your business details, the customer's details, items with their unit and date, totals, notes and "
                  "payment details — but only what you filled in. Long invoices continue on a second page, with the totals kept together with the last item."),
        ]),
        "free-vs-pro": ("Free plan vs. Invoice Cove Pro", [
            ("p", "Invoice Cove is free to use, with a few sensible limits:"),
            ("ul", [
                "Up to 3 invoices and 3 quotes generated per calendar month",
                "Up to 3 customers at a time",
                "Invoice and quote numbers are assigned automatically and can't be edited",
                "Excel, CSV and ZIP export are Pro-only",
                "Backup &amp; Restore is Pro-only",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> is a single one-time purchase through Google Play — not a subscription — that removes every one of those limits "
                  "for good. Drafts, all templates and languages, App Lock, and creating, previewing and sharing documents are free for everyone. See the "
                  "<a href=\"terms.html\">Terms of Use</a> for the full details."),
        ]),
    },
}
