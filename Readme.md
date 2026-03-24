# Sobre o Projeto
A Calculadora de Consumo Elétrico é um programa em Python desenvolvido como parte de um programa de iniciação em tecnologia. Seu objetivo é ajudar usuários a estimarem quanto cada aparelho elétrico consome de energia por mês, além do custo estimado na conta de luz — promovendo consciência energética e economia doméstica. Esse projeto foi desenvolvido por mim Gilson Camargo e juntamente com o Claude.IA que me auxiliou com comandos e verificações de códigos.

Funcionalidades

Entrada do nome do aparelho
Entrada da potência em watts (W)
Entrada do tempo médio de uso diário (horas)
Cálculo do consumo mensal em kWh
Cálculo do custo estimado em reais (R$)
Classificação do consumo (baixo, moderado, alto) """Sugestão do Claude que mantive, embora acho que não seja um parâmetro bem orientado"""
Suporte para calcular múltiplos aparelhos em sequência


Fórmula Utilizada
consumoMensal (kWh) = (potência × horas_por_dia × 30) / 1000
Exemplo — Geladeira:

Potência: 150 W
Uso diário: 24 horas
Consumo: (150 × 24 × 30) / 1000 = 108 kWh/mês
Custo estimado: 108 × R$ 0,75 = R$ 81,00/mês


A tarifa padrão utilizada é R$ 0,75/kWh (valor médio sugerido para este projeto).

