Basta testarmos até $\dfrac{n}{2}$, pois, se $n$ é composto, um dos números primos que dividem $n$ é menor que $n$, então, se $p$ é esse primo, $\dfrac{n}{p} \geq 2 \implies \dfrac{n}{2} \geq p$, então só temos que testar até esse número. E, se não tiver primo até ele, significa que $n$ é primo.

---

Basta testarmos até $\sqrt{n}$, pois, se $n$ é composto e $p$ é o menor primo que divide $n$, temos que $\dfrac{n}{p}$ divide $n$, e como $p$ é o menor primo, $\dfrac{n}{p} \leq p \implies p^2 \geq n \implies p \geq \sqrt{n}$, então, só temos que testar até esse número. E, se não tiver primo até ele, significa que $n$ é primo.