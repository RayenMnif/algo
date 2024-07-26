`
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
`
# language introduction and setup
## introduction
algo is interpreted programming language fully written in python by the brilliant dev 'Rayen Mnif' me :)
as a '3eme anne science d'informatique' student (i don't want to say cs student cause it's nothing like cs) i hated the algorithme so much even tho i was excellent and i had good grades, i hated it because it have never been an actual language, there's no way of debuging or compiling the code, there been times where teacher gived me bad grades because my code looks like nothing like what they used to be taught and what they teach even tho the code is actually corret and likely more optimized and more efficient but ofc here in Tunisia we have "a7fed wsob" policy.
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
###### note : you have to install [python3](https://www.python.org/downloads/)

## variables
algo is a dynamically typed language. This means that variables do not have types; only values do. There are no type definitions in the language except [function](###function) and [procdure](###procedure) . All values carry their own type.
### variables types


## functions
### user defined functions
#### fonction

##### general syntax
`fonction hello(name : chaine) : chaine
  debut  
    x <- "hello " + name
    retourner x
  fin
`
#### procedure
procedure in algo are more likely for organizing the code they're like moving a chunck of code, their return value is of type [Nulle](####Nulle)
##### general syntax
`procedure hello(name : chaine)
  debut  
    x <- "hello " + name
  fin
`


## code simples
