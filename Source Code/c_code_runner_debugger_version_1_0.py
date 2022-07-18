import os
import sys
import time
import argparse


def start_debugging():
    a = time.time()
    mingw_path_added = False
    c_code_runner_path_added = False
    c_code_runner_exe_found = False

    os.system("cls")

    for i in range(5):
        dots = "."*i

        print(
            f"\nProcess Starts {dots}",
            flush=True
        )

        time.sleep(0.4)
        os.system("cls")

    c_code_runner_installed = os.path.exists(
        "C:\\C Code Runner\\c_code_runner.exe"
    )

    os.system("cls")

    for i in range(5):
        dots = "."*i

        print(
            f"\nProcess Starts {dots}",
            flush=True
        )

        time.sleep(0.4)
        os.system("cls")

    for i in os.environ.get("PATH").split(";"):

        if i.endswith("MinGW\\bin"):
            mingw_path_added = True

        if i.endswith("C Code Runner"):
            c_code_runner_path_added = True
            if os.path.exists(f'{i}\\c_code_runner.exe'):
                c_code_runner_exe_found = True

    for i in range(5):
        dots = "."*i

        print(
            f"\nProcess Starts {dots}",
            flush=True
        )

        time.sleep(0.4)
        os.system("cls")

    if not mingw_path_added:
        print(
            "\n",
            "*"*46,
            "\nError found:",
            "\nMinGW path is not add to environment variable.\n",
            "Please add MinGW path to environment variable.\n",
            "*"*46,
            "\n",
            sep=""
        )
    elif not c_code_runner_path_added:
        print(
            "\n",
            "*"*66,
            "\nError found:",
            "C Code Runner path is not add to environment variable.\n",
            "Please add this path 'C:\\C Code Runner' to environment "
            "variable.\n",
            "*"*66,
            "\n",
            sep=""
        )
    elif not c_code_runner_exe_found:
        print(
            "\n",
            "*"*33,
            "\nError found:\n",
            "c_code_runner.exe file not found.\n",
            "*"*33,
            "\n",
            sep=""
        )
    elif not c_code_runner_installed:
        print(
            "\n",
            "*"*82,
            "\nError found:",
            "\nC Code Runner is not installed on your system.\n",
            "Please install C Code Runner utility.",
            "\nFollow path given below to download C Code Runner:\n",
            "https://github.com/DeveloperSwastik/C-Code-Runner-Comm"
            "and-Line-Tool/wiki/Downloads \n",
            "*"*82,
            "\n",
            sep=""
        )
    elif (
            c_code_runner_installed 
            and 
            c_code_runner_path_added 
            and 
            mingw_path_added 
            and 
            c_code_runner_exe_found
        ):
        print(
            "\n",
            "*"*52,
            "\nNO error found:",
            "\nC Code Runner is perfectly installed on your system.\n",
            "*"*52,
            "\n",
            sep=""
        )
    sys.exit()


def about_display():
    about_test = [
        "~"*123,
        "        ###           ###      ###    ###     #######      "
        "   ####      #   #   #      #  #      #  #######    ####   ",
        "       #    #        #    #   #   #   #  #    #            "
        "   #   #    #     #  # #    #  # #    #  #          #   #  ",
        "      #             #        #     #  #   #   #            "
        "   #    #   #     #  #  #   #  #  #   #  #          #    # ",
        "      #             #        #     #  #    #  #####        "
        "   #####    #     #  #   #  #  #   #  #  #####      #####  ",
        "       #    #        #    #   #   #   #   #   #            "
        "   #  #      #   #   #    # #  #    # #  #          #  #   ",
        "        ###            ###     ###    ####    #########    "
        "   #    ##    ###    #      #  #      #  #########  #    ##",
        "",
        "                   #####     #######    #####      #   #   "
        "  ###        ###      #######    ####                      ",
        "                   #    #    #          #    #    #     #  "
        " #   #      #   #     #          #   #                     ",
        "                   #     #   #          #     #   #     #  "
        "#          #          #          #    #                    ",
        "                   #      #  #####      ######    #     #  "
        "#    ####  #    ####  #####      #####                     ",
        "                   #     #   #          #     #    #   #   "
        " #   #  #   #   #  #  #          #  #                      ",
        "                   ######    #########  ######      ###    "
        "  ###   #    ###   #  #########  #    ##                   ",
        "~"*123,
        "Type            : Command line utility",
        "Developer       : Swastik Sharma",
        "Version         : 1.0",
        "About           :",
        "~ C Code Runner Debugger utility use to debug installation of "
        "'C Code Runner' command line utility",
        "For more details:",
        "~ Read documentation at \n'https://github.com/DeveloperS"
        "wastik/C-Code-Runner-Command-Line-Tool/wiki/C-Code-Runner"
        "-Debugger-Version-1.0-Documentation'",
        "\u00A9 DeveloperSwastik",
        "~"*123,
    ]

    i = 0
    while (
        i < len(about_test)
    ):
        print(about_test[i], flush=True)

        if i < 14:
            time.sleep(0.2)
        else:
            time.sleep(0.3)
        i += 1

    sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "About: C Code Runner debugger utility is use for "
            "debug C Code Runner Utility installation"
        )
    )

    parser.version = 'C Code Runner Debugger Version: 1.0'

    parser.add_argument(
        '--about', action="store_true",
        help=(
            "This argument return the basic documentation"
        )
    )

    parser.add_argument(
        '--run', action="store_true",
        help=(
            "This argument start the debugging process"
        )
    )

    parser.add_argument(
        '--version', action="version",
        help="This argument show the current version of utility",
    )

    args = parser.parse_args()
    
    if args.run:
        start_debugging()
        

    if args.about:
        about_display()

    if args.run == False and args.about == False:
        print(
            "\n",
            "-"*57,
            "\nArgumentNotPassError: You doesn't pass any argument .....\n",
            "-"*57,
            "\n", sep=""
        )
