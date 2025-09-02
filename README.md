This project automatically creates vocab flashcard sets from the AP Pyschology textbook's bolded vocabulary words. This sets can be imported into quizlet to study.

Instructions: To create a vocab set run the command:

extract_vocab_from_pdf(pdf_path, output_csv, by_unit, by_module, chapters)

pdf_path; Path; is the relative path to the ap pysch textbool. Currently "Book.pdf"

output_csv; String; the name of the output file, ends in .csv for example: "Units1-5.cvs"

by_unit; Boolean; weather or not the flashcards will be generated based on units

by_module; Boolean; weather or not the flashcards will be generated based on modules

chapters; int list; the units or modules included in the set

Example set generation:

extract_vocab_from_pdf(pdf_file, "module9-14_23_60-63.csv", False,True,[9,10,11,12,13,14,23,60,61,62,63])

This will generate a set of flashcards for the modules 9,10,11,12,13,14,23,60,62,62 and 63 in the "module9-14_23_60-63.csv" file.
