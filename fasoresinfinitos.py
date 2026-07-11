import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# ============================================================
# Parâmetros
# ============================================================

R = 3.5                     # raio
phi = np.deg2rad(80)         # abertura angular

# Centro escolhido para que o arco comece na origem
C = np.array([0.0, R])

theta0 = -np.pi/2
theta1 = theta0 + phi

# Pontos inicial e final do arco
P0 = C + R*np.array([np.cos(theta0), np.sin(theta0)])
Pf = C + R*np.array([np.cos(theta1), np.sin(theta1)])

# ============================================================
# Figura
# ============================================================

fig, ax = plt.subplots(figsize=(8,8))
ax.set_aspect('equal')

# Circunferência completa (pontilhada)
t = np.linspace(0,2*np.pi,500)
ax.plot(C[0]+R*np.cos(t),
        C[1]+R*np.sin(t),
        ':',
        color='0.55',
        lw=1.3)

# Arco principal (contínuo preto)
ta = np.linspace(theta0,theta1,300)
ax.plot(C[0]+R*np.cos(ta),
        C[1]+R*np.sin(ta),
        color='black',
        lw=2.8)

# ============================================================
# Corda
# ============================================================

ax.annotate(
    "",
    xy=Pf,
    xytext=P0,
    arrowprops=dict(
        arrowstyle="->",
        color="crimson",
        lw=2.5,
        mutation_scale=25,
        shrinkA=0,
        shrinkB=0
    )
)

# Ponto médio da corda
Pm = 0.5*(P0+Pf)

# Linha centro -> ponto médio
ax.plot([C[0],Pm[0]],
        [C[1],Pm[1]],
        '--',
        color='forestgreen',
        lw=1.8)

# ============================================================
# Raios
# ============================================================

ax.plot([C[0],P0[0]],
        [C[1],P0[1]],
        '--',
        color='royalblue',
        lw=1.7)

ax.plot([C[0],Pf[0]],
        [C[1],Pf[1]],
        '--',
        color='royalblue',
        lw=1.7)

# ============================================================
# Centro
# ============================================================

ax.scatter(*C,s=35,color='black')
ax.text(C[0]-0.18,C[1]+0.18,r'$C$',fontsize=14)

# ============================================================
# Tangentes
# ============================================================

def tangent(theta):
    return np.array([-np.sin(theta), np.cos(theta)])

L = 0.9

t0 = tangent(theta0)
tf = tangent(theta1)

ax.arrow(P0[0],P0[1],
         L*t0[0],L*t0[1],
         head_width=0.08,
         head_length=0.12,
         fc='black',ec='black',
         length_includes_head=True)

ax.arrow(Pf[0],Pf[1],
         L*tf[0],L*tf[1],
         head_width=0.08,
         head_length=0.12,
         fc='black',ec='black',
         length_includes_head=True)

# ============================================================
# Cota do raio
# ============================================================

midR = 0.5*(C+Pf)
ax.text(midR[0]+0.1,
        midR[1],
        r'$R$',
        fontsize=14,
        color='royalblue')

# ============================================================
# Abertura angular phi
# ============================================================

arc_phi = Arc(C,
              1.2,
              1.2,
              angle=0,
              theta1=np.degrees(theta0),
              theta2=np.degrees(theta1),
              color='black',
              lw=1.2)

ax.add_patch(arc_phi)

theta_mid = theta0+0.2

ax.text(C[0]+0.75*np.cos(theta_mid),
        C[1]+0.75*np.sin(theta_mid),
        r'$\phi$',
        fontsize=14)

# ============================================================
# Comprimento do arco
# ============================================================

theta_arc = (theta0+theta1)/2

P_arc = C + (R+0.45)*np.array([np.cos(theta_arc),
                               np.sin(theta_arc)])

ax.text(P_arc[0]-0.23,
        P_arc[1]+0.15,
        r'$\sqrt{I_0}$',
        fontsize=14)

# ============================================================
# Cota da corda
# ============================================================

offset = np.array([0.18,-0.12])

ax.text(Pm[0]+offset[0],
        Pm[1]+offset[1],
        r'$\hat{\psi}_R$',
        color='crimson',
        fontsize=14)

# ============================================================
# Cotas das tangentes
# ============================================================

ax.text(P0[0]+0.30,
        P0[1]-0.23,
        r'$\hat{\psi}_1$',
        fontsize=14)

ax.text(Pf[0]+0.15,
        Pf[1]+0.25,
        r'$\hat{\psi}_f$',
        fontsize=14)

# ============================================================
# Aparência
# ============================================================

ax.set_xlim(-1.2,5.0)
ax.set_ylim(-1.0,5.5)

ax.axis('off')

plt.tight_layout()
plt.savefig('fasoresinfinitos.png')
