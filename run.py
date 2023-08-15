import pyfiglet as pyf


def display_welcome_msg():
    pikachu = r"""                                                                   
                            ⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
                            ⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
                            ⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
                            ⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
                            ⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
                            ⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
                            ⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
                            ⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋
"""

    font = pyf.Figlet(font="rectangles")
    welcome_msg = font.renderText("Pokemon Portfolio")
    print(welcome_msg)

    font1 = pyf.Figlet(font="small")
    welcome_msg1 = font1.renderText("Pokemon Portfolio")
    print(welcome_msg1)

    font2 = pyf.Figlet(font="smslant")
    welcome_msg2 = font2.renderText("Pokemon Portfolio")
    print(welcome_msg2)

    font3 = pyf.Figlet(font="big", width=110)
    welcome_msg3 = font3.renderText("Pokemon Portfolio")
    print(welcome_msg3)

    font4 = pyf.Figlet(font="doom", width=110)
    welcome_msg4 = font4.renderText("Pokemon Portfolio")
    print(welcome_msg4)

    font5 = pyf.Figlet(font="ogre", width=110)
    welcome_msg5 = font5.renderText("Pokemon Portfolio")
    print(welcome_msg5)

    font6 = pyf.Figlet(font="rounded", width=110)
    welcome_msg6 = font6.renderText("Pokemon Portfolio")
    print(welcome_msg6)

    font7 = pyf.Figlet(font="slant", width=110)
    welcome_msg7 = font7.renderText("Pokemon Portfolio")
    print(welcome_msg7)

    font8 = pyf.Figlet(font="standard", width=110)
    welcome_msg8 = font8.renderText("Pokemon Portfolio")
    print(welcome_msg8)

    font9 = pyf.Figlet(font="stop", width=110)
    welcome_msg9 = font9.renderText("Pokemon Portfolio")
    print(welcome_msg9)

    # welcome_msg1 = pyf.figlet_format("Pokemon-Portfolio", "small")
    # print(welcome_msg1)
    # welcome_msg2 = pyf.figlet_format("Pokemon-Portfolio", "smslant")
    # print(welcome_msg2)
    # welcome_msg3 = pyf.figlet_format("Pokemon-Portfolio", "big")
    # print(welcome_msg3)
    # welcome_msg4 = pyf.figlet_format("Pokemon-Portfolio", "doom")
    # print(welcome_msg4)
    # welcome_msg5 = pyf.figlet_format("Pokemon-Portfolio", "ogre")
    # print(welcome_msg5)
    # welcome_msg6 = pyf.figlet_format("Pokemon-Portfolio", "rounded")
    # print(welcome_msg6)
    # welcome_msg7 = pyf.figlet_format("Pokemon-Portfolio", "slant")
    # print(welcome_msg7)
    # welcome_msg8 = pyf.fig_format("Pokemon-Portfolio", "standard")
    # print(welcome_msg8)
    # welcome_msg9 = pyfig.figlet_format("Pokemon-Portfolio", "stop")
    # print(welcome_msg9)
    # print(pikachu)


# ----------------------------- MAIN -------------------------------


def main():
    """
    Run Pokemon Portfolio command-line utility
    """
    display_welcome_msg()


main()
