import PyPDF2

# merge given PDF files into one PDF
def PDFmerge(pdfs, output):
    # creating pdf file merger object
    pdfMerger = PyPDF2.PdfFileMerger()
    # appending pdfs one by one
    for pdf in pdfs:
        with open(pdf, 'rb') as f:
            pdfMerger.append(f)
    # writing combined pdf to output PDF file
    with open(output, 'wb') as f:
        pdfMerger.write(f)


pdfs = ['f1_Beyond_Fintech_A_Pragmatic_Assessment_of_Disruptive_Potential_in_Financial_Services.pdf',
        'f2_WEF_A_Blueprint_for_Digital_Identity.pdf',
        'f3_WEF_The_future_of_financial_infrastructure.pdf',
        'f4_WEF_The_future_of_financial_services.pdf']
merge_output = 'f0_combined_file.pdf'
PDFmerge(pdfs=pdfs, output=merge_output)