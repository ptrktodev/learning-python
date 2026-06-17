## Conceitos trabalhados

**Classe e instância**
- Declaração de classe com `class Funcionario`
- Criação de instâncias (`patrick`, `funcio_desc`)
- Diferença entre acessar via classe (`Funcionario.empresa`) vs via objeto (`patrick.localizacao`)

**Atributos**
- Atributos de classe (compartilhados por todas as instâncias): `empresa`, `ANO_ATUAL`, etc.
- Atributos de instância (únicos por objeto): `nome`, `idade`, `cargo`, definidos no `__init__`
- Type hints nos atributos e parâmetros

**Métodos**
- `__init__` (construtor / dunder method)
- Métodos de instância com `self`
- Métodos de classe com `@classmethod` e `cls`
- Factory method via `criar_zerado` (padrão de criação alternativa de objetos)

**Ferramentas**
- `rich.inspect` para visualizar objetos
- `rich.traceback` para tracebacks mais legíveis

---

## Observações no código

**Positivas**
- Separação clara entre atributos de classe e de instância com comentários
- Uso correto de `cls` vs `self`
- `ANO_ATUAL` em maiúsculo sinalizando constante — boa convenção
- Factory method `criar_zerado` bem aplicado

