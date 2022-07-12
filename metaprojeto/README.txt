Aula: https://youtu.be/O3bs4JtHrow

Convenção de Estrutura de Software:
 - docs
   >> Documentação
 - nome_do_software ou src
   >> Código Fonte
 - tests
   >> Testes
 - scripts (Se necessário)

========================================================
Geral:

Definir versão do python para o projeto:
Instalar python com pyenv:
$ pyenv install 3.8.12
Listar versões instaladas:
$ pyenv versions
Utilizar versão específica:
$ pyenv local 3.8.12

Escolha de ferramenta para ambientes virtuais:
 - virtualenv
 - venv
 - poetry
 - pipenv

pyproject.toml ou requirements.txt

Versionamento de código:
 - git

Segurança de bibliotecas:
 - pip-audit
 - safety
 - pyup

========================================================
src:

Formatadores automáticos de código (live #39):
 - blue (Talvez o melhor, segue a pep8)
 - black
 - isort (Faz sort das importações)
 - autopep8
 - YAPF
 - darker

Análise estática, linters (live #38):
 - flake8 (Checador da pep-8)
 - pylint (Padronização, convenções e erros)
 - pydocstyle (Checador da pep-257)
 - bandit (Problemas de segurança)
 - Randon (Busca de complexidade de código)
 - Prospector (Agregador de ferramentas) (Flake8, Mccabe, pylint, pep8, pep257)
 - mypy (Checador de sugestões de tipo)

========================================================
tests:

Framework de Testes:
 - pytest (live #167)
 - unittest (live #75)
 - behave (live #10)
 - ward

$ mkdir tests
$ touch tests/__init__.py

========================================================
docs:

Criadores de documentação:
 - mkdocs (live #189)
 - sphinx

========================================================
Automatizar comandos (live #184):
 - "São muitas ferramentas e comandos, para facilitar podemos automatizar tudo."

GNU Make
 - makefile

###########################################################
#                    Template Makefile                    #
###########################################################
# .PHONY: install format lint test sec                    #
#                                                         #
# install:                                                #
#         @poetry install                                 #
# format:                                                 #
#         @isort .                                        #
#         @blue .                                         #
# lint:                                                   #
#         @blue . --check                                 #
#         @isort . --check                                #
#         @prospector --with-tool pep257 --doc-warning    #
# test:                                                   #
#         @pytest -v                                      #
# sec:                                                    #
#         @pip-audit                                      #
###########################################################

$ make install
$ make format
$ make lint
$ make test
$ make sec

Faz tudo de uma vez
$ make

Hooks - pre-commit:
$ touch .git/hooks/pre-commit

###########################################################
#              Template .git/hooks/pre-commit             #
###########################################################
# make lint                                               #
# make test                                               #
###########################################################

$ chmod +x .git/hooks/pre-commit
