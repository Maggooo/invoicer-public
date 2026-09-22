T = {
    "title": "Manual de usuario",
    "subtitle": "Todo lo que Invoice Cove puede hacer, pantalla por pantalla.",
    "meta_desc": "Manual de usuario completo de Invoice Cove - Offline Billing.",
    "lang_label": "Idioma",
    "brand_alt": "Invoice Cove",
    "toc": "Contenido",
    "footer_questions": "¿Preguntas?",
    "lede": (
        "Invoice Cove funciona por completo en tu dispositivo: las facturas, los presupuestos, los clientes y el perfil de tu negocio se guardan localmente, "
        "no en ningún servidor de Invoice Cove. <strong>No recopilamos, vemos ni recibimos ningún dato sobre tus facturas ni sobre cómo usas la aplicación</strong> "
        "— no hay analítica, ni seguimiento, ni se envía nada en segundo plano. "
        "La única vez que la propia aplicación necesita conexión a internet es para procesar la compra única de Invoice Cove Pro a través de Google Play. "
        "Consulta la <a href=\"privacy.html\">Política de privacidad</a> para más detalles."
    ),
    "warn": (
        "<strong>Antes de desinstalar la aplicación o borrar su almacenamiento:</strong> nosotros no guardamos una copia de esos datos en ningún sitio. "
        "Desinstalar Invoice Cove, o borrar su almacenamiento desde los ajustes de Android, elimina para siempre todas las facturas, presupuestos, clientes "
        "y ajustes de este dispositivo: no hay copia en la nube desde la que restaurar. Protégete: crea una copia de seguridad "
        "con Invoice Cove Pro (consulta <a href=\"#backup\">Copia de seguridad y restauración</a>) o exporta lo que necesites a Excel, CSV o ZIP "
        "(consulta <a href=\"#export\">Exportar facturas</a>)."
    ),
    "sections": {
        "home": ("Pantalla de inicio", [
            ("p", "La pantalla de inicio es tu punto de partida, con un icono para cada acción principal: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> y "
                  "<strong>{{common_reports_title}}</strong>. Toca cualquiera para ir directamente."),
            ("p", "La barra inferior te da siempre acceso rápido a <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (una factura nueva), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> y <strong>{{nav_reports}}</strong>."),
            ("p", "El icono de engranaje (⚙️) de la esquina superior derecha de la mayoría de las pantallas abre los <a href=\"#settings\">Datos del negocio y ajustes</a>."),
        ]),
        "customers": ("Clientes", [
            ("p", "Añade un cliente desde la pestaña <strong>{{nav_customers}}</strong> (toca el icono +), con el icono <strong>{{home_new_customer_title}}</strong> "
                  "o sobre la marcha al crear una factura o un presupuesto. Solo el nombre es obligatorio. Campos opcionales: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, la dirección, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} y un color que tiñe sus documentos. Cada campo muestra un ejemplo para que sepas qué escribir."),
            ("p", "Toca un cliente para editarlo (<strong>{{common_edit}}</strong>), abrir su <strong>{{customers_view_history}}</strong> (facturas, presupuestos y borradores) "
                  "o eliminarlo (<strong>{{common_delete}}</strong>)."),
            ("p", "En tus facturas y presupuestos, los datos del cliente se imprimen bajo su nombre en un orden fijo: número de cliente, identificación fiscal, número de IVA, "
                  "número del registro mercantil y después dirección, correo electrónico y teléfono. Lo que dejes vacío simplemente no se imprime."),
            ("note", "<strong>Guardar funciona aquí de otra manera que en las facturas.</strong> Un cliente tiene su propio botón <strong>{{customers_form_save_customer}}</strong> "
                     "(o <strong>{{customers_form_save_changes}}</strong> al editar): se guarda en cuanto lo tocas. Si intentas cerrar el formulario "
                     "con cambios sin guardar, Invoice Cove te pide confirmación antes."),
            ("note", "Eliminar un cliente no elimina las facturas y presupuestos que ya le hayas emitido. Sus <a href=\"#drafts\">borradores</a> sin terminar "
                     "se eliminan con él; se te pregunta antes."),
        ]),
        "new-invoice": ("Crear una factura", [
            ("p", "Desde <strong>{{nav_new}}</strong> (o el icono <strong>{{home_new_invoice_title}}</strong>): elige un cliente —o crea uno en el momento—, "
                  "indica la fecha de la factura y la fecha de vencimiento, y añade tus artículos."),
            ("p", "Toca <strong>{{newinvoice_add_item_details_button}}</strong> y rellena la descripción, la cantidad, el precio por unidad y, si quieres, una unidad "
                  "(como h, uds. o kg) y una fecha y hora. La unidad se imprime junto a la cantidad en el PDF. Toca el lápiz (✏️) de un artículo para corregirlo "
                  "o la papelera (🗑️) para quitarlo. Las descripciones y precios que ya usaste se sugieren mientras escribes."),
            ("p", "Después añade, si los necesitas, un tipo de impuesto, un <strong>{{newinvoice_discount_label}}</strong> (porcentaje o importe fijo) y "
                  "<strong>{{common_notes_label}}</strong>. El número de factura se asigna solo (con Pro puedes editarlo); la moneda se elige a su lado."),
            ("p", "<strong>{{common_preview_button}}</strong> genera un PDF temporal para que veas cómo queda; todavía no se guarda nada. "
                  "El botón <strong>{{common_template_button}}</strong> muestra qué plantilla se usará; tócalo para elegir otra solo para este documento."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> hace tres cosas a la vez: guarda la factura, crea el PDF y abre el menú de compartir "
                     "de tu dispositivo para enviarla. ¿Aún no está lista? Usa <strong>{{newinvoice_save_draft_button}}</strong>; consulta <a href=\"#drafts\">Borradores</a>."),
        ]),
        "drafts": ("Borradores", [
            ("p", "No pierdes una factura en la que todavía trabajas. En cuanto has elegido un cliente y añadido al menos un artículo o una nota, Invoice Cove "
                  "guarda un <strong>borrador</strong> y lo actualiza un momento después de que dejes de escribir, y una vez más cuando sales de la aplicación. No hay "
                  "pregunta de «¿descartar los cambios?» al salir de la pantalla; un mensaje breve te avisa de que el borrador se guardó."),
            ("p", "Toca <strong>{{newinvoice_save_draft_button}}</strong> (bajo {{newinvoice_generate_button}}) para apartar la factura a propósito: se guarda y "
                  "el formulario se vacía, listo para la siguiente. Funciona en cuanto hay un cliente elegido, incluso antes de añadir artículos."),
            ("p", "Encuentra tus borradores en <strong>{{nav_customers}}</strong> → el cliente → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Cada borrador muestra cuándo se editó por última vez, cuántos artículos tiene y su total. Tócalo para seguir "
                  "editándolo o para generar la factura; toca la papelera para eliminarlo."),
            ("ul", [
                "Un borrador nunca usa un número de factura y no cuenta para el límite mensual gratuito. El número solo se asigna cuando generas la factura "
                "final, y el borrador queda sustituido por ella.",
                "Un borrador conserva la fecha de factura y la de vencimiento solo si las elegiste tú; si no, al reabrirlo usa la fecha de hoy.",
                "Eliminar un cliente también elimina sus borradores (se te pregunta antes). Los borradores se incluyen en una copia de seguridad.",
                "Los borradores existen para las facturas; los presupuestos no los tienen.",
            ]),
        ]),
        "invoices": ("Gestionar facturas", [
            ("p", "La pestaña <strong>{{nav_invoices}}</strong> agrupa tus facturas en una carpeta por cliente, que puedes ordenar por "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> o <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Abre una carpeta para ver sus facturas, ordenadas por fecha, valor, número o estado."),
            ("p", "Cada factura tiene un estado: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (pasó su vencimiento), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (se registró un anticipo), <strong>{{invoices_status_paid}}</strong> o "
                  "<strong>{{invoices_status_void}}</strong>. Toca una factura para verla ({{common_view}}), volver a enviarla ({{common_share}}), marcarla como pagada o anulada, o eliminarla."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> pide la fecha del pago y cómo se pagó (transferencia bancaria, efectivo, tarjeta, PayPal u otro). "
                "Una factura pagada ya no puede volver a no pagada.",
                "<strong>{{deposit_record_title}}</strong> anota un pago adelantado. La factura aparece entonces como <strong>{{invoices_status_partially_paid}}</strong>, y el anticipo no puede superar el total.",
                "<strong>{{invoices_action_mark_void}}</strong> conserva la factura en tus registros pero la marca como cancelada. Es mejor que eliminarla: una factura eliminada "
                "no se puede recuperar.",
            ]),
            ("p", "Con Pro, la carpeta de un cliente también se puede guardar o compartir como ZIP de PDF, y toda la lista se puede exportar para tu contable; consulta "
                  "<a href=\"#export\">Exportar facturas</a>."),
        ]),
        "export": ("Exportar facturas (Excel, CSV, ZIP)", [
            ("p", "Disponible con Invoice Cove Pro. Toca el icono de exportar (📄) en la parte superior de la pestaña <strong>{{nav_invoices}}</strong>. Elige qué facturas incluir "
                  "con los selectores de año y mes (<strong>{{invoices_export_all}}</strong>, un año o un mes de un año; solo se ofrecen los años y meses que "
                  "tienen facturas) y después elige qué hacer:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong>: una hoja de cálculo de Excel (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong>: la misma tabla como archivo CSV.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong>: los PDF de las facturas en un ZIP, una carpeta por cliente.",
                "<strong>{{invoices_export_delete}}</strong>: elimina para siempre las facturas seleccionadas, tras dos confirmaciones.",
            ]),
            ("p", "<em>Guardar</em> te deja elegir en qué lugar del dispositivo queda el archivo; <em>Compartir</em> abre el menú de compartir de Android para enviarlo "
                  "por correo o en un chat."),
            ("p", "Excel y CSV están pensados para tu contable: por defecto, <strong>una fila por factura</strong> — número y fechas, nombre, número, "
                  "identificación fiscal, número de IVA, número del registro mercantil y dirección del cliente, subtotal, descuento, tipo de IVA, importe de "
                  "IVA y total de la factura, la moneda y el estado, la fecha y el método de pago. Los encabezados de columna y las palabras fijas (factura, "
                  "pagada, sin pagar, métodos de pago) se escriben en el idioma configurado en la aplicación."),
            ("p", "Activa <strong>{{invoices_export_detailed_toggle}}</strong> en el mismo panel para obtener en su lugar una fila por cada artículo de la "
                  "factura, con los datos de la factura repetidos en cada fila y la descripción, cantidad, unidad, precio e importe neto de cada artículo "
                  "añadidos."),
        ]),
        "new-quote": ("Crear un presupuesto", [
            ("p", "<strong>{{home_new_quote_title}}</strong> funciona como New Invoice: los mismos campos, los mismos botones <strong>{{common_preview_button}}</strong> y <strong>{{common_template_button}}</strong>, y el mismo "
                  "<strong>{{newquote_generate_button}}</strong> que guarda, crea el PDF y abre el menú de compartir con un toque, con una "
                  "<strong>{{newquote_date_label}}</strong> y una fecha <strong>{{newquote_valid_until_label}}</strong> en lugar de la fecha de factura y el vencimiento. "
                  "Los presupuestos no tienen borradores."),
        ]),
        "quotes": ("Gestionar presupuestos y convertirlos en factura", [
            ("p", "La pantalla <strong>{{common_quotes_title}}</strong> (desde el icono de inicio) lista tus presupuestos por cliente, igual que las facturas. Abre un presupuesto para "
                  "verlo o compartirlo, usa <strong>{{quotes_action_accept}}</strong> o <strong>{{quotes_action_decline}}</strong> cuando el cliente responda, "
                  "registra un anticipo o elimínalo. El anticipo no puede superar el total del presupuesto."),
            ("p", "Cuando un cliente acepta un presupuesto, usa <strong>{{quotes_action_convert_to_invoice}}</strong> para convertir las líneas marcadas en una factura real, "
                  "editable de forma independiente: el vencimiento y el descuento aún se pueden ajustar, y el presupuesto original se marca como "
                  "<strong>{{quotes_status_converted}}</strong> y se conserva en tus registros."),
        ]),
        "calendar": ("Calendario y recordatorios", [
            ("p", "La pantalla <strong>{{calendar_title}}</strong> es una vista mensual para tus propias notas. Toca un día para ver o añadir notas; una nota tiene título y texto y, "
                  "con <strong>{{calendar_remind_me}}</strong> y una hora, te envía una notificación en ese momento. El primer día de la semana sigue tu ajuste."),
            ("p", "Aparte, Invoice Cove envía recordatorios de pago: notificaciones locales de facturas que vencen pronto o están vencidas. No se envía nada hacia ni desde ningún servidor."),
        ]),
        "reports": ("Informes", [
            ("p", "<strong>{{common_reports_title}}</strong> te da una visión rápida: los importes <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> y <strong>{{reports_stat_overdue}}</strong>, cuántas facturas tienes, "
                  "<em>{{reports_revenue_by_month}}</em> y tus <em>{{reports_top_customers}}</em> por total facturado."),
            ("p", "Toca la tarjeta <strong>{{reports_stat_outstanding}}</strong> o <strong>{{reports_stat_overdue}}</strong> para abrir la lista exacta de esas facturas."),
        ]),
        "settings": ("Datos del negocio y ajustes", [
            ("p", "Abre los ajustes desde el icono de engranaje; la pantalla se llama <strong>{{settings_title}}</strong>. Empieza con tus preferencias: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} u {{settings_theme_dark}}), la "
                  "<strong>{{settings_invoice_template_label}}</strong> predeterminada, la <strong>{{settings_tax_label_label}}</strong> (IVA, GST…), "
                  "el <strong>{{settings_first_day_of_week_label}}</strong> y el <strong>{{settings_due_date_default_label}}</strong> (rellena el vencimiento automáticamente, p. ej. Net 30). "
                  "Debajo vienen <strong>{{settings_security_label}}</strong> (consulta <a href=\"#app-lock\">Bloqueo de la aplicación</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> y <strong>{{settings_backup_restore_label}}</strong> (consulta <a href=\"#backup\">Copia de seguridad y restauración</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> recuerda descripciones y precios de artículos para sugerirlos mientras escribes; <em>{{common_clear}}</em> los olvida "
                  "sin tocar tus facturas."),
            ("p", "Más abajo está el perfil de tu negocio, que se imprime en cada factura y presupuesto: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, un lema breve (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, el <strong>{{settings_date_format_label}}</strong> de las fechas, la dirección, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (número de registro, capital social y similares), tu "
                  "<strong>{{settings_business_logo_label}}</strong> y tus <strong>{{settings_payment_details_label}}</strong> (IBAN, enlace de PayPal.me…). Cada campo "
                  "tiene un ejemplo, y <strong>cualquier campo que dejes vacío simplemente no aparece en tus facturas</strong>. Toca <strong>{{common_done}}</strong> cuando "
                  "termines; si sales con cambios sin guardar, se te pregunta antes."),
            ("p", "Al final del todo: este <strong>{{settings_user_manual}}</strong> y <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Copia de seguridad y restauración", [
            ("p", "Disponible con Invoice Cove Pro. En <strong>{{settings_backup_restore_label}}</strong>, <strong>{{settings_create_backup_title}}</strong> guarda "
                  "todo (facturas, presupuestos, borradores, clientes, calendario, ajustes, tu logotipo y los PDF) en un solo archivo. Elige "
                  "<strong>{{backup_save_button}}</strong> para guardarlo donde quieras, o <strong>{{backup_share_button}}</strong> para enviarlo a un lugar seguro."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> lo devuelve todo, por ejemplo en un teléfono nuevo. Solo funciona en una instalación nueva, antes de que hayas "
                  "añadido datos, así que nunca puede sobrescribir lo que ya tienes. Invoice Cove comprueba que el archivo esté intacto y te avisa si está dañado, "
                  "si no es una copia de Invoice Cove o si la hizo una versión más reciente de la aplicación (actualiza primero)."),
            ("note", "Un archivo de copia de seguridad <strong>no está cifrado</strong>: quien lo tenga puede leer tus datos. Guárdalo en un lugar privado. El PIN de bloqueo de la aplicación no "
                     "se incluye nunca."),
        ]),
        "app-lock": ("Bloqueo de la aplicación", [
            ("p", "En <strong>{{settings_security_label}}</strong> puedes activar <strong>{{settings_app_lock_title}}</strong>: Invoice Cove te pedirá entonces tu PIN "
                  "(o tu huella) cuando la aplicación se abra de nuevo desde cero o tras reiniciar el teléfono, no cada vez que vuelvas a ella."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: elige un PIN de 4 dígitos y confírmalo.",
                "Después recibes un <strong>código de recuperación</strong> de 6 dígitos, que se muestra una sola vez. Anótalo y guárdalo en un lugar seguro.",
                "Si tu teléfono lo admite, desbloquea con tu huella (<strong>{{security_use_fingerprint}}</strong>).",
                "¿Olvidaste el PIN? Usa <strong>{{security_forgot_pin}}</strong> e introduce el código de recuperación. Tras 5 intentos erróneos debes esperar 30 segundos; "
                "la espera aumenta con más intentos erróneos.",
            ]),
            ("note", "Si pierdes tanto el PIN como el código de recuperación, y no has configurado el desbloqueo con huella, no hay forma de volver a entrar. No podemos restablecerlo "
                     "por ti."),
        ]),
        "languages": ("Idiomas", [
            ("p", "Invoice Cove habla 13 idiomas: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands y Svenska. Toca el icono redondo con la bandera en la parte superior de los ajustes para cambiar; la aplicación cambia al instante."),
            ("p", "El texto de tus PDF y de las exportaciones a Excel/CSV sigue el idioma configurado en la aplicación, y este manual está disponible en los mismos 13 idiomas "
                  "(usa la barra de idiomas de la parte superior de la página)."),
        ]),
        "templates": ("Plantillas PDF", [
            ("p", "Invoice Cove incluye 18 diseños de PDF: Classic, Client Color (teñido con el color del cliente), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves y Spooky Hollow."),
            ("p", "Elige tu plantilla predeterminada en Ajustes → <strong>{{settings_invoice_template_label}}</strong>: toca un diseño y después <strong>{{common_done}}</strong>. Se "
                  "aplica a todo lo que generes a partir de ese momento. Para una sola factura o presupuesto, usa el botón <strong>{{common_template_button}}</strong> "
                  "del formulario."),
            ("p", "Todas las plantillas imprimen la misma información (los datos de tu negocio, los del cliente, los artículos con su unidad y fecha, los totales, las notas y "
                  "los datos de pago), pero solo lo que hayas rellenado. Las facturas largas continúan en una segunda página, con los totales junto al último artículo."),
        ]),
        "free-vs-pro": ("Plan gratuito frente a Invoice Cove Pro", [
            ("p", "Invoice Cove es gratuito, con unos pocos límites razonables:"),
            ("ul", [
                "Hasta 3 facturas y 3 presupuestos generados por mes natural",
                "Hasta 3 clientes a la vez",
                "Los números de factura y presupuesto se asignan automáticamente y no se pueden editar",
                "La exportación a Excel, CSV y ZIP es solo de Pro",
                "La copia de seguridad y la restauración son solo de Pro",
            ]),
            ("p", "<strong>Invoice Cove Pro</strong> es una única compra a través de Google Play (no una suscripción) que elimina todos esos límites para siempre. "
                  "Los borradores, todas las plantillas e idiomas, el bloqueo de la aplicación y crear, previsualizar y compartir documentos son gratis para todos. "
                  "Consulta las <a href=\"terms.html\">Condiciones de uso</a> para todos los detalles."),
        ]),
    },
}
