import argparse
import os
import shutil
import sys
import time


def about_display():
    about_test = [
        "~"*124,
        "        ###           ###      ###    ###     #######         "
        "####      #   #   #      #  #      #  #######    ####   ",
        "       #    #        #    #   #   #   #  #    #               "
        "#   #    #     #  # #    #  # #    #  #          #   #  ",
        "      #             #        #     #  #   #   #               "
        "#    #   #     #  #  #   #  #  #   #  #          #    # ",
        "      #             #        #     #  #    #  #####           "
        "#####    #     #  #   #  #  #   #  #  #####      #####  ",
        "       #    #        #    #   #   #   #   #   #               "
        "#  #      #   #   #    # #  #    # #  #          #  #   ",
        "        ###            ###     ###    ####    #########       "
        "#    ##    ###    #      #  #      #  #########  #    ##",
        "~"*124,
        "Type        : Command line utility",
        "Developer   : Swastik Sharma",
        "Version     :"f" {CURRENT_INSTALLED_VERSION_PATCH[0:3]}",
        "About       :",
        "~ C Code Runner utility automate compilation and execution c progr"
        "am using"
        " gcc compiler in single line of command.",
        "~ C Code Runner is only Windows friendly.",
        "For more details:",
        "~ Read documentation at \n"
        "~ https://github.com/DeveloperSwastik/C-Code-Runner-Command-Line-To"
        "ol/wiki/C-Code-Runner-Installer-Version-1.1-Documentation",
        "\u00A9 DeveloperSwastik",
        "~"*124,
    ]

    i = 0
    while (
        i < len(about_test)
    ):
        print(about_test[i], flush=True)

        if i < 6:
            time.sleep(0.2)
        else:
            time.sleep(0.3)
        i += 1

    sys.exit()


def transfer_file():
    if os.path.exists("C:\\C Code Runner"):
        file_present = os.path.exists("C:\\C Code Runner\\c_code_runner.exe")

        if file_present:
            print(
                "\n",
                "*"*28,
                "\nSetup already executed .....",
                "\nNo Need of Rexecution ......\n",
                "*"*28,
                "\n",
                sep=''
            )

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
            r"'C:\C Code Runner' to the environment variable""\n",
            "~"*64,
            sep=""
        )

    except FileNotFoundError:
        pass

    sys.exit()


CURRENT_INSTALLED_VERSION_PATCH = '1.1.0'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "About: C Code Runner utility is use for one "
            "line compilation and execution of c program."
        )
    )

    parser.version = (
        'C Code Runner Version: '
        f'{CURRENT_INSTALLED_VERSION_PATCH[0:3]}'
    )

    parser.add_argument(
        '--f', type=str,
        help=r"This argument take the name of input {.c} file"
    )

    parser.add_argument(
        '--d', type=str,
        help=(
            "This argument take the directory path "
            r"where input {.c} file store. If file is"
            " not store in current directory"
        )
    )

    parser.add_argument(
        '--o', type=str,
        help=r"This argument take the name of output {.exe} file"
    )

    parser.add_argument(
        '--about', type=str,
        help=(
            "This argument take 'About' or 'about' as value and return "
            "the basic documentation"
        )
    )

    parser.add_argument(
        '--run', type=str,
        help=(
            "This argument start the setup process by taking 'Start_process'"
            " or 'start_process' as value"
        )
    )

    parser.add_argument(
        '--version', action="version",
        help="This argument show the current version of utility",
    )

    args = parser.parse_args()

    if args.run is not None:
        if args.run == "Start_process" or args.run == "start_process":
            transfer_file()
        else:
            print(
                "\n",
                "-"*66,
                "\nInvalidArgumentError: Given value to argument is invalid",
                " .........\n",
                "-"*66,
                "\n",
                sep=""
            )

    if args.about is not None:
        if args.about == "About" or args.about == "about":
            about_display()
        else:
            print(
                "\n",
                "-"*66,
                "\nInvalidArgumentError: Given value to argument is invalid",
                " .........\n",
                "-"*66,
                "\n",
                sep=""
            )

    if args.d is not None:
        try:
            if (args.d).count('--'):
                arguments = args.d.split('--')
                if arguments[0].strip().endswith('"'):
                    args.d = arguments[0].strip()[0:len(arguments[0])-2]
                else:
                    args.d = arguments[0]
                for i in arguments:
                    if i.startswith('f'):
                        args.f = i[1:len(i)].strip()
                    if i.startswith('o'):
                        args.o = i[1:len(i)].strip()
            elif args.d.strip().endswith('"'):
                if args.d.strip()[0:len(args.d)-2].startswith(".\\"):
                    args.d = args.d.strip()[0:len(args.d)].lstrip(".\\")
                args.d = args.d.rstrip('"').strip()

            os.chdir(args.d)

            if args.f is None:
                print(
                    "------------------------------------\n\n"
                    "Compilation Doesn't Starts ...."
                )

                print(
                    f"FileNameNotGivenError: C file name not given"
                    " .... \n\n"
                    "------------------------------------"
                )
                sys.exit()

        except FileNotFoundError:
            print(
                "------------------------------------\n\n"
                "Compilation Doesn't Starts ...."
            )

            print(
                f"DirectoryNotFoundError: Directory '{args.d}' "
                "not exists ...\n\n"
                "------------------------------------"
            )

            sys.exit()

        except NotADirectoryError:
            print(
                "------------------------------------\n\n"
                "Compilation Doesn't Starts ...."
            )

            print(
                f"NotADirectoryError: Given path '{args.d}' "
                "is not a path of directory ...\n\n"
                "------------------------------------"
            )

            sys.exit()

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

            compilation_time = end_compilation - start_compilation
            execution_time = end_execution - start_execution

            print(
                f"Compilation time :{compilation_time:.12f} Secounds"
            )

            print(
                f"Execution time   :{execution_time:.12f} Secounds"
            )

        else:
            print(
                "------------------------------------\n\n"
                "Compilation Doesn't Starts ...."
            )

            print(
                f"FileNotFoundError: File '{args.f}' not exists ...\n\n"
                "------------------------------------"
            )

            sys.exit()

    if (
        args.run == None and args.d == None and args.o == None
        and args.about == None and args.f == None
    ):
        print(
            "\n",
            "-"*57,
            "\nArgumentNotPassError: You doesn't pass any argument .....\n",
            "-"*57,
            "\n", sep=""
        )
