# 🐍 Diário de Estudos: Python (Método Cornell)

Este repositório serve como um registro do aprendizado contínuo em Python. O fluxo de estudo funciona da seguinte forma:

1. O arquivo `Projeto.py` é utilizado como um **bloco de rascunhos** durante as aulas.
2. Posteriormente, o conteúdo é **modularizado** em arquivos temáticos.
3. Cada novo arquivo recebe **exercícios práticos** para solidificar o conhecimento e treinar lógica de programação (nível LeetCode).
4. Este README é atualizado utilizando o **Método Cornell** para revisão rápida.

---

## 📅 Data: 02/09/2026 | Assunto: Fundamentos Iniciais de Python

| Tópicos Principais (Dicas / Perguntas)                                                                 | Notas (Pontos Importantes / Detalhes)                                                                                                                                                                    |
| :----------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Configuração de Ambiente**<br>- Como criar um ambiente virtual?<br>- Como ativar?                    | - Criar: `python3 -m venv .venv`<br>- Ativar (Win): `.venv\Scripts\Activate.ps1`<br>- Ativar (Linux): `source .venv/bin/activate`                                                                        |
| **Saída de Dados e Comentários**<br>- Função `print()`?<br>- Argumentos `sep` e `end`<br>- Comentários | - `print()` exibe dados no console.<br>- `sep`: altera o separador (padrão é espaço).<br>- `end`: altera o final (padrão é `\n` - quebra de linha).<br>- `#` (comentário de linha) e `"""` (Docstrings). |
| **Tipos Primitivos**<br>- Quais os principais?<br>- Como verificar?<br>- Conversão (Casting)           | - `str` (texto), `int` (inteiro), `float` (real), `bool` (lógico: True/False).<br>- `type(variavel)` descobre o tipo.<br>- Converter chamando o tipo: `int('1')`, `float('2.5')`.                        |
| **Variáveis e Op. Aritméticas**<br>- Como declarar?<br>- Operadores básicos<br>- Prioridade matemática | - Tipagem dinâmica: `nome = 'Nico'`.<br>- Operadores: `+` `-` `*` `/` (divisão real) `//` (divisão inteira) `**` (exponenciação) `%` (resto).<br>- Prioridade: `()` > `**` > `* / // %` > `+ -`.         |
| **Formatação de Strings**<br>- F-strings<br>- `.format()`                                              | - F-strings: `f'Nome: {nome}'` (avalia variáveis direto).<br>- Formatação específica: `{valor:.2f}` para 2 casas decimais.<br>- `.format()`: Alternativa usando placeholders.                            |
| **Entrada e Condicionais**<br>- Como receber dados?<br>- Estruturas de decisão                         | - `input('Mensagem:')` - **Atenção:** sempre retorna `str`!<br>- Controle de fluxo: `if` (se), `elif` (se não, se), `else` (se não).<br>- Trabalham com condições booleanas e operadores lógicos.        |

### 📝 Resumo da Revisão

**O que vimos:** A base absoluta da linguagem Python. Passamos desde a configuração inicial do ambiente até o controle de fluxo do código.
**Como vimos:** Através de exemplos práticos no `Projeto.py` que depois foram separados logicamente nos módulos `01` ao `05`.
**O que fazer:** Utilizar o arquivo `Projeto.py` como página em branco para resolver a lista de 5 exercícios que estão nas DocStrings ao final de cada um dos 5 scripts criados.

---

_(Novos estudos e revisões serão adicionados acima ou abaixo desta linha conforme o curso avançar)_
