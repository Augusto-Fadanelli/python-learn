Escopo de Classe:
  -> "Utilizar o escopo de classe permite chamar um método ou atributo sem instanciá-lo. Em python utilizamos o decorator @classmethod para indicar um método de classe e passamos o parâmetro cls. O Escopo de instância está contido no escopo de classe, portanto podemos chamar um atributo/método do escopo da classe em uma instância também."

Escopo de Instância:
 -> "Só é permitido chamar um atributo/método do escopo da instância em objetos instânciados. A vantagem é que cada objeto poderá ter seus próprios valores únicos. Enquanto que uma alteração no escopo da classe altera todas os objetos instânciados após a alteração no escopo da classe."
 -> Método inicializador (__init__):
   >> "No python raramente se utiliza o método construtor (__new__), ao invés disso utilizamos o método inicializador (__init__)."

Exemplo da Pizza:
 -> "Neste exemplo demonstro como utilizar o escopo de classe juntamente com o de instância em uma mesma classe."
 -> Métodos estáticos:
  >> "Os métodos estáticos são como funções dentro da classe. Não se comunicam com o escopo da classe nem com o de instância, mas podem ser chamados das duas formas."

Exemplo do Carro:
 -> Encapsulamento:
  >> "Em python não se tem encapsulamento como estamos acostumados em java. No lugar temos convenções utilizadas pela comunidade python que indicam que determinado atributo ou método não devem ser acessados de fora da classe. Para isso utilizamos _ ou __ antes de um atributo/classe"
 -> Composição:
  >> "A composição acontece quando um objeto é instanciado dentro de uma classe ou é passado como parâmetro de algum método. Nesse exemplo a composição acontece quando um objeto Motor é passado como parâmetro do método __init__ da classe Carro."

Herança:
 -> "A herança é considerado por muitos programadores a característica principal do paradigma de POO. Neste exemplo criei uma supeclasse Animal, as classes Mamimefero e Ave herdam as características de Animal. Além deles, há também as subclasses de Ave e de Mamifero, ressaltando o caso do Ornitorrinco que herda as duas classes."
 -> Polimorfismo:
  >> "Não há nada de tão diferente aqui. Para implementar o polimorfismo basta criar um atributo/método com mesmo nome do equivalente na superclasse. Não utiliza-se @override."
 -> Classes e métodos abstratos
  >> "Para criar uma classe abstrata em python é necessário importar ABC e abstractmethod. Existe uma peculiaridade, para que a classe seja considerada abstrata de fato, além de herdar ABC, ela deve conter pelo menos um método abstrato. Isso pode ser testado no código ao comentar @abstractmethod em Animal e fazer uma instância de Animal no clientCode. A instância será feita sem erros, mas ao descomentar @abstractmethod a classe Animal volta a ser abstrata e o python acusará um erro de instânciação."
 -> super()
  >> "O super() serve para chamar um atributo/método da superclasse."
 -> Herança múltipla:
  >> "No python não existem interfaces, para suprir essa demanda é permitido que uma classe herde mais de uma superclasse. Então para criar uma interface basta criar uma classe abstrata apenas com métodos abstratos."
  >> "Por conta disso em algumas linguagens com herança múltipla pode ocorrer um famos problema chamado de Diamond of Death. O python contorna esse problema dando prioridade para a superclasse herdada mais a direita. (Esse conceito pode ser melhor entendido com uma imagem)."


