import fitz 
import csv
import re
from pathlib import Path



def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for symbol in reversed(roman):
        if symbol in roman_dict:
            value = roman_dict[symbol]
            if value < prev_value:
                result -= value  # Subtract if smaller value comes before larger value
            else:
                result += value  # Add if larger or equal value comes before
            prev_value = value
        else:
            return -1
    if result == 0: 
        return -1
    return result


def extract_vocab_from_pdf(pdf_path, output_csv, byUnit, byModule, groupedModules):
    doc = fitz.open(pdf_path)
    vocab_list = []
    start_unit = 1
    start_module = 1
    i = 0 

    for page in doc:
        if page ==0:
            page = 40
        

        i +=1
        if i> 1500:
            break
        if True:#i == 55 or i == 56 or i ==57:
            text = page.get_text("text")
        
            # Detect bolded vocab words (assumed format: 'word  definition.') notice doulbe space and period end
           
            unit_number = start_unit
            unit_position = text.find("Unit")
            if unit_position != -1:  # Check if "unit" was found
                 # Slice the string after "unit" and get the Roman numeral
                unit_roman = text[unit_position + len("Unit"):].strip().split()[0]  # Get the first word after "unit"
    
            #    # Convert the Roman numeral to an integer
                unit_num = roman_to_int(unit_roman)
                
                if unit_num != -1:
                    unit_number = unit_num
            
            module_number = start_module
            mod_position = text.find("Module")
            if mod_position != -1:  # Check if "unit" was found
                 # Slice the string after "unit" and get the Roman numeral
                mod_number = text[mod_position + len("Module"):].strip().split()[0]  # Get the first word after "unit"
                if mod_number.isdigit():
                    module_number = mod_number
                    module_number = int(mod_number)
                    #print(module_number)
           
            if byModule and start_module != module_number:
                
                if groupedModules == []:
                    # Save to CSV
                    if vocab_list != []:
                        output_csv = "Module " + str(start_module) + ".csv"
                        with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(["Term", "Definition"])
                            writer.writerows(vocab_list)
                            
                
                elif start_module in groupedModules:
                    print("valid")
                    print(start_module)
                    if vocab_list != []:
                        print("worete module")
                        #output_csv = "Module " + str(start_module) + ".csv"

                        with open(output_csv, "a", newline="", encoding="utf-8") as csvfile:
                            writer = csv.writer(csvfile)
    
                            # Only write the header if the file is empty
                            if csvfile.tell() == 0:  
                                writer.writerow(["Term", "Definition"])
    
                            writer.writerows(vocab_list)  # Append new data without deleting old content

                start_module = module_number
                vocab_list = []
                

            
            elif byUnit and start_unit != unit_number:
                if vocab_list != []:
                    output_csv = "Unit " + str(start_unit) + ".csv"
                    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(["Term", "Definition"])
                        writer.writerows(vocab_list)
                start_unit = unit_number
                vocab_list = []

            matches = re.findall(r'([A-Za-z\s]+)\s{2,}(.*?)(?=\s*\.)', text.replace("\n", ""))
        
            for word, definition in matches:
                word = word.strip()
                definition = definition.strip()
                if len(word) > 0 and len(definition) > 0:
                    if "Module" not in word and "Module" not in definition:
                        if "Unit" not in word and "Unit" not in definition:
                            if not word[0].isupper() and not definition[0].isupper():
                              
                                vocab_list.append([word.replace(","," "), definition.replace(","," ")])
 
   

# Example usage
BASE_DIR = Path(__file__).resolve().parent   # the TextBookScanner folder
pdf_file = BASE_DIR / "Book.pdf"
#pdf_file = pdf_file = r"C:\Users\xavar\OneDrive\Documents\VS_Code\TextBookScanner\Book.pdf" 
output_file = "module9-14_23_60-63.csv"
extract_vocab_from_pdf(pdf_file, output_file, False,True,[9,10,11,12,13,14,23,60,61,62,63])
