import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

#DATA LOAD
try:
    wavenumber1, spectrum1= np.loadtxt('spettro1.dat', unpack=True, comments='#')
    wavenumber2, spectrum2= np.loadtxt('spettro1.dat', unpack=True, comments='#')

except FileNotFoundError:
    print("File 'spectra.dat' non trovato. Uso dati di esempio.")

Z = np.outer(spectrum2, spectrum1)

fig = plt.figure(figsize=(12, 12)) # SIZE

gs = GridSpec(nrows=2, ncols=2,
              width_ratios=[1, 3], height_ratios=[1, 3],
              left=0.06, right=0.95, bottom=0.12, top=0.90, # Margini della figura
              wspace=0.10, hspace=0.10) # Spaziatura tra i subplot


ax_2d = fig.add_subplot(gs[1, 1])            
ax_spec1 = fig.add_subplot(gs[0, 1], sharex=ax_2d) 
ax_spec2 = fig.add_subplot(gs[1, 0], sharey=ax_2d) 
ax_corner = fig.add_subplot(gs[0, 0])         

num_levels = 50 
contour_levels = np.linspace(np.min(Z), np.max(Z), num_levels)
ax_2d.contour(wavenumber1, wavenumber2, Z, levels=contour_levels, colors='black', linewidths=0.7)

x_min, x_max =800,4000 #X range
ax_2d.set_xlim(x_max, x_min) 
ax_2d.set_ylim(x_max, x_min)

ax_spec1.set_xlabel(r'Wave number, $\nu_1$, cm$^{-1}$', fontsize=11)
ax_spec1.xaxis.set_label_position('top')

ax_spec2.set_ylabel(r'Wave number, $\nu_2$, cm$^{-1}$', fontsize=11)

ax_2d.plot([x_max, x_min], [x_max, x_min], ls="--", color="grey", lw=1)


-
ax_spec1.plot(wavenumber1, spectrum1, color='black', lw=1)

plt.setp(ax_spec1.get_xticklabels(), visible=False)

ax_spec1.xaxis.tick_top()

ax_spec1.set_yticks([])
ax_spec1.set_yticklabels([])

ax_spec1.set_ylim(0, np.max(spectrum1) * 1.1 if np.max(spectrum1) > 0 else 1)



ax_spec2.plot(spectrum2, wavenumber2, color='red', lw=1) 

plt.setp(ax_spec2.get_yticklabels(), visible=False)

ax_spec2.yaxis.tick_left()

ax_spec2.set_xticks([])
ax_spec2.set_xticklabels([])

ax_spec2.set_xlim(0, np.max(spectrum2) * 1.1 if np.max(spectrum2) > 0 else 1)
ax_spec2.invert_xaxis() # Inverte l'asse x di ax_spec2 (intensità)

#font regulation x1
ax_spec1_twin = ax_spec1.secondary_xaxis('top') 
ax_spec1_twin.set_xlabel(r'Wavenumber, $\nu_1$, cm$^{-1}$', fontsize=11) 

ax_spec1.set_xlabel('')


#font regulation x2
ax_spec2_twin = ax_spec2.secondary_yaxis('left') 
ax_spec2_twin.set_ylabel(r'Wavenumber, $\nu_2$, cm$^{-1}$', fontsize=11) 

ax_spec2.set_ylabel('')

ax_corner.text(0.95, 0.75, r'$NM49(\nu_1)$', ha='right', va='top', fontsize=12, transform=ax_corner.transAxes)
ax_corner.text(0.25, 0.1, r'$NM49(\nu_2)$', ha='left', va='bottom', fontsize=12, transform=ax_corner.transAxes)
ax_corner.axis('off') # Nasconde gli assi del subplot d'angolo

plt.show()
