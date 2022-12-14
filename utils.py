import os
from tkinter import filedialog
import tkinter as tk
#import pdfplumber
from pylatexenc.latex2text import LatexNodes2Text
import csv
import xlsxwriter
class Utils:
    
    def __init__(self, inputPath, outputPath):
        self.inputPath = inputPath
        self.outputPath = outputPath
        
    """
    Provides dialog to open a file from lokal file system
    """
    def get_file(self):
        root = tk.Tk()
        root.withdraw()
        root.filename = filedialog.askopenfilename(
            initialdir="./", title="Select file", filetypes=(("all files", "*.*"), ("all files", "*.*")))
        return (root.filename)

    """
    Reads data from a give file path
    """
    def read_file(self, filename=False):
        if filename == False:
            filename = self.get_file()
        if filename.endswith(".tex"):
            texFileObj = open(os.path.join(self.inputPath, filename),
                            'r', encoding="utf-8")
            content = texFileObj.read()
            return LatexNodes2Text().latex_to_text(content)

        #elif filename.endswith('.pdf'):
            #with pdfplumber.open(os.path.join(self.inputPath, filename)) as pdf:
            #    text = ""
            #    for i in pdf.pages:
            #        text += " " + str(i.extract_text())
            #
            #    return text

        elif filename.endswith('.txt'):
            textFileObj = open(os.path.join(
                self.inputPath, filename), 'r', encoding="utf-8")
            content = textFileObj.read()
            return content

        else:
            print('Dieser Datentyp wird leider nicht unterstützt')

    """
    Saves data to text file
    """
    def save_txt(self, textsummary, filename=False, prefix=''):
        outfilename = 'summarized.txt'
        if filename != False:
            outfilename = os.path.basename(filename).replace(
                '.txt', prefix
            ).replace(
                '.pdf', prefix)

        with open(os.path.join(self.outputPath, outfilename), 'w') as f:
            f.write(textsummary)
            f.close()
            
    """
    Saves data to csv file
    """
    def save_csv(self, textsummary, filename=False, prefix=''):
        outfilename = 'generated_sentences.csv'
        if filename != False:
            outfilename = os.path.basename(filename).replace(
                '.txt', prefix
            ).replace(
                '.pdf', prefix)
        with open(os.path.join(self.outputPath, outfilename), 'w') as f:
            writer = csv.writer(f, 
                                delimiter=';',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
            for i in textsummary:
                writer.writerow(i)
    
    """
    Saves data to csv file
    """

    def save_xlsx(self, textsummary, filename=False, prefix=''):
        outfilename = 'generated_sentences.xlsx'
        if filename != False:
            outfilename = os.path.basename(filename).replace(
                '.txt', prefix
            ).replace(
                '.pdf', prefix)
        workbook = xlsxwriter.Workbook(os.path.join(self.outputPath, outfilename))
        worksheet = workbook.add_worksheet()
        row = 0
        col = 0
        
        # add header row
        header = [
            'Wahre Aussage',
            'Kontext (0/1)',
            'Syntax  (0/1)',
            'Falsche Aussage',
            'Kontext  (0/1)',
            'Syntax (0/1)',
            'Fachliche Einordnung (0/1)',
            'Plausibilität (0/1)',
            'Logik (0/1)',
            'Falschheit (0/1)',
            'Schwierigkeit (1-10)',
        ]
        col = 0
        for element in header:
            worksheet.write(row, col, element)
            col += 1
            
        # fill data
        row = 1
        col = 0
        #worksheet.set_row(0, 1, 40)
        link_format = workbook.add_format({
            #'color': 'blue',
            'text_wrap': True,
            'align':'left',
            'valign':'top'
            })
        for item in textsummary:
            worksheet.write(row, 0, item[0], link_format)
            worksheet.write(row, 3, item[1], link_format)
            # worksheet.set_row(row, 1, 25)
            row += 1
        
        workbook.close()
            
            
            
  


    
