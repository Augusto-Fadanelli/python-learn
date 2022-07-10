Aula: https://youtu.be/naGF7EIUFp0
Aula: https://youtu.be/cEkA9PH2oEk
Requirements doc: https://pip.pypa.io/en/stable/reference/requirements-file-format/

$ python -m venv nome_venv

Posso ter mais de um ambiente venv em um projeto

#######################################################################
#                     Ativando o ambiente virtual                     #
#######################################################################
# Plataforma: |      Shell:     | Comando para ativar:                #
#    Unix     |     bash/zsh    | $ source <venv>/bin/activate        #
#    Unix     |       fish      | $ source <venv>/bin/activate.fish   #
#    Unix     |     csh/tcsh    | $ source <venv>/bin/activate.csh    #
#    Unix     | PowerShell Core | $ <venv>/bin/Activate.ps1           #
#   Windows   |     cmd.exe     | C:\> <venv>\Scripts\activate.bat    #
#   Windows   |    PowerShell   | PS C:\> <venv>\Scripts\Activate.ps1 #
#######################################################################

Desativar ambiente virtual:
$ deactivate

===========================================================

###########################################################
#                 Template requirements.txt               #
###########################################################
# # Pacotes que quero instalar:                           #
# httpx                                                   #
# pandas                                                  #
#                                                         #
# # Pacotes com versões específicas:                      #
# numpy == 0.6.1                                          #
# django >= 4.1.1                                         #
# flask != 3.5                                            #
# selenium ~= 1.1 # Maior ou igual a 1.1, mas menor que 2 #
# pacote>3.0, <4.0 # Maior que 3.0 e menor que 4.0        #
###########################################################

Obs.: Utilizar ~= faz com que o pacote seja sempre compativel e permite utilizar o mais recente compativel. É recomendado remover o número de patch: Ex.: flask == 1.0.4 ficaria flask ~= 1.0

Instalar requirements:
$ pip install -r requirements.txt

Requirements_dev.txt lista as bibliotecas que não irão para o ambiente de produção mas para o de desenvolvimento.
###########################################################
#               Template requirements_dev.txt             #
###########################################################
# # Instala as bibliotecas de produção                    #
# -r requirements.txt                                     #
#                                                         #
# # Bibliotecas de desenvolvimento:                       #
# black                                                   #
# ipdb                                                    #
# ipython                                                 #
# pytest                                                  #
###########################################################

Instalar requirements e requirements_dev:
$ pip install -r requirements_dev.txt

constraints.txt define versões que devem ser instaladas das libs que são dependencias ou sub-dependencias das que estão em requirements e requirements.txt
Obs.: Se alguma lib em constraints não for dependencia nem sub-dependencia, então não será instalado
###########################################################
#                  Template constraints.txt               #
###########################################################
# # Dependencias e sub-dependencias                       #
# pytz==2020.1                                            #
# splitty==0.0.8                                          #
###########################################################

Instalar requirements, requirements_dev e setar versões das dependencias:
$ pip install -r requirements_dev.txt -c constraints.txt

===========================================================

PIP:
Listar:
$ pip list
$ pip freeze
Listar e informar se estiver desatualizado:
$ pip list -o
Atualizar pip:
$ pip install --upgrade pip

ferramenta para remover dependencias de libs pip:
$ pip install pip-autoremove
$ pip-autoremove nome_da_lib

Outras ferramentas
pipdeptree
pyenv
pipx # para instalar libs globais sem sujar o ambiente
poetry

===========================================================

git e versionamento.

Criando o arquivo pre-commit:
 > Com essa configuração, sempre que for feito um commit será informado se algum pacote estiver desatualizado.

$ git init
$ touch .git/hooks/pre-commit

###########################################################
#              Template .git/hooks/pre-commit             #
###########################################################
# IFS=                                                    #
# pip_out=$(pip list -o 2> /dev/null)                     #
#                                                         #
# if [ $(echo $pip_out | wc -l) -ge 1 ]; then             #
#     echo "Existem pacotes desatualizados (pip list -o):"#
#     echo $pip_out                                       #
#     exit 1                                              #
# fi                                                      #
###########################################################

$ chmod +x .git/hooks/pre-commit

Atualizar requirements.txt sem atualizar pacotes no venv:
$ pip install pip-upgrade
$ pip-upgrade requirements.txt -p all --skip-package-installation

===========================================================

Segurança:

Site que lista vulnerabilidades: https://cve.mitre.org/
Site que lista vulnerabilidades: https://nvd.nist.gov/

Procura pacotes com vulnerabilidades:
$ pip install safety
Procura pacotes instalados:
$ safety check
Procura pacotes setados no requirements.txt:
$ safety check -r requirements.txt --full-report

Configurar pre-commit para não permitir commit se encontrar vulnerabilidades:

################################################################
#                Template .git/hooks/pre-commit                #
################################################################
# IFS=                                                         #
# pip_out=$(pip list -o 2> /dev/null)                          #
#                                                              #
# if [ $(echo $pip_out | wc -l) -ge 1 ]; then                  #
#     echo "Existem pacotes desatualizados (pip list -o):"     #
#     echo $pip_out                                            #
# fi                                                           #
#                                                              #
# safety_out=$(safety check -r requirements.txt --full-report) #
# safety_filter=$($safety_out |& grep "Affected" | wc -l)      #
#                                                              #
# if [ $safety_filter -ge 1 ]; then                            #
#     echo "Commit não efetuado, vulnerabilidade encontrada"   #
#     echo $safety_out                                         #
#     exit 1                                                   #
# fi                                                           #
################################################################