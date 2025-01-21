class prints():

    def print_colored(text, color_code):
        print(f"\033[{color_code}m{text}\033[0m")

    def print_colored_bold(text, color_code):
        bold_text = f"\033[1m\033[{color_code}m{text}\033[0m"
        print(bold_text)