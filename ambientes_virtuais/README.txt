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
###########################################################

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
