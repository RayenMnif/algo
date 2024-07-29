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

procedure in algo are more likely for organizing the code they're like moving a chunck of code, their return value is of type [Nulle](####Nulle)
and same as [fonction](#fonction) you need to specify arguments types

**here's an example**

```
procedure hello(name : chaine)
  debut  
    x <- "hello " + name
  fin
```

### native functions
native functions are functions implimented directly in the interpreter 
#### functions simples
- 


## operations

### binary operation 

- **+** : Addition (+): Adds two operands.

  ```
  x <- 4 + 12                 # returns 16
  x <- 4 + 12.5               # returns 16.5
  x <- 0.2 + 0.15             # returns 0.17
  x <- "hello " + 'world'     # returns "hello world"
  ```

- **\*** : Subtraction (-): Subtracts the second operand from the first.
    
    ```
    x <- 12 - 4                 # returns 8
    x <- 4 - 12.5               # returns -8.5
    x <- 0.2 - 0.15             # returns -0.13
    ```
- **/** : Division (/): Divides the first operand by the second.
  ```
  x <- 12 / 4                 # returns 3.0
  x <- 4 / 12.5               # returns 0.32
  x <- 0.2 / 0.15             # returns 1.3333
  ```
- **mod** : Modulo (mod): Returns the remainder of the division of the first operand by the second.
    
    ```
    x <- 12 mod 5                 # returns 2
    x <- 4 mod 12                 # returns 4
    x <- 0.2 mod 0.15             # returns 0.05
    ```
- **div** : Integer Division (div): Divides the first operand by the second and returns the integer quotient, discarding the remainder.
  ```
  x <- 12 div 5                # returns 2
  x <- 4 div 12                # returns 0
  ```

### Logical Operations

- **et** : Logical AND (et): Returns `vrai` if both operands are `vrai`; otherwise, returns `faux`.

  ```faux
  x <- vrai et vrai              # returns vrai
  x <- vrai et faux              # returns faux
  x <- faux et faux              # returns faux
  ```

- **ou** : Logical OR (ou): Returns `vrai` one or both operands are `vrai`; otherwise, returns `faux`.

  ```faux
  x <- vrai ou vrai              # returns vrai
  x <- vrai ou faux              # returns vrai
  x <- faux ou faux              # returns faux
  ```

- **=** : Logical Equals (=): Returns `vrai` operands values are equals ; otherwise, returns `faux`.

  ```
  x <- vrai = vrai               # returns vrai
  x <- 5 = 5                     # returns vrai
  x <- "hello" = "hi"            # returns faux
  ```

- **!=** : Logical Not (!=): Returns `vrai` operands values are diffrent ; otherwise, returns `faux`.

  ```
  x <- vrai != vrai                  # returns faux
  x <- 5 != vrai                     # returns vrai
  x <- "hello" != "hello"            # returns faux
  ```

## code simples
