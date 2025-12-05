# Uso de IA no Laboratório

A utilização da IA foi basicamente para ajudar em montar o gráfico, pois não sabia como que montava um grafico de linha nem como colocar legenda no próprio.

Então utilizei no trecho:

```python
def showGraph(funcs, labels, title, ylabel, xlabel):
    global resultados

    plt.figure(figsize=(10, 6))
    for func, label in zip(funcs, labels):
        x, y = func(resultados)
        plt.plot(x, y, marker='o', linestyle='-', label=label)

    # Personalizando o gráfico
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.grid(True, alpha=0.3)

    plt.legend()
    plt.show()
```

Também utilizei para pegar os dados da minha máquina em que estou rodando o notebook:

```md
Processador:
    Chip: Apple M4 Pro
    Arquitetura: ARM64
    Núcleos: 12
Modelo:
    Modelo: MacBook Pro
Memória:
    RAM: 24 GB
Sistema:
    OS: macOS
```