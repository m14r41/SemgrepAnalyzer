#!/usr/bin/env python3
import os
import subprocess
import json
from json2html import json2html

# Define ANSI color codes
GREEN = '\033[0;32m'
CYAN = '\033[0;36m'
YELLOW = '\033[1;33m'
RED = '\033[0;31m'
NC = '\033[0m'  # No Color


# Additional ASCII art
ASCII_ART = """
 .-.                                     .               .                  
(   )                                   / \\              |                  
 `-.  .-. .--.--.  .-...--. .-. .,-.   /___\\  .--.  .-.  | .  .---. .-. .--.
(   )(.-' |  |  | (   ||   (.-' |   ) /     \\ |  | (   ) | |  | .' (.-' |   
 `-'  `--''  '  `- `-`|'    `--'|`-' '       `'  `- `-'`-`-`--|'--- `--''   
                   ._.'         |                             ;             
                                '                          `-'               
"""



def display_blinking_box(text):
    width = len(text) + 4  # Calculate the width of the box
    border_color = "\e[91m"  # Red color for the border
    text_color = "\e[5;34m"   # Blinking blue color for the text
    reset = "\e[0m"          # Reset formatting and color

    print(f"{border_color}+{'-' * width}+{reset}")
    print(f"{border_color}|{text_color}  {text}  {border_color}|{reset}")
    print(f"{border_color}+{'-' * width}+{reset}")

def run_semgrep(option, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    current_folder_name = os.path.basename(os.getcwd())  # Get the current folder name
    custom_command_success = False  # Flag to track success of the custom command

    if option == "1":
        print(f"{YELLOW}Running Semgrep option 1...{NC}")
        subprocess.run(["semgrep", "scan", "--config=auto", "--output", os.path.join(output_folder, f"{current_folder_name}.txt"), "--force-color", "--text"])
    elif option == "2":
        print(f"{YELLOW}Running Semgrep option 2...{NC}")
        subprocess.run(["semgrep", "scan", "--config=auto", "--output", os.path.join(output_folder, f"{current_folder_name}-Pro.txt"), "--force-color", "--text", "--pro"])
    elif option == "3":
        print(f"{YELLOW}Running Semgrep option 3...{NC}")
        subprocess.run(["semgrep", "scan", "--config=auto", "--output", os.path.join(output_folder, f"{current_folder_name}.json"), "--force-color", "--json"])
    elif option == "4":
        print(f"{YELLOW}Running Semgrep option 4...{NC}")
        subprocess.run(["semgrep", "scan", "--config=auto", "--output", os.path.join(output_folder, f"{current_folder_name}-Pro.json"), "--force-color", "--json", "--pro"])
    elif option == "5":
        custom_command = input(f"{CYAN}Enter custom Semgrep command: {NC}")
        if "semgrep" in custom_command:  # Check if the command includes "semgrep"
            result = subprocess.run(custom_command, shell=True)
            if result.returncode == 0:  # Check if the command ran successfully
                custom_command_success = True  # Set the flag if successful
            else:
                print(f"{RED}Error: Custom Semgrep command failed.{NC}")  # Error message for command failure
        else:
            print(f"{RED}Error: Please enter a valid Semgrep command.{NC}")  # Error message for invalid command
    elif option == "all":
        print(f"{YELLOW}Running all Semgrep options...\n{NC}")
        for idx in range(1, 5):
            run_semgrep(str(idx), output_folder)
    else:
        print(f"{RED}Invalid option. Please enter 1, 2, 3, 4, 5, or all.{NC}")
        return

    return custom_command_success  # Return the success flag

def generate_html(output_folder):
    for filename in os.listdir(output_folder):
        if filename.endswith(".txt") or filename.endswith(".json"):
            file_path = os.path.join(output_folder, filename)
            base_name = os.path.splitext(filename)[0]
            ext = filename.split('.')[-1]

            # Create the corresponding HTML filename
            html_file_name = os.path.join(output_folder, f"{base_name}-{ext}.html")

            if ext == "json":
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    html_content = json2html.convert(json=data)
                with open(html_file_name, 'w') as html_file:
                    html_file.write(html_content)
            else:
                with open(file_path, 'r') as text_file:
                    text_content = text_file.read()
                with open(html_file_name, 'w') as html_file:
                    html_file.write(f"<html><body><pre>{text_content}</pre></body></html>")

            print(f"{GREEN}Generated HTML file: {html_file_name}{NC}")

def main():
  print(ASCII_ART)  # Display the main ASCII art
    print(f"{GREEN}Welcome to the SemgrepAnalyzer!{NC}")

    # Display options and descriptions
    print(f"{YELLOW}Available options:{NC}")
    print(f"{CYAN}1) Run Normal & Output in Text/HTML{NC}")
    print(f"{CYAN}2) Run with Pro Rules & Output in Text/HTML{NC}")
    print(f"{CYAN}3) Run Normal & Output in JSON/HTML{NC}")
    print(f"{CYAN}4) Run with Pro Rules & Output in JSON/HTML{NC}")
    print(f"{CYAN}5) Enter your custom option{NC}")
    print(f"{CYAN}all) Run all Semgrep options{NC}")

    # Prompt user for input
    option = input(f"{RED}Enter the option:\n{NC}")
    
    output_folder = "SemgrepOutput"
    custom_command_success = run_semgrep(option, output_folder)

    # Only generate HTML if a custom command ran successfully
    if custom_command_success:
        generate_html(output_folder)

    print(f"{GREEN}All Semgrep scans completed!{NC}")

if __name__ == "__main__":
    main()

