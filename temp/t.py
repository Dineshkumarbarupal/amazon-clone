import zipfile
from fpdf import FPDF
from pathlib import Path
import requests

# Step 1: Prepare folder
base_path = Path("cheatsheet_package")
base_path.mkdir(parents=True, exist_ok=True)
pdf_path = base_path / "JS_jQuery_CheatSheet.pdf"
font_regular = base_path / "DejaVuSans.ttf"
font_bold = base_path / "DejaVuSans-Bold.ttf"

# Step 2: Download fonts
font_urls = {
    font_regular: "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/DejaVuSans.ttf",
    font_bold: "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/DejaVuSans-Bold.ttf",
}

for path, url in font_urls.items():
    if not path.exists():
        response = requests.get(url)
        path.write_bytes(response.content)

# Step 3: Create PDF
class PDF(FPDF):
    def header(self):
        self.set_font("DejaVu", "B", 14)
        self.cell(0, 10, "Mini JavaScript + jQuery CheatSheet", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("DejaVu", "B", 12)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def chapter_body(self, body):
        self.set_font("DejaVu", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

pdf.add_font("DejaVu", "", str(font_regular), uni=True)
pdf.add_font("DejaVu", "B", str(font_bold), uni=True)

sections = [
    ("1. Element Select करना", 
     "JavaScript:\n- By ID: document.getElementById(\"id\")\n- By class: document.querySelector(\".class\")\n- By tag: document.querySelectorAll(\"li\")\n\n"
     "jQuery:\n- By ID: $(\"#id\")\n- By class: $(\".class\")\n- By tag: $(\"li\")"),
    
    ("2. Click Event लगाना",
     "JavaScript:\n- el.addEventListener(\"click\", function() { ... })\n\n"
     "jQuery:\n- $(\"#btn\").on(\"click\", function() { ... });"),
    
    ("3. Show / Hide करना",
     "JavaScript:\n- Show: el.style.display = \"block\"\n- Hide: el.style.display = \"none\"\n\n"
     "jQuery:\n- Show: $(\".menu\").show()\n- Hide: $(\".menu\").hide()\n- Toggle: $(\".menu\").toggle()"),
    
    ("4. Class Add / Remove / Toggle करना",
     "JavaScript:\n- Add: el.classList.add(\"active\")\n- Remove: el.classList.remove(\"active\")\n- Toggle: el.classList.toggle(\"active\")\n\n"
     "jQuery:\n- Add: $(\".box\").addClass(\"active\")\n- Remove: $(\".box\").removeClass(\"active\")\n- Toggle: $(\".box\").toggleClass(\"active\")"),
    
    ("5. Inner Text या HTML बदलना",
     "JavaScript:\n- Text: el.textContent = \"Hello\"\n- HTML: el.innerHTML = \"<b>Hi</b>\"\n\n"
     "jQuery:\n- Text: $(\"#el\").text(\"Hello\")\n- HTML: $(\"#el\").html(\"<b>Hi</b>\")"),
    
    ("6. Input Value लेना",
     "JavaScript:\n- let val = document.getElementById(\"myInput\").value;\n\n"
     "jQuery:\n- let val = $(\"#myInput\").val();"),
    
    ("Bonus: See All / See Less Toggle Example (jQuery)",
     "$(\"#toggleLink\").on(\"click\", function(e) {\n"
     "  e.preventDefault();\n"
     "  $(\".submenu\").slideToggle();\n"
     "  let isExpanded = $(this).text() === \"See Less\";\n"
     "  $(this).text(isExpanded ? \"See All\" : \"See Less\");\n"
     "});")
]

for title, body in sections:
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf.output(str(pdf_path))

# Step 4: Create zip file
zip_path = "JS_jQuery_CheatSheet_Package.zip"
with zipfile.ZipFile(zip_path, 'w') as zipf:
    zipf.write(pdf_path, pdf_path.name)
    zipf.write(font_regular, font_regular.name)
    zipf.write(font_bold, font_bold.name)

print(f"✅ All done! ZIP file created at: {zip_path}")
