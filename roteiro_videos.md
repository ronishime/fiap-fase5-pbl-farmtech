
---

## Guia de gravação do Vídeo 2 – passo a passo com os cliques

**Preparação (antes de apertar REC)**

1. Abra o Chrome com 2 abas: (a) `https://calculator.aws/#/addService/ec2-enhancement` (já abre direto na configuração do EC2; se aparecer o aviso de cookies, clique em *Decline/Recusar*); (b) o `README.md` do projeto (no VS Code com *preview* ou no GitHub) rolado até a seção "Entrega 2", para mostrar a tabela e o gráfico.
2. Gravação de tela: a mesma ferramenta do vídeo 1 (no Windows 11, `Win + Alt + R` grava a tela com a Xbox Game Bar; `Win + Alt + R` de novo para parar).
3. Faça um ensaio sem gravar: a tabela de instâncias demora alguns segundos para carregar e o vídeo precisa ficar em 5 min.

**Roteiro (≈ 4 min)**

| # | Clique / tela | Fale |
|---|---------------|------|
| 1 | Tela da calculadora aberta | "Sou Ronaldo Nishime, RM 571759, grupo 69. Na Entrega 2 preciso hospedar a API com o modelo de ML em uma máquina Linux simples na AWS: 2 vCPUs, 1 GiB, até 5 Gigabit de rede e 50 GB de disco, On-Demand com 100% de uso. Vou cotar em Norte da Virgínia e em São Paulo." |
| 2 | *Escolher uma região* → **Leste dos EUA (N. da Virgínia)** | "Começo pela Virgínia do Norte." |
| 3 | *Especificações do EC2*: Locação = Instâncias compartilhadas, Sistema operacional = **Linux**, Carga = *Uso constante*, Número de instâncias = 1 | "Linux, locação compartilhada, uso constante, uma instância." |
| 4 | Campo *Pesquisar tipo de instância* → digite `t3.micro` → marque o botão redondo da linha **t3.micro** | "A t3.micro é a instância que atende exatamente ao pedido: 2 vCPUs, 1 GiB de memória e rede *Up to 5 Gigabit*. Custa 0,0104 dólar por hora aqui." (aponte as colunas da tabela) |
| 5 | *Opções de pagamento*: marque **Sob demanda**; confira *Uso = 100* e *Utilization percent per month* | "Modalidade sob demanda, 100% de utilização, que dá 730 horas por mês." |
| 6 | *Amazon EBS*: tipo **SSD de uso geral (gp3)**, *Quantidade de armazenamento* = **50** GB, snapshots = *Sem armazenamento* | "Disco de 50 GB no tipo gp3, sem snapshots." |
| 7 | Rodapé: **Custo mensal total: 11,59 USD**. Clique em *Mostrar detalhes* / *Mostrar cálculos* | "Total de 11,59 dólares por mês: 730 horas vezes 0,0104 dá 7,59 da instância, mais 50 GB vezes 0,08 dá 4,00 do disco." |
| 8 | Volte ao topo: *Escolher uma região* → **América do Sul (São Paulo)**. Se a tabela de instâncias resetar, pesquise `t3.micro` e marque de novo | "Agora a mesma configuração em São Paulo: a instância sobe para 0,0168 por hora e o disco para 0,152 por GB." |
| 9 | Rodapé: **Custo mensal total: 19,86 USD** (12,26 instância + 7,60 disco) | "Total de 19,86 dólares por mês em São Paulo, contra 11,59 na Virgínia." |
| 10 | (opcional) *Salvar e visualizar resumo* | "Aqui o resumo da estimativa." |
| 11 | Aba do README: tabela de custos e gráfico `aws_comparacao_custos.png` | "Resposta da pergunta 1: a solução mais barata é Norte da Virgínia — 8,27 dólares a menos por mês, cerca de 71% de diferença, uns 99 dólares por ano. A instância é 61% mais cara em São Paulo e o disco, 90%. Alternativas com a mesma especificação, como a t3a.micro e a t4g.micro, são um pouco mais baratas, mas a diferença entre regiões continua." |
| 12 | README: seção "2) Acesso rápido aos dados dos sensores e restrições legais" | "Resposta da pergunta 2: mesmo mais cara, eu escolho São Paulo. Primeiro, a restrição legal: pela LGPD, guardar os dados fora do país é transferência internacional e exige mecanismos do artigo 33; em São Paulo os dados ficam no Brasil. Segundo, latência: a fazenda está no Brasil e a resposta para São Paulo fica em torno de 10 a 30 milissegundos, contra 120 a 150 para a Virgínia — importante para uma API que recebe dados de sensores o tempo todo. Terceiro, o custo extra é pequeno, 8 dólares por mês, e pode cair usando a t4g.micro ou um Savings Plan." |
| 13 | Encerramento | "Resumindo: a mais barata é a Virgínia do Norte, mas a correta para o cenário da FarmTech é São Paulo. Obrigado." |

**Depois de gravar**: subir no YouTube como **Não listado** (não "Privado"), título sugerido `FIAP - Fase 5 PBL - Entrega 2 (Custos AWS) - Grupo 69 - Ronaldo Nishime RM571759`, e colocar o link no README.
