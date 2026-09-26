T = {
    "title": "Guia do utilizador",
    "subtitle": "Tudo o que o Invoice Cove faz, ecrã a ecrã.",
    "meta_desc": "Guia do utilizador completo do Invoice Cove - Offline Billing.",
    "lang_label": "Idioma",
    "brand_alt": "Invoice Cove",
    "toc": "Índice",
    "footer_questions": "Dúvidas?",
    "lede": (
        "O Invoice Cove funciona inteiramente no seu dispositivo: faturas, orçamentos, clientes e o perfil do seu negócio ficam guardados localmente, "
        "e não em qualquer servidor do Invoice Cove. Não recolhemos, não vemos nem recebemos quaisquer dados sobre as suas faturas ou sobre a forma "
        "como usa a aplicação. Não há análise, não há rastreio, nada é enviado em segundo plano. "
        "A única vez que a própria aplicação precisa de ligação à internet é para processar a compra única do Invoice Cove Pro através do Google Play. "
        "Consulte a <a href=\"privacy.html\">Política de privacidade</a> para mais detalhes."
    ),
    "warn": (
        "Lembre-se! Antes de desinstalar a aplicação ou limpar o seu armazenamento: esses dados não são guardados por nós em lado nenhum. "
        "Desinstalar o Invoice Cove, ou limpar o seu armazenamento nas definições do Android, elimina definitivamente todas as faturas, orçamentos, clientes "
        "e definições deste dispositivo — não existe cópia na nuvem para restaurar. Para proteger os seus ficheiros: crie uma cópia de segurança "
        "com o Invoice Cove Pro (veja <a href=\"#backup\">Cópia de segurança e restauro</a>) ou exporte o que precisar para Excel, CSV ou ZIP "
        "(veja <a href=\"#export\">Exportar faturas</a>)."
    ),
    "sections": {
        "home": ("Ecrã inicial", [
            ("p", "O ecrã inicial é o seu ponto de partida, com um mosaico para cada ação principal: {{home_new_quote_title}}, "
                  "{{common_quotes_title}}, {{home_new_invoice_title}}, {{common_invoices_title}}, "
                  "{{home_new_customer_title}}, {{nav_customers}}, {{calendar_title}} e "
                  "{{common_reports_title}}. Toque num mosaico para ir diretamente para lá."),
            ("p", "A barra inferior dá-lhe acesso rápido a {{nav_home}}, {{nav_new}} (nova fatura), "
                  "{{nav_invoices}}, {{nav_customers}} e {{nav_reports}}."),
            ("p", "O ícone de roda dentada (⚙️) no canto superior direito da maioria dos ecrãs abre os <a href=\"#settings\">Dados do negócio e definições</a>."),
        ]),
        "customers": ("Clientes", [
            ("p", "Para adicionar um cliente, vá ao separador {{nav_customers}} e toque no ícone +, ou use o mosaico {{home_new_customer_title}}. "
                  "Também pode adicionar um ao criar uma fatura ou um orçamento. Para criar a ficha de um cliente basta o nome. "
                  "Os campos opcionais incluem: {{customers_form_customer_number_label}}, "
                  "{{common_field_email}}, {{common_field_phone}}, a morada, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} e um tom de cor para os documentos do cliente. Cada campo mostra um exemplo para saber o que preencher."),
            ("p", "Toque num cliente para o editar ({{common_edit}}), abrir o seu {{customers_view_history}} (faturas, orçamentos e rascunhos) "
                  "ou eliminá-lo ({{common_delete}})."),
            ("p", "Nas suas faturas e orçamentos, os dados do cliente são impressos por baixo do nome numa ordem fixa: número de cliente, número fiscal, número de IVA, "
                  "número do registo comercial e depois morada, e-mail e telefone. O que deixar em branco não é impresso."),
            ("note", "Aqui, guardar funciona de forma diferente das faturas. Um cliente tem o seu próprio botão {{customers_form_save_customer}} "
                     "(ou {{customers_form_save_changes}} ao editar) e fica guardado assim que lhe toca. Se tentar fechar o formulário "
                     "com alterações por guardar, o Invoice Cove pede primeiro confirmação."),
            ("note", "Eliminar um cliente não elimina as faturas e os orçamentos que já lhe emitiu. No entanto, os seus <a href=\"#drafts\">rascunhos</a> por terminar "
                     "são eliminados com ele; o Invoice Cove pede primeiro confirmação."),
        ]),
        "new-invoice": ("Criar uma fatura", [
            ("p", "Em {{nav_new}} (ou no mosaico {{home_new_invoice_title}}): escolha um cliente (ou crie um na hora) "
                  "e defina a data da fatura e a data de vencimento e depois adicione os artigos."),
            ("p", "Toque em {{newinvoice_add_item_details_button}} e preencha a descrição, a quantidade, o preço por unidade e, opcionalmente, uma unidade "
                  "(como h, un. ou kg) e uma data e hora. A unidade é impressa junto à quantidade no PDF. Toque no lápis (✏️) de um artigo para o corrigir "
                  "ou no caixote do lixo (🗑️) para o remover. As descrições e os preços que já usou são sugeridos enquanto escreve."),
            ("p", "Depois adicione, se necessário, uma taxa de imposto, um {{newinvoice_discount_label}} (percentagem ou valor fixo) e "
                  "{{common_notes_label}}. O número da fatura é atribuído por si (com o Invoice Cove Pro pode ser editado), e a moeda escolhe-se ao lado."),
            ("p", "{{common_preview_button}} gera um PDF temporário para ver como fica — ainda não se guarda nada. "
                  "O botão {{common_template_button}} mostra o modelo que será usado; toque nele para escolher outro apenas para este documento."),
            ("note", "{{newinvoice_generate_button}} faz três coisas ao mesmo tempo: guarda a fatura, cria o PDF e abre o menu de partilha "
                     "do dispositivo para a poder enviar. Ainda não está pronta? Use {{newinvoice_save_draft_button}} — veja <a href=\"#drafts\">Rascunhos</a>."),
        ]),
        "drafts": ("Rascunhos", [
            ("p", "Não perde uma fatura em que ainda está a trabalhar. Assim que escolher um cliente e adicionar pelo menos um artigo ou uma nota, o Invoice Cove "
                  "guarda um rascunho e atualiza-o pouco depois de parar de escrever, e mais uma vez quando sai da aplicação. Não há "
                  "a pergunta «descartar alterações?» ao sair do ecrã; uma mensagem curta avisa-o de que o rascunho foi guardado."),
            ("p", "Toque em {{newinvoice_save_draft_button}} (por baixo de {{newinvoice_generate_button}}) para pôr a fatura de lado de propósito: fica guardada e "
                  "o formulário é limpo, pronto para a fatura seguinte. Funciona assim que houver um cliente escolhido, mesmo antes de adicionar artigos."),
            ("p", "Encontre os seus rascunhos em {{nav_customers}} → o cliente → {{customers_view_history}} → "
                  "{{customers_history_drafts_title}}. Cada rascunho mostra quando foi editado pela última vez, quantos artigos tem e o total. Toque nele para continuar "
                  "a editar ou para gerar a fatura; toque no caixote do lixo para o eliminar."),
            ("ul", [
                "Um rascunho nunca usa um número de fatura e não conta para o limite mensal gratuito. O número só é atribuído quando gera a fatura "
                "final — o rascunho é então substituído por ela.",
                "Um rascunho só guarda a data da fatura e a data de vencimento se as tiver escolhido; caso contrário, ao reabri-lo usa a data de hoje.",
                "Eliminar um cliente também elimina os seus rascunhos (o Invoice Cove pergunta primeiro). Os rascunhos estão incluídos numa cópia de segurança.",
                "Os rascunhos existem para faturas; os orçamentos não os têm.",
            ]),
        ]),
        "invoices": ("Gerir faturas", [
            ("p", "O separador {{nav_invoices}} agrupa as suas faturas numa pasta por cliente, que pode ordenar por "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> ou <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Abra uma pasta para ver as suas faturas, ordenadas por data, valor, número ou estado."),
            ("p", "Cada fatura tem um estado: {{invoices_status_unpaid}}, {{invoices_status_overdue}} (passou o vencimento), "
                  "{{invoices_status_partially_paid}} (foi registado um sinal), {{invoices_status_paid}} ou "
                  "{{invoices_status_void}}. Toque numa fatura para a ver ({{common_view}}), reenviá-la ({{common_share}}), marcá-la como paga ou anulada, ou eliminá-la."),
            ("ul", [
                "{{invoices_action_mark_paid}} pede a data do pagamento e a forma como foi pago (transferência bancária, dinheiro, cartão, PayPal ou outra). "
                "Depois de paga, uma fatura já não pode voltar a não paga.",
                "{{deposit_record_title}} regista um pagamento adiantado. A fatura passa a aparecer como {{invoices_status_partially_paid}}, e o sinal não pode exceder o total.",
                "{{invoices_action_mark_void}} mantém a fatura nos seus registos mas marca-a como cancelada. É preferível a eliminar, porque uma fatura eliminada "
                "não pode ser recuperada.",
            ]),
            ("p", "Com o Pro, a pasta de um cliente também pode ser guardada ou partilhada como ZIP de PDF, e toda a lista pode ser exportada para o seu contabilista — veja "
                  "<a href=\"#export\">Exportar faturas</a>."),
        ]),
        "export": ("Exportar faturas (Excel, CSV, ZIP)", [
            ("p", "Disponível com o Invoice Cove Pro. Toque no ícone de exportação (📄) no topo do separador {{nav_invoices}}. Escolha as faturas a incluir "
                  "com os seletores de ano e mês ({{invoices_export_all}}, um ano ou um mês de um ano; só são oferecidos os anos e os meses "
                  "que têm faturas) e depois escolha o que fazer:"),
            ("ul", [
                "{{invoices_export_save_xlsx}} / {{invoices_export_share_xlsx}} — uma folha de cálculo Excel (.xlsx).",
                "{{invoices_export_save_csv}} / {{invoices_export_share_csv}} — a mesma tabela como ficheiro CSV.",
                "{{invoices_export_save_zip}} / {{invoices_export_share_zip}} — os PDF das faturas num ZIP, uma pasta por cliente.",
                "{{invoices_export_delete}} — elimina definitivamente as faturas selecionadas após duas confirmações.",
            ]),
            ("p", "<em>Guardar</em> deixa-o escolher onde no dispositivo fica o ficheiro; <em>Partilhar</em> abre o menu de partilha do Android para o enviar "
                  "por e-mail ou numa mensagem."),
            ("p", "O Excel e o CSV são feitos para o seu contabilista: por predefinição, uma linha por fatura, com número e datas, nome, número, "
                  "número fiscal, número de IVA, número do registo comercial e morada do cliente, subtotal, desconto, taxa de IVA, valor do IVA e total da "
                  "fatura, a moeda, e o estado, a data e o método de pagamento. Os cabeçalhos das colunas e as palavras fixas (fatura, paga, não paga, métodos "
                  "de pagamento) são escritos no idioma definido na aplicação."),
            ("p", "Para obter uma linha por artigo da fatura, com os dados da fatura repetidos em cada linha e a descrição, quantidade, unidade, "
                  "preço e valor líquido de cada artigo adicionados, ative {{invoices_export_detailed_toggle}}."),
        ]),
        "new-quote": ("Criar um orçamento", [
            ("p", "O mosaico {{home_new_quote_title}} funciona como o mosaico Nova fatura: os mesmos campos, os mesmos botões {{common_preview_button}} e {{common_template_button}}, o mesmo "
                  "{{newquote_generate_button}} que guarda, cria o PDF e abre o menu de partilha com um toque, mas com uma "
                  "{{newquote_date_label}} e uma data {{newquote_valid_until_label}} em vez da data da fatura e do vencimento."),
            ("p", "Os orçamentos não têm rascunhos."),
        ]),
        "quotes": ("Gerir orçamentos e convertê-los em fatura", [
            ("p", "O ecrã {{common_quotes_title}} (a partir do mosaico do ecrã inicial) lista os seus orçamentos por cliente, tal como as faturas. Abra um orçamento para "
                  "o ver ou partilhar, use {{quotes_action_accept}} ou {{quotes_action_decline}} quando o cliente responder, "
                  "registe um sinal ou elimine-o. O sinal não pode exceder o total do orçamento."),
            ("p", "Quando um cliente aceita um orçamento, use {{quotes_action_convert_to_invoice}} para transformar as linhas marcadas numa fatura real, "
                  "editável de forma independente. O vencimento e o desconto ainda se podem ajustar, e o orçamento original fica marcado como "
                  "{{quotes_status_converted}} e guardado nos seus registos."),
        ]),
        "calendar": ("Calendário e lembretes", [
            ("p", "O ecrã {{calendar_title}} é uma vista mensal para as suas notas. Toque num dia para ver ou adicionar notas; uma nota tem um título e um texto e, "
                  "com {{calendar_remind_me}} e uma hora, envia-lhe uma notificação na data e hora definidas. O primeiro dia da semana segue as suas definições."),
            ("p", "À parte, o Invoice Cove envia lembretes de pagamento — notificações locais para faturas que vencem em breve ou estão vencidas. Nada é enviado para um servidor nem recebido de um."),
        ]),
        "reports": ("Relatórios", [
            ("p", "{{common_reports_title}} dá-lhe uma visão rápida: os valores {{reports_stat_revenue}}, "
                  "{{reports_stat_outstanding}} e {{reports_stat_overdue}}, quantas faturas tem, "
                  "<em>{{reports_revenue_by_month}}</em> e os seus <em>{{reports_top_customers}}</em> por total faturado."),
            ("p", "Toque no cartão {{reports_stat_outstanding}} ou {{reports_stat_overdue}} para abrir a lista exata dessas faturas."),
        ]),
        "settings": ("Dados do negócio e definições", [
            ("p", "Abra as definições a partir do ícone de roda dentada; este ecrã chama-se {{settings_title}}. Começa pelas suas preferências opcionais: "
                  "{{settings_appearance_label}} ({{settings_theme_light}} ou {{settings_theme_dark}}), "
                  "{{settings_invoice_template_label}} predefinido, {{settings_tax_label_label}} (IVA, GST…), "
                  "{{settings_first_day_of_week_label}} e {{settings_due_date_default_label}}, que preenche o vencimento automaticamente (por exemplo Net 30). "
                  "Por baixo seguem-se {{settings_security_label}} (veja <a href=\"#app-lock\">Bloqueio da aplicação</a>), "
                  "{{settings_item_suggestions_label}} e {{settings_backup_restore_label}} (veja <a href=\"#backup\">Cópia de segurança e restauro</a>)."),
            ("p", "{{settings_item_memory_title}} memoriza descrições e preços dos artigos para os sugerir enquanto escreve; <em>{{common_clear}}</em> esquece-os "
                  "sem tocar nas suas faturas."),
            ("p", "Mais abaixo está o perfil do seu negócio, impresso em cada fatura e orçamento: {{settings_business_name_label}}, "
                  "{{settings_your_name_label}}, um lema curto ({{settings_business_location_label}}), {{common_field_email}}, "
                  "{{common_field_phone}}, o {{settings_date_format_label}} das datas, a morada, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, {{common_field_registration_info}} (número de registo, capital social e semelhantes), o seu "
                  "{{settings_business_logo_label}} e os seus {{settings_payment_details_label}} (IBAN, ligação PayPal.me). Cada campo "
                  "tem um exemplo, e qualquer campo que deixe em branco não aparece nas suas faturas. Toque em {{common_done}} quando "
                  "tiver terminado; se sair com alterações por guardar, é-lhe pedida confirmação."),
            ("p", "No fim são apresentados este {{settings_user_manual}} e {{settings_share_this_app}}."),
        ]),
        "backup": ("Cópia de segurança e restauro", [
            ("p", "Disponível com o Invoice Cove Pro, em {{settings_backup_restore_label}}. {{settings_create_backup_title}} guarda "
                  "tudo: faturas, orçamentos, rascunhos, clientes, calendário, definições, o seu logótipo e os PDF, tudo num único ficheiro. Escolha "
                  "{{backup_save_button}} para o guardar onde quiser, ou {{backup_share_button}} para o enviar para um local seguro."),
            ("p", "{{settings_restore_backup_title}} traz tudo de volta, caso precise de passar para um telemóvel novo. Só funciona numa instalação nova, antes de ter "
                  "adicionado dados, pelo que nunca pode substituir o que já tem. O Invoice Cove verifica se o ficheiro está intacto e avisa se estiver danificado, "
                  "se não for uma cópia do Invoice Cove ou se tiver sido feito por uma versão mais recente da aplicação (atualize primeiro)."),
            ("note", "Um ficheiro de cópia de segurança não está cifrado: quem o tiver pode ler os seus dados. Guarde-o num local privado. O PIN de bloqueio da aplicação nunca "
                     "está incluído."),
        ]),
        "app-lock": ("Bloqueio da aplicação", [
            ("p", "Em {{settings_security_label}} pode ativar o {{settings_app_lock_title}}: o Invoice Cove pede então o seu PIN "
                  "(ou a sua impressão digital) quando a aplicação é aberta de novo de raiz ou depois de reiniciar o telemóvel — não sempre que volta a ela."),
            ("ul", [
                "{{settings_set_pin}}: escolha um PIN de 4 dígitos e confirme-o.",
                "Recebe depois um código de recuperação de 6 dígitos, mostrado apenas uma vez. Anote-o e guarde-o num local seguro.",
                "Se o seu telemóvel o permitir, desbloqueie com a impressão digital ({{security_use_fingerprint}}).",
                "Esqueceu-se do PIN? Use {{security_forgot_pin}} e introduza o código de recuperação. Após 5 tentativas erradas tem de esperar 30 segundos – "
                "a espera aumenta com mais tentativas erradas.",
            ]),
            ("note", "Se perder o PIN e o código de recuperação e não tiver configurado o desbloqueio por impressão digital, não há forma de voltar a entrar. Não o podemos repor "
                     "por si."),
        ]),
        "languages": ("Idiomas", [
            ("p", "O Invoice Cove fala 13 idiomas: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands e Svenska. Toque no ícone redondo com a bandeira no topo das definições para mudar — a aplicação muda de imediato."),
            ("p", "O texto dos seus PDF e das exportações Excel/CSV segue o idioma definido na aplicação, e este guia está disponível nos mesmos 13 idiomas "
                  "(use a barra de idiomas no topo da página)."),
        ]),
        "templates": ("Modelos PDF", [
            ("p", "O Invoice Cove oferece, por agora, 18 modelos de PDF: Classic, Client Color (com o tom da cor do cliente), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves e Spooky Hollow."),
            ("p", "Escolha o modelo predefinido em Definições → {{settings_invoice_template_label}}: toque num modelo e depois em {{common_done}}. Aplica-se "
                  "a tudo o que gerar a partir daí. Para uma só fatura ou orçamento, use o botão {{common_template_button}} "
                  "do formulário."),
            ("p", "Todos os modelos imprimem a mesma informação: os dados do seu negócio, os do cliente, os artigos com a sua unidade e data, os totais, as notas e "
                  "os dados de pagamento — mas apenas o que preencheu. As faturas longas continuam numa segunda página, com os totais juntos ao último artigo."),
        ]),
        "free-vs-pro": ("Plano gratuito versus Invoice Cove Pro", [
            ("p", "O Invoice Cove é gratuito, com alguns limites razoáveis:"),
            ("ul", [
                "Até 3 faturas geradas por mês civil",
                "Até 3 orçamentos gerados por mês civil",
                "Até 3 clientes de cada vez",
                "Os números das faturas e dos orçamentos são atribuídos automaticamente e não se podem editar",
                "A exportação para Excel, CSV e ZIP é exclusiva do Pro",
                "A cópia de segurança e o restauro são exclusivos do Pro",
            ]),
            ("p", "O Invoice Cove Pro é uma única compra através do Google Play (não uma subscrição) que remove todos estes limites para sempre. "
                  "Os rascunhos, todos os modelos e idiomas, o bloqueio da aplicação e a criação, pré-visualização e partilha de documentos são gratuitos para todos. "
                  "Consulte os <a href=\"terms.html\">Termos de utilização</a> para todos os detalhes."),
        ]),
    },
}
