
# Especificações do Projeto

Após a apresentação do embasamento e dos objetivos desse projeto, será esclarecido o modo pelo qual tais objetivos serão concretizados.

## Personas
As personas são representações das histórias, características e motivações do público-alvo do projeto. Aqui estão as personas identificadas para o **Vagas Inclusivas**:

### Ana Almeida, Recrutadora
- **Idade:** 32 anos  
- **Localização:** São Paulo - SP  
- **Motivação:** Promover diversidade e inclusão nas contratações.  
- **Necessidades:** Identificar e corrigir termos excludentes em descrições de vagas, além de sugerir alternativas inclusivas.  

### Carlos Costa, Gerente de RH  
- **Idade:** 45 anos  
- **Localização:** Rio de Janeiro - RJ  
- **Motivação:** Melhorar a reputação da empresa como um local inclusivo.  
- **Necessidades:** Garantir que as descrições de vagas sejam atraentes para candidatos de diversos perfis.  

### Mariana Mendes, Candidata  
- **Idade:** 28 anos  
- **Localização:** Belo Horizonte - MG  
- **Motivação:** Encontrar oportunidades de trabalho em empresas que valorizam a diversidade.  
- **Necessidades:** Acessar descrições de vagas claras e inclusivas.  

## Histórias de Usuários
Com base nas personas, foram identificadas as seguintes histórias de usuários:

| EU COMO... | PERSONA | QUERO/PRECISO ... FUNCIONALIDADE | PARA ... MOTIVO/VALOR |
|------------|---------|----------------------------------|-----------------------|
| Ana Almeida | Recrutadora | Identificar termos excludentes em descrições de vagas | Garantir que as vagas sejam inclusivas e atraiam candidatos diversos. |
| Ana Almeida | Recrutadora | Receber sugestões de alternativas inclusivas | Substituir termos problemáticos por linguagem neutra e inclusiva. |
| Carlos Costa | Gerente de RH | Analisar descrições de vagas em lote | Economizar tempo e garantir consistência nas descrições. |
| Mariana Mendes | Candidata | Visualizar descrições de vagas claras e inclusivas | Sentir-se representada e motivada a se candidatar. |

## Modelagem do Processo de Negócio

### Análise da Situação Atual
Atualmente, muitas empresas utilizam termos excludentes ou sexistas em suas descrições de vagas, o que pode desencorajar candidatos de grupos sub-representados. A proposta do **Vagas Incluvisas** é automatizar a identificação desses termos e sugerir alternativas inclusivas, promovendo um mercado de trabalho mais diversificado.

### Descrição Geral da Proposta
O **InclusiVagas** é uma ferramenta que analisa descrições de vagas, identifica termos excludentes e sugere alternativas inclusivas. A ferramenta visa auxiliar empresas e recrutadores na criação de descrições de vagas mais acessíveis e inclusivas.

### Limitações
- A ferramenta concentra-se apenas na análise de descrições de vagas, não abrangendo outras áreas de recrutamento.  
- Depende da qualidade e atualização do banco de dados de termos excludentes e alternativas inclusivas.  

### Alinhamento com Estratégias de Negócio
A proposta está alinhada com a estratégia de promover diversidade e inclusão nas empresas, melhorando a reputação e atraindo talentos diversos.

## Processos

### Processo 1 – Análise de Descrições de Vagas
Este processo descreve como a ferramenta analisa as descrições de vagas e identifica termos excludentes.

### Processo 2 – Sugestão de Alternativas Inclusivas
Este processo detalha como a ferramenta sugere alternativas inclusivas para os termos identificados.

## Indicadores de Desempenho

| Indicador | Objetivos | Descrição | Fórmula de Cálculo | Fonte de Dados | Perspectiva |
|-----------|-----------|-----------|--------------------|----------------|-------------|
| Número de Empresas Cadastradas | Expandir a base de usuários | Quantifica o total de empresas que utilizam a ferramenta | Total de empresas cadastradas | Banco de Dados | Crescimento do Produto |
| Número de Descrições Analisadas | Aumentar o uso da ferramenta | Quantifica o número de descrições de vagas analisadas | Total de descrições analisadas | Sistema de Análise | Engajamento |
| Taxa de Conversão | Otimizar a adoção da ferramenta | Calcula a proporção de empresas que adotam as sugestões | (Número de Sugestões Adotadas / Total de Sugestões) * 100 | Dados de Uso | Desempenho Comercial |

## Requisitos

### Requisitos Funcionais

| ID | Descrição do Requisito | Prioridade |
|----|------------------------|------------|
| RF-001 | A ferramenta deve identificar termos excludentes em descrições de vagas | ALTA |
| RF-002 | A ferramenta deve sugerir alternativas inclusivas para termos excludentes | ALTA |
| RF-003 | A ferramenta deve permitir a análise de descrições de vagas em lote | MÉDIA |
| RF-004 | A ferramenta deve gerar relatórios de análise | BAIXA |

### Requisitos Não Funcionais

| ID | Descrição do Requisito | Prioridade |
|----|------------------------|------------|
| RNF-001 | A ferramenta deve garantir a confidencialidade dos dados | ALTA |
| RNF-002 | A interface deve ser intuitiva e fácil de usar | MÉDIA |
| RNF-003 | A ferramenta deve ser compatível com diferentes navegadores | MÉDIA |

## Restrições

| ID | Restrição |
|----|-----------|
| RE-01 | O projeto deve ser concluído até 27/06/2025 |
| RE-02 | A ferramenta não pode gerar custos para os usuários |
| RE-03 | A equipe não pode subcontratar o desenvolvimento |
