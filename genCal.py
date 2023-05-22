from fpdf import FPDF
import calendar

def main():
    input_year = ask_user("What year to generate a calendar?: ")
    #year = text_calendar(input_year)
    #print(year)
    generate_pdf(input_year)

# Implement verification
def ask_user(prompt):
    return int(input(prompt)) 

def text_calendar(year, month=1):
    c = calendar.TextCalendar(calendar.MONDAY)
    print(c.formatyear(year, m=3))
    return c.formatyear(year, m=3)
   


def generate_pdf(year):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", '', 8)
    pdf.cell(40, 10, text_calendar(year), new_x="LMARGIN", new_y="NEXT")
    pdf.output(f"Agenda{year}.pdf")

if __name__=="__main__":
    main()