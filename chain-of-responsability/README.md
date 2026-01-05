# Chain of Responsibility

Esse padrão é um padrão comportamental que permite que algum determinado objeto passe por uma cadeia de, cada um decidindo se irá ou não processar o objeto.
Isso impede de uma classe conhecer toda a estrutura da cadeia, promovendo o baixo acoplamento.

1. Defina uma interface para os manipuladores na cadeia.
2. Crie classes concretas que implementem essa interface.
3. Cada classe concreta deve ter uma referência para o próximo manipulador na cadeia.
4. Implemente a lógica para processar o objeto ou passar para o próximo manipulador.
5. Configure a cadeia de manipuladores no cliente.

