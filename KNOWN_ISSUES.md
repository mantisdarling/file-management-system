# Known Issues

This document explains a few runtime issues you might encounter when running this project, along with their causes and how to handle them.

---

## 1. EOFError: EOF when reading a line

This error appears when Python expects user input using `input()`, but no input is provided.

Since this project is interactive and depends on terminal input, it may fail in environments that do not support user interaction.

### How to fix it
Run the program in a proper terminal environment such as:
- VS Code integrated terminal  
- Windows Command Prompt (CMD)  
- PowerShell  
- Linux / macOS terminal  

Avoid using online runners that do not support interactive input.

---

## 2. OSError: [Errno 29] I/O error

This error occurs when the runtime environment does not support standard input/output operations.

In this project, it usually happens because the execution environment blocks interactive programs.

### How to fix it
Use a local Python environment with full terminal support instead of restricted or sandboxed online compilers.

---

## Note

These issues are not related to the code itself.  
The program works correctly when executed in a proper Python terminal environment.
