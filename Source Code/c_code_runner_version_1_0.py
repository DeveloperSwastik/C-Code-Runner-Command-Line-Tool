import argparse
import os
import time
import shutil
import sys


def about_display():
    about_test = [
        "~"*113,
        "    ###           ###      ###    ###     #######         ####    "
        " #   #   #      #  #      #  #######    ####   ",
        "   #    #        #    #   #   #   #  #    #               #   #   "
        "#     #  # #    #  # #    #  #          #   #  ",
        "  #             #        #     #  #   #   #               #    #  "
        "#     #  #  #   #  #  #   #  #          #    # ",
        "  #             #        #     #  #    #  #####           #####   "
        "#     #  #   #  #  #   #  #  #####      #####  ",
        "   #    #        #    #   #   #   #   #   #               #  #    "
        " #   #   #    # #  #    # #  #          #  #   ",
        "    ###            ###     ###    ####    #########       #    ## "
        "  ###    #      #  #      #  #########  #    ##",
        "~"*113,
        "Type        : Command line utility",
        "Developer   : Swastik",
        "Version     : 1.0",
        "About       :",
        "~ C Code Runner utility automate compilation and execution c program"
        " using gcc compiler in single line of command.",
        "~ C Code Runner is only Windows friendly",
        "Requirement : ",
        "~gcc compiler should be installed and path is added to environment "
        "variables",
        "For more details:",
        "~Read documentation at 'https://github.com/DeveloperSwastik/C-Code-"
        "Runner-Command-Line-Tool'",
        "\u00A9 DeveloperSwastik",
        "~"*113,
    ]

    i = 0
    while (
        i < len(about_test)
    ):
        print(about_test[i], flush=True)

        if i < 6:
            time.sleep(0.3)
        else:
            time.sleep(0.6)
        i += 1
    
    sys.exit()


def transfer_file():
    if os.path.exists("C:\\C Code Runner"):
        output = [
            "\n",
            "*"*28,
            "Setup already executed .....",
            "No Need of Rexecution ......",
            "*"*28,
            "\n"
        ]

        for statement in output:
            print(statement)

        sys.exit()

    os.system("cls")

    for i in range(5):
        dots = "."*i

        print(
            f"\nProcess Starts {dots}",
            flush=True
        )

        time.sleep(0.4)
        os.system("cls")

    try:
        os.mkdir("C:\\C Code Runner")
    except FileExistsError:
        pass

    f = open("C:\\C Code Runner\\c_code_runner.exe", "a")

    for i in range(5):
        dots = "."*i

        print(
            f"\nProcess Starts {dots}",
            flush=True
        )

        time.sleep(0.4)
        os.system("cls")

    try:
        shutil.copyfile(
            ".\\c_code_runner.exe",
            "C:\\C Code Runner\\c_code_runner.exe"

        )

        os.system("cls")

        os.system('attrib +h "C:\\C Code Runner"')

        print(
            "~"*65,
            "\nProcess Completed Succesfully."
            "\nNow you can delete the downloaded file\nAnd Add the path "
            r"'C:\C_Code_Runner' to the environment variable""\n",
            "~"*64
        )
        
    except FileNotFoundError:
        pass

    sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "About: C Code Runner utility is use for one "
            "line compilation and execution of c program."
        )
    )

    parser.version = 'C Code Runner Version : 1.0'

    parser.add_argument(
        '--f', type=str,
        help=r"This argument take the path of input {.c} file"
    )

    parser.add_argument(
        '--o', type=str,
        help=r"This argument take the path of output {.exe} file",
    )

    parser.add_argument(
        '--about', type=str,
        help=(
            "This argument take 'About' or 'about' as value "
            "and return the basic documentation"
        )
    )

    parser.add_argument(
        '--run', type=str,
        help=(
            "This argument start the setup process by taking "
            "'Start_process' or 'start_process' as value",
        )
    )

    parser.add_argument(
        '--version', action="version",
        help="This argument show the current version of utility",
    )

    args = parser.parse_args()

    if args.run == "Start_process" or args.run == "start_process":
        transfer_file()

    if args.about == "About" or args.about == "about":
        about_display()

    if args.f is not None:
        file_exists = os.path.exists(args.f)

        if file_exists:

            if (args.f).startswith(".\\"):
                args.f = (args.f).lstrip(".\\")
                input_file = os.path.splitext(args.f)[0]
                input_file_extension = os.path.splitext(args.f)[1]
            else:
                input_file = os.path.splitext(args.f)[0]
                input_file_extension = os.path.splitext(args.f)[1]

            if args.o is None:
                output_file = input_file
                output_file_extension = ""
            else:
                output_file = os.path.splitext(args.o)[0]
                output_file_extension = os.path.splitext(args.o)[1]

                if (output_file).startswith(".\\"):
                    output_file = (output_file).lstrip(".\\")

            if output_file_extension == "" or output_file_extension == ".":
                output_file_extension = ".exe"

            try:
                os.remove(f"{output_file}{output_file_extension}")
            except FileNotFoundError:
                pass

            start_compilation = time.time()
            os.system(
                f"gcc {input_file}{input_file_extension} "
                f"-o {output_file}{output_file_extension}"
            )
            end_compilation = time.time()

            if os.path.exists(f"{output_file}{output_file_extension}"):
                pass
            else:
                print(
                    f"CompilationError: There is error in compilation "
                    f"of {input_file}{input_file_extension}"
                )

                sys.exit()

            print(
                "Execution Starts ....\n"
                "---------------------"
            )

            start_execution = time.time()
            os.system(f"{output_file}{output_file_extension}")
            end_execution = time.time()

            print(
                "\n---------------------"
                "\nExecution Ends ......"
            )

            print(
                f"Compilation time :{end_compilation - start_compilation}"
            )

            print(
                f"Execution time :{end_execution - start_execution}"
            )
            
        else:
            print(
                "------------------------------------\n\n"
                "Execution Doesn't Starts ...."
            )

            print(
                f"FileNotFoundError: File '{args.f}' "
                "not exists ...\n\n"
                "------------------------------------"
            )

            sys.exit()