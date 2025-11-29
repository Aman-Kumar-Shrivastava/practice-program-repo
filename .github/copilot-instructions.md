# AI Agent Instructions for practice-program-repo-1

## Project Overview
This repository contains a collection of C programs focused on different functionalities:

1. `guessing_game.c` - A number guessing game
2. `soiltest.c` - A soil analysis program based on wavelength data
3. `new.c` - A basic Hello World program

## Development Environment
- Language: C
- Compiler: GCC (MinGW)
- Build System: VS Code tasks

## Key Development Patterns

### Build Process
- The project uses VS Code's built-in C/C++ build task
- Files are compiled individually using gcc
- Example build command structure:
  ```
  gcc -fdiagnostics-color=always -g {sourceFile} -o {outputFile}
  ```

### Code Organization
1. **Main Program Structure**:
   - Each program is self-contained in a single .c file
   - Standard include pattern: `<stdio.h>` and other required headers at the top
   - Main function with return type `int`

2. **Function Organization Pattern**:
   - Function declarations at the top (see `soiltest.c`)
   - Implementation following the main function
   - Consistent return type declarations

### Project-Specific Conventions

1. **Input Handling**:
   - User input collected via `scanf`
   - Input validation through if-else conditions
   - Example from `soiltest.c`:
   ```c
   scanf("%d", &wavelength);
   if(wavelength >= 400 && wavelength < 500) {
       // Processing logic
   }
   ```

2. **Output Formatting**:
   - Clear user prompts before input collection
   - Structured output with newlines for readability
   - Tabular data formatted with consistent spacing (see `TabularChart()` in `soiltest.c`)

3. **Error Handling**:
   - Range validation for numeric inputs
   - Default cases in switch statements
   - Clear error messages for invalid inputs

## Key Files/Components

### guessing_game.c
- Random number generation using `rand()` with proper seeding
- Interactive game loop using do-while
- Progress tracking (attempts counter)

### soiltest.c
- Menu-driven interface
- Modular function design
- Scientific data ranges (400-900nm wavelength)
- Structured data presentation in tabular format

## Debugging
- Debug builds include symbols (-g flag)
- VS Code's built-in debugger can be used with the configured build task

## Future Development
When adding new programs to this repository:
1. Follow the existing file naming convention (lowercase with underscores)
2. Include appropriate header files
3. Implement proper input validation
4. Add clear user instructions in output messages
5. Use modular function design for complex programs