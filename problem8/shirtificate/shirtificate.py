from fpdf import FPDF, Align


def main():
    pdf = PDF()
    pdf.add_page()
    pdf.print_shirt(input("Name: "))
    pdf.output("shirtificate.pdf")


class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", style="", size=64)
        # Moving cursor to the right:
        # Printing title:
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        # Performing a line break:

    def print_shirt(self, name):
        mid = (297-160)/2
        self.set_y(mid)
        self.image("shirtificate.png", w=170, x=Align.C)
        self.set_y(mid+60)
        self.set_font("helvetica", style="", size=30)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{name.title()} took CS50", align="C")


if __name__ == "__main__":
    main()
