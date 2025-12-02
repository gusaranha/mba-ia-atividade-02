# Respostas do Trabalho - Pipeline de ML

## Identificação do Grupo

- **Integrantes:**
  1. Nome: Gustavo Aranha Araújo Costa dos Reis
  2. Nome:
  3. Nome:
  4. Nome:

---

## Parte 1: Resultados do Pipeline

### 1.1 O pipeline executou sem erros?
<!-- Marque com X a opção correta -->
- [X] Sim
- [ ] Não

### 1.2 F1-Score obtido:
<!-- Copie o valor exibido ao final da execução -->
```
F1-Score: 0.4074
```

### 1.3 Cole aqui o output final do pipeline:
<!-- Execute: python main.py e copie a saída -->
```

🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀
 INICIANDO PIPELINE DE ML
🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀


[ETAPA 1/4] Carregando dados...
 ✅ 5000 linhas carregadas

==================================================
EXPLORAÇÃO DOS DADOS
==================================================

Shape: (5000, 8)
Linhas (clientes): 5,000
Colunas (características): 8

Detalhamento das colunas:
cliente_id              int64
idade                   int64
renda_mensal          float64
tempo_conta_meses       int64
num_produtos            int64
tem_cartao_credito      int64
score_credito         float64
respondeu_campanha      int64
dtype: object

5 primeiros clientes:
   cliente_id  idade  renda_mensal  tempo_conta_meses  num_produtos  tem_cartao_credito  score_credito  respondeu_campanha
0           1     56      46917.46                229             4                   1          600.0                   1
1           2     69      41274.41                  9             3                   0          758.2                   0
2           3     46      40649.98                 25             2                   1          595.7                   1
3           4     32      44336.79                217             5                   1          584.3                   0
4           5     60      35301.68                225             4                   0          797.8                   0


==================================================
DISTRIBUIÇÃO DO TARGET
==================================================

respondeu_campanha
0    2803
1    2197
Name: count, dtype: int64

respondeu_campanha
0    0.5606
1    0.4394
Name: proportion, dtype: float64


[ETAPA 2/4] Validando dados...
 ✅ Dados válidos!

[ETAPA 3/4] Treinando modelo...
Dados de treino: 4000 registros
Dados de teste: 1000 registros
Treinando modelo...
 ✅ Modelo treinado!
Modelo salvo em: models/modelo_campanha.pkl

[ETAPA 4/4] Avaliando modelo...

==================================================
RESULTADOS DA AVALIAÇÃO
==================================================

📊 MÉTRICAS:
   Accuracy:  0.5520 (55.20%)
   Precision: 0.4904
   Recall:    0.3484
   F1-Score:  0.4074

📋 MATRIZ DE CONFUSÃO:
   Verdadeiros Negativos (TN): 398
   Falsos Positivos (FP):      160
   Falsos Negativos (FN):      288
   Verdadeiros Positivos (TP): 154

==================================================
🎯 F1-SCORE FINAL: 0.4074
==================================================

✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
PIPELINE CONCLUÍDO COM SUCESSO!
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅

📝 Anote o F1-Score no arquivo RESPOSTAS.md: 0.4074

```

---

## Parte 2: Interpretação dos Resultados

### 2.1 O modelo é bom ou ruim? Por quê?
<!-- Considere: F1 de 0.5 seria jogar moeda. Acima de 0.5 = melhor que aleatório. -->

O modelo é ruim, pois além do F1 Score ser abaixo de 0.5 (0.4074 - um valor pior que aleatório),
o Recall também foi baixo (0.3484) indicando que o modelo deixa passar muitos clientes que responderiam a campanha,
mas não foram indicados - falsos negativos. 


### 2.2 O dataset é balanceado ou desbalanceado? Como você descobriu?
<!-- Dica: veja a proporção da variável target na exploração dos dados -->

O dataset é levemente desbalanceado, pois 56% dos clientes responderam a campanha em contrapartida com
43,94% que não responderam. Mostrando um desequilíbrio entre os grupos.

### 2.3 Por que usamos F1-Score e não apenas Accuracy neste caso?
<!-- Dica: pense no que aconteceria se o modelo previsse sempre 0 -->

Porque a acurácia pode mostrar resultados errados com datasets desbalanceados. Se o modelo previsse que todos os clientes
não responderiam a campanha, a acurácia teria sido alta, pois 56% dos clientes de fato não responderam.

---

## Parte 3: Validação de Dados

### 3.1 Liste as validações Pandera que você implementou:
<!-- Descreva cada validação que você adicionou -->

1. cliente_id: inteiro positivo; não nulo; único
2. idade: inteiro positivo; valor entre 18 e 80 anos
3. renda_mensal: float; valor positivo; valor entre 1000 e 50000
4. score_credito: float; valor positivo; valor entre 300 e 850
5. respondeu_campanha: inteiro; valor entre 0 e 1

### 3.2 Por que validar dados ANTES de treinar o modelo?
<!-- Pense no contexto de produção: o que aconteceria se dados inválidos entrassem no modelo? -->

Porque dados inválidos podem prejudicar o modelo. Valores que não existem, valores fora do intervalo esperado, 
dados faltantes, etc podem gerar padrões falsos.

---

## Parte 4: Versionamento

### 4.1 Liste os commits que vocês fizeram (copie do git log):
<!-- Execute: git log --oneline e cole aqui -->
```
ecec508 (HEAD -> main, origin/main, origin/HEAD) Respostas às questões
0ca7d21 Treinamento dos dados e criação do modelo
ae74f58 Validação dos dados do dataframe (ajustes no log)
bc315b6 Validação dos dados do dataframe
fdb814d Carregamento dos dados
fc9e9fa Carregamento dos dados
3837edf Estrutura inicial do projeto
1d31db6 Initial commit
```

### 4.2 Por que mensagens de commit descritivas são importantes?
<!-- Pense: se outra pessoa olhar o histórico, vai entender o que foi feito? -->

Para poder entender o que foi feito e por que foi feito, além do que se trata cada commit/atualização/feature.

---

## Parte 5: Reflexão (Opcional)

### 5.1 Qual foi a maior dificuldade do grupo?



### 5.2 O que vocês fariam diferente se fossem refazer?



---

**Data de entrega:** 02/12/2025
