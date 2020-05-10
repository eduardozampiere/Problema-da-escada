# Problema-da-escada
  Sabendo que é possível subir uma escada de um em um degrau, de dois em dois degraus ou alternando entre essas formas.
  De quantas formas é possível subir uma escada com N degraus?
  
  
  
## Visualizando o problema

  Vamos imaginar a situação.
  Temos na nossa frente uma escada com 1 degrau apenas, de quantas formas podemos subir ?
    R: 1 forma apenas.
   
  
  Temos agora na nossa frente uma escada com 2 degraus. Entao podemos subi-la de 2 formas: Usando o primeiro degrau e logo depois o segundo. Ou indo direto para o segundo.
    R: 2 formas
    
   
  Temos agora uma escada com tres degraus.
    Podemos começar tanto do primeiro quanto do segundo degrau. Comecemos pelo primeiro.
    Ao subir o primeiro degrau temos agora na nossa frente uma "nova" escada com dois degraus.
    Se começassemos pelo segundo degrau, teríamos a nossa frente uma "nova" escada com apenas um degrau.
    
    Logo é possível afirmar que o numero de maneiras de subir uma escada de tres degraus é o numero de maneiras de subir uma 
    de um degrau + o numero de maneiras de subir uma de dois degraus.
    
    f(n) = f(n-1) + f(n-2)
    
    Temos agora um problema básico de Fibonacci.
    
 ## Resolvendo o problema.
 
    Logo de cara veio na minha cabeça a seguinte resposta
```python
  def f(x):
       if x == 1:
		    return 1
          
       if x < 1:
		     return 0
	   return step(x-1) + step(x-2)
```
   Essa solução funciona. Porém para valores mto grandes fica extremamente lento.
   
   
   Pensei então em uma segunda solução que está no step-1.py
   É basicamente inicializar um array contendo os valores de fibonacci do 1 ao 100000(ou um outro numero grande). Assim o sistema geraria apenas uma vez e o usuario poderia chamar a função quantas vezes quisesse.
   
   Porem é um grande desperdício de tempo se o usuario nao quiser saber o valor de f(100000).
   
   
   Então pensei na terceira soluçao que esta no step.py
   
   Na primeira chamada da função eu inicializaria um array contendo os valores de fibonacci do 1 ao n (numero inserido pelo usuario)
   na segunda chamada se o novo n ja tivesse sido criado, seria apenas retornas o valor de array[n].
   Se nao tivesse sido criado, eu acrescento no primeiro array os valores até chegar no que o usuario quer.
   
   Dessa forma alimento o meu array de acordo com o uso do usuario.
 
  
 
