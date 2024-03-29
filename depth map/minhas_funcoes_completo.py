import math
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c * 1000
    return distance

def estah_dentro_área(lat, lon, lat_min, lon_min, lat_max, lon_max):
    return lat_min <= lat <= lat_max and lon_min <= lon <= lon_max

def ler_arquivo(file_path):
    with open('A1_CUBE_BNB.txt', 'r') as file:
        dados = [linha.strip().split() for linha in file.readlines()]
        dados = [(float(lon), float(lat), float(prof)) for lon, lat, prof in dados]
        lat_min = min(dados, key=lambda x: x[1])[1]
        lon_min = min(dados, key=lambda x: x[0])[0]
        lat_max = max(dados, key=lambda x: x[1])[1]
        lon_max = max(dados, key=lambda x: x[0])[0]
    return dados, lat_min, lon_min, lat_max, lon_max

def encontrar_posicao_mais_próxima(dados, lat, lon):
    min_distance = float('inf')
    closest_position = None
    closest_depth = None

    for row in dados:
        lat2, lon2, depth = row
        distance = haversine(lat, lon, lat2, lon2)
        if distance < min_distance:
            min_distance = distance
            closest_position = (lat2, lon2)
            closest_depth = depth

    return closest_position, min_distance, closest_depth

# Lê o arquivo e obtém os dados
dados, lat_min, lon_min, lat_max, lon_max = ler_arquivo('A1_CUBE_BNB.txt')

# Imprime os limites de latitude e longitude
print(f'Latitude mínima: {lat_min}, Longitude mínima: {lon_min}')
print(f'Latitude máxima: {lat_max}, Longitude máxima: {lon_max}')

# Recebe a entrada do usuário
lat = float(input("Digite a latitude: ").replace(',', '.'))
lon = float(input("Digite a longitude: ").replace(',', '.'))

# Verifica se o ponto está dentro da área e imprime o resultado
dentro_da_area = estah_dentro_área(lat, lon, lat_min, lon_min, lat_max, lon_max)
print(f'O ponto está dentro da área? {dentro_da_area}')

if dentro_da_area:
    # Mede o tempo antes da chamada da função
    inicio = time.time()

    # Chama a função e obtém o resultado
    closest_position, min_distance, closest_depth = encontrar_posicao_mais_próxima(dados, lat, lon)

    # Mede o tempo após a chamada da função
    fim = time.time()

    # Imprime os resultados
    print(f"Posição mais próxima: {closest_position}")
    print(f"Distância para a posição mais próxima: {min_distance:.2f} metros")
    print(f"Profundidade na posição mais próxima: {closest_depth:.2f} metros")
    print(f"Tempo decorrido: {fim - inicio:.2f} segundos")

    # Plota os pontos
    lons, lats, depths = zip(*dados)
    plt.scatter(lons, lats, c=depths, cmap='viridis')
    plt.colorbar(label='Profundidade (metros)')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Mapa de Profundidade')
    
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()
    
    formatter = FuncFormatter(lambda x, pos: f'{x:.3f}')
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.gca().yaxis.set_major_formatter(formatter)
    
    plt.show()
