# Principais Comandos Git

O Git é um sistema de controle de versão distribuído amplamente utilizado para rastrear mudanças no código-fonte durante o desenvolvimento de software. Aqui estão alguns dos comandos mais comuns do Git:

## Configuração Inicial

1. **git init**: Inicializa um repositório Git em um diretório local.
2. **git config --global user.name "Seu Nome"**: Configura o nome de usuário global do Git.
3. **git config --global user.email "seu@email.com"**: Configura o email global do Git.

## Gerenciamento de Mudanças

4. **git add <arquivo>**: Adiciona um arquivo ao índice (staging area) para ser incluído no próximo commit.
5. **git add .**: Adiciona todas as mudanças no diretório atual ao índice.
6. **git commit -m "Mensagem do Commit"**: Registra as mudanças no repositório Git com uma mensagem de commit.
7. **git commit -am "Mensagem do Commit"**: Adiciona e registra todas as mudanças ao mesmo tempo.

## Examinar o Histórico

8. **git log**: Mostra o histórico de commits.
9. **git log --oneline**: Mostra o histórico de commits de forma resumida.
10. **git log --graph**: Mostra o histórico de commits em formato de grafo.
11. **git log --author="Nome do Autor"**: Mostra o histórico de commits de um autor específico.

## Ramificação e Mesclagem

12. **git branch**: Lista todas as branches locais.
13. **git branch <nome-da-branch>**: Cria uma nova branch.
14. **git checkout <nome-da-branch>**: Muda para uma branch específica.
15. **git merge <nome-da-branch>**: Mescla uma branch com a branch atual.

## Trabalhando com Repositórios Remotos

16. **git remote add origin <URL-do-Repositório-Remoto>**: Adiciona um repositório remoto.
17. **git push -u origin <nome-da-branch>**: Envia os commits locais para o repositório remoto.
18. **git pull origin <nome-da-branch>**: Puxa as mudanças do repositório remoto e mescla com a branch local.
19. **git clone <URL-do-Repositório>**: Clona um repositório remoto para o diretório local.

## Outros Comandos Úteis

20. **git status**: Mostra o estado atual do repositório.
21. **git diff**: Mostra as diferenças entre o diretório de trabalho e o índice (staging area).
22. **git reset HEAD <arquivo>**: Remove um arquivo do índice (staging area), mantendo as alterações no diretório de trabalho.
23. **git checkout -- <arquivo>**: Descarta as mudanças em um arquivo no diretório de trabalho.

Estes são apenas alguns dos comandos mais comuns do Git. Com o tempo, você pode explorar mais comandos e aprender a usá-los conforme necessário para o seu fluxo de trabalho.

## Boas Práticas - GitFlow

O Gitflow é um modelo de fluxo de trabalho baseado no Git que define uma estrutura para gerenciar o desenvolvimento de software de forma organizada e escalável. Desenvolvido por Vincent Driessen, o Gitflow é amplamente adotado na indústria de desenvolvimento de software devido à sua clareza e eficácia.

Este modelo de fluxo de trabalho define uma estrutura de branches específica e estabelece um conjunto de regras e convenções para o desenvolvimento colaborativo, integração contínua e lançamento de software. Ele se baseia em duas branches principais: `main` e `develop`, além de branches de suporte para recursos, lançamentos e correções de bugs.

Na figura abaixo há um exemplo da dinâmica do GitFlow.

![Texto Alternativo](https://wac-cdn.atlassian.com/dam/jcr:34c86360-8dea-4be4-92f7-6597d4d5bfae/02%20Feature%20branches.svg?cdnVersion=1551)


O Gitflow facilita a separação de diferentes estágios de desenvolvimento, como o desenvolvimento de novas funcionalidades, a preparação para lançamentos e a correção de bugs, mantendo o histórico do repositório organizado e legível.

Ao entender e adotar o Gitflow, as equipes de desenvolvimento podem melhorar a colaboração, a qualidade do código e a eficiência do processo de desenvolvimento de software.

Para mais informações, verifique o material da Atlassian de [GitFlow](https://www.atlassian.com/br/git/tutorials/comparing-workflows/gitflow-workflow).

## Boas Práticas - Convenções de Mensagens de Commits e Branches

As Convenções de Git referem-se a um conjunto de práticas e padrões que são seguidos ao trabalhar com o Git, um sistema de controle de versão amplamente utilizado no desenvolvimento de software. Essas convenções são projetadas para promover a consistência, clareza e colaboração entre membros da equipe, facilitando a compreensão do histórico do repositório e simplificando processos como revisão de código, integração contínua e lançamento de software.

Adotar e aplicar convenções de Git consistentes em um projeto ou equipe oferece uma série de benefícios:

- Clareza e Legibilidade: Mensagens de commit, nomes de branches e outras convenções são padronizados e significativos, facilitando a compreensão do histórico de alterações.

- Colaboração Eficiente: Todos os membros da equipe podem entender facilmente o estado do projeto e contribuir de forma consistente, mesmo em um ambiente distribuído.

- Automatização e Integração: Ferramentas de automação, como pipelines de CI/CD, podem ser configuradas com base nas convenções, simplificando o processo de desenvolvimento e lançamento.

- Redução de Erros: Convenções claras ajudam a evitar erros comuns e melhoram a qualidade do código e do processo de desenvolvimento.

Algumas das principais áreas cobertas pelas convenções de Git incluem mensagens de commit, nomenclatura de branches, versionamento semântico, uso de tags e muito mais.

Ao adotar e aplicar convenções de Git em seu projeto, você pode promover uma cultura de colaboração eficaz, melhorar a qualidade do código e facilitar o gerenciamento de mudanças ao longo do tempo.

Para mais informações, consulte [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).