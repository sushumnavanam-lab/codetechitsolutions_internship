from fpdf  import FPDF

#step1
#reading the data
def read_the_file(filename="information.txt"):
  try:
     with open(filename, "r") as f:
       content = f.read()
     return content   
  except FileNotFoundError:
    print("file doesnot exist")
    return ""

#step 2
#analyzing the data
def analyzing_the_data(text):
   words = text.split()
   wc=len(words) #count of words
   cc=len(text) #count of characters.
   lc= len(text.splitlines())#count of number of lines
   
   #to find shortest and longest words in a text
   if words:
     longestwords=max(words,key=len)
     shortestwords=min(words,key = len)
    #if empty 
   else:
    longestwords=""
    shortestwords=""
   return wc,cc,lc,longestwords,shortestwords

#step 3
#creating a pdf
pdf=FPDF(format ='A4')


#setting the pdf size like margin
pdf.set_margins(10,15,10)
pdf.add_page()

#setting the font
pdf.set_font("Times","B",20)


#displaying the heading of the pdf
pdf.cell(200, 10, "Automated Report", ln=True, align="C")
pdf.ln(5)

#get the data from the file
text=read_the_file()

#analyzing the data
data=analyzing_the_data(text)

#summary heading
pdf.set_font("Arial", "B", 15)
pdf.cell(200, 11, "Summary", ln=True)

# summary values
pdf.set_font("Arial", "", 12)
pdf.cell(200, 8, "Word Count: " + str(data[0]), ln=True)
pdf.cell(200, 8, "Character Count: " + str(data[1]), ln=True)
pdf.cell(200, 8, "Line Count: " + str(data[2]), ln=True)
pdf.cell(200, 8, "Longest Word: " + data[3], ln=True)
pdf.cell(200, 8, "Shortest Word: " + data[4], ln=True)

# space
pdf.ln(10)

# original content heading
pdf.set_font("Times", "B", 14)
pdf.cell(200, 10, "Original Content", ln=True)

# content
pdf.set_font("Times", "", 12)
pdf.multi_cell(0, 7, text)

# save pdf
pdf.output("output.pdf")

print("PDF created successfully!")


   


  