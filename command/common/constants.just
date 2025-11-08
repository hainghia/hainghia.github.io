# https://hainghia.github.io/colors-cheat-sheet.html

COLOR_ANSI := "\u{1B}[38;5;"
ORANGE1 := COLOR_ANSI + "214m"
ORANGERED1 := COLOR_ANSI + "202m"
GREY46 := COLOR_ANSI + "243m"

# Define color codes
[group('Common')]
colors:
    @echo "List of available colors:"
    @echo -e "{{ RED }}Red syntax:: {{{{RED}}{{ NORMAL }}"
    @echo -e "{{ GREEN }}Green syntax:: {{{{GREEN}}{{ NORMAL }}"
    @echo -e "{{ YELLOW }}Yellow syntax:: {{{{YELLOW}}{{ NORMAL }}"
    @echo -e "{{ BLUE }}Blue syntax:: {{{{BLUE}}{{ NORMAL }}"
    @echo -e "{{ MAGENTA }}Magenta syntax:: {{{{MAGENTA}}{{ NORMAL }}"
    @echo -e "{{ CYAN }}Cyan syntax:: {{{{CYAN}}{{ NORMAL }}"
    @echo -e "{{ WHITE }}White syntax:: {{{{WHITE}}{{ NORMAL }}"
    @echo -e "{{ BLACK }}Black syntax:: {{{{BLACK}}{{ NORMAL }}"
    @echo -e "{{ ORANGE1 }}Orange syntax:: {{{{ORANGE1}}{{ NORMAL }}"
    @echo -e "{{ ORANGERED1 }}Orange-Red syntax:: {{{{ORANGERED1}}{{ NORMAL }}"
    @echo -e "{{ GREY46 }}Grey syntax:: {{{{GREY46}}{{ NORMAL }}"
