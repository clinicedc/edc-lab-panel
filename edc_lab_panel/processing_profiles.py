from edc_lab import ProcessingProfile, disposable, sputum, wb

blood_glucose_processing = ProcessingProfile(name="Blood Glucose", aliquot_type=wb)
chemistry_alt_processing = ProcessingProfile(name="Chem + ALT", aliquot_type=wb)
fbc_processing = ProcessingProfile(name="FBC", aliquot_type=wb)
hba1c_processing = ProcessingProfile(name="HbA1c", aliquot_type=wb)
insulin_processing = ProcessingProfile(name="Insulin", aliquot_type=wb)
lft_processing = ProcessingProfile(name="LFT", aliquot_type=wb)
lipids_processing = ProcessingProfile(name="Lipids", aliquot_type=wb)
poc_processing = ProcessingProfile(name="POC", aliquot_type=disposable)
rft_processing = ProcessingProfile(name="RFT", aliquot_type=wb)
sputum_processing = ProcessingProfile(name="Sputum", aliquot_type=sputum)
vl_processing = ProcessingProfile(name="Viral load", aliquot_type=wb)
cd4_processing = ProcessingProfile(name="CD4", aliquot_type=wb)
