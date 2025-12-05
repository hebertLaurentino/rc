# Uso de IA no Laboratório

A utilização da IA foi basicamente para ajudar em montar o gráfico, pois não sabia como que passava o eixo x e y para o matplot e nem como destacar
um ponto em específico.

Então utilizei no trecho:

```python
# Destacar o ponto de primeiro bit comprometido
plt.scatter(primeiro_bit_comprometido - 1, qtd_bits_comprometidos_por_snr[primeiro_bit_comprometido - 1], color='red', s=75)
plt.annotate(f"Primeiro bit comprometido: {primeiro_bit_comprometido}", xy=(primeiro_bit_comprometido - 1, qtd_bits_comprometidos_por_snr[primeiro_bit_comprometido - 1]), xytext=(primeiro_bit_comprometido - 6, qtd_bits_comprometidos_por_snr[primeiro_bit_comprometido - 1] + 1))

# Destacar o ponto de todos os bits comprometidos
plt.scatter(len(qtd_bits_comprometidos_por_snr)-1, qtd_bits_comprometidos_por_snr[-1], color='red', s=75)
plt.annotate(f"{len(qtd_bits_comprometidos_por_snr)} dB", xy=(len(qtd_bits_comprometidos_por_snr)-1, qtd_bits_comprometidos_por_snr[-1]), xytext=(len(qtd_bits_comprometidos_por_snr)-2, qtd_bits_comprometidos_por_snr[-1] - 2))

# Personalizando o gráfico
plt.title("Quantidade de errors X SNR (dB)")
plt.ylabel("Quantidade de errors")
plt.xlabel("SNR (dB)")
```
