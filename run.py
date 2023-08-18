import pyfiglet as pyf
from ascii_magic import AsciiArt
import ascii_art
import os


def display_welcome_msg():
    # font = pyf.Figlet(font="big", width=110)
    # welcome_msg = font.renderText("Pokemon Portfolio")
    # # welcome_msg = rendered_msg.center(110)

    # print(welcome_msg)

    # font4 = pyf.Figlet(font="doom", width=110)
    # welcome_msg4 = font4.renderText("Pokemon Portfolio")
    # print(welcome_msg4)

    # font8 = pyf.Figlet(font="standard", width=110)
    # welcome_msg8 = font8.renderText("Pokemon Portfolio")
    # print(welcome_msg8)

    # print(pikachu)

    # pikachu = AsciiArt.from_image("pikachu.png")
    # pikachu.to_terminal(columns=50, width_ratio=1)

    # pikachu = AsciiArt.from_image("Alakazam.png")
    # pikachu.to_terminal(columns=100, width_ratio=2)

    print_ascii_art("banner")
    print_ascii_art("pikachu_banner")

    # clear_terminal()

    # print_ascii_art("alakazam")
    # print_ascii_art("blastoise")
    # print_ascii_art("chansey")
    # print_ascii_art("charizard")
    # print_ascii_art("clefairy")
    # print_ascii_art("gyarados")
    # print_ascii_art("hitmonchan")
    # print_ascii_art("machamp")
    # print_ascii_art("magneton")
    # print_ascii_art("mewtwo")
    # print_ascii_art("nidoking")
    # print_ascii_art("ninetales")
    # print_ascii_art("poliwrath")
    # print_ascii_art("raichu")
    # print_ascii_art("venusaur")
    # print_ascii_art("zapdos")
    # print_ascii_art("beedrill")
    # print_ascii_art("dragonair")
    # print_ascii_art("dugtrio")
    # print_ascii_art("electabuzz")
    # print_ascii_art("electrode")
    # print_ascii_art("pidgeotto")
    # print_ascii_art("arcanine")
    # print_ascii_art("charmeleon")
    # print_ascii_art("dewgong")
    # print_ascii_art("dratini")
    # print_ascii_art("farfetchd")
    # print_ascii_art("growlithe")
    # print_ascii_art("haunter")
    # print_ascii_art("ivysaur")
    # print_ascii_art("jynx")
    # print_ascii_art("kadabra")
    # print_ascii_art("kakuna")
    # print_ascii_art("machoke")
    # print_ascii_art("magikarp")
    # print_ascii_art("magmar")
    # print_ascii_art("nidorino")
    # print_ascii_art("poliwhirl")
    # print_ascii_art("porygon")
    # print_ascii_art("raticate")
    # print_ascii_art("seel")
    # print_ascii_art("wartortle")
    # print_ascii_art("abra")

    # print_ascii_art("bulbasaur")
    # print_ascii_art("caterpie")
    # print_ascii_art("charmander")
    # print_ascii_art("diglett")
    # print_ascii_art("doduo")
    # print_ascii_art("drowzee")
    # print_ascii_art("gastly")
    # print_ascii_art("koffing")
    # print_ascii_art("machop")
    # print_ascii_art("magnemite")
    # print_ascii_art("metapod")
    # print_ascii_art("nidoran_m")
    # print_ascii_art("onix")
    # print_ascii_art("pidgey")
    # print_ascii_art("pikachu")
    # print_ascii_art("poliwag")
    # print_ascii_art("ponyta")
    # print_ascii_art("rattata")
    # print_ascii_art("sandshrew")
    # print_ascii_art("squirtle")
    # print_ascii_art("starmie")
    # print_ascii_art("staryu")
    # print_ascii_art("tangela")
    # print_ascii_art("voltorb")
    # print_ascii_art("vulpix")
    # print_ascii_art("weedle")

    # print_ascii_art("clefairy_doll")
    # print_ascii_art("computer_search")
    # print_ascii_art("devolution_spray")
    # print_ascii_art("impostor_professor_oak")
    # print_ascii_art("item_Finder")
    # print_ascii_art("lass")
    # print_ascii_art("pokemon_breeder")
    # print_ascii_art("pokemon_trader")
    # print_ascii_art("scoop_up")
    # print_ascii_art("super_energy_removal")
    # print_ascii_art("defender")
    # print_ascii_art("energy_retrieval")
    # print_ascii_art("full_heal")
    # print_ascii_art("maintenance")
    # print_ascii_art("plus_power")
    # print_ascii_art("pokemon_center")
    # print_ascii_art("pokemon_flute")
    # print_ascii_art("pokedex")
    # print_ascii_art("professor_oak")
    # print_ascii_art("revive")
    # print_ascii_art("super_potion")
    # print_ascii_art("bill")
    # print_ascii_art("energy_removal")
    # print_ascii_art("gust_of_wind")
    # print_ascii_art("potion")
    # print_ascii_art("switch")
    # print_ascii_art("double_colorless_energy")
    # print_ascii_art("fighting_energy")
    # print_ascii_art("fire_energy")
    # print_ascii_art("grass_energy")
    # print_ascii_art("lightning_energy")
    # print_ascii_art("psychic_energy")
    # print_ascii_art("water_energy")


def print_ascii_art(art_name):
    a_art = getattr(ascii_art, art_name)
    print(a_art)


# ----------------------------- MAIN -------------------------------
def clear_terminal():
    if os.name == "posix":  # Linux and macOS
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")


def main():
    """
    Run Pokemon Portfolio command-line utility
    """
    display_welcome_msg()


main()
