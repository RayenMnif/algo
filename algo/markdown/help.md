         ▄▄▄       ██▓      ▄████  ▒█████  
        ▒████▄    ▓██▒     ██▒ ▀█▒▒██▒  ██▒
        ▒██  ▀█▄  ▒██░    ▒██░▄▄▄░▒██░  ██▒
        ░██▄▄▄▄██ ▒██░    ░▓█  ██▓▒██   ██░
        ▓█   ▓██▒░██████▒░▒▓███▀▒░ ████▓▒░
        ▒▒   ▓▒█░░ ▒░▓  ░ ░▒   ▒ ░ ▒░▒░▒░ 
         ▒   ▒▒ ░░ ░ ▒  ░  ░   ░   ░ ▒ ▒░ 
         ░   ▒     ░ ░   ░ ░   ░ ░ ░ ░ ▒  
             ░  ░    ░  ░      ░     ░ ░  
                                          
     Tunisian shitty pseudo/programming language

> [!NOTE] This is a beta version of the project. It may be buggy and unstable, as it was developed by a single developer with no prior experience. Your contributions are welcome, especially if you encounter any issues.


# Table of Contents

- [Language Introduction and Setup](#language-introduction-and-setup)
  - [Introduction](#introduction)
  - [Setup](#setup)
- [Variables](#variables)
  - [Variable Types](#variable-types)
    - [Entier](#entier)
    - [Reel](#reel)
    - [Chaine](#chaine)
    - [Booleen](#booleen)
    - [Nulle](#nulle)
    - [Tableau](#tableau)
    - [Matrice](#matrice)
- [Loops](#loops)
  - [Boucle Pour](#boucle-pour)
  - [Boucle Tant_que](#boucle-tant_que)
  - [Boucle Repeter](#boucle-repeter)
- [Functions](#functions)
  - [Fonction](#fonction)
  - [Procedure](#procedure)
  - [Native Functions](#native-functions)
- [Operations](#operations)
  - [Binary Operations](#binary-operations)
  - [Logical Operations](#logical-operations)
  - [Comparison Operations](#comparison-operations)
- [Code Simples](#code-simples)
  - [Reading and Writing from a Tableau](#reading-and-writing-from-a-tableau)
  - [Reading and Writing from a Matrice](#reading-and-writing-from-a-matrice)
# language introduction and setup

## introduction

algo is interpreted programming language fully written in python by the brilliant dev 'Rayen Mnif' me :)
as a '3eme anne science d'informatique' student (i don't want to say cs student cause it's nothing like cs) (currently bac since this is my summer project and i had shit going on) i hated the algorithme so much even tho i was excellent and i had good grades, i hated it because it have never been an actual language, there's no way of debuging or compiling the code, there been times where teacher gived me bad grades because my code looks like nothing like what they used to be taught and what they teach even tho the code is actually corret and likely more optimized and more efficient but ofc here in Tunisia we have "a7fed wsob" policy.
and this was my motivation of writting this interpreter, hoping that it will fix our educational shitty system and prove to the brilliant minds of "municipalité d'education |  وزارة التربية" that a 17 year old kid have done something they at least should've done it for a long time.
i'm not "Mr Robot" or something i've done my best the language still in beta so it will probably have some errors and will need some fixes, and you can do it, you're likely a better coder than I am so feel free to contribut to the project
the language has been tested and fully working on my personal machine a laptop runing arch linux with Linux 6.10.0-arch1-2 kernal
\- Rayen Mnif

## setup

the language was added to The [Python Package Index (PyPI)](https://pypi.org/) or shortly [pip](https://pypi.org/) so if you have `pip3` or `pip` installed you can simly run
`pip install algo`
or
`pip3 install algo`
or you can compile the code yourself runing the `setup.py` script

> [!NOTE] you have to install [python3](https://www.python.org/downloads/)

## variables

algo is a dynamically typed language. This means that variables do not have types; only values do. There are no type definitions in the language except [fonction](#fonction) and [procdure](#procedure) . All values carry their own type.

### variables types

#### entier
* **entier** : integers (a number that is not a fraction; a whole number.)

    **Example asignig x to an integer** ``` x <- 5 ```  

#### reel
- **reel** or **réel** : A floating point number (a positive or negative whole number with a decimal point.)

    **Example asignig x to an reel** ``` x <- 5.10 ```  

#### chaine
- **chaine** or **chaine_de_caractere** or **chaine_de_caractère** : A string (an object of type String whose value is text)

    **Example asignig x to an chaine** ``` x <- "hello world" ``` or  ``` x <- 'hello world' ```

     >[!NOTE] you can use both double and single quotes for declaring var type [chaine](#chaine)


#### booleen
- **booleen** or **booléen** : 
Boolean values, named after the mathematician George Boole, represent one of two possible states: `vrai` or `faux`. In computer science and programming, Boolean values are used to perform [logical operations](#logical-operations) and control the flow of a program through conditions and loops.


#### nulle
- **nulle**: null is a variable does not reference any object or value. It is often used to indicate an absence of a value or an uninitialized variable. Mostly used for empty alocated memory like in [matrice](#matrice) and [tableau](#tableau)


#### tableau
- **tableau** : array of values, our language auto assign it like the real tunisian algo 

    **Example asignig a tableau**
      
    - in [procedure](#procedure)

      ```
      procedure get_tab(m : tableau, n : entier)
           debut
              pour i de 0 a n - 1 faire
                lire(m[i])
              fin_pour
            fin
      
      nombre <- 5
      get_tab(t, nombre)
      ``` 

    - in [fonction](#fonction)

      ```
      fonction get_tab(m : tableau, n : entier) : tableau
            debut
              pour i de 0 a n - 1 faire
                lire(m[i])
              fin_pour
              retourner m
            fin
      
      nombre <- 5
      tab <- get_tab(t, nombre)
      ``` 

    here in those [function](#functions) you declared a tableau and stored 5 values to it, algo like the real algo auto malloc values in tableau and empty values are  assigned to nulle 

     >[!NOTE] you can only assign tableau in [functions](#functions) since the [functions](#functions) auto assigns them

#### matrice
- **matrice** : A matrix is a two-dimensional array of values arranged in rows and columns, our language auto assign it like the real tunisian algo 

    **Example asignig a matrice**
      
    - in [procedure](#procedure)

      ```
      procedure get_mat(m : matrice, n : entier)
           debut
              pour i de 0 a n - 1 faire
                pour j de 0 a n - 1 faire
                  lire(m[i, j])
                fin_pour
              fin_pour
            fin
      
      get_mat(mat, 5)
      ``` 

    - in [fonction](#fonction)

      ```
      fonction get_mat(m : matrice, n : entier) : matrice
            debut
              pour i de 0 a n - 1 faire
                pour j de 0 a n - 1 faire
                  lire(m[i, j])
                fin_pour
              fin_pour
              retourner m
            fin
      
      nombre <- 5
      mat <- get_mat(mat, nombre)
      ``` 

    here in those [function](#functions) you declared a matrice stored 25 (5 * 5) values to it, algo like the real algo auto malloc values in matrice and empty values are  assigned to nulle 

     >[!NOTE] you can only assign tableau in [functions](#functions) since the [functions](#functions) auto assigns them

## loops

### boucle pour
#### main syntax
```
pour <var> de <entier> a <entier> faire 
  <statement>
fin_pour
```

```
pour <var> de <entier> a <entier> pas <entier> faire 
  <statement>
fin_pour
```
#### example

```
pour i de 0 a 5 faire 
  ecrire(i)
fin_pour
```
```
pour i de 0 a 5 pas 2 faire 
  ecrire(i)
fin_pour
```

### boucle tant_que
#### main syntax
```
tant_que <boolean expression> faire 
  <statement>
fin_tant_que
```

#### example
```
i <- 0
tant_que i < 5 faire 
  i <- i + 1
  ecrire(i)
fin_tant_que
```
### boucle repeter
#### main syntax
```
repeter 
  <statement>
jusqu'a <boolean expression>
```

#### example
```
i <- 0
repeter 
  i <- 1 + i
  ecrire(i) 
jusqu'a i > 5
```

## functions


### fonction
fonction in algo act like every programming language on earth, they get some args or no args then they return something 

 >[!NOTE] you need to declare arguments types, see [variables types](#variables-types) for more

**here is an example of a function that takes a [chaine](#chaine) and returns a [chaine](#chaine)**
```
fonction hello(name : chaine) : chaine
  debut  
    x <- "hello " + name
    retourner x
  fin
```

### procedure

procedure in algo are more likely for organizing the code they're like moving a chunck of code, their return value is of type [Nulle](#nulle)
and same as [fonction](#fonction) you need to specify arguments types

**here's an example**

```
procedure hello(name : chaine)
  debut  
    x <- "hello " + name
  fin
```

### native functions

1. `ecrire(x)`
   - **Description**: Displays the value of `x` to the console. Can handle various types such as entier, reel, chaine, etc.
   - **Example**: `ecrire("Hello, World!")` will output `Hello, World!`.

2. `lire()`
   - **Description**: Reads a single line of input from the user and returns it as a string.
   - **Example**:
      - `x <- lire()` will prompt the user for input and store it in `x`.
      - `lire(M[i, j])` used for reading [matrice](#matrice) content where `i` and `j` are both [entier](#entier)
      - `lire(M[i])` used for reading [tableau](#tableau) content where `i` is an [entier](#entier)

3. `long(chaine)`
   - **Description**: Returns the length of the given string.
   - **Example**: `long("Hello")` returns `5`.

4. `valeur(chaine)`
   - **Description**: Converts a string to an integer.
   - **Example**: `x <- valeur("123")` will convert the string `"123"` to the integer `123`.

5. `convch(x)`
   - **Description**: Converts a string to a floating-point number.
   - **Example**: `x <- convch(123.45)` will convert the number `123.45` to the string number `"123.45"`.

6. `abs(x)`
   - **Description**: Returns the absolute value of a number.
   - **Example**: `abs(-5)` returns `5`.

7. `sous_chaine(chaine, debut, fin)`
   - **Description**: Returns the substring of `chaine` starting at index `debut` and ending at index `fin`.
   - **Example**: `sous_chaine("Hello, World!", 0, 5)` returns `"Hello"`.

8. `effacer(chaine, debut, fin)`
   - **Description**: Returns the deleted part of substing of `chaine` starting at index `debut` and ending at index `fin`.
   - **Example**: `effacer("Hello, World!", 0, 5)` returns `", World!"`.

9. `alea(debut, fin)`
   - **Description**: Returns a random integer between `debut` and `fin` inclusive.
   - **Example**: `alea(1, 10)` might return any integer between `1` and `10`.

10. `arrondi(x)`
   - **Description**: Rounds the given floating-point number to the nearest entier.
   - **Example**: `arrondi(4.7)` returns `5`.

11. `racine_carre(x)`
    - **Description**: Returns the square root of the given number.
    - **Example**: `racine_carre(16)` returns `4`.

12. `ent(x)`
    - **Description**: Returns the integer part of a floating-point number (truncates the decimal part).
    - **Example**: `ent(4.7)` returns `4`.

13. `majus(chaine)`
    - **Description**: Converts all characters in the string to uppercase.
    - **Example**: `majus("Hello, World!")` returns `"HELLO, WORLD!"`.

14. `pos(ch1, ch2)`
    - **Description**: return the starting index of ch1 in ch2 else it returns `-1`
    - **Example**: `pos("3456", "123456789)` returns `2`.



## operations

### binary operation 

- **+** : Addition (+): Adds two operands.

  ```
  4 + 12                 # returns 16
  4 + 12.5               # returns 16.5
  0.2 + 0.15             # returns 0.17
  "hello " + 'world'     # returns "hello world"
  ```

- **\*** : Subtraction (-): Subtracts the second operand from the first.
    
    ```
    12 - 4                 # returns 8
    4 - 12.5               # returns -8.5
    0.2 - 0.15             # returns -0.13
    ```
- **/** : Division (/): Divides the first operand by the second.
  ```
  12 / 4                 # returns 3.0
  4 / 12.5               # returns 0.32
  0.2 / 0.15             # returns 1.3333
  ```
- **mod** : Modulo (mod): Returns the remainder of the division of the first operand by the second.
    
    ```
    12 mod 5                 # returns 2
    4 mod 12                 # returns 4
    0.2 mod 0.15             # returns 0.05
    ```
- **div** : Integer Division (div): Divides the first operand by the second and returns the integer quotient, discarding the remainder.
  ```
  12 div 5                # returns 2
  4 div 12                # returns 0
  ```

### Logical Operations

- **et** : Logical AND (et): Returns `vrai` if both operands are `vrai`; otherwise, returns `faux`.

  ```
  vrai et vrai              # returns vrai
  vrai et faux              # returns faux
  faux et faux              # returns faux
  ```

- **ou** : Logical OR (ou): Returns `vrai` one or both operands are `vrai`; otherwise, returns `faux`.

  ```
  vrai ou vrai              # returns vrai
  vrai ou faux              # returns vrai
  faux ou faux              # returns faux
  ```

- **=** : Logical Equals (=): Returns `vrai` operands values are equals ; otherwise, returns `faux`.

  ```
  vrai = vrai               # returns vrai
  5 = 5                     # returns vrai
  "hello" = "hi"            # returns faux
  ```

- **!=** : Logical Not (!=): Returns `vrai` operands values are diffrent ; otherwise, returns `faux`.

  ```
  vrai != vrai                  # returns faux
  5 != vrai                     # returns vrai
  "hello" != "hello"            # returns faux
  ```

### Comparison Operations

- **<** : Less than (<): Returns vrai if the first operand is less than the second operand; otherwise, returns faux.


  ```
  3 < 5                     # returns vrai
  5 < 3                     # returns faux
  ```

- **>** : Greater than (>): Returns vrai if the first operand is greater than the second operand; otherwise, returns faux.

    ```
    5 > 3                     # returns vrai
    3 > 5                     # returns faux
    ```

- **<=** : Less than or equal to (<=): Returns vrai if the first operand is less than or equal to the second operand; otherwise, returns faux.

  ```
  3 <= 5                    # returns vrai
  5 <= 5                    # returns vrai
  5 <= 3                    # returns faux
  ```

- **>=** : Greater than or equal to (>=): Returns vrai if the first operand is greater than or equal to the second operand; otherwise, returns faux.

  ```
  5 >= 3                    # returns vrai
  5 >= 5                    # returns vrai
  3 >= 5                    # returns faux
  ```
## code simples
<details>

  <summary>hello world</summary>

  ### code

  ```
  name <- lire()
  ecrire("hello ", name,"!")
  ```

### output

```
> rayen
hello rayen!
```

</details>

<details>

  <summary>reading and writing from a `tableau`</summary>

  ### code

  ```
  procedure remplir(tab : tableau, n : entier)
debut

   # lire n (n is being auto allocataed in memory)

   repeter
       n <- lire("lire n: ")
       n <- valeur(n) # returns a float
       n <- ent(n)
    jusqu'a n >= 3

   # lire tab

   pour i de 0 a n - 1 faire
       lire(tab[i])
   fin_pour

fin

procedure afficher(tab: tableau, n: entier)
debut
    i <- 0
    tant_que i < n faire
       ecrire(tab[i])
       i <- i + 1
    fin_tant_que
fin

remplir(T, n)
afficher(T, n)
```

### output

```
lire n: 3
> 165
> 48769
> 645
165
48769
645
```

</details>
<details>

  <summary>reading and writing from a `matrice`</summary>

  ### code

  ```
procedure remplir(mat : matrice, n : entier)
debut 
   
   repeter
       n <- lire("lire n: ")
       n <- valeur(n) # returns a float
       n <- ent(n)
   jusqu'a n >= 3

   pour i de 0 a n - 1 faire
       pour j de 0 a n - 1 faire
           ecrire("mat[",i,',',j,']: ')
           lire(mat[i, j])
           mat[i, j] <- valeur(mat[i, j])
        fin_pour
   fin_pour 
   
fin

procedure afficher(mat: matrice, n: entier)
debut
    pour i de 0 a n - 1 faire
        pour j de 0 a n - 1 faire
           ecrire(mat[i, j])
        fin_pour
    fin_pour
fin 

remplir(T, n)
afficher(T, n)
```

### output

```
lire n: 3
mat[0,0]:
> 654
mat[0,1]:
> 978
mat[0,2]:
> 798
mat[1,0]:
> 645
mat[1,1]:
> 798
mat[1,2]:
> 798
mat[2,0]:
> 789
mat[2,1]:
> 798
mat[2,2]:
> 978
654.0
978.0
798.0
645.0
798.0
798.0
789.0
798.0
978.0
```

</details>
