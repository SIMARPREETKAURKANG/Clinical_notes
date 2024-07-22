import tkinter
from tkinter import ttk
from tkinter import font as tkfont

service_providers = ["Dr. Sivendra", "Dr. Mobini"]
isolation_options = ["CRI", "DRI angle"]
matrix_options = ["Sectional", "V3 Ring", "Garrison Ring", "Contour Wedge", "Contour Band", "Mylar Strip"]
protocol_options = ["XTR", "One Coat", "AE+Solo", "Surefil, Sonicfil A2", "Surefil, TPH A", "Surefil, Brilliant A2/B2"]
occlusion_options = ["Checked", "Adjusted", "Good", "Finished margins", "Contour", "Polish"]
post_treatment_options = ["Gingival irritation", "possible post-op sensitivity"]
additional_instructions_options = [
    "Informed patient of the need to be cautious of lip/cheek/tongue injury as frozen",
    "Advised to wait until anesthesia wears off before eating/drinking hot to avoid injury"
]
additional_instructions_displayedText = ["Lip/cheek/tongue injury","Anesthesia - to avoid injury"]
ipac_options = [
    "RCDSO, CDHO, IPAC Guidelines followed by all treating staff. Class 4 indicator inside.",
    "Pouches turned brown indicating autoclave processed.",
]
# TODO: Second blank in 3rd option
anesthetic_options = [
    "Topical 2% Lidocaine, with epi 1:100Tx 1 carp, Quad ____, INFIL/ IANB",
    "Topical 4% Articaine, with epi 1:100Tx 1 carp, Quad ____, INFIL/ IANB",
    "Topical 3% Carbocaine, no epi, ??? carp, Quad ____, INFIL/ IANB"
]

def enter_data():
    # Get data from widgets
    selected_providers = [provider for provider, var in serviceProviders_selected.items() if var.get() == 1]
    serviceProvider = ", ".join(selected_providers)

    billing_Info_lines = billingInfo_text.get("1.0", tkinter.END).strip().split("\n")
    billedBy = billedBy_entry.get()
    formatted_billing_info = "\n".join([line for line in billing_Info_lines if line.strip() and not line.strip().endswith(")")])
   
    nextAppointments_lines = nextAppointments_text.get("1.0", tkinter.END).strip().split("\n")
    formatted_nextAppointments = "\n".join([line for line in nextAppointments_lines if line.strip() and not line.strip().endswith(")")])

    medical_history_reviewed = "Medical History Reviewed" if medical_history_var.get() == 1 else ""
    changes = f"Changes: {changes_var.get()}"
    vic_from = "Tx discussed. Obtained VIC from: " + ", ".join([key for key, var in vic_from_vars.items() if var.get() == 1])

    selected_anesthetics = []
    for i, (var, entry, value) in enumerate(zip(anesthetic_checkbox_vars, anesthetic_entry_vars, option_variables)):
        if var.get() == 1:
            option = anesthetic_options[i]
            parts = option.split("____")
            if i == 2:
                parts = option.split("???")
                entry_value = entry.get()
                second_part = parts[1].strip().split("____")
                entry2 = thirdOption_entry.get()
                dropdown = value.get()
                formatted_option = f"{parts[0].strip()} {entry_value} {second_part[0].strip()} {entry2}, {dropdown}"
            else:
                entry_value=entry.get()
                dropdown = value.get()
                formatted_option = f"{parts[0].strip()} {entry_value}, {dropdown}"
            selected_anesthetics.append(formatted_option)
    
    anesthetic = "\n".join(selected_anesthetics)

    isolation_selected = [isolation_options[i] for i, var in enumerate(isolation_vars) if var.get() == 1]
    isolation = ", ".join(isolation_selected)
    matrix_selected = [matrix_options[i] for i, var in enumerate(matrix_vars) if var.get() == 1]
    matrix = ", ".join(matrix_selected)
    protocol_selected = [protocol_options[i] for i, var in enumerate(protocol_vars) if var.get() == 1]
    protocol = ", ".join(protocol_selected)
    occlusion_selected = [occlusion_options[i] for i, var in enumerate(occlusion_vars) if var.get() == 1]
    occlusion = ", ".join(occlusion_selected)
    post_treatment_selected = [post_treatment_options[i] for i, var in enumerate(post_treatment_vars) if var.get() == 1]
    post_treatment = ", ".join(post_treatment_selected)
    additional_instructions_selected = []
    for i, var in enumerate(additional_instructions_vars):
        if var.get() == 1:
            additional_instructions_selected.append(additional_instructions_options[i])
    additional_instructions = "\n".join(additional_instructions_selected)

    ipac_selected=[]
    for i, var in enumerate(ipac_vars):
        if var.get() == 1:
            ipac_selected.append(ipac_options[i])
    ipac ="\n".join(ipac_selected)

    # Example: Format the data for display in the text widget
    formatted_data = f"Service Provider: {serviceProvider}\n" \
                     f"\n------------------------------------------\n"\
                     f"Billing \n\n{formatted_billing_info}\n" \
                     f"\nBilled By: {billedBy}\n" \
                     f"\n------------------------------------------\n"\
                     f"Next Appointments:\n\n{formatted_nextAppointments}\n" \
                     f"\n------------------------------------------\n"\
                     f"Treatment Plan\n"\
                     f"\n------------------------------------------\n"\
                     f"Pretreatment Protocols\n\n{medical_history_reviewed}\n"\
                     f"{changes}\n" \
                     f"{vic_from}\n"\
                     f"\n------------------------------------------\n"\
                     f"Local Anesthetic & Preparation: \n\n{anesthetic}\n" \
                     f"\n------------------------------------------\n"\
                     f"Operative Procedure\n\n"\
                     f"Isolation: {isolation}\n" \
                     f"Matrix: {matrix}\n" \
                     f"Protocol: {protocol}\n" \
                     f"Occlusion: {occlusion}\n\n" \
                     f"Contact: {'Achieved' if contact_var.get() == 1 else ''}\n\n" \
                     f"Post-Treatment: {post_treatment}\n" \
                     f"\n------------------------------------------\n"\
                     f"Additional Instructions:\n\n{additional_instructions}\n"\
                     f"\n------------------------------------------\n" \
                     f"IPAC\n\n"\
                     f"{ipac}"  
                     

    # Clear previous content and insert new formatted data
    submitted_data_text.delete("1.0", tkinter.END)
    submitted_data_text.insert(tkinter.END, formatted_data)

def copy_text():
    # Get all the text
    text = submitted_data_text.get("1.0", "end-1c")
    
    # Copy the text to the clipboard
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update() 

def clear_text():
    submitted_data_text.delete('1.0', tkinter.END)

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

def handle_checkbox_change():
    for i in range(len(anesthetic_options)):
        if anesthetic_checkbox_vars[i].get() == 1:
            anesthetic_entry_vars[i].config(state=tkinter.NORMAL)
            option_dropdowns[i].config(state=tkinter.NORMAL)
            if i==2:
                anesthetic_entry_vars[i+1].config(state=tkinter.NORMAL)
        else:
            anesthetic_entry_vars[i].delete(0, tkinter.END)
            anesthetic_entry_vars[i].config(state=tkinter.DISABLED)
            option_dropdowns[i].config(state=tkinter.DISABLED)
            if i==2:
                anesthetic_entry_vars[i+1].delete(0,tkinter.END)
                anesthetic_entry_vars[i+1].config(state=tkinter.DISABLED)

window = tkinter.Tk()
window.title("Clinical Notes Form")
window.state('zoomed')  # Set window to maximized view

# Create a canvas and a scrollbar
canvas = tkinter.Canvas(window)
scrollbar = tkinter.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=scrollbar.set)

frame = tkinter.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Bind the canvas to the frame size
frame.bind("<Configure>", on_frame_configure)

# Form title
title_frame = tkinter.LabelFrame(frame, text="")
title_frame.grid(row= 0, column=0)

title_label = tkinter.Label(title_frame, text="DR Billing")
title_label.grid(row= 0, column=0)

# DDS Billing Service Provider
serviceProvider_frame = tkinter.LabelFrame(frame, text="DDS Billing Service Provider")
serviceProvider_frame.grid(row= 1, column=0)

serviceProvider_label = tkinter.Label(serviceProvider_frame, text="Service Provider: ")
serviceProvider_label.grid(row = 0, column= 0)

serviceProviders_selected = {}
# Loop through the service providers and create a checkbox for each
for i, provider in enumerate(service_providers):
    var = tkinter.IntVar()
    serviceProviders_selected[provider] = var
    checkbox = tkinter.Checkbutton(serviceProvider_frame, text=provider, variable=var)
    checkbox.grid(row=0, column=i+1)

# Billing
billing_frame = tkinter.LabelFrame(frame, text="Billing")
billing_frame.grid(row= 2, column=0)

billing_label =  tkinter.Label(billing_frame, text="(Services Codes, Tooth #, Surfaces, Lab)")
billing_label.grid(row= 0, column=0)

billingInfo_text = tkinter.Text(billing_frame, height=5, width=55)
billingInfo_text.grid(row=1, column=0, columnspan=2)
for i in range(1, 6):
    billingInfo_text.insert(f"{i}.0", f"{i}) \n")

billedBy_label = tkinter.Label(billing_frame, text="Billed By: ")
billedBy_label.grid(row= 6, column=0)

billedBy_entry = tkinter.Entry(billing_frame)
billedBy_entry.grid(row=6, column=1)


# Next Appointments
nextAppointments_frame = tkinter.LabelFrame(frame, text="Next Appointments")
nextAppointments_frame.grid(row= 3, column=0)

nextAppointments_label =  tkinter.Label(nextAppointments_frame, text="(Jobs, Units, Provider)")
nextAppointments_label.grid(row= 0, column=0)

nextAppointments_text = tkinter.Text(nextAppointments_frame, height=5, width=55)
nextAppointments_text.grid(row=1, column=0, columnspan=2)
for i in range(1, 6):
    nextAppointments_text.insert(f"{i}.0", f"{i}) \n")

# TODO: TreatmentPlan
treatmentPlan_frame = tkinter.LabelFrame(frame, text="Treatment Plan")
treatmentPlan_frame.grid(row= 4, column=0)

treatmentPlan_label = tkinter.Label(treatmentPlan_frame, text="(Enter directly into Tx Plan Notes, if not copy into Tx Plan Notes)")
treatmentPlan_label.grid(row=0,column=0)

# Pretreatment Protocols
pretreatmentProtocols_frame = tkinter.LabelFrame(frame, text="Pretreatment Protocols")
pretreatmentProtocols_frame.grid(row= 5, column=0)

medical_history_var = tkinter.IntVar(value=1)
medical_history_checkbox = tkinter.Checkbutton(pretreatmentProtocols_frame, text="Medical History Reviewed", variable=medical_history_var)
medical_history_checkbox.grid(row=0, column=0)

changes_label = tkinter.Label(pretreatmentProtocols_frame, text="Changes:")
changes_label.grid(row=1, column=0)
changes_var = tkinter.StringVar(value="No")
changes_yes_radiobutton = tkinter.Radiobutton(pretreatmentProtocols_frame, text="Yes", variable=changes_var, value="Yes")
changes_yes_radiobutton.grid(row=1, column=1)
changes_no_radiobutton = tkinter.Radiobutton(pretreatmentProtocols_frame, text="No", variable=changes_var, value="No")
changes_no_radiobutton.grid(row=1, column=2)

tx_discussed_var = tkinter.IntVar(value=1)
tx_discussed_checkbox = tkinter.Checkbutton(pretreatmentProtocols_frame, text="Tx discussed. Obtained VIC from:", variable=tx_discussed_var)
tx_discussed_checkbox.grid(row=2, column=0)

vic_from_vars = {"Patient": tkinter.IntVar(), "Parent": tkinter.IntVar(), "Guardian": tkinter.IntVar()}
vic_from_patient_checkbox = tkinter.Checkbutton(pretreatmentProtocols_frame, text="Patient", variable=vic_from_vars["Patient"])
vic_from_patient_checkbox.grid(row=3, column=1)
vic_from_parent_checkbox = tkinter.Checkbutton(pretreatmentProtocols_frame, text="Parent", variable=vic_from_vars["Parent"])
vic_from_parent_checkbox.grid(row=3, column=2)
vic_from_guardian_checkbox = tkinter.Checkbutton(pretreatmentProtocols_frame, text="Guardian", variable=vic_from_vars["Guardian"])
vic_from_guardian_checkbox.grid(row=3, column=3)

# Local Anesthetic & Preparation
anesthetic_frame = tkinter.LabelFrame(frame, text="Local Anesthetic & Preparation")
anesthetic_frame.grid(row=6, column=0)

anesthetic_label = tkinter.Label(anesthetic_frame, text ="Select any one: ")
anesthetic_label.grid(row= 0, column=0)

anesthetic_checkbox_vars = []
anesthetic_entry_vars = []
# for i, option in enumerate(anesthetic_options):
#     var = tkinter.IntVar()
#     checkbox = tkinter.Checkbutton(anesthetic_frame, text=option.split("____")[0], variable=var)
#     checkbox.grid(row=i+1, column=0)
#     anesthetic_checkbox_vars.append(var)
    
#     entry = tkinter.Entry(anesthetic_frame)
#     entry.grid(row=i+1, column=1)
#     anesthetic_entry_vars.append(entry)
    
#     # Add the remaining part of the option text after the entry field
#     remaining_text = tkinter.Label(anesthetic_frame, text=option.split("____")[1])
#     remaining_text.grid(row=i+1, column=2)
# Create checkboxes, entry boxes, and labels for each option
option_dropdowns = []
option_variables = []

# Create checkboxes, entry boxes, and option menus for each option
for i, option in enumerate(anesthetic_options):
    var = tkinter.IntVar()
    checkbox_text = option.split("____")[0]
    if i==2:
        checkbox_text=option.split("???")[0]
    checkbox = tkinter.Checkbutton(anesthetic_frame, text=checkbox_text, variable=var, command=handle_checkbox_change)
    checkbox.grid(row=i+1, column=0)
    anesthetic_checkbox_vars.append(var)
    
    entry = tkinter.Entry(anesthetic_frame, state=tkinter.DISABLED)
    entry.grid(row=i+1, column=1)
    anesthetic_entry_vars.append(entry)
    
    # Replace "____" with an entry box in the third option
    if i == 2:
        checkbox_text_remaining = option.split("???")[1]
        thirdOption_partTwo = checkbox_text_remaining.split("____")[0]
        thirdOption_label = tkinter.Label(anesthetic_frame, text=thirdOption_partTwo)
        thirdOption_label.grid(row=i+1,column=2)
        thirdOption_entry = tkinter.Entry(anesthetic_frame, state=tkinter.DISABLED)
        thirdOption_entry.grid(row=i+1, column=3)
        anesthetic_entry_vars.append(thirdOption_entry)
    
    # Create an OptionMenu for INFIL/IANB selection
    option_var = tkinter.StringVar()
    option_dropdown = tkinter.OptionMenu(anesthetic_frame, option_var, "INFIL", "IANB")
    option_dropdown.config(state=tkinter.DISABLED)
    option_dropdown.grid(row=i+1, column=4)
    option_var.set("INFIL")  # Set default option
    option_dropdowns.append(option_dropdown)
    option_variables.append(option_var)


# Operative Procedure & Additional Instructions
operativeProcedure_frame = tkinter.LabelFrame(frame, text="Operative Procedure")
operativeProcedure_frame.grid(row=7, column=0)

isolation_label = tkinter.Label(operativeProcedure_frame, text="Isolation:")
isolation_label.grid(row=0, column=0)
isolation_vars = [tkinter.IntVar() for _ in range(len(isolation_options))]
isolation_checkboxes = []
for i, option in enumerate(isolation_options):
    checkbox = tkinter.Checkbutton(operativeProcedure_frame, text=option, variable=isolation_vars[i])
    checkbox.grid(row=0, column=i+1)
    isolation_checkboxes.append(checkbox)

matrix_label = tkinter.Label(operativeProcedure_frame, text="Matrix:")
matrix_label.grid(row=1, column=0)
matrix_vars = [tkinter.IntVar() for _ in range(len(matrix_options))]
matrix_checkboxes = []
row_num = 1
for i, option in enumerate(matrix_options):
    if i % 3 == 0:
        row_num += 1
    checkbox = tkinter.Checkbutton(operativeProcedure_frame, text=option, variable=matrix_vars[i])
    checkbox.grid(row=row_num, column=i%3 + 1)
    matrix_checkboxes.append(checkbox)

protocol_label = tkinter.Label(operativeProcedure_frame, text="Protocol:")
protocol_label.grid(row=row_num + 1, column=0)
protocol_vars = [tkinter.IntVar() for _ in range(len(protocol_options))]
protocol_checkboxes = []
row_num += 1
for i, option in enumerate(protocol_options):
    if i % 3 == 0:
        row_num += 1
    checkbox = tkinter.Checkbutton(operativeProcedure_frame, text=option, variable=protocol_vars[i])
    checkbox.grid(row=row_num, column=i%3 + 1)
    protocol_checkboxes.append(checkbox)

occlusion_label = tkinter.Label(operativeProcedure_frame, text="Occlusion:")
occlusion_label.grid(row=row_num + 1, column=0)
occlusion_vars = [tkinter.IntVar() for _ in range(len(occlusion_options))]
occlusion_checkboxes = []
row_num += 1
for i, option in enumerate(occlusion_options):
    if i % 3 == 0:
        row_num += 1
    checkbox = tkinter.Checkbutton(operativeProcedure_frame, text=option, variable=occlusion_vars[i])
    # if option=="Good":
    #     option_var = tkinter.IntVar(value=1)
    #     checkbox = tkinter.Checkbutton(operativeProcedure_frame, text=option, variable=option_var)
    # else:
    #     checkbox = tkinter.Checkbutton(operativeProcedure_frame, text=option, variable=occlusion_vars[i])
    checkbox.grid(row=row_num, column=i%3 + 1)
    occlusion_checkboxes.append(checkbox)

contact_var = tkinter.IntVar(value=1)
contact_checkbox = tkinter.Checkbutton(operativeProcedure_frame, text="Contact : Achieved", variable=contact_var)
contact_checkbox.grid(row=row_num + 1, column=0)

post_treatment_label = tkinter.Label(operativeProcedure_frame, text="Post-Treatment:")
post_treatment_label.grid(row=row_num + 2, column=0)
post_treatment_vars = [tkinter.IntVar() for _ in range(len(post_treatment_options))]
post_treatment_checkboxes = []
row_num += 1
for i, option in enumerate(post_treatment_options):
    checkbox = tkinter.Checkbutton(operativeProcedure_frame, text=option, variable=post_treatment_vars[i])
    checkbox.grid(row=row_num+1, column=i+1)
    post_treatment_checkboxes.append(checkbox)

additional_instructions_label = tkinter.Label(operativeProcedure_frame, text="Additional Instructions:")
additional_instructions_label.grid(row=row_num + 3, column=0)
additional_instructions_vars = [tkinter.IntVar() for _ in range(len(additional_instructions_displayedText))]
additional_instructions_checkboxes = []
for i, option in enumerate(additional_instructions_displayedText):
    checkbox = tkinter.Checkbutton(operativeProcedure_frame, text=option, variable=additional_instructions_vars[i])
    checkbox.grid(row=row_num + 3, column=i+1)
    additional_instructions_checkboxes.append(checkbox)

# TODO: IPAC
ipac_frame = tkinter.LabelFrame(frame, text="IPAC")
ipac_frame.grid(row=8, column=0)

ipac_label = tkinter.Label(ipac_frame, text="IPAC: ")
ipac_label.grid(row=0,column=0)

ipac_vars = [tkinter.IntVar() for _ in range(len(ipac_options))]
ipac_checkboxes = []
col_num=0
for i, option in enumerate(ipac_options):
    checkbox = tkinter.Checkbutton(ipac_frame, text=option, variable=ipac_vars[i])
    checkbox.grid(row=i+1, column=col_num)
    ipac_checkboxes.append(checkbox)

# Done / Submit Button
submit_button= tkinter.Button(frame, text="Done", command= enter_data)
submit_button.grid(row=9, column=0)

# Displaying submitted data
    # Scrollbar
scrollbar = tkinter.Scrollbar(frame)
scrollbar.grid(row=0, column=2, rowspan=20, sticky="ns")

submitted_data_text = tkinter.Text(frame, height=20, width=80)
submitted_data_text.grid(row=0, column=1, rowspan=9)
    # Configure to use scrollbar
submitted_data_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=submitted_data_text.yview)

# Button frame - copy and clear button
button_frame = tkinter.Frame(frame)
button_frame.grid(row=9, column=1, pady=20)

# Create Copy Button
copy_button = tkinter.Button(button_frame, text="Copy", command=copy_text)
copy_button.grid(row=0, column=0)

# Create Clear Button
clear_button = tkinter.Button(button_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=1)

# Define a custom font
default_font = tkfont.Font(family="Helvetica", size=12)
header_font = tkfont.Font(family="Helvetica", size=14, weight="bold")
body_font = tkfont.Font(family="Helvetica", size=10)

label_background="#e0e0e0"

# Set overall style for the application
style = ttk.Style()
style.configure("TFrame", background="#92E2FC")
style.configure("TLabel", background="#92E2FC", font=default_font)
style.configure("TButton", font=default_font, padding=6)
style.configure("TCheckbutton", background="#92E2FC", font=body_font)
style.configure("TText", background="#ffffff", font=default_font)
style.configure("TLabelFrame", background="#92E2FC", font=header_font)

# Update button style for a more modern look
style.map("TButton",
          foreground=[('pressed', 'black'), ('active', 'blue')],
          background=[('pressed', '!disabled', 'lightgrey'), ('active', 'lightblue')])

# Update text widget style
style.map("TText",
          background=[('focus', 'lightyellow')],
          foreground=[('focus', 'black')])

# Update Checkbutton style
style.map("TCheckbutton",
          background=[('selected', 'lightgreen')])

# Applying style changes to the existing widgets
title_frame.config(bg="#e0e0e0")
title_label.config(bg="#e0e0e0", font=header_font)

serviceProvider_label.config(bg=label_background, font=body_font)
billing_label.config(bg=label_background, font=body_font)
billedBy_label.config(bg=label_background, font=body_font)
nextAppointments_label.config(bg=label_background, font=body_font)
treatmentPlan_label.config(bg=label_background, font=body_font)
isolation_label.config(bg=label_background, font=body_font)
matrix_label.config(bg=label_background, font=body_font)
protocol_label.config(bg=label_background, font=body_font)
occlusion_label.config(bg=label_background, font=body_font)
contact_checkbox.config(bg=label_background, font=body_font)
changes_label.config(bg=label_background, font=body_font)
post_treatment_label.config(bg=label_background, font=body_font)
additional_instructions_label.config(bg=label_background, font=body_font)
ipac_label.config(bg=label_background, font=body_font)
anesthetic_label.config(bg=label_background, font=body_font)
billing_label.config(bg=label_background, font=body_font)
billing_label.config(bg=label_background, font=body_font)
billing_label.config(bg=label_background, font=body_font)
billing_label.config(bg=label_background, font=body_font)

billedBy_entry.config(bg="white", font=body_font)


# Update the layout and styles for the form elements
def style_widgets():
    for widget in frame.winfo_children():
        if isinstance(widget, tkinter.LabelFrame):
            widget.config(bg="#e0e0e0", font=header_font)
            for child in widget.winfo_children():
                if isinstance(child, tkinter.LabelFrame):
                    child.config(bg="#e0e0e0", font=header_font)
                elif isinstance(child, tkinter.Label):
                    widget.config(bg="#e0e0e0", font=default_font)
                # elif isinstance(child, tkinter.Button):
                #     widget.config(style="TButton")
                # elif isinstance(child, ttk.Checkbutton):
                #     widget.config(style="TCheckbutton")
                # elif isinstance(child, tkinter.Text):
                #     widget.config(style="TText")
                elif isinstance(child, tkinter.Entry):
                    widget.config(font=default_font)
        elif isinstance(widget, tkinter.Label):
            widget.config(bg="#e0e0e0", font=default_font)
        # elif isinstance(widget, tkinter.Button):
        #     widget.config(style="TButton")
        elif isinstance(widget, ttk.Checkbutton):
            widget.config(style="TCheckbutton")
        # elif isinstance(widget, tkinter.Text):
        #     widget.config(style="TText")
        elif isinstance(widget, tkinter.Entry):
            widget.config(font=default_font)
        
# Update styling of text widgets and entry fields
billingInfo_text.config(font=default_font)
nextAppointments_text.config(font=default_font)
submitted_data_text.config(font=default_font)

# Apply the styling function
style_widgets()

# Setting padding for all objects
for widget in frame.winfo_children():
    widget.grid_configure(padx=10, pady=7, sticky="news")
    for child in widget.winfo_children():
        child.grid_configure(padx=5, pady=5, sticky="nws")

canvas.bind_all("<MouseWheel>", on_mousewheel)
canvas.bind_all("<Button-4>", on_mousewheel)  # For Linux systems
canvas.bind_all("<Button-5>", on_mousewheel)  # For Linux systems

# Make sure the window adjusts to fit the content
window.update_idletasks()
window.geometry(f"{window.winfo_reqwidth()}x{window.winfo_reqheight()}")

window.mainloop()
