# python-Projects

 Descrição do Projeto:
O projeto consiste em processar dados de um arquivo chamado “A1_CUBE_BNB.txt”, que contém informações sobre coordenadas geográficas (latitude, longitude) e profundidades.
O objetivo é encontrar a posição mais próxima a partir das coordenadas fornecidas pelo usuário e calcular a distância até essa posição, bem como a profundidade associada.

Funcionalidades do Projeto:
Leitura do arquivo: O código lê o arquivo “A1_CUBE_BNB.txt” e extrai os dados relevantes.
Cálculo da distância: Utiliza a fórmula de haversine para calcular a distância entre duas coordenadas geográficas.
Determinação da posição mais próxima: Encontra a posição (latitude, longitude) mais próxima com base na distância calculada.
Verificação da área: Verifica se as coordenadas fornecidas pelo usuário estão dentro da área delimitada pelos limites de latitude e longitude do conjunto de dados.

Resultados:
O programa imprime os limites de latitude e longitude do conjunto de dados.
Verifica se o ponto fornecido pelo usuário está dentro da área.
Se estiver dentro da área, calcula a posição mais próxima, a distância até essa posição e a profundidade associada.
Exibe os resultados na saída padrão.

Visualização Gráfica:
O projeto também inclui uma visualização gráfica dos pontos no mapa.
Os pontos representam as coordenadas geográficas do conjunto de dados, e a cor indica a profundidade associada.

Tempo de Execução:
O tempo de execução é medido antes e após a chamada da função para encontrar a posição mais próxima.
