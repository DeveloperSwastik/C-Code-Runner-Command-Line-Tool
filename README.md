<p align="center">
  <img alt="Logo Image" src="https://raw.githubusercontent.com/DeveloperSwastik/C-Code-Runner-Command-Line-Tool/main/Images/C%20Code%20Runner%20Logo.png">
</p>

# C Code Runner {Command Line Utility}
> _Current version of C Code Runner is 1.0 [Download Latest Version](https://drive.google.com/uc?id=1QvSeVv8UYtgz-amEek7iHxGBP7vxG6Q9&export=download)_

## Table of Contents

- [About C Code Runner](#about-c-code-runner-)
- [Benefits of Using C Code Runner](#benefits-of-using-c-code-runner-)
- [How to Setup C Code Runner On Your Windows Machine](#how-to-setup-c-code-runner-on-your-windows-machine-)
  - [Method 1 {Recommended Method}](#method-1)
  - [Method 2](#method-2)
- [Arguments Pass to C Code Runner](#arguments-pass-to-c-code-runner-)
- [How to Compile And Execute C File Using C Code Runner](#how-to-compile-and-execute-c-file-using-c-code-runner-)
- [Pre Requirements for C Code Runner](#pre-requirements-for-c-code-runner-)
- [C Code Runner All Versions Download Links](#c-code-runner-all-versions-download-links-)

## About C Code Runner [🔝](#table-of-contents)

- _**C Code Runner** is a command line utility help developer to compile and run complied C file in a
Single command instead of writing compilation and the execution command individually._

- _**C Code Runner** use **gcc** compiler for compilation. So, it required that gcc is installed and it path is added to environment variable._

- _**C Code Runner** is written in **Python** Programming Language._

- _**C Code Runner** Is **Open Source Project**. To View Code [Click Here](https://github.com/DeveloperSwastik/C-Code-Runner-Command-Line-Tool/blob/main/Source%20Code/c_code_runner.py)._

- _**C Code Runner** is only **Windows** friendly._

## Benefits of Using C Code Runner [🔝](#table-of-contents)

- You have to write single statement for compilation and execution.
- Output file by default is a.exe but **C Code Runner** create output file as same as the name of input file.
- **C Code Runner** automatically count both compilation and execution time in secounds and output it after the execution of script.

## How to Setup C Code Runner On Your Windows Machine [🔝](#table-of-contents)

<a name="method-1"></a>
### Method 1 {Recommended Method}: [🔝](#table-of-contents)
_Step 1: Download **C_Code_Runner.exe** file by clicking below download link._

<a href="https://drive.google.com/uc?id=1QvSeVv8UYtgz-amEek7iHxGBP7vxG6Q9&export=download">Download Latest Version</a>

> _Note 1: If you are getting any warning form Google drive during downloading. Then don't worry about it happening because this is an .exe type of file which is treated as dangerous file by Google drive. Download file anyway._

_Step 2: Reach the file location in CMD where **C_Code_Runner.exe** file is downloaded._

_Step 3: Run the below command in CMD._

```
c_code_runner.exe --run Start_process
```

_Step 4: Now you can delete the downloaded file._

_Step 5: Now you have to add **"C:\C Code Runner"** path to user environment variable._

> How to add path to Environment Variable:

- _Step 1: Press **windows + r** key to open Run Command Window._
- _Step 2: Type command **system.cpl** and press ok. This open **System properties panel**._
- _Step 3: Click on **Advance** option at the top._
- _Step 4: Click on **Environment Variables...** option at the top._
- _Step 5: In user variable double click on **PATH**._
- _Step 6: Click on **New** option at the top right._
- _Step 7: Paste the path in new entry box._
- _Step 8: Then press ok._
- _Step 9: Then again press ok._
- _Step 10: Then again press ok._
- _Now your path is added to environment variable._

_Step 6: Verify installation, reopen CMD and run command given below._

```
c_code_runner --about About
```

> _If it show the output similar to given below. Then congratulations **c_code_runner** utility is successfully installed in your machine._

<p align="center">
  <img alt="Output Image" src="https://raw.githubusercontent.com/DeveloperSwastik/C-Code-Runner-Command-Line-Tool/main/Images/screen%20shot.png">
</p>

> _Note 2: If you are using any code editor having its own terminal like VScode then you have to restart the software to refresh it terminal._

> _If you got error the please retry the installation process or try second method._

<a name="method-2"></a>
### Method 2 : [🔝](#table-of-contents)

_Step 1: Download **C_Code_Runner.exe** file by clicking below download link._

<a href="https://drive.google.com/uc?id=1QvSeVv8UYtgz-amEek7iHxGBP7vxG6Q9&export=download" style="color: black; text-decoration: none;">Download Latest Version</a>

> _Note 3: If you are getting any warning form Google drive during downloading. Then don't worry about it happening because this is an .exe type of file which is treated as dangerous file by Google drive. Download file anyway._

_Step 2: Copy and paste the file in the directory where you are working and now you can use the features of **C Code Runner** without any setup._

## Arguments Pass to C Code Runner [🔝](#table-of-contents)

|Arguments      |Input                                             |Working                                                    |
|---------------|--------------------------------------------------|-----------------------------------------------------------|
|  _--h_        |_Take no input_                                   |_Show Help Message_                                        |
|  _--f_        |_Take file name of .c {input} file_               |_Compile file to .exe_                                     |
|  _--o_        |_Take file name of .exe {output} file_            |_Use file name instead of default{file name of input file}_|
|  _--about_    |_Take 'About' or 'about' as value_                |_Display the basic documentation of utility_               |
|  _--run_      |_Take 'Start_process' or 'start_process' as value_|_Start the setup process of C Code Runner_                 |
|  _--version_  |_Take no input_                                   |_Show the current version of software_                     |

## How to Compile And Execute C File Using C Code Runner [🔝](#table-of-contents)
- _If you want to see help message. Use command given below and press enter._

```
c_code_runner --h
```

- _For compile and execute c code. Use command given below and then and press enter._

```
c_code_runner --f input_file_name.c
```

- _For compile file with specific name by default it is of the same name of input file with .exe extension and then execute it. Use command given below and press enter._

```
c_code_runner --f input_file_name.c --o output_file_name.exe
```

- _For starting the setup process. Use the command given below and press enter._

```
c_code_runner --run Start_process
```

- _If you want to get details about C Code Runner. Use command given below and press enter._

```
c_code_runner --about About
```

- _If you want to know the currently installed version of C Code Runner. Use the command given below and press enter.

```
c_code_runner --version
```
> _Note 4: Above commands work in case of method first of setup._

> _Note 5: If you are following method 2 then you have to just give relative path of **c_code_runner.exe** file to execute command if you copy paste the file in current working directory or else give absolute path to the **c_code_runner.exe** file to take use of it._

```
.\c_code_runner.exe --arguments
```
or
```
%path%\c_code_runner.exe --arguments
```

## Pre Requirements for C Code Runner [🔝](#table-of-contents)

- _**gcc** compiler should be installed in your machine._
- _gcc compiler path should be add to **environment variables**._

## C Code Runner All Versions Download Links [🔝](#table-of-contents)

|Vesions         | Release Date |Download Link                                                                                                                 |
|----------------|--------------|------------------------------------------------------------------------------------------------------------------------------|
|_Latest Version_|2022-18-06    |<a href="https://drive.google.com/uc?id=1QvSeVv8UYtgz-amEek7iHxGBP7vxG6Q9&export=download">Download Latest Version</a>        |
|_Version 1.0_   |2022-18-06    |<a href="https://drive.google.com/uc?id=1QvSeVv8UYtgz-amEek7iHxGBP7vxG6Q9&export=download">Download Version 1.0</a>           |
