import argparse
import os
import sys
import time


def about_display():
    about_test = [
        "~"*126,
        "          ###           ###      ###    ###     #######     "
        "    ####      #   #   #      #  #      #  #######    ####   ",
        "         #    #        #    #   #   #   #  #    #           "
        "    #   #    #     #  # #    #  # #    #  #          #   #  ",
        "        #             #        #     #  #   #   #           "
        "    #    #   #     #  #  #   #  #  #   #  #          #    # ",
        "        #             #        #     #  #    #  #####       "
        "    #####    #     #  #   #  #  #   #  #  #####      #####  ",
        "         #    #        #    #   #   #   #   #   #           "
        "    #  #      #   #   #    # #  #    # #  #          #  #   ",
        "          ###            ###     ###    ####    #########   "
        "    #    ##    ###    #      #  #      #  #########  #    ##",
        "",
        "              #   #   #      #  #######  #      #   #####   "
        "#######     #     #        #       #######    ####         ",
        "             #     #  # #    #     #     # #    #  #        "
        "   #       # #    #        #       #          #   #        ",
        "             #     #  #  #   #     #     #  #   #   #####   "
        "   #      #   #   #        #       #          #    #       ",
        "             #     #  #   #  #     #     #   #  #        #  "
        "   #      #####   #        #       #####      #####        ",
        "              #   #   #    # #     #     #    # #  #     #  "
        "   #     #     #  #        #       #          #  #         ",
        "               ###    #      #  #######  #      #   #####   "
        "   #     #     #  #######  ####### #########  #    ##      ",
        "~"*126,
        "Type            : Command line utility",
        "Developer       : Swastik Sharma",
        "Version         : 1.0",
        "About           :",
        "~ C Code Runner Uninstaller utility use to uninstall "
        "'C Code Runner' command line utility",
        "For more details:",
        "~ Read documentation at \n'https://github.com/DeveloperS"
        "wastik/C-Code-Runner-Command-Line-Tool/wiki/C-Code-Runner"
        "-Uninstaller-Version-1.0-Documentation'",
        "\u00A9 DeveloperSwastik",
        "~"*126,
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


def uninstall_file():
    if os.path.exists("C:\\C Code Runner"):
        os.system("cls")

        no_of_files_in_dir = os.listdir("C:\\C Code Runner")

        if len(no_of_files_in_dir) == 1:
            pass
        else:
            print(
                "\n",
                "*"*91,
                "\nUninstallation failed ......",
                "\nYou have to manually delete 'C:\\C Code runner' folder"
                " to uninstall 'C Code Runner' utility.\n",
                "*"*91,
                "\n",
                sep=""
            )

            os.system('attrib -h "C:\\C Code Runner"')
            sys.exit()

        for i in range(5):
            dots = "."*i

            print(
                f"\nProcess Starts {dots}",
                flush=True
            )

            time.sleep(0.4)
            os.system("cls")

        os.chdir("C:\\")

        for i in range(5):
            dots = "."*i

            print(
                f"\nProcess Starts {dots}",
                flush=True
            )

            time.sleep(0.4)
            os.system("cls")

        os.remove("C Code Runner\\c_code_runner.exe")

        for i in range(5):
            dots = "."*i

            print(
                f"\nProcess Starts {dots}",
                flush=True
            )

            time.sleep(0.4)
            os.system("cls")

        os.system('rmdir "C Code Runner"')

        print(
            "\n",
            "*"*77,
            "\nUninstallation process completed succesfully .....",
            "\nNow you can remove the environment varible you "
            "add during installation ......\n",
            "*"*77,
            "\n",
            sep=""
        )

        sys.exit()
    else:
        print(
            "\n",
            "*"*75,
            "\nUninstallation failed ......",
            "\nFor uninstallation you have to firstly install "
            "C Code Runner utility ......\n",
            "*"*75,
            "\n",
            sep=''
        )

        sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "About: C Code Runner Uninstaller utility is use for "
            "uninstall C Code Runner Utility"
        )
    )

    parser.version = 'C Code Runner Uninstaller Version: 1.0'

    parser.add_argument(
        '--about', action="store_true",
        help=(
            "This argument return the basic documentation"
        )
    )

    parser.add_argument(
        '--run', action="store_true",
        help=(
            "This argument start the uninstallation process"
        )
    )

    parser.add_argument(
        '--version', action="version",
        help="This argument show the current version of utility",
    )

    args = parser.parse_args()

    if args.run:
        uninstall_file()

    if args.about:
        about_display()

    if args.about == None and args.run == None:
        print(
            "\n",
            "-"*57,
            "\nArgumentNotPassError: You doesn't pass any argument .....\n",
            "-"*57,
            "\n", sep=""
        )