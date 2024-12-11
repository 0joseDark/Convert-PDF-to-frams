import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os
import pdfplumber
import markdown

# Function to select the input folder
def select_input_folder():
    folder = filedialog.askdirectory(title="Select Input Folder")
    if folder:
        input_var.set(folder)

# Function to select the output folder
def select_output_folder():
    folder = filedialog.askdirectory(title="Select Output Folder")
    if folder:
        output_var.set(folder)

# Function to convert PDFs to Markdown
def convert_pdf_to_markdown():
    input_folder = input_var.get()
    output_folder = output_var.get()

    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return

    # List only PDF files in the input folder
    pdfs = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

    if not pdfs:
        messagebox.showwarning("Warning", "No PDF files found in the input folder.")
        return

    progress_bar["maximum"] = len(pdfs)
    progress_bar["value"] = 0

    try:
        for index, file in enumerate(pdfs):
            pdf_path = os.path.join(input_folder, file)
            md_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.md")

            try:
                # Extract text from the PDF
                with pdfplumber.open(pdf_path) as pdf:
                    text = ""
                    for page in pdf.pages:
                        extracted = page.extract_text()
                        if extracted:  # Check if text was extracted
                            text += extracted + "\n"

                # Check if any text was extracted
                if text.strip():
                    # Convert text to Markdown and save it
                    markdown_text = markdown.markdown(text)
                    with open(md_path, "w", encoding="utf-8") as md_file:
                        md_file.write(markdown_text)
                else:
                    messagebox.showwarning("Warning", f"Could not extract text from PDF: {file}")
            
            except Exception as pdf_error:
                messagebox.showerror("Error", f"Failed to process {file}: {pdf_error}")

            # Update progress bar
            progress_bar["value"] = index + 1
            percentage_var.set(f"{int((index + 1) / len(pdfs) * 100)}%")
            window.update_idletasks()

        messagebox.showinfo("Success", "Conversion completed successfully!")
    except Exception as e:
        # Capture unexpected errors
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Main window
window = tk.Tk()
window.title("PDF to Markdown Converter")

# Variables to store folder paths
input_var = tk.StringVar()
output_var = tk.StringVar()
percentage_var = tk.StringVar(value="0%")

# Labels and input fields
tk.Label(window, text="Input Folder Path:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
tk.Entry(window, textvariable=input_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(window, text="Select", command=select_input_folder).grid(row=0, column=2, padx=5, pady=5)

tk.Label(window, text="Output Folder Path:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
tk.Entry(window, textvariable=output_var, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(window, text="Select", command=select_output_folder).grid(row=1, column=2, padx=5, pady=5)

# Convert button
tk.Button(window, text="Convert", command=convert_pdf_to_markdown).grid(row=2, column=1, pady=10)

# Progress bar
progress_bar = ttk.Progressbar(window, length=400, mode="determinate")
progress_bar.grid(row=3, column=1, pady=10)

# Label to show percentage
tk.Label(window, textvariable=percentage_var).grid(row=4, column=1, pady=5)

# Exit button
tk.Button(window, text="Exit", command=window.quit).grid(row=5, column=1, pady=10)

# Main application loop
window.mainloop()
