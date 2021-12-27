import pandas as pd
import matplotlib.pyplot as plt
import pyupset as pyu
import upsetplot as up

plt.ion()
plt.rc('font',size=24)

"""
Names = ["Healthy_results_eletrofi_Rmd_Rms_5params_equal_len_diam_Refinement_Boolean.csv",
         "Hyper_results_eletrofi_Rmd_Rms_5params_equal_len_diam_Refinement_Boolean.csv",
         "Normal_results_eletrofi_Rmd_Rms_5params_equal_len_diam_Refinement_Boolean.csv",
         "Hypo_results_eletrofi_Rmd_Rms_5params_equal_len_diam_Refinement_Boolean.csv"]

Names = ["Healthy_results_eletrofi_Rmd_Rms_5params_equal_len_diam_APCharacteristics_Boolean.csv",
         "Hyper_results_eletrofi_Rmd_Rms_5params_equal_len_diam_APCharacteristics_Boolean.csv",
         "Normal_results_eletrofi_Rmd_Rms_5params_equal_len_diam_APCharacteristics_Boolean.csv",
         "Hypo_results_eletrofi_Rmd_Rms_5params_equal_len_diam_APCharacteristics_Boolean.csv"]

Names = ["Healthy_results_PassiveProperties_milhao_Boolean.csv",
         "Hyper_results_PassiveProperties_milhao_Boolean.csv", 
         "Normal_results_PassiveProperties_milhao_Boolean.csv", 
         "Hypo_results_PassiveProperties_milhao_Boolean.csv"] 

Names = ["Healthy_results_Passive_Refinement_milhao_Boolean.csv",
         "Hyper_results_Passive_Refinement_milhao_Boolean.csv", 
         "Normal_results_Passive_Refinement_milhao_Boolean.csv", 
         "Hypo_results_Passive_Refinement_milhao_gain_Boolean.csv"] 

Names = ["Healthy_results_Refinement_milhao_Boolean.csv",
         "Hyper_results_Refinement_milhao_Boolean.csv", 
         "Normal_results_Refinement_milhao_Boolean.csv", 
         "Hypo_results_Refinement_milhao_Boolean.csv"] 
"""

Names = ["Results_contador_Healthy_Refinement_boolean.csv",
         "Results_contador_Hyper_Refinement_boolean.csv",
         "Results_contador_Normal_Refinement_boolean.csv",
         "Results_contador_Hypo_Refinement_boolean.csv"]

Title = ["A","B","C","D"]
    
fig_list = []
plt.ion()

#db = pd.read_csv(Names[0])
#data = db.groupby(db.columns.tolist(),as_index=True)


for i,n in enumerate(Names):
    
    fig_list.append(plt.figure())
    db = pd.read_csv(n)

    #db=db.drop('Unnamed: 0', axis = 1)
    data = db.groupby(db.columns.tolist(),as_index=True).size()
    
    #faithful_data = DataFrame.from_csvfile(n, sep = " ")
    #m = make_comb_mat(faithful_data)
    #UpSet(m)
    
    set_order=('Gld','Gls','diam','diam_soma','gcal','gks','gnap','Ld') #sort_by='None'

    myplot=up.UpSet(data,show_counts=True,show_percentages=True,element_size=140,intersection_plot_elements=3)
    myplot.plot(fig=fig_list[-1])  
    fig_list[-1].set_size_inches((20,10)) 
    plt.rc('font',size=24)
    plt.title(Title[i],loc='right')
    
    # Save the 4 plots
    fig_list[-1].savefig("fig"+str(i)+"_MN.png")
plt.close('all')
print("Saved: 4 individual plots")

import matplotlib.image as mpimg
# CREATE SUBPLOTS FROM TEMPORAL IMAGES

f, axarr = plt.subplots(2, 2, figsize=(20,10))
axarr.shape = (2,max(axarr.shape))


axarr[0,0].imshow(mpimg.imread('fig0_MN.png'))
axarr[0,0].set_xticks(())
axarr[0,0].set_yticks(())
axarr[0,0].spines['right'].set_visible(False)
axarr[0,0].spines['top'].set_visible(False)
axarr[0,0].spines['left'].set_visible(False)
axarr[0,0].spines['bottom'].set_visible(False)
plt.tight_layout(0.1)

axarr[0,1].imshow(mpimg.imread('fig1_MN.png'))
axarr[0,1].set_xticks(())
axarr[0,1].set_yticks(())
axarr[0,1].spines['right'].set_visible(False)
axarr[0,1].spines['top'].set_visible(False)
axarr[0,1].spines['left'].set_visible(False)
axarr[0,1].spines['bottom'].set_visible(False)
plt.tight_layout(0.1)

axarr[1,0].imshow(mpimg.imread('fig2_MN.png'))
axarr[1,0].set_xticks(())
axarr[1,0].set_yticks(())
axarr[1,0].spines['right'].set_visible(False)
axarr[1,0].spines['top'].set_visible(False)
axarr[1,0].spines['left'].set_visible(False)
axarr[1,0].spines['bottom'].set_visible(False)
plt.tight_layout(0.1)

axarr[1,1].imshow(mpimg.imread('fig3_MN.png'))
axarr[1,1].set_xticks(())
axarr[1,1].set_yticks(())
axarr[1,1].spines['right'].set_visible(False)
axarr[1,1].spines['top'].set_visible(False)
axarr[1,1].spines['left'].set_visible(False)
axarr[1,1].spines['bottom'].set_visible(False)
plt.tight_layout(0.1)

plt.tight_layout(0.1)
#plt.savefig("artigo_PassiveProperties_upset.png")
#plt.savefig("artigo_APCharacteristics_upset.png")
plt.savefig("artigo_Refinement_upset_params.png")
