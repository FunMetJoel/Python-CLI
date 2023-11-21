# Python-CLI
 A Command Line Interface library for Python

## Installation:
To use the library, just download the `CLI.py` file in custCLI and drop it in to you'r working folder <br>
Or install the library using pip:
```
pip install custCLI
```


*When using microPython, copy the `CLI.py` file from the microPython folder* 
[MicroPython files](https://github.com/FunMetJoel/Python-CLI/tree/main/microPython)



## How to use:

1. Import the necessary classes and enums:
   ```python
   from CLI import CLI, Command, Parameter, DataType
   ```
2. Define your custom functions that will be executed when a command is called. For example:
    ```python
    def testFunction(params):
      print("testFunction")     
      for param in params:
        print(f"\t{param}")
    ```

3. Create instances of the `Command` class for each command you want to add. For example:
     ```python
     command1 = Command("test1", 
                   "test1 description", 
                   testFunction, 
                   [Parameter("param1", "param1 description",DataType.STRING), 
                    Parameter("param2", "param2 description", DataType.INTEGER)]
                   )
     ```

4. Optionally, define more custom functions and create additional `Command` instances.

5. Create an instance of the `CLI` class, passing in the name, description, and a list of commands. For example:
    ```python
    cli = CLI("Test CLI", "Test CLI description", [command1, command2])
    ```

6. Print the header of the CLI using the `printHeader()` method:
    ```python
    cli.printHeader()
    ```

7. Enter a loop to continuously accept user commands using the `newCommand()` method:
    ```python
    while True:
        cli.newCommand()
    ```
How to use:
   ```python
   from CLI import CLI, Command, Parameter, DataType

   def testFunction(params):
    print("testFunction")     
    for param in params:
        print(f"\t{param}")

   command1 = Command("test1", "test1 description", testFunction, [Parameter("param1", "param1 description", DataType.STRING), Parameter("param2", "param2 description", DataType.INTEGER)])

   def testFunction2(params):
     print("testFunction2")
     for param in params:
         print(f"\t{param.name} - {param.dataType.value} - {param.value}")

   command2 = Command("test2", "test2 description", testFunction2, [Parameter("param1", "param1 description", DataType.STRING), Parameter("param2", "param2 description", DataType.INTEGER)])

   cli = CLI("Test CLI", "Test CLI description", [command1, command2])
   cli.printHeader()

   while True:
     cli.newCommand()
   ```