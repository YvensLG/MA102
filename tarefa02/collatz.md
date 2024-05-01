# Collatz

## Entrada:
* A entrada será um inteiro positivo $n \leq 2^{68}$.

## Saída:

* A saída será um inteiro representando o comprimento da sequência de Collatz do número $n$.
## Algoritmo
```
Tome nota de um contador=0;
Receber inteiro positivo n;

Enquanto n não for 1, faça o seguinte procedimento:
    Contador aumenta em 1;
    Se n é par:
        n recebe n/2;
    Senão:
        n recebe 3n+1.;

Retornar o contador;
Terminar.
```

## Estruturas de Controle Utilizadas

Foi utilizado o __Sequenciamento Direto__ durante a maior parte do algoritmo, indicando a ordem convencional de se seguir os comandos.

Utilizou-se de __Iteração Condicional__ logo após receber o inteiro $n$, onde a estrutura itera enquanto $n \neq 1$.

Dentro da iteração condicional, ainda foi usado __Desvio Condicional__ para indicar as condições do problema de Collatz: se $n$ for par, divida-o por 2, se não for par (se for ímpar), multiplique-o por 3 e some 1. 
