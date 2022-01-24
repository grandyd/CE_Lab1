import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import cmath

def graph(t,S,j):
   plt.plot(t, S[:,0], 'o-', linewidth = 1, label ='x(t)')
   plt.plot(t, S[:,1], 'o-', linewidth = 1, label ='y(t)')
   plt.xlabel('t')
   plt.ylabel('x(t)    y(t)')
   plt.legend()
   plt.grid()
   if j==0:
      name='graph_uzel'
   else:
      name='graph_focus'
   plt.savefig(name+'.png', bbox_inches='tight')
   plt.show()

def plot(t,S,j):
   plt.plot(S[:,0], S[:,1], 'o-', linewidth = 1)
   plt.axis([-20, 20, -20, 20])
   plt.xlabel('x')
   plt.ylabel('y')
   plt.grid()
   if j==0:
      name='plot_uzel'
   else:
      name='plot_focus'
   plt.savefig(name+'.png', bbox_inches='tight')
   plt.show()

 

def plot_afch(AFCH,j):
   plt.plot(AFCH.real, AFCH.imag, 'o-', label = 'АФЧХ')
   plt.xlabel('Re')
   plt.ylabel('Im')
   plt.legend()
   plt.grid()
   if j==0:
      name='AFCH_uzel'
   else:
      name='AFCH_focus'
   plt.savefig(name+'.png', bbox_inches='tight')
   plt.show()
#
#! График АЧХ
def plot_ach(t,ACH,j):
   plt.plot(t, ACH, 'o-', label = 'АЧХ')
   plt.xlabel('v')
   plt.ylabel('A(v)')
   plt.legend()
   plt.grid()
   if j==0:
      name='ACH_uzel'
   else:
      name='ACH_focus'
   plt.savefig(name+'.png', bbox_inches='tight')
   plt.show()

def plot_fch(t,FCH,j):
   plt.plot(t, FCH, 'o-', label = 'ФХЧ')
   plt.xlabel('v')
   plt.ylabel('phi(v)')
   plt.legend()
   plt.grid()
   if j==0:
      name='FCH_uzel'
   else:
      name='FCH_focus'
   plt.savefig(name+'.png', bbox_inches='tight')
   plt.show()

if __name__=='__main__':
   for j in range(2):
      if j==0:
         # уст узел
         omega=delta=0.5
      else:
         # уст фокус
         omega,delta=1,0.2


      def dx_dy(s, t):
         dx = s[1]
         dy = -(omega ** 2) * s[0] - (2 * delta) * s[1]
         return [dx, dy]


      t = np.linspace(0, 6)
      XY = [-1, 19]  # начальная точка
      S = odeint(dx_dy, XY, t)  # решение ОДУ

      graph(t,S,j)
      plot(t,S,j)
      a = 2
      i = 0


      AFCH = (a)/((omega**2) - (t**2) + (2*delta*t*1j))                   #Вычисление АФЧХ
      ACH = np.absolute(AFCH)                                             #АЧХ=|АФЧХ|

      FCH = []                                                            #ФЧХ=arg(АФЧХ)
      while i < len(t):
         phi = cmath.phase(AFCH[i])
         FCH.append(phi)
         i +=1
      plot_afch(AFCH,j)
      plot_ach(t,ACH,j)
      plot_fch(t,FCH,j)
