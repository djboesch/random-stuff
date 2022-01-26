import pickle
from matplotlib import pyplot as plt
import numpy as np

with open(r'C:\Users\rest\of\path', 'rb') as f:
    data = pickle.load(f)
    print("sucessfully loaded")
   


pae_output = (data['predicted_aligned_error'],
              data['max_predicted_aligned_error'])

plt.subplot(1, 1, 1)
pae, max_pae = pae_output
plt.imshow(pae, vmin=0., vmax=max_pae, cmap='Greens_r')
plt.colorbar(fraction=0.046, pad=0.04)

plt.title('Predicted Aligned Error')
plt.xlabel('Scored residue')
plt.ylabel('Aligned residue')

plt.show()
