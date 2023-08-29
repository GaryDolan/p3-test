# ------------------------- LIBRARY IMPORTS ---------------------------
# Created by me to store and print pokemon ascii art
from pokemon_ascii_art import print_pokemon

# Creates text-based ASCII art banners
import pyfiglet as pyf

# Allows interaction with the operating systems functionalities
import os

# Add colors to text output
from termcolor import colored

# Allows access to functions to work with regular expressions
import re


# ---------------------------- API SETUP ------------------------------

# Import the entire gspread library -
# - access to all classes, methods and functions
# import gspread

# Import Credentials class from the service account function -
# - part of the google oauth library
# from google.oauth2.service_account import Credentials

# Specify what parts of the google account the user has access to
# SCOPE = [
#     "https://www.googleapis.com/auth/spreadsheets",
#     "https://www.googleapis.com/auth/drive.file",
#     "https://www.googleapis.com/auth/drive"
#     ]

# Create a Credentials instance from a service account json file
# CREDS = Credentials.from_service_account_file('creds.json')

# Create a copy of the credentials with specified scope
# SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Create gspread client using gspread authorize method
# GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Access sheet for project
# SHEET = GSPREAD_CLIENT.open('pokemon_portfolio')

# login = SHEET.worksheet('login')

# data = login.get_all_values()
# print(data)

# --------------------------- CLASSES -----------------------------


# --------------------- APP LOGIC FUNCTIONS -----------------------


def display_welcome_banner():
    """
    Displays welcome banner and image

    Parameters:
        None
    Returns:
        None
    """
    print_art_font("Pokemon Portfolio", "yellow")

    print_pokemon("pikachu_banner")

    login_options()


def login_options():
    """
    Displays the login opitions to user.
    Takes user input, validates and calls appropiate function.

    Parameters:
        None
    Returns:
        None
    """
    while True:
        # colored_text = colored(
        #     "Please select an option (1-3) from the options and enter it below\n",
        #     attrs=["bold", "underline"],
        # )
        # print(len(colored_text))
        # print(repr(colored_text))

        # plain_colored_text = re.sub(r'(\x1b|\\e|\\033)\[[0-9;]*m', "", colored_text)
        # print(len(plain_colored_text))
        # print(plain_colored_text)

        msg = "Please select an option (1-3) from the options and enter it below\n"
        msglength = len(msg)
        print(msglength)

        print_center_text(colored(msg, attrs=["bold", "underline"]), msglength)

        print_center_text(
            "Please select an option (1-3) from the options and enter it below\n", 66
        )
        print("1. Log into your account")
        print("2. Create an account")
        print("3. Password recovery\n")

        login_selection = input("Enter your selection:\n")

        validated_selection = validate_input(login_selection, list(range(1, 4)))

        if validated_selection == 1:
            account_login()
            break
        elif validated_selection == 2:
            create_account()
            break
        elif validated_selection == 3:
            password_recovery()
            break


def account_login():
    clear_terminal()
    print_art_font("        Account Login" "yellow")


def create_account():
    clear_terminal()
    print_art_font(" Account Creation", "yellow")


def password_recovery():
    clear_terminal()
    print_art_font("       Password Reset" "yellow")


# ----------------------- HELPER FUNCTIONS ------------------------


def print_art_font(string, color):
    """ """
    font = pyf.Figlet(font="big", width=110)
    msg = font.renderText(string)
    msg = msg.rstrip()

    print(colored(msg, color))


def print_center_text(text, length):
    """
    Centers and prints the given text to the terminal
    If text contains ascii escape codes for color etc
    the function will stip these out for calculating
    spacing but will still print original text

    Parameters:
        text (string): Text to be centered and printed
    Returns:
        None
    """

    terminal_width = os.get_terminal_size().columns

    if isinstance(text, str):
        processed_text = text
    else:
        # Text contain ascii escape chars, use re to clear them before calculations
        processed_text = re.sub(r"(\x1b|\e|\033)\[[0-9;]*m", "", text)
    print(repr(processed_text))
    # print(len(processed_text))
    spaces = int((terminal_width - length) / 2)
    # print(spaces)
    centered_text = " " * spaces + text
    # print(centered_text)


def clear_terminal():
    if os.name == "posix":  # Linux and macOS
        os.system("clear")
    elif os.name == "nt":  # Windows
        os.system("cls")


def validate_input(input_str, available_choices):
    """
    Validates input can be converted to an int
    Also validates that user input was one of the available choices


    Parameters:
        input (string): User input to be validated
        available_choices (list): List of choices available to user
    Returns:
        int or False: Returns input value as an int if valid otherwise returns False
    """
    try:
        input_value = int(input_str)
        if input_value not in available_choices:
            raise ValueError(
                f"Input must be 1 of the choices given ({available_choices[0]} - {available_choices[-1]}), you entered {input_value}\n"
            )
    except ValueError as e:
        print(f"\nInvalid selection: {e}, please select one of the options listed\n")
        return False
    return input_value


# ----------------------------- MAIN -------------------------------


def main():
    """
    Run Pokemon Portfolio terminal application
    """
    display_welcome_banner()


main()
