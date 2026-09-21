T = {
    "title": "Manual do utilizador",
    "subtitle": "Tudo o que o Invoice Cove faz, ecrã a ecrã.",
    "meta_desc": "Manual do utilizador completo do Invoice Cove - Offline Billing.",
    "lang_label": "Idioma",
    "brand_alt": "Invoice Cove",
    "toc": "Índice",
    "footer_questions": "Dúvidas?",
    "lede": (
        "O Invoice Cove funciona inteiramente no seu dispositivo — faturas, orçamentos, clientes e o perfil do seu negócio ficam guardados localmente, "
        "e não em qualquer servidor do Invoice Cove. <strong>Não recolhemos, não vemos nem recebemos quaisquer dados sobre as suas faturas ou sobre a forma "
        "como usa a aplicação</strong> — não há análise, não há rastreio, nada é enviado em segundo plano. "
        "A única vez que a própria aplicação precisa de ligação à internet é para processar a compra única do Invoice Cove Pro através do Google Play. "
        "Consulte a <a href=\"privacy.html\">Política de privacidade</a> para mais detalhes."
    ),
    "warn": (
        "<strong>Antes de desinstalar a aplicação ou limpar o seu armazenamento:</strong> esses dados não são guardados por nós em lado nenhum. "
        "Desinstalar o Invoice Cove, ou limpar o seu armazenamento nas definições do Android, elimina definitivamente todas as faturas, orçamentos, clientes "
        "e definições deste dispositivo — não existe cópia na nuvem para restaurar. Proteja-se: crie uma cópia de segurança "
        "com o Invoice Cove Pro (veja <a href=\"#backup\">Cópia de segurança e restauro</a>) ou exporte o que precisar para Excel, CSV ou ZIP "
        "(veja <a href=\"#export\">Exportar faturas</a>)."
    ),
    "sections": {
        "home": ("Ecrã inicial", [
            ("p", "O ecrã inicial é o seu ponto de partida, com um mosaico para cada ação principal: <strong>{{home_new_quote_title}}</strong>, "
                  "<strong>{{common_quotes_title}}</strong>, <strong>{{home_new_invoice_title}}</strong>, <strong>{{common_invoices_title}}</strong>, "
                  "<strong>{{home_new_customer_title}}</strong>, <strong>{{nav_customers}}</strong>, <strong>{{calendar_title}}</strong> e "
                  "<strong>{{common_reports_title}}</strong>. Toque num mosaico para ir diretamente para lá."),
            ("p", "A barra inferior dá-lhe sempre acesso rápido a <strong>{{nav_home}}</strong>, <strong>{{nav_new}}</strong> (uma nova fatura), "
                  "<strong>{{nav_invoices}}</strong>, <strong>{{nav_customers}}</strong> e <strong>{{nav_reports}}</strong>."),
            ("p", "O ícone de roda dentada (⚙️) no canto superior direito da maioria dos ecrãs abre os <a href=\"#settings\">Dados do negócio e definições</a>."),
        ]),
        "customers": ("Clientes", [
            ("p", "Adicione um cliente no separador <strong>{{nav_customers}}</strong> (toque no ícone +), com o mosaico <strong>{{home_new_customer_title}}</strong> "
                  "ou diretamente ao criar uma fatura ou um orçamento. Só o nome é obrigatório. Campos opcionais: <strong>{{customers_form_customer_number_label}}</strong>, "
                  "{{common_field_email}}, {{common_field_phone}}, a morada, {{common_field_tax_id}}, {{common_field_vat_number}}, "
                  "{{common_field_trade_register}} e uma cor que dá o tom aos documentos do cliente. Cada campo mostra um exemplo para saber o que preencher."),
            ("p", "Toque num cliente para o editar (<strong>{{common_edit}}</strong>), abrir o seu <strong>{{customers_view_history}}</strong> (faturas, orçamentos e rascunhos) "
                  "ou eliminá-lo (<strong>{{common_delete}}</strong>)."),
            ("p", "Nas suas faturas e orçamentos, os dados do cliente são impressos por baixo do nome numa ordem fixa: número de cliente, número fiscal, número de IVA, "
                  "número do registo comercial e depois morada, e-mail e telefone. O que deixar em branco simplesmente não é impresso."),
            ("note", "<strong>Aqui, guardar funciona de forma diferente das faturas.</strong> Um cliente tem o seu próprio botão <strong>{{customers_form_save_customer}}</strong> "
                     "(ou <strong>{{customers_form_save_changes}}</strong> ao editar) — fica guardado assim que lhe toca. Se tentar fechar o formulário "
                     "com alterações por guardar, o Invoice Cove pede primeiro confirmação."),
            ("note", "Eliminar um cliente não elimina as faturas e os orçamentos que já lhe emitiu. Os seus <a href=\"#drafts\">rascunhos</a> por terminar "
                     "são eliminados com ele — é perguntado primeiro."),
        ]),
        "new-invoice": ("Criar uma fatura", [
            ("p", "Em <strong>{{nav_new}}</strong> (ou no mosaico <strong>{{home_new_invoice_title}}</strong>): escolha um cliente — ou crie um na hora — "
                  "defina a data da fatura e a data de vencimento e depois adicione os artigos."),
            ("p", "Toque em <strong>{{newinvoice_add_item_details_button}}</strong> e preencha a descrição, a quantidade, o preço por unidade e, opcionalmente, uma unidade "
                  "(como h, un. ou kg) e uma data e hora. A unidade é impressa junto à quantidade no PDF. Toque no lápis (✏️) de um artigo para o corrigir "
                  "ou no caixote do lixo (🗑️) para o remover. As descrições e os preços que já usou são sugeridos enquanto escreve."),
            ("p", "Depois adicione, se precisar, uma taxa de imposto, um <strong>{{newinvoice_discount_label}}</strong> (percentagem ou valor fixo) e "
                  "<strong>{{common_notes_label}}</strong>. O número da fatura é atribuído por si (com o Pro pode editá-lo); a moeda escolhe-se ao lado."),
            ("p", "<strong>{{common_preview_button}}</strong> gera um PDF temporário para ver como fica — ainda não se guarda nada. "
                  "O botão <strong>{{common_template_button}}</strong> mostra o modelo que será usado; toque nele para escolher outro apenas para este documento."),
            ("note", "<strong>{{newinvoice_generate_button}}</strong> faz três coisas ao mesmo tempo: guarda a fatura, cria o PDF e abre o menu de partilha "
                     "do dispositivo para a poder enviar. Ainda não está pronta? Use <strong>{{newinvoice_save_draft_button}}</strong> — veja <a href=\"#drafts\">Rascunhos</a>."),
        ]),
        "drafts": ("Rascunhos", [
            ("p", "Não perde uma fatura em que ainda está a trabalhar. Assim que escolher um cliente e adicionar pelo menos um artigo ou uma nota, o Invoice Cove "
                  "guarda um <strong>rascunho</strong> e atualiza-o pouco depois de parar de escrever — e mais uma vez quando sai da aplicação. Não há "
                  "a pergunta «descartar alterações?» ao sair do ecrã; uma mensagem curta avisa-o de que o rascunho foi guardado."),
            ("p", "Toque em <strong>{{newinvoice_save_draft_button}}</strong> (por baixo de {{newinvoice_generate_button}}) para pôr a fatura de lado de propósito: fica guardada e "
                  "o formulário é limpo, pronto para a fatura seguinte. Funciona assim que houver um cliente escolhido, mesmo antes de adicionar artigos."),
            ("p", "Encontre os seus rascunhos em <strong>{{nav_customers}}</strong> → o cliente → <strong>{{customers_view_history}}</strong> → "
                  "<strong>{{customers_history_drafts_title}}</strong>. Cada rascunho mostra quando foi editado pela última vez, quantos artigos tem e o total. Toque nele para continuar "
                  "a editar ou para gerar a fatura; toque no caixote do lixo para o eliminar."),
            ("ul", [
                "Um rascunho nunca usa um número de fatura e não conta para o limite mensal gratuito. O número só é atribuído quando gera a fatura "
                "final — o rascunho é então substituído por ela.",
                "Um rascunho só guarda a data da fatura e a data de vencimento se as tiver escolhido; caso contrário, ao reabri-lo usa a data de hoje.",
                "Eliminar um cliente também elimina os seus rascunhos (é perguntado primeiro). Os rascunhos estão incluídos numa cópia de segurança.",
                "Os rascunhos existem para faturas; os orçamentos não os têm.",
            ]),
        ]),
        "invoices": ("Gerir faturas", [
            ("p", "O separador <strong>{{nav_invoices}}</strong> agrupa as suas faturas numa pasta por cliente, que pode ordenar por "
                  "<em>{{invoices_folder_sort_last_invoiced}}</em>, <em>{{invoices_folder_sort_alphabetical}}</em> ou <em>{{invoices_folder_sort_invoice_count}}</em>. "
                  "Abra uma pasta para ver as suas faturas, ordenadas por data, valor, número ou estado."),
            ("p", "Cada fatura tem um estado: <strong>{{invoices_status_unpaid}}</strong>, <strong>{{invoices_status_overdue}}</strong> (passou o vencimento), "
                  "<strong>{{invoices_status_partially_paid}}</strong> (foi registado um sinal), <strong>{{invoices_status_paid}}</strong> ou "
                  "<strong>{{invoices_status_void}}</strong>. Toque numa fatura para a ver ({{common_view}}), reenviá-la ({{common_share}}), marcá-la como paga ou anulada, ou eliminá-la."),
            ("ul", [
                "<strong>{{invoices_action_mark_paid}}</strong> pede a data do pagamento e a forma como foi pago (transferência bancária, dinheiro, cartão, PayPal ou outra). "
                "Depois de paga, uma fatura já não pode voltar a não paga.",
                "<strong>{{deposit_record_title}}</strong> regista um pagamento adiantado. A fatura passa a aparecer como <strong>{{invoices_status_partially_paid}}</strong>, e o sinal não pode exceder o total.",
                "<strong>{{invoices_action_mark_void}}</strong> mantém a fatura nos seus registos mas marca-a como cancelada. Prefira isto a eliminar — uma fatura eliminada "
                "não pode ser recuperada.",
            ]),
            ("p", "Com o Pro, a pasta de um cliente também pode ser guardada ou partilhada como ZIP de PDF, e toda a lista pode ser exportada para o seu contabilista — veja "
                  "<a href=\"#export\">Exportar faturas</a>."),
        ]),
        "export": ("Exportar faturas (Excel, CSV, ZIP)", [
            ("p", "Disponível com o Invoice Cove Pro. Toque no ícone de exportação (📄) no topo do separador <strong>{{nav_invoices}}</strong>. Escolha as faturas a incluir "
                  "com os seletores de ano e mês (<strong>{{invoices_export_all}}</strong>, um ano ou um mês de um ano — só são oferecidos os anos e os meses "
                  "que têm faturas) e depois escolha o que fazer:"),
            ("ul", [
                "<strong>{{invoices_export_save_xlsx}}</strong> / <strong>{{invoices_export_share_xlsx}}</strong> — uma folha de cálculo Excel (.xlsx).",
                "<strong>{{invoices_export_save_csv}}</strong> / <strong>{{invoices_export_share_csv}}</strong> — a mesma tabela como ficheiro CSV.",
                "<strong>{{invoices_export_save_zip}}</strong> / <strong>{{invoices_export_share_zip}}</strong> — os PDF das faturas num ZIP, uma pasta por cliente.",
                "<strong>{{invoices_export_delete}}</strong> — elimina definitivamente as faturas selecionadas, após duas confirmações.",
            ]),
            ("p", "<em>Guardar</em> deixa-o escolher onde no dispositivo fica o ficheiro; <em>Partilhar</em> abre o menu de partilha do Android para o enviar "
                  "por e-mail ou numa conversa."),
            ("p", "O Excel e o CSV são feitos para o seu contabilista: <strong>uma linha por artigo da fatura</strong>, com os dados da fatura repetidos em cada linha — "
                  "número e datas, nome, número, número fiscal, número de IVA, número do registo comercial e morada do cliente, descrição, quantidade, unidade, "
                  "preço e valor líquido do artigo, subtotal, desconto, taxa de IVA, valor do IVA e total da fatura, a moeda, e o estado, a data e o "
                  "método de pagamento. Os cabeçalhos das colunas e as palavras fixas (fatura, paga, não paga, métodos de pagamento) são escritos no idioma definido na aplicação."),
        ]),
        "new-quote": ("Criar um orçamento", [
            ("p", "<strong>{{home_new_quote_title}}</strong> funciona como o New Invoice — os mesmos campos, os mesmos botões <strong>{{common_preview_button}}</strong> e <strong>{{common_template_button}}</strong> e o mesmo "
                  "<strong>{{newquote_generate_button}}</strong> que guarda, cria o PDF e abre o menu de partilha com um toque — com uma "
                  "<strong>{{newquote_date_label}}</strong> e uma data <strong>{{newquote_valid_until_label}}</strong> em vez da data da fatura e do vencimento. "
                  "Os orçamentos não têm rascunhos."),
        ]),
        "quotes": ("Gerir orçamentos e convertê-los em fatura", [
            ("p", "O ecrã <strong>{{common_quotes_title}}</strong> (a partir do mosaico do ecrã inicial) lista os seus orçamentos por cliente, tal como as faturas. Abra um orçamento para "
                  "o ver ou partilhar, use <strong>{{quotes_action_accept}}</strong> ou <strong>{{quotes_action_decline}}</strong> quando o cliente responder, "
                  "registe um sinal ou elimine-o. O sinal não pode exceder o total do orçamento."),
            ("p", "Quando um cliente aceita um orçamento, use <strong>{{quotes_action_convert_to_invoice}}</strong> para transformar as linhas marcadas numa fatura real, "
                  "editável de forma independente — o vencimento e o desconto ainda se podem ajustar, e o orçamento original fica marcado como "
                  "<strong>{{quotes_status_converted}}</strong> e guardado nos seus registos."),
        ]),
        "calendar": ("Calendário e lembretes", [
            ("p", "O ecrã <strong>{{calendar_title}}</strong> é uma vista mensal para as suas notas. Toque num dia para ver ou adicionar notas; uma nota tem um título e um texto e, "
                  "com <strong>{{calendar_remind_me}}</strong> e uma hora, envia-lhe uma notificação nesse momento. O primeiro dia da semana segue a sua definição."),
            ("p", "À parte, o Invoice Cove envia lembretes de pagamento — notificações locais para faturas que vencem em breve ou estão vencidas. Nada é enviado para um servidor nem recebido de um."),
        ]),
        "reports": ("Relatórios", [
            ("p", "<strong>{{common_reports_title}}</strong> dá-lhe uma visão rápida: os valores <strong>{{reports_stat_revenue}}</strong>, "
                  "<strong>{{reports_stat_outstanding}}</strong> e <strong>{{reports_stat_overdue}}</strong>, quantas faturas tem, "
                  "<em>{{reports_revenue_by_month}}</em> e os seus <em>{{reports_top_customers}}</em> por total faturado."),
            ("p", "Toque no cartão <strong>{{reports_stat_outstanding}}</strong> ou <strong>{{reports_stat_overdue}}</strong> para abrir a lista exata dessas faturas."),
        ]),
        "settings": ("Dados do negócio e definições", [
            ("p", "Abra as definições a partir do ícone de roda dentada — o ecrã chama-se <strong>{{settings_title}}</strong>. Começa pelas suas preferências: "
                  "<strong>{{settings_appearance_label}}</strong> ({{settings_theme_light}} ou {{settings_theme_dark}}), "
                  "<strong>{{settings_invoice_template_label}}</strong> predefinido, <strong>{{settings_tax_label_label}}</strong> (IVA, GST…), "
                  "<strong>{{settings_first_day_of_week_label}}</strong> e <strong>{{settings_due_date_default_label}}</strong> (preenche o vencimento automaticamente, por exemplo Net 30). "
                  "Por baixo seguem-se <strong>{{settings_security_label}}</strong> (veja <a href=\"#app-lock\">Bloqueio da aplicação</a>), "
                  "<strong>{{settings_item_suggestions_label}}</strong> e <strong>{{settings_backup_restore_label}}</strong> (veja <a href=\"#backup\">Cópia de segurança e restauro</a>)."),
            ("p", "<strong>{{settings_item_memory_title}}</strong> memoriza descrições e preços dos artigos para os sugerir enquanto escreve; <em>{{common_clear}}</em> esquece-os "
                  "sem tocar nas suas faturas."),
            ("p", "Mais abaixo está o perfil do seu negócio, impresso em cada fatura e orçamento: <strong>{{settings_business_name_label}}</strong>, "
                  "<strong>{{settings_your_name_label}}</strong>, um lema curto (<strong>{{settings_business_location_label}}</strong>), {{common_field_email}}, "
                  "{{common_field_phone}}, o <strong>{{settings_date_format_label}}</strong> das datas, a morada, {{common_field_tax_id}}, "
                  "{{common_field_vat_number}}, <strong>{{common_field_registration_info}}</strong> (número de registo, capital social e semelhantes), o seu "
                  "<strong>{{settings_business_logo_label}}</strong> e os seus <strong>{{settings_payment_details_label}}</strong> (IBAN, ligação PayPal.me…). Cada campo "
                  "tem um exemplo, e <strong>qualquer campo que deixe em branco simplesmente não aparece nas suas faturas</strong>. Toque em <strong>{{common_done}}</strong> quando "
                  "terminar; se sair com alterações por guardar, é perguntado primeiro."),
            ("p", "No fim: este <strong>{{settings_user_manual}}</strong> e <strong>{{settings_share_this_app}}</strong>."),
        ]),
        "backup": ("Cópia de segurança e restauro", [
            ("p", "Disponível com o Invoice Cove Pro. Em <strong>{{settings_backup_restore_label}}</strong>, <strong>{{settings_create_backup_title}}</strong> guarda "
                  "tudo — faturas, orçamentos, rascunhos, clientes, calendário, definições, o seu logótipo e os PDF — num único ficheiro. Escolha "
                  "<strong>{{backup_save_button}}</strong> para o guardar onde quiser, ou <strong>{{backup_share_button}}</strong> para o enviar para um local seguro."),
            ("p", "<strong>{{settings_restore_backup_title}}</strong> traz tudo de volta — por exemplo num telemóvel novo. Só funciona numa instalação nova, antes de ter "
                  "adicionado dados, pelo que nunca pode substituir o que já tem. O Invoice Cove verifica se o ficheiro está intacto e avisa se estiver danificado, "
                  "se não for uma cópia do Invoice Cove ou se tiver sido feito por uma versão mais recente da aplicação (atualize primeiro)."),
            ("note", "Um ficheiro de cópia de segurança <strong>não está cifrado</strong>: quem o tiver pode ler os seus dados. Guarde-o num local privado. O PIN de bloqueio da aplicação nunca "
                     "está incluído."),
        ]),
        "app-lock": ("Bloqueio da aplicação", [
            ("p", "Em <strong>{{settings_security_label}}</strong> pode ativar o <strong>{{settings_app_lock_title}}</strong>: o Invoice Cove pede então o seu PIN "
                  "(ou a sua impressão digital) quando a aplicação é aberta de novo de raiz ou depois de reiniciar o telemóvel — não sempre que volta a ela."),
            ("ul", [
                "<strong>{{settings_set_pin}}</strong>: escolha um PIN de 4 dígitos e confirme-o.",
                "Recebe depois um <strong>código de recuperação</strong> de 6 dígitos, mostrado apenas uma vez. Anote-o e guarde-o num local seguro.",
                "Se o seu telemóvel o permitir, desbloqueie com a impressão digital (<strong>{{security_use_fingerprint}}</strong>).",
                "Esqueceu-se do PIN? Use <strong>{{security_forgot_pin}}</strong> e introduza o código de recuperação. Após 5 tentativas erradas tem de esperar 30 segundos; "
                "a espera aumenta com mais tentativas erradas.",
            ]),
            ("note", "Se perder o PIN e o código de recuperação — e não tiver configurado o desbloqueio por impressão digital — não há forma de voltar a entrar. Não o podemos repor "
                     "por si."),
        ]),
        "languages": ("Idiomas", [
            ("p", "O Invoice Cove fala 13 idiomas: English, Română, Deutsch, Français, Español, Italiano, Português, Polski, Čeština, Slovenčina, Magyar, "
                  "Nederlands e Svenska. Toque no ícone redondo com a bandeira no topo das definições para mudar — a aplicação muda de imediato."),
            ("p", "O texto dos seus PDF e das exportações Excel/CSV segue o idioma definido na aplicação, e este manual está disponível nos mesmos 13 idiomas "
                  "(use a barra de idiomas no topo da página)."),
        ]),
        "templates": ("Modelos PDF", [
            ("p", "O Invoice Cove inclui 18 modelos de PDF: Classic, Client Color (com o tom da cor do cliente), Minimal, Bold Corporate, Classic Clean, Modern Dark "
                  "Accent, Organic Flow, Modern Professional Business, Minimalist Bakery Service, Gentle Flower, Cozy Paws, Soft Elegant, Solid Craft, Crimson Frame, "
                  "Blush Botanical, Vintage Garage, Sparkle Waves e Spooky Hollow."),
            ("p", "Escolha o modelo predefinido em Definições → <strong>{{settings_invoice_template_label}}</strong>: toque num modelo e depois em <strong>{{common_done}}</strong>. Aplica-se "
                  "a tudo o que gerar a partir daí. Para uma só fatura ou orçamento, use o botão <strong>{{common_template_button}}</strong> "
                  "do formulário."),
            ("p", "Todos os modelos imprimem a mesma informação — os dados do seu negócio, os do cliente, os artigos com a sua unidade e data, os totais, as notas e "
                  "os dados de pagamento — mas apenas o que preencheu. As faturas longas continuam numa segunda página, com os totais juntos ao último artigo."),
        ]),
        "free-vs-pro": ("Plano gratuito versus Invoice Cove Pro", [
            ("p", "O Invoice Cove é gratuito, com alguns limites razoáveis:"),
            ("ul", [
                "Até 3 faturas e 3 orçamentos gerados por mês civil",
                "Até 3 clientes de cada vez",
                "Os números das faturas e dos orçamentos são atribuídos automaticamente e não se podem editar",
                "A exportação para Excel, CSV e ZIP é exclusiva do Pro",
                "A cópia de segurança e o restauro são exclusivos do Pro",
            ]),
            ("p", "O <strong>Invoice Cove Pro</strong> é uma única compra através do Google Play — não uma subscrição — que remove todos estes limites para sempre. "
                  "Os rascunhos, todos os modelos e idiomas, o bloqueio da aplicação e a criação, pré-visualização e partilha de documentos são gratuitos para todos. "
                  "Consulte os <a href=\"terms.html\">Termos de utilização</a> para todos os detalhes."),
        ]),
    },
}
