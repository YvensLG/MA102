# Calculadora de Datas

### __Nosso objetivo é somar `s` dias à data `d/m/a`, gerando, assim, uma data final `d1/m1/a1`.__

## Entrada:
* A primeria entrada são três números inteiros não negativos `d`, `m`, `a`, que indicam a data inicial. `d` indica o dia, `m` indica o mês e `a` indica o ano (`d/m/a`).

* A segunda entrada é um número inteiro não negativo `s` que indica o número de dias que vão passar.

## Saída:

* A saída serão três números inteiros não negativos `d1`, `m1`, `a1`, que indicam a data final. `d1` indica o dia, `m1` indica o mês e `a1` indica o ano (`d1/m1/a1`).
## Algoritmo

### Instruções Elementares Permitidas:

* Receber uma entrada inteira e guardá-la.
* Devolver saídas inteiras.
* Terminar o algoritmo.
* Somar e subtrair valores inteiros.
* Analisar igualdade e desigualdade entre dois números (maior, menor e igual).
* Alterar o valor de uma entrada anteriormente recebida.
* Entender as condições "se" e "senão".
* Enternder a condição "enquanto".


### Sequência de Instruções que Resolvem o Problema:
```
Receber dia inicial "d"
Receber mês inicial "m"
Receber ano inicial "a"
Receber dias a se somar "s"

Enquanto s>0, faça o seguinte procedimento:
    Se m = 01, 03, 05, 07, 08, 10 ou 12 (Meses de 31 dias):
        Se s+d for menor ou igual a 31:
            d aumenta s unidades (d recebe s+d).
            s recebe 0.
        Se não:
            s recebe s+d-32.
            d recebe 1.
            m aumenta em 1 unidade (m recebe m+1).
            
    Senão, se m = 04, 06, 09 ou 11 (Meses de 30 dias):
        Se s+d for menor ou igual a 30:
            d aumenta s unidades (d recebe s+d).
            s recebe 0.
        Se não:
            s recebe s+d-31.
            d recebe 1.
            m aumenta em 1 unidade (m recebe m+1).
            
    Senão, se m = 02 (Mês de 28 dias):
        Se s+d for menor ou igual a 28:
            d aumenta s unidades (d recebe s+d).
            s recebe 0.
        Se não:
            s recebe s+d-29.
            d recebe 1.
            m aumenta em 1 unidade (m recebe m+1).

    Se m=13:
        m recebe 1.
        a aumenta 1 unidade (a recebe a+1).
    

Devolver d (dia final), m (mês final) e a (ano final).
Terminar.
```

# Calculadora de Datas 2
### __Nosso objetivo é somar `s` dias _úteis_ à data `d/m/a`, gerando, assim, uma data final `d1/m1/a1`.__

Nesse caso, a entrada e saídas seriam praticamente as mesmas, com a diferença de que a relação entre elas seria somar `s` dias úteis ao invés de `s` dias. 

Com essa diferença, deve haver uma parte a mais no algoritmo, na qual se descobre o dia da semana da data inicial, para, assim, ser possível descrever a condição dos dias úteis, e podermos "ignorar" os fins de semana.
