# 🍔 Sistema de Vendas - Hamburgueria & Açaiteria (CLI)

Este projeto consiste em um **Sistema de Vendas** desenvolvido em **Python** via linha de comando (CLI - *Command Line Interface*). O sistema foi projetado para auxiliar no gerenciamento de vendas, cadastro de produtos, controle de estoque e atendimento de pedidos de forma simples e direta.

---

## 👥 Visão Geral e Histórias de Usuário (User Stories)

O projeto foi estruturado considerando a visão e as necessidades de diferentes papéis e atores dentro do negócio:

* **PO (Dono do Negócio):** *"Como dono do negócio, quero um sistema de vendas para a minha hamburgueria para que eu possa controlar as vendas e produtos."*
* **QA / Cliente:** *"Como cliente, quero um sistema de vendas para a minha hamburgueria para que eu possa comprar meus produtos favoritos de forma fácil e rápida."*
* **Tech (Programador):** *"Como programador, quero um sistema de vendas para a minha hamburgueria para que eu possa desenvolver um software eficiente e funcional para o negócio."*
* **Dev (Desenvolvedor):** *"Como programador, quero um sistema de vendas para a minha hamburgueria para que eu possa implementar as funcionalidades necessárias para atender às necessidades do negócio e dos clientes."*
* **UX (Designer):** *"Como designer de experiência do usuário, quero um sistema de vendas para a minha hamburgueria para que eu possa criar uma interface intuitiva e agradável para os usuários, garantindo uma experiência de compra satisfatória."*
* **IA (Analista de Dados):** *"Como analista de dados, quero um sistema de vendas para a minha hamburgueria para que eu possa coletar e analisar os dados de vendas, ajudando a identificar padrões de consumo e otimizar as estratégias de marketing e estoque."*

---

## 🔄 Ciclo de Vida do Desenvolvimento

1. **Planejamento:** Levantamento de requisitos e mapeamento de necessidades do negócio.
2. **Análise:** Modelagem dos dados e definição dos fluxos do menu principal.
3. **Desenvolvimento:** Implementação da lógica de programação em Python (CLI).
4. **Testes:** Validação dos fluxos de cadastro de produtos, pedidos e listagem.
5. **Implantação:** Execução do script no terminal local.
6. **Manutenção & Evolução:** Refatoração de código e preparação para futuras integrações (GUI e Banco de Dados).

---

## 🚀 Funcionalidades do Sistema

* **1. Cardápio:** Consulta da variedade de hambúrgueres e acompanhamentos (Carne, Frango, Vegetariano, Vegano, Batata Frita, Onion Rings, Salada).
* **2. Bebidas:** Opções de refrigerantes, sucos naturais, água mineral e cervejas.
* **3. Sobremesas:** Cardápio de milkshakes, sorvetes, brownies e pudins.
* **4. Combos:** Opções combinadas de Hambúrguer + Acompanhamento + Bebida.
* **5. Cadastrar Produtos:** Permite o cadastro individual de produtos informando Nome, Quantidade em Estoque, Preço, Validade e Descrição.
* **6. Fazer Pedidos:** Registro rápido de pedidos selecionando o combo e a forma de pagamento.
* **7. Combo Infantil:** Opções de combos adaptados para o público infantil.
* **8. Formas de Pagamento:** Suporte a Dinheiro, Cartão de Crédito, Cartão de Débito e Pix.
* **9. Combo do Dia:** Seleção e pedido de ofertas promocionais do dia.
* **10. Listar Produtos:** Exibição completa dos produtos cadastrados com todos os seus detalhes e saldo em estoque.
* **0. Sair:** Encerramento seguro do sistema.

---

## 🛠️ Tecnologias e Conceitos Utilizados

* **Linguagem:** Python 3
* **Estrutura de Repetição:** Laço `while True` para navegação contínua no menu.
* **Estrutura Condicional:** Estruturas `if / elif / else` para direcionamento de opções.
* **Variáveis e Memória:** Armazenamento individual de dados e atributos de produtos.
* **Formatação de Saída:** Uso de *f-strings* e formatadores numéricos (`:.2f`).

---

## 💻 Como Executar o Programa

### Pré-requisitos
* **Python 3.x** instalado na máquina.

### Passo a Passo

1. **Clonar ou Baixar o Projeto:**
   Salve o arquivo Python (por exemplo, `main.py` ou `hamburgueria.py`) na sua máquina.

2. **Abrir o Terminal:**
   Navegue até a pasta onde o arquivo `.py` foi salvo.

3. **Executar a Aplicação:**
   Digite o seguinte comando:
   ```bash
   python main.py