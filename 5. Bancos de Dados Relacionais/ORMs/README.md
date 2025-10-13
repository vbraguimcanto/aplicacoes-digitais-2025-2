# Alembic — Controle de Migrations

O **Alembic** é uma ferramenta oficial do SQLAlchemy para **gerenciar versões do banco de dados** (migrations).  
Ele permite criar, aplicar e reverter alterações de schema sem perder dados existentes.

---

## 📁 Estrutura típica do projeto

```
meu_projeto/
│
├── models.py              # Definição das tabelas (SQLAlchemy)
├── alembic.ini            # Configuração principal do Alembic
└── alembic/
    ├── env.py             # Integra o Alembic com os modelos SQLAlchemy
    ├── script.py.mako     # Template padrão de migrations
    └── versions/          # Onde ficam os arquivos de migration
```

---

## Inicialização

Para criar a estrutura inicial do Alembic:

```bash
alembic init alembic
```

Isso cria o diretório `alembic/` e o arquivo `alembic.ini`.

---

## Configuração básica

1. No arquivo **`alembic.ini`**, defina a URL do banco:

   ```ini
   sqlalchemy.url = sqlite:///meubanco.db
   ```

2. No arquivo **`alembic/env.py`**, importe os modelos:

   ```python
   from models import Base
   target_metadata = Base.metadata
   ```

   > Se `models.py` estiver em outro diretório, adicione:
   >
   > ```python
   > import os, sys
   > sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
   > ```

---

## Criando uma migration

Quando você **modificar seus modelos** (ex: adicionar uma coluna, tabela, etc.), gere uma nova migration automaticamente:

```bash
alembic revision --autogenerate -m "mensagem descritiva"
```

O Alembic analisa o `Base.metadata` e cria um arquivo em `alembic/versions/` com as mudanças detectadas.

---

## Aplicando migrations

Para aplicar (executar) todas as migrations pendentes:

```bash
alembic upgrade head
```

---

## Revertendo migrations

Para desfazer a última migration aplicada:

```bash
alembic downgrade -1
```

---

## Verificando a versão atual

Para saber em que versão o banco está:

```bash
alembic current
```

---

## Fluxo de uso típico

1. Modifique os modelos em `models.py`  
2. Gere uma nova migration  
   ```bash
   alembic revision --autogenerate -m "adiciona campo idade"
   ```
3. Aplique as mudanças  
   ```bash
   alembic upgrade head
   ```
4. Se precisar reverter:  
   ```bash
   alembic downgrade -1
   ```

---

## Exemplo de migration gerada

```python
def upgrade():
    op.add_column('usuarios', sa.Column('idade', sa.Integer(), nullable=True))

def downgrade():
    op.drop_column('usuarios', 'idade')
```

---

## Dica

- Sempre **comite os arquivos de migration** junto com o código no Git.  
- Nunca edite migrations aplicadas em produção, crie uma nova.
