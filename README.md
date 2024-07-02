The code is split into two parts. The first part contains the analytical energy method as described in S. Zhang's 1999 PhD thesis "The Mechanics of Ship Collisions". 

This thesis is split into two parts: The first part contains a rigid body analysis to determine the total global energy loss, while the second part contains an in-depth analysis in material failure energy and attenuation losses.
The first part is covered from pages 8-22, and is contained in the directory "EnergyEstimation". 
The second part is covered from pages 74-135, and is contained in the directory "DeflectionEstimation". 

NOTE: Errors may be present in the code. Care has been taken to filter these out, but it is not guaranteed.

The second part of the code itself is used to process the raw output from LS-DYNA simulations. 
This is contained within the directory "LSDYNAProcessing". An additional directory named "LSDynaVerification" exists to compare the results from LS-DYNA and the analytical results from above.

This is a project done as part of a half-year tenure at Holland Shipyards, as part of their partnership with SH2IPDRIVE. 

There will be no further updates to the code as of the 2nd of July, 2024. 
No attempts to fix any existing bugs will be done. 
No attempts will be made to keep the code up to date. 
