import extract_text_from_pdf as ext

pdf0 = 'f0_combined_file.pdf'
output0 = 'cleaned_text_combined_file.csv'
ext.textExtract(pdf=pdf0, output=output0)

pdf1 = 'f1_Beyond_Fintech_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services.pdf'
output1 = 'cleaned_text_file_1.csv'
ext.textExtract(pdf=pdf1, output=output1)

pdf2 = 'f2_WEF_A_Blueprint_for_Digital_Identity.pdf'
output2 = 'cleaned_text_file_2.csv'
ext.textExtract(pdf=pdf2, output=output2)

pdf3 = 'f3_WEF_The_future_of_financial_infrastructure.pdf'
output3 = 'cleaned_text_file_3.csv'
ext.textExtract(pdf=pdf3, output=output3)

pdf4 = 'f4_WEF_The_future_of_financial_services.pdf'
output4 = 'cleaned_text_file_4.csv'
ext.textExtract(pdf=pdf4, output=output4)

# output5 = 'cleaned_text_combined_file_origin_sort.csv'
# ext.textExtract(pdf=pdf0, output=output5)