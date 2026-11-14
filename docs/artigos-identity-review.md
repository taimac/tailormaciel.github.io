<!-- purpose: personal Artigos visual assessment and engineering evidence; date: 2026-11-14; domain: Branding -->
# Artigos: revisão da identidade TM

A seção publicada em #96 perdeu o cabeçalho e o rodapé completos do portfólio.
Esta correção aproxima índice e leitura das páginas existentes; a avaliação visual
final pertence ao proprietário. Base: `main` publicada
`e9ec12a6df7a43241a6179a29e650219eeaddb2b`. Escopo: [#97](https://github.com/taimac/tailormaciel.github.io/issues/97).

## Prévia navegável

Execute `node scripts/previewArticles.js 8787` e abra:

- [Início → Artigos → artigo sintético → voltar](http://127.0.0.1:8787/).
- [Índice vazio real, com a correção](http://127.0.0.1:8787/_states/empty/artigos/).

O helper usa cópias públicas em uma pasta temporária fora do projeto. O artigo
sintético é identificado no próprio texto e existe somente na prévia. Nenhum
HTML de demonstração entra em `artigos/`; o índice de produção continua vazio.
A prévia é local, não uma publicação ou alteração do site público.

## Comparações

As imagens do índice anterior vêm da base publicada. A leitura anterior é uma
**simulação do gerador publicado usando o mesmo texto sintético** da proposta;
não havia esse artigo publicado. Capturas Firefox, viewport desktop 1440 × 1000
e celular 390 × 844, escala 1, página completa; comparação desktop reduzida a
720 px por coluna. As capturas originais estão na mesma pasta.

| Superfície | Desktop | Celular |
|---|---|---|
| Índice vazio: antes / proposta | [Comparar](evidence/artigos-identity/compare-desktop-empty.png) | [Comparar](evidence/artigos-identity/compare-mobile-empty.png) |
| Leitura sintética: gerador anterior / proposta | [Comparar](evidence/artigos-identity/compare-desktop-reading.png) | [Comparar](evidence/artigos-identity/compare-mobile-reading.png) |
| Índice com artigo sintético | [Ver](evidence/artigos-identity/desktop-after-populated.png) | [Ver](evidence/artigos-identity/mobile-after-populated.png) |
| Menu da leitura | — | [Ver](evidence/artigos-identity/mobile-reading-menu.png) |
| Interface em inglês, artigo em português | [Ver](evidence/artigos-identity/desktop-reading-en.png) | [Ver](evidence/artigos-identity/mobile-reading-en.png) |

Referência visual: `about.html` e os estilos compartilhados do próprio portfólio.
O gerador reutiliza a navegação e o rodapé dessa página, ajustando caminhos para
`artigos/`. O CSS local usa as fontes, cores e espaçamentos existentes. A coluna
de leitura organiza título, introdução, parágrafos, h2/h3, listas e referências.
Os controles PT/EN usam o controlador existente; o conteúdo do artigo mantém
`lang="pt-BR"`. Os cinco documentos do portfólio só ganham a chave de tradução
de Artigos nos links existentes, sem mudança de composição.

## Registro de engenharia

Aplicado: Root `ENGINEERING_DESIGN_SECURITY_PLAYBOOK` v1.1.0.
Achados do implementador: nenhum pendente nesta candidata; revisão independente
é registrada no PR, não substituída por esta afirmação.

| Checks | Evidência e resultado |
|---|---|
| ENG-DESIGN-READY-01, ENG-DESIGN-EARLY-01 | **Atestado pelo implementador:** problema observado pelo proprietário, escopo limitado a índice/leitura e prévia. Sem migração ou publicação. |
| ENG-DESIGN-LAYER-01, ENG-QUAL-COHESION-01, ENG-QUAL-CONTRACT-01, ENG-QUAL-READ-01 | **Atestado pelo implementador:** estilos de Artigos separados; shell herdado de `about.html`; falha explícita se a referência sumir; controlador compartilhado preservado. |
| ENG-DESIGN-REVERSIBLE-01 | Reversível pelo revert do PR; nenhum dado ou conteúdo real alterado. Prévia descartável fora da árvore de produção. |
| ENG-TEST-BEHAVIOR-01, ENG-TEST-REGRESSION-01 | 12 testes Node passam. Os 3 testes novos de shell, hierarquia/referências e cards falham contra o gerador publicado e passam com a correção. |
| ENG-TEST-DETERMINISM-01 | Índice reproduzível byte a byte; ordem de páginas ordenada; teste com índice vazio e populado. |
| ENG-SEC-INPUT-01, ENG-SEC-PARSE-01 | Rejeições de aprovação, marca, status, slug, duplicatas e campos obrigatórios preservadas; HTML escapado, URL insegura e URL com credenciais não viram links; entidades não escapadas duas vezes. Não se ampliou o contrato para HTML arbitrário ou Markdown completo. |
| ENG-SEC-EXPOSURE-01, ENG-SEC-LOG-01 | **Atestado pelo implementador:** helper só copia arquivos públicos e serve em loopback sem indexação. Fontes, `.git`, caminhos privados e traversal receberam 404 na verificação HTTP. Sem credencial ou nota real nos artefatos. |
| Verificação visual/responsiva | **Atestado pelo implementador:** capturas desktop/celular inspecionadas; sem sobreposição ou rolagem horizontal. Percurso clicável, menu e idioma exercitados no navegador; não equivalem à aceitação visual do proprietário. |

Checks sem aplicação: família ENG-SEC-EXTMUT-* (nenhuma nova capacidade de escrita
externa), ENG-SEC-DEPS-01 (nenhum manifesto/dependência do produto alterado).
O browser de QA usa Firefox instalado e Puppeteer somente em diretório temporário;
não é dependência do site. ENG-REVIEW-FINDINGS-01 será fechado com a revisão do PR.

### Contraprovas e caminhos análogos

- Classe do shell: índice vazio, índice populado e página individual receberam a
  navegação, marca, menu, idioma e rodapé completos. Links em navbar e footer nos
  cinco documentos raiz receberam a mesma tradução de Artigos.
- Tentativas de quebrar o conteúdo: HTML em título/corpo, `javascript:`, URL HTTPS
  com credenciais, marca Fermac, aprovação falsa, slug traversal e `index`.
  Foram escapados ou recusados conforme o contrato existente.
- Tentativas de quebrar o layout/rotas: 320, 768, 900, 1024 e 1440 px nos três
  estados; nenhum overflow horizontal. Navegação e assets locais responderam 200.
  [Resultado do percurso](evidence/artigos-identity/journey.json).
- Privacidade: 12 testes das classes PublicationTests/PublicationPrivacyTests do
  Editorial #22 passam. A projeção pública da fixture foi enviada ao **gerador
  real corrigido**: texto público presente, `PRIVATE`, `INTERNAL`, Claims Ledger,
  Source & Evidence, Website Version e Verification ausentes. Nenhuma nota real.
- Equivalência: corpo/links escapados e critérios de aprovação anteriores
  continuam cobertos pelos sete testes existentes. A exclusão de notas privadas
  continua no adaptador Editorial; o renderer recebe somente a projeção pública.
- Lições aplicadas: Visual Evidence Override e Intent/Recipient Misread exigiram
  inspecionar capturas reais, sem declarar aceitação do proprietário; Source-Ungrounded
  Assertions exigiu base/PRs verificados e separação entre publicado, proposto e ativado.

Sem CI configurado no repositório: estes resultados são **evidência local**, não
CI verde. O proprietário aceitou separadamente a evidência local **somente para #98**
em 14/11/2026; a decisão está no PR e na issue #97. A exceção anterior continua
limitada a #96 e Fermac #27. Merge, publicação e ativação do Hermes
Editorial permanecem decisões distintas do proprietário. Não se deduz defeito
visual no site da Fermac a partir desta correção pessoal.

### Correções da Advisory Review

Revisor independente: novo contexto Codex, revisão somente de leitura, modelo
exato não exposto. Achados no head `74f8fcc`, registrados no PR:

| Achado | Check / impacto | Correção e contraprova |
|---|---|---|
| P2: skip link interceptado pelo smooth scroll | ENG-TEST-BEHAVIOR-01 / acessibilidade por teclado | O controlador preserva o comportamento nativo de `.article-skip`; `main` tem `tabindex=-1`. Tab → Enter foca `main`, e o próximo Tab fica no conteúdo em índice vazio, populado e leitura. |
| P2: palavras longas cortadas no hero mobile | ENG-TEST-REGRESSION-01 / conteúdo ilegível | `overflow-wrap:anywhere` em título, introdução e metadados dos cards. “Desinstitucionalização”, “Interdisciplinaridade” e URL longa cabem em 320 px; `scrollWidth` do elemento não supera `clientWidth`. |

[Contraprovas de teclado e clipping](evidence/artigos-identity/adversarial.json).
O revisor reproduziu os dois defeitos antes da correção. A seleção de checks foi
ampliada para foco real e clipping por elemento: medir só a largura do documento
não detecta texto escondido pelo `overflow:hidden` de um ancestral. Estes testes
passam após a correção. O cache do controlador nas páginas geradas ganhou versão
nova, para que o leitor não receba a implementação antiga. Nenhum outro
comportamento de âncora foi alterado.

Na segunda rodada, a seleção de lições foi reavaliada: Source-Ungrounded Assertions
continua aplicável; a classe inclui os três estados de Artigos e os campos
variáveis de título/introdução/cards. A comparação entre Advisory e Independent
fica registrada no PR quando a revisão independente terminar. Sem mudança de
escopo ou aceitação visual inferida.
