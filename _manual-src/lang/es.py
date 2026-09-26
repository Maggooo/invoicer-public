T = {
    "title": "Guía de usuario",
    "subtitle": "Todo lo que Invoice Cove puede hacer, pantalla por pantalla.",
    "meta_desc": "Guía de usuario completa de Invoice Cove - Offline Billing.",
    "lang_label": "Idioma",
    "brand_alt": "Invoice Cove",
    "toc": "Contenido",
    "footer_questions": "¿Preguntas?",
    "lede": (
        "Invoice Cove funciona por completo en tu dispositivo: las facturas, los presupuestos, los clientes y el perfil de tu negocio se guardan localmente, "
        "no en ningún servidor de Invoice Cove. No recopilamos, vemos ni recibimos ningún dato sobre tus facturas ni sobre cómo usas la aplicación. "
        "No hay analítica, ni seguimiento, ni se envía nada en segundo plano. "
        "La única vez que la propia aplicación necesita conexión a internet es para procesar la compra única de Invoice Cove Pro a través de Google Play. "
        "Consulta la <a href=\"privacy.html\">Política de privacidad</a> para más detalles."
    ),
    "warn": (
        "¡Recuerda! Antes de desinstalar la aplicación o borrar su almacenamiento: nosotros no guardamos una copia de esos datos en ningún sitio. "
        "Desinstalar Invoice Cove, o borrar su almacenamiento desde los ajustes de Android, elimina para siempre todas las facturas, presupuestos, clientes "
        "y ajustes de este dispositivo: no hay copia en la nube desde la que restaurar. Para proteger tus archivos: crea una copia de seguridad "
        "con Invoice Cove Pro (consulta <a href=\"#backup\">Copia de seguridad y restauración</a>) o exporta lo que necesites a Excel, CSV o ZIP "
        "(consulta <a href=\"#export\">Exportar facturas</a>)."
    ),
    "sections": {
        "home": ("Pantalla de inicio", [
            ("p", "La pantalla de inicio es tu punto de partida, con un icono para cada acción principal: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} y "
                  "{{common_reports_title}}. Toca cualquiera para ir directamente."),
            ("p", "La barra inferior te da acceso rápido a {{nav_home}}, {{nav_new}} (factura nueva), "
                  "{{nav_invoices}}, {{nav_customers}} y {{nav_reports}}."),
            ("p", "El icono de engranaje (⚙️) de la esquina superior derecha de la mayoría de las pantallas abre los <a href=\"#settings\">Datos del negocio y ajustes</a>."),
        ]),
        "customers": ("Clientes", [
            ("p", "Para añadir un cliente, ve a la pestaña {{nav_customers}} y toca el icono +, o usa el icono {{home_new_customer_title}}. "
                  "También puedes añadir uno al crear una factura o un presupuesto. Solo hace falta el nombre para crear la ficha de un cliente. "
                  "Los campos opcionales incluyen: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, la dirección, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} y un tono de color para sus documentos. Cada campo muestra un ejemplo para que sepas qué escribir."),
            ("p", "Toca un cliente para editarlo ({{common_edit}}), abrir su {{customers_view_history}} (facturas, presupuestos y borradores) "
                  "o eliminarlo ({{common_delete}})."),
            ("p", "En tus facturas y presupuestos, los datos del cliente se imprimen bajo su nombre en un orden fijo: número de cliente, identificación fiscal, número de IVA, "
                  "número del registro mercantil y después dirección, correo electrónico y teléfono. Lo que dejes vacío no se imprime."),
            ("note", "Guardar funciona aquí de otra manera que en las facturas. Un cliente tiene su propio botón {{customers_form_save_customer}} "
                     "(o {{customers_form_save_changes}} al editar) y se guarda en cuanto lo tocas. Si intentas cerrar el formulario "
                     "con cambios sin guardar, Invoice Cove te pide confirmación antes."),
            ("note", "Eliminar un cliente no elimina las facturas y presupuestos que ya le hayas emitido. Sin embargo, sus <a href=\"#drafts\">borradores</a> sin terminar "
                     "se eliminan con él; Invoice Cove te pide confirmación antes."),
        ]),
        "new-invoice": ("Crear una factura", [
            ("p", "Desde {{nav_new}} (o el icono {{home_new_invoice_title}}): elige un cliente (o crea uno en el momento) "
                  "e indica la fecha de la factura y la fecha de vencimiento, y añade tus artículos."),
            ("p", "Toca {{newinvoice_add_item_details_button}} y rellena la descripción, la cantidad, el precio por unidad y, si quieres, una unidad "
                  "(como h, uds. o kg) y una fecha y hora. La unidad se imprime junto a la cantidad en el PDF. Toca el lápiz (✏️) de un artículo para corregirlo "
                  "o la papelera (🗑️) para quitarlo. Las descripciones y precios que ya usaste se sugieren mientras escribes."),
            ("p", "Después añade, si es necesario, un tipo de impuesto, un {{newinvoice_discount_label}} (porcentaje o importe fijo) y "
                  "{{common_notes_label}}. El número de factura se asigna solo (con Invoice Cove Pro se puede editar), y la moneda se elige a su lado."),
            ("p", "{{common_preview_button}} genera un PDF temporal para que veas cómo queda; todavía no se guarda nada. "
                  "El botón {{common_template_button}} muestra qué plantilla se usará; tócalo para elegir otra solo para este documento."),
            ("note", "{{newinvoice_generate_button}} hace tres cosas a la vez: guarda la factura, crea el PDF y abre el menú de compartir "
                     "de tu dispositivo para enviarla. ¿Aún no está lista? Usa {{newinvoice_save_draft_button}}; consulta <a href=\"#drafts\">Borradores</a>."),
        ]),
        "drafts": ("Borradores", [
            ("p", "No pierdes una factura en la que todavía trabajas. En cuanto has elegido un cliente y añadido al menos un artículo o una nota, Invoice Cove "
                  "guarda un borrador y lo actualiza un momento después de que dejes de escribir, y una vez más cuando sales de la aplicación. No hay "
                  "pregunta de «¿descartar los cambios?» al salir de la pantalla; un mensaje breve te avisa de que el borrador se guardó."),
            ("p", "Toca {{newinvoice_save_draft_button}} (bajo {{newinvoice_generate_button}}) para apartar la factura a propósito: se guarda y "
                  "el formulario se vacía, listo para la siguiente. Funciona en cuanto hay un cliente elegido, incluso antes de añadir artículos."),
            ("p", "Encuentra tus borradores en {{nav_customers}} → el cliente → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Cada borrador muestra cuándo se editó por última vez, cuántos artículos tiene y su total. Tócalo para seguir "
                  "editándolo o para generar la factura; toca la papelera para eliminarlo."),
            ("ul", [
                "Un borrador nunca usa un número de factura y no cuenta para el límite mensual gratuito. El número solo se asigna cuando generas la factura "
                "final, y el borrador queda sustituido por ella.",
                "Un borrador conserva la fecha de factura y la de vencimiento solo si las elegiste tú; si no, al reabrirlo usa la fecha de hoy.",
                "Eliminar un cliente también elimina sus borradores (Invoice Cove te lo pregunta antes). Los borradores se incluyen en una copia de seguridad.",
                "Los borradores existen para las facturas; los presupuestos no los tienen.",
            ]),
        ]),
        "invoices": ("Gestionar facturas", [
            ("p", "La pestaña {{nav_invoices}} agrupa tus facturas en una carpeta por cliente, que puedes ordenar por "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> o <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Abre una carpeta para ver sus facturas, ordenadas por fecha, valor, número o estado."),
            ("p", "Cada factura tiene un estado: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (pasó su vencimiento), "
                  "{{invoices_status_partially_paid}} (se registró un anticipo), {{invoices_status_paid}} o "
                  "{{invoices_status_void}}. Toca una factura para verla ({{common_view}}), volver a enviarla ({{common_share}}), marcarla como pagada o anulada, o eliminarla."),
            ("ul", [
                "{{invoices_action_mark_paid}} pide la fecha del pago y cómo se pagó (transferencia bancaria, efectivo, tarjeta, PayPal u otro). "
                "Una factura pagada ya no puede volver a no pagada.",
                "{{deposit_record_title}} anota un pago adelantado. La factura aparece entonces como {{invoices_status_partially_paid}}, y el anticipo no puede superar el total.",
                "{{invoices_action_mark_void}} conserva la factura en tus registros pero la marca como cancelada. Es preferible a eliminarla, ya que una factura eliminada "
                "no se puede recuperar.",
            ]),
            ("p", "Con Pro, la carpeta de un cliente también se puede guardar o compartir como ZIP de PDF, y toda la lista se puede exportar para tu contable; consulta "
                  "<a href=\"#export\">Exportar facturas</a>."),
        ]),
        "export": ("Exportar facturas (Excel, CSV, ZIP)", [
            ("p", "Disponible con Invoice Cove Pro. Toca el icono de exportar (📄) en la parte superior de la pestaña {{nav_invoices}}. Elige qué facturas incluir "
                  "con los selectores de año y mes ({{invoices_export_all}}, un año o un mes de un año; solo se ofrecen los años y meses que "
                  "tienen facturas) y después elige qué hacer:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}}: una hoja de cálculo de Excel (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}}: la misma tabla como archivo CSV.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}}: los PDF de las facturas en un ZIP, una carpeta por cliente.",
                "{{invoices_export_delete}}: elimina para siempre las facturas seleccionadas tras dos confirmaciones.",
            ]),
            ("p", "<em>Guardar</em> te deja elegir en qué lugar del dispositivo queda el archivo; <em>Compartir</em> abre el menú de compartir de Android para enviarlo "
                  "por correo o en un mensaje."),
            ("p", "Excel y CSV están pensados para tu contable: por defecto, una fila por factura, con número y fechas, nombre, número, "
                  "identificación fiscal, número de IVA, número del registro mercantil y dirección del cliente, subtotal, descuento, tipo de IVA, importe de "
                  "IVA y total de la factura, la moneda y el estado, la fecha y el método de pago. Los encabezados de columna y las palabras fijas (factura, "
                  "pagada, sin pagar, métodos de pago) se escriben en el idioma configurado en la aplicación."),
            ("p", "Para obtener una fila por cada artículo de la factura, con los datos de la factura repetidos en cada fila y la descripción, cantidad, "
                  "unidad, precio e importe neto de cada artículo añadidos, activa {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Crear un presupuesto", [
            ("p", "El icono {{home_new_quote_title}} funciona como el icono Nueva factura: los mismos campos, los mismos botones {{common_preview_button}} y {{common_template_button}}, el mismo "
                  "{{newquote_generate_button}} que guarda, crea el PDF y abre el menú de compartir con un toque, pero con una "
                  "{{newquote_date_label}} y una fecha {{newquote_valid_until_label}} en lugar de la fecha de factura y el vencimiento."),
            ("p", "Los presupuestos no tienen borradores."),
        ]),
        "quotes": ("Gestionar presupuestos y convertirlos en factura", [
            ("p", "La pantalla {{common_quotes_title}} (desde el icono de inicio) lista tus presupuestos por cliente, igual que las facturas. Abre un presupuesto para "
                  "verlo o compartirlo, usa {{quotes_action_accept}} o {{quotes_action_decline}} cuando el cliente responda, "
                  "registra un anticipo o elimínalo. El anticipo no puede superar el total del presupuesto."),
            ("p", "Cuando un cliente acepta un presupuesto, usa {{quotes_action_convert_to_invoice}} para convertir las líneas marcadas en una factura real, "
                  "editable de forma independiente. El vencimiento y el descuento aún se pueden ajustar, y el presupuesto original se marca como "
                  "{{quotes_status_converted}} y se conserva en tus registros."),
        ]),
        "calendar": ("Calendario y recordatorios", [
            ("p", "La pantalla {{calendar_title}} es una vista mensual para tus propias notas. Toca un día para ver o añadir notas; una nota tiene título y texto y, "
                  "con {{calendar_remind_me}} y una hora, te envía una notificación en la fecha y hora indicadas. El primer día de la semana sigue tus ajustes."),
            ("p", "Aparte, Invoice Cove envía recordatorios de pago: notificaciones locales de facturas que vencen pronto o están vencidas. No se envía nada hacia ni desde ningún servidor."),
        ]),
        "reports": ("Informes", [
            ("p", "{{common_reports_title}} te da una visión rápida: los importes {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} y {{reports_stat_overdue}}, cuántas facturas tienes, "
                  "<em>{{reports_revenue_by_month}}</em> y tus <em>{{reports_top_customers}}</em> por total facturado."),
            ("p", "Toca la tarjeta {{reports_stat_outstanding}} o {{reports_stat_overdue}} para abrir la lista exacta de esas facturas."),
        ]),
        "settings": ("Datos del negocio y ajustes", [
            ("p", "Abre los ajustes desde el icono de engranaje; esta pantalla se llama {{settings_title}}. Empieza con tus preferencias opcionales: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} u {{settings_theme_dark}}), la "
                  "{{settings_invoice_template_label}} predeterminada, la {{settings_tax_label_label}} (IVA, GST…), "
                  "el {{settings_first_day_of_week_label}} y el {{settings_due_date_default_label}}, que rellena el vencimiento automáticamente (p. ej. Net 30). "
                  "Debajo vienen {{settings_security_label}} (consulta <a href=\"#app-lock\">Bloqueo de la aplicación</a>), "
                  "{{settings_item_suggestions_label}} y {{settings_backup_restore_label}} (consulta <a href=\"#backup\">Copia de seguridad y restauración</a>)."),
            ("p", "{{settings_item_memory_title}} recuerda descripciones y precios de artículos para sugerirlos mientras escribes; <em>{{common_clear}}</em> los olvida "
                  "sin tocar tus facturas."),
            ("p", "Más abajo está el perfil de tu negocio, que se imprime en cada factura y presupuesto: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, un lema breve ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, el {{settings_date_format_label}} de las fechas, la dirección, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (número de registro, capital social y similares), tu "
                  "{{settings_business_logo_label}} y tus {{settings_payment_details_label}} (IBAN, enlace de PayPal.me). Cada campo "
                  "tiene un ejemplo, y cualquier campo que dejes vacío no aparece en tus facturas. Toca {{common_done}} cuando "
                  "hayas terminado; si sales con cambios sin guardar, se te pide confirmación."),
            ("p", "Al final del todo se muestran esta {{settings_user_manual}} y {{settings_share_this_app}}."),
        ]),
        "backup": ("Copia de seguridad y restauración", [
            ("p", "Disponible con Invoice Cove Pro, en {{settings_backup_restore_label}}. {{settings_create_backup_title}} guarda "
                  "todo: facturas, presupuestos, borradores, clientes, calendario, ajustes, tu logotipo y los PDF, todo en un solo archivo. Elige "
                  "{{backup_save_button}} para guardarlo donde quieras, o {{backup_share_button}} para enviarlo a un lugar seguro."),
            ("p", "{{settings_restore_backup_title}} lo devuelve todo, por si necesitas pasar tus datos a un teléfono nuevo. Solo funciona en una instalación nueva, antes de que hayas "
                  "añadido datos, así que nunca puede sobrescribir lo que ya tienes. Invoice Cove comprueba que el archivo esté intacto y te avisa si está dañado, "
                  "si no es una copia de Invoice Cove o si la hizo una versión más reciente de la aplicación (actualiza primero)."),
            ("note", "Un archivo de copia de seguridad no está cifrado: quien lo tenga puede leer tus datos. Guárdalo en un lugar privado. El PIN de bloqueo de la aplicación no "
                     "se incluye nunca."),
        ]),
        "app-lock": ("Bloqueo de la aplicación", [
            ("p", "En {{settings_security_label}} puedes activar {{settings_app_lock_title}}: Invoice Cove te pedirá entonces tu PIN "
                  "(o tu huella) cuando la aplicación se abra de nuevo desde cero o tras reiniciar el teléfono, no cada vez que vuelvas a ella."),
            ("ul", [
                "{{settings_set_pin}}: elige un PIN de 4 dígitos y confírmalo.",
                "Después recibes un código de recuperación de 6 dígitos, que se muestra una sola vez. Anótalo y guárdalo en un lugar seguro.",
                "Si tu teléfono lo admite, desbloquea con tu huella ({{security_use_fingerprint}}).",
                "¿Olvidaste el PIN? Usa {{security_forgot_pin}} e introduce el código de recuperación. Tras 5 intentos erróneos debes esperar 30 segundos – "
                "la espera aumenta con más intentos erróneos.",
            ]),
            ("note", "Si pierdes tanto el PIN como el código de recuperación y no has configurado el desbloqueo con huella, no hay forma de volver a entrar. No podemos restablecerlo "
                     "por ti."),
        ]),
        "languages": ("Idiomas", [
            ("p", "Invoice Cove habla 13 idiomas: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands y Svenska. Toca el icono redondo con la bandera en la parte superior de los ajustes para cambiar; la aplicación cambia al instante."),
            ("p", "El texto de tus PDF y de las exportaciones a Excel/CSV sigue el idioma configurado en la aplicación, y esta guía está disponible en los mismos 13 idiomas "
                  "(usa la barra de idiomas de la parte superior de la página)."),
        ]),
        "templates": ("Plantillas PDF", [
            ("p", "Invoice Cove ofrece por ahora 18 diseños de PDF: Classic, Client Color (teñido con el color del cliente), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves y Spooky Hollow."),
            ("p", "Elige tu plantilla predeterminada en Ajustes → {{settings_invoice_template_label}}: toca un diseño y después {{common_done}}. Se "
                  "aplica a todo lo que generes a partir de ese momento. Para una sola factura o presupuesto, usa el botón {{common_template_button}} "
                  "del formulario."),
            ("p", "Todas las plantillas imprimen la misma información (los datos de tu negocio, los del cliente, los artículos con su unidad y fecha, los totales, las notas y "
                  "los datos de pago), pero solo lo que hayas rellenado. Las facturas largas continúan en una segunda página, con los totales junto al último artículo."),
        ]),
        "free-vs-pro": ("Plan gratuito frente a Invoice Cove Pro", [
            ("p", "Invoice Cove es gratuito, con unos pocos límites razonables:"),
            ("ul", [
                "Hasta 3 facturas generadas por mes natural",
                "Hasta 3 presupuestos generados por mes natural",
                "Hasta 3 clientes a la vez",
                "Los números de factura y presupuesto se asignan automáticamente y no se pueden editar",
                "La exportación a Excel, CSV y ZIP es solo de Pro",
                "La copia de seguridad y la restauración son solo de Pro",
            ]),
            ("p", "Invoice Cove Pro es una única compra a través de Google Play (no una suscripción) que elimina todos esos límites para siempre. "
                  "Los borradores, todas las plantillas e idiomas, el bloqueo de la aplicación y crear, previsualizar y compartir documentos son gratis para todos. "
                  "Consulta las <a href=\"terms.html\">Condiciones de uso</a> para todos los detalles."),
        ]),
    },
}
