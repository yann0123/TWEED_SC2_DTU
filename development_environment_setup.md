# Set up the development environment

**Important note**: If your computer already have Git, Python and you can use conda to manage environment, you may skip this guide.
---
This instruction shows you how to set up the recommended development environment for this course, which is composed of following three.

-   [Git](https://git-scm.com/): a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
-   [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main): a free, miniature installation of Anaconda Distribution that includes only Conda, Python, the packages they both depend on, and a small number of other useful packages. Conda is a widely used environment and package manager in the Python ecosystem.
-   [VS Code](https://code.visualstudio.com/): Visual Studio Code (VS Code) is a free, powerful, lightweight code editor for Windows, macOS and Linux. It is one of the most widely used IDEs (integrated development environment). It can also be used as a general purpose text editor, such as for writing documents in latex, markdown, etc. 



**Important note**: Using **Git** for version control is required, but using **Miniconda** and **VS Code** is only recommended. If you have experience with using other Python distribution and code editor/IDE, you can continue with the setup that you are more comfortable with.

Here, the steps to set up the recommended development environment are given for different operation system (OS), follow the one for the OS you are using.

***

## **Part 1: Windows**

### 1. Install Git

Go to the official [Git website](https://git-scm.com/downloads/win) and download the installer for Windows. Run the installer and accept all default settings. The installer includes **Git Bash**, the command-line interface you'll be using.

### 2. Install Miniconda

Download the **Miniconda** installer for Windows from the [Anaconda website](https://www.anaconda.com/download/success). Choose the Miniconda installer (shown on the right). During installation, it's recommended to:

-   **Leave the box "Add Miniconda3 to my PATH environment variable" unchecked.** This prevents potential conflicts with other software.
-   Keep the box to "Register Miniconda3 as the system Python 3.X" checked.

### 3. Install VS Code

Go to the [**VS Code website**](https://code.visualstudio.com/download) and download the installer for Windows. Run the installer and accept all default settings.

### 4. Configure VS Code

-   **Set Git Bash as the Integrated Terminal:**
    1.  Open VS Code. Press `Ctrl+Shift+P` to open the Command Palette.
    2.  Type `Terminal: Select Default Profile` and press Enter.
    3.  Select `Git Bash` from the list. This ensures consistency with the Unix-like environment used in many tutorials.
-   **Install the Python Extension:**
    1.  Go to the Extensions view by clicking the four-square icon on the left sidebar or by pressing `Ctrl+Shift+X`.
    2.  Search for and install the **"Python" extension** by Microsoft.
-   **Initialize Conda in Git Bash:**
    1.  Open the VS Code integrated terminal by going to **View** \> **Terminal** (or pressing `` Ctrl+`  ``).
    2.  Navigate to the `condabin` directory within your Miniconda installation. A typical path would be: `cd "C:/Users/[YourUsername]/AppData/Local/miniconda3/condabin"`
    3.  Run the initialization command directly: `./conda.bat init bash`
    4.  Close and reopen the terminal for the changes to take effect. You should see `(base)` at the start of your command prompt.

***

## **Part 2: macOS**

### 1. Install Git

Open the Terminal application and type `git --version`. If Git is not installed, macOS will prompt you to install the Xcode Command Line Tools, which includes Git.

### 2. Install Miniconda

Download the **Miniconda** installer for Mac from the [Anaconda website](https://www.anaconda.com/download/success). Choose the Miniconda installer (shown on the right).

The installer is a `.pkg` file. Run the installer and follow the on-screen instructions. It will automatically configure your shell (typically Zsh).

-   If you don't see `(base)` in your terminal prompt, close and reopen the terminal. If that still doesn't work, run `conda init zsh` and then restart your terminal.

### 3. Install VS Code

Download the VS Code installer for macOS from the official [website](https://code.visualstudio.com/download) and drag the application to your Applications folder.

### 4. Configure VS Code

-   **Install the Python Extension:** Open VS Code. Go to the Extensions view (`Cmd+Shift+X`) and install the **"Python" extension** by Microsoft.
-   The integrated terminal in VS Code will automatically use your system shell (Zsh) and should be correctly configured for Conda.

***

## **Part 3: Linux**

### 1. Install Git

Git is often pre-installed. To check, open a terminal and run `git --version`. If it's not installed, use your package manager: `sudo apt update` `sudo apt install git`

### 2. Install Miniconda

Download the **Miniconda** installer for Linux from the [Anaconda website](https://www.anaconda.com/download/success). Choose the Miniconda installer (shown on the right). You can do this from the command line using `wget`: `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`

Then, run the installer script: `bash Miniconda3-latest-Linux-x86_64.sh`

Follow the prompts, and make sure to type `yes` when prompted to run `conda init`. Close and reopen the terminal for the changes to take effect.

### 3. Install VS Code

Download the package for VS Code from the official [website](https://code.visualstudio.com/download). Install it from the command line:

`sudo dpkg -i code_*.deb` or `sudo dpkg -i code_*.rpm` depending on your Linux distribution.

`sudo apt-get install -f`

### 4. Configure VS Code

-   **Install the Python Extension:** Open VS Code. Go to the Extensions view (`Ctrl+Shift+X`) and install the **"Python" extension** by Microsoft.
-   The integrated terminal (`` Ctrl+`  ``) will automatically open in a shell that is correctly initialized with Conda.
