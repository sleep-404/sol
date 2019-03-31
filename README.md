# The First challenge
This challenge is named compilation challenge in the repository.
This directory has output logs of 
```sh
$ cmake ..
$ make
```
and also has a screenshot of running camserver 

------

# The Second challenge
The second challenge has a file named 2.cpp which solves this challenge.
It can be compiled and run using the below commands
```sh
$ g++ 2.cpp -o 2
$ ./2 input.txt
```
It expects an text file as input and stores the output in **output.txt**
Please check the attached ** input.txt (0 to 5)** files cases attached with this repo.
They have been made with utmost effort to gurantee the correctness.

------

# The Third challenge
This is a python implementation of Game_of_life. It has 3 three files
a **Game_of_Life.py** a python module , an **app.py** the app which implements the module
and a **test.py** which guarantees the correctness by testing all the functions in the module.
It takes in a **config.json** file where you can describe the size of the board and initial 
conditions of different cells<br />
**rows** -> number of rows of the board<br />
**coloumns** -> number of coloumns of the board<br />
**Initial** -> Cell co-ordinates where there are alive cells initially.<br />
**Zero indexing** is followed in the above line<br />
