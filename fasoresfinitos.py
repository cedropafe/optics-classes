import matplotlib.pyplot as plt
import numpy as np

# Configuração da figura
fig, ax = plt.subplots(figsize=(11, 9))

# Parâmetros dos Fasores
N = 5
amplitude = 2.0        # Comprimento de cada fasor individual (A)
ang_inicial = np.radians(15)  # Inclinação inicial ligeiramente maior que zero
delta_phi_deg = 22     # Ângulo constante entre os fasores sucessivos
delta_phi_rad = np.radians(delta_phi_deg)

# Inicialização das variáveis de posição
x_atual, y_atual = 0.0, 0.0
ang_atual = ang_inicial

# Listas para guardar as coordenadas das junções
posicoes = [(x_atual, y_atual)]
direcoes = []

# --- 1. Desenho dos 5 Fasores Somados (Pretos) ---
for i in range(N):
    # Calcula as componentes dx e dy do fasor atual
    dx = amplitude * np.cos(ang_atual)
    dy = amplitude * np.sin(ang_atual)

    # Desenha o vetor atual em preto
    ax.annotate('', xy=(x_atual + dx, y_atual + dy), xytext=(x_atual, y_atual),
                arrowprops=dict(arrowstyle="->", color='black', lw=2,
                             mutation_scale=15, shrinkA=0, shrinkB=0))

    # Rótulo do fasor (\hat{\psi}_i) posicionado acima/esquerda do fasor
    mx, my = x_atual + dx/2, y_atual + dy/2
    ax.text(mx - 0.25 * np.sin(ang_atual), my + 0.25 * np.cos(ang_atual),
            rf'$\hat{{\psi}}_{i+1}$', fontsize=12, color='black', ha='center', va='center')

    # Guarda dados para referências posteriores
    direcoes.append(ang_atual)
    x_atual += dx
    y_atual += dy
    posicoes.append((x_atual, y_atual))

    # Atualiza o ângulo para o próximo fasor
    ang_atual += delta_phi_rad

# --- 2. Desenho do Fasor Resultante (\hat{\psi}_R) ---
x_fim, y_fim = posicoes[-1]
ax.annotate('', xy=(x_fim, y_fim), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color='crimson', lw=3,
                         mutation_scale=18, shrinkA=0, shrinkB=0, zorder=4))

# Rótulo do fasor resultante
ax.text(x_fim/2 - 0.4, y_fim/2 + 0.3, r'$\hat{\psi}_R$', fontsize=16,
        color='crimson', weight='bold', ha='center', va='center')

# --- 3. Cotagem da Amplitude 'A' ABAIXO do primeiro fasor ---
# Invertido o sinal do deslocamento para mover a cota para baixo
offset_cota = 0.4
cx1 = 0.0 + offset_cota * np.sin(ang_inicial)
cy1 = 0.0 - offset_cota * np.cos(ang_inicial)
cx2 = posicoes[1][0] + offset_cota * np.sin(ang_inicial)
cy2 = posicoes[1][1] - offset_cota * np.cos(ang_inicial)

ax.annotate('', xy=(cx2, cy2), xytext=(cx1, cy1),
            arrowprops=dict(arrowstyle='<->', color='dimgray', lw=1))
ax.text((cx1 + cx2)/2 + 0.1, (cy1 + cy2)/2 - 0.2, r'$A$', fontsize=14, color='dimgray', ha='center', va='center')

# Linhas de chamada auxiliares para a cota A
ax.plot([0.0, cx1], [0.0, cy1], color='dimgray', linestyle=':', lw=1)
ax.plot([posicoes[1][0], cx2], [posicoes[1][1], cy2], color='dimgray', linestyle=':', lw=1)

# --- 4. Cotagem de TODOS os ângulos de fase diferenciais (\Delta \phi) ---
for j in range(1, N):
    x_intersec = posicoes[j]
    ang1 = direcoes[j-1]
    ang2 = direcoes[j]

    # Linha tracejada estendendo a direção do fasor anterior
    extensao_l = 1.0
    ax.plot([x_intersec[0], x_intersec[0] + extensao_l * np.cos(ang1)],
            [x_intersec[1], x_intersec[1] + extensao_l * np.sin(ang1)],
            color='gray', linestyle='--', lw=1.2)

    # Desenha o arco do ângulo \Delta \phi
    arc_ang = np.linspace(ang1, ang2, 50)
    arc_radius = 0.7
    ax.plot(x_intersec[0] + arc_radius * np.cos(arc_ang),
            x_intersec[1] + arc_radius * np.sin(arc_ang), color='black', lw=1.0)

    # Texto da cota \Delta \phi posicionado no centro de cada arco correspondente
    ax.text(x_intersec[0] + (arc_radius + 0.4) * np.cos((ang1 + ang2)/2),
            x_intersec[1] + (arc_radius + 0.4) * np.sin((ang1 + ang2)/2),
            r'$\Delta \phi$', fontsize=11, ha='center', va='center')

# --- Ajustes Finais do Gráfico ---
ax.set_xlim(-1.5, x_fim + 2)
ax.set_ylim(-1.5, y_fim + 2)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()

plt.savefig('fasoresfinitos.png')
