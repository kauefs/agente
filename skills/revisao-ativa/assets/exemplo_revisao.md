# Exemplo de Revisão Ativa Preenchida

Use este exemplo para calibrar o nível de detalhe e o formato esperado.

---

## 🧠 Material de Revisão Ativa: Closures em JavaScript

### 🎴 Flashcards de Estudo (5 cards)

> **Dica de uso:** Tente responder à pergunta da **Frente** de memória antes de revelar o **Verso**.

| # | Frente (Pergunta / Conceito) | Verso (Resposta / Explicação) |
|---|---|---|
| 1 | O que é uma closure em JavaScript? | Função que retém o acesso a variáveis do seu escopo léxico externo mesmo após a execução desse escopo ter terminado. |
| 2 | O que é o escopo léxico? | Mecanismo que define o acesso a variáveis com base no local onde as funções foram declaradas no código fonte. |
| 3 | Qual um uso prático comum para closures? | Criar variáveis privadas (encapsulamento) e geradores de funções customizadas (factory functions). |
| 4 | Como closures afetam a memória da aplicação? | As variáveis referenciadas pela closure continuam na memória e não são coletadas pelo Garbage Collector. |
| 5 | Como o `let` no laço `for` resolve problemas de escopo assíncrono? | Criando uma nova ligação de variável para cada iteração do laço, preservando o valor correto na closure. |

---

### 📝 Quiz de Fixação (5 Perguntas)

#### 1. Qual das alternativas define corretamente uma closure?
A) Uma função que não aceita argumentos.  
B) A combinação de uma função com o seu ambiente léxico de declaração.  
C) Um método estático dentro de uma classe.  
D) Uma arrow function sem bloco de código.

#### 2. Qual será o valor impresso no console ao executar o código abaixo?
```javascript
function criarContador() {
    let c = 0;
    return () => ++c;
}
const conta = criarContador();
conta();
console.log(conta());
```
A) 0  
B) 1  
C) 2  
D) ReferenceError

#### 3. Por que o uso indiscriminado de closures pode levar a vazamento de memória (*memory leak*)?
A) Porque bloqueia a thread de execução do evento loop.  
B) Porque retém referências no escopo pai que o Garbage Collector não pode liberar.  
C) Porque força a compilação JIT repetida.  
D) Porque converte tipos primitivos em objetos.

#### 4. O que acontece ao tentar acessar a variável `c` diretamente fora da função `criarContador`?
A) Lança `ReferenceError`.  
B) Retorna `undefined`.  
C) Retorna `0`.  
D) Retorna `null`.

#### 5. O que difere a palavra-chave `let` da `var` em um laço `for` com callback assíncrono?
A) `let` tem escopo de bloco e cria um novo binding a cada iteração; `var` tem escopo de função.  
B) `var` é síncrono e `let` é assíncrono.  
C) `let` impede a execução do callback até o laço terminar.  
D) Não há diferença prática entre elas.

---

<details>
<summary>🔑 Clique aqui para ver o Gabarito Comentado</summary>

1. **B** — A closure é a junção da função com o contexto léxico onde foi criada.
2. **C** — A primeira chamada `conta()` incrementa `c` para 1; a segunda incrementa para 2 e retorna esse valor.
3. **B** — Como a closure mantém o ponteiro para o ambiente externo, as variáveis não são elegíveis para limpeza enquanto a função existir.
4. **A** — Como `c` está encapsulada dentro do escopo de `criarContador`, ela não está acessível no escopo global.
5. **A** — `let` possui escopo de bloco, garantindo que cada iteração tenha sua própria variável `i` capturada no callback.

</details>
