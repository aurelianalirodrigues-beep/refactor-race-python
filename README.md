# REFactor Race Python

## EQUIPE

- Aureliana Rodrigues
- Adicionar demais integrantes da equipe

## DESCRIÇÃO

Projeto desenvolvido para a atividade REFactor Race Python, com o objetivo de melhorar a qualidade interna de um sistema legado de processamento de pedidos sem alterar seu comportamento esperado.

A evolução foi validada por testes automatizados e métricas de qualidade.

## DIAGNÓSTICO INICIAL

Antes da refatoração foram identificados os seguintes problemas:

1. A função `process_order` concentrava diversas responsabilidades.
2. O cálculo do subtotal estava duplicado.
3. Existiam condicionais complexas e excessivamente aninhadas.
4. Existiam números e valores fixos espalhados pelo código.
5. As regras de desconto, frete, impostos e pontos estavam misturadas.
6. A identificação de produtos duplicados utilizava loops aninhados.
7. O código apresentava baixa separação de responsabilidades.
8. O Ruff identificava quatro problemas de análise estática.

## CODE SMELLS ENCONTRADOS

Foram encontrados principalmente:

- Long Method;
- código duplicado;
- números mágicos;
- condicionais complexas;
- responsabilidades misturadas;
- baixa coesão da função principal;
- algoritmo pouco eficiente para identificação de duplicados;
- regras de negócio concentradas em uma única função.

## REFATORAÇÕES REALIZADAS

A função principal foi dividida em funções especializadas:

- `calculate_subtotal`;
- `calculate_customer_discount`;
- `calculate_coupon_discount`;
- `calculate_discount`;
- `calculate_weight`;
- `calculate_shipping`;
- `calculate_tax`;
- `calculate_points`;
- `find_duplicate_products`.

Também foram criadas constantes para representar regras anteriormente espalhadas pelo código.

A identificação de produtos duplicados passou a utilizar um conjunto (`set`) para controlar os produtos já encontrados, eliminando a necessidade dos dois loops aninhados existentes anteriormente.

As condicionais foram simplificadas e as responsabilidades foram separadas.

## TESTES

Os quatro testes originais foram preservados e continuaram passando após a refatoração.

A cobertura aumentou de 83% para 93%.

## MÉTRICAS ANTES E DEPOIS

| Indicador | Antes | Depois |
|---|---:|---:|
| Testes passando | 4/4 | 4/4 |
| Cobertura | 83% | 93% |
| Complexidade de `process_order` | E (34) | A (1) |
| Complexidade média | E (34.0) | A (3.1) |
| Manutenibilidade | A (51.69) | A (35.68) |
| Problemas Ruff | 4 | 0 |

A maior melhoria observada ocorreu na complexidade da função principal, que passou de E (34) para A (1).

O índice numérico de manutenibilidade diminuiu, embora tenha permanecido classificado como A. Essa limitação foi mantida de forma transparente na análise.

## DECISÕES TÉCNICAS

A equipe priorizou a preservação do comportamento existente.

As regras de negócio não foram alteradas sem requisito específico. A refatoração concentrou-se na organização interna, separação de responsabilidades, redução da complexidade e melhoria da legibilidade.

Os tickets de novos requisitos não foram implementados sem liberação.

## USO DE INTELIGÊNCIA ARTIFICIAL

**Ferramenta utilizada:** ChatGPT.

**Finalidade:** apoio na análise de code smells, organização da refatoração, interpretação das métricas e documentação técnica.

**Exemplo de sugestão recebida:** separar a função principal em funções menores responsáveis por subtotal, desconto, frete, impostos, pontos e identificação de produtos duplicados.

**A sugestão foi aceita, modificada ou rejeitada?**  
As sugestões foram analisadas e aplicadas de acordo com as regras existentes do sistema.

**Como a equipe validou a solução?**  
Por meio da execução dos testes automatizados, medição de cobertura, análise de complexidade com Radon, índice de manutenibilidade e análise estática com Ruff.

## MELHORIAS FUTURAS

- ampliar a suíte de testes;
- criar testes específicos para funcionários;
- testar todos os tipos de cupons;
- ampliar testes de frete expresso;
- testar estados fora da região Sudeste;
- avaliar formas de melhorar o índice de manutenibilidade;
- implementar novos requisitos somente quando formalmente liberados.

## CONCLUSÃO

A melhoria do código foi comprovada por evidências.

Os testes originais continuaram passando, a cobertura aumentou, a complexidade da função principal caiu significativamente e os problemas identificados pelo Ruff foram eliminados.

Portanto, a melhoria não foi avaliada apenas pela quantidade de linhas ou aparência do código, mas por testes, métricas e análise técnica.