# SCOSourceControl
![Tests](https://github.com/JamieMair/SCOSourceControl/actions/workflows/python-app.yml/badge.svg)

## User

University Username:

Real Name:


# Project Description

A project to help learn the basics of source control. The main code of the project is in python and focuses on writing functions which handle nearest neighbour calculations.

The idea of this task is to practise using Git and test driven development. The code you will be implementing will be based on calculating the nearest neighbours of points in a d-dimensional space. The code you need to write for this project is minimal. There are some additional functions to implement to practise plotting in Python.

You should only need to modify `main.py`, and you do not need to change any of the tests.

**Note:** In order to have the tests badge to run correctly you have to change the link in this markdown file to: `https://github.com/UoNPhysics/REPOSITORYNAME/actions/workflows/python-app.yml/badge.svg`, making sure to replace `REPOSITORYNAME` with the name of your own repository. To edit, click the pencil icon where the markdown file is displayed. You will end up with something at the top of your README.md file like this:
```
![Tests](https://github.com/UoNPhysics/sourcecontrol-JamieMair/actions/workflows/python-app.yml/badge.svg)
```

# Getting Started Video

[![Watch the video](https://img.youtube.com/vi/Lrq5c3U7FdY/maxresdefault.jpg)](https://www.youtube.com/watch?v=Lrq5c3U7FdY)

# Troubleshooting

Below is a video which goes over all of the issues you may see when trying to get your code to work. If you have an issue, it is most likely covered in this video.

[![Watch the video](https://img.youtube.com/vi/LSNNDcguQx0/maxresdefault.jpg)](https://www.youtube.com/watch?v=LSNNDcguQx0)

## Some Frequent Issues/Questions:
**1. The modules are not imported correctly**

_This likely happens because the version of python in the terminal, or selected by VS code is wrong. Try opening a new terminal to begin with. Make sure you have installed all the dependencies with `pip install -r requirements.txt`. You can have multiple versions of python on your computer, it is important to make sure you are using the right one._

**2. Debugging gives a numpy error when using the base anaconda environment**

_If you have installed anaconda, it is likely your default python. This version has issues with debugging, which is very useful for developing. You need to create a new environment in the anaconda terminal. Detailed instructions are in the video. The command to do this is:_
```
conda create -n uni python==3.8
```

**3. Cannot discover tests**

_This is likely due to not having installed the correct dependencies. For example, you may not have installed them to right version of python. You must select the correct python interpreter from the menu (type Ctrl+Shift+P and then start to type interpreter, and choose "Select Python Interpreter" from the drop down menu). You must make sure this version of python has the scipy, matplotlib, numpy and pytest packages installed. More detailed instructions are in the video._

**4. What am I even meant to do?**

_Below are all of the tasks. If you are not sure what to do after watching the videos, and you have setup VS Code correctly, you need to start by creating a new branch in Github Desktop, and then implementing the functions inside of `main.py`. There are two functions which currently have the word `pass`. Replace this word with the correct implementation until the tests pass. Make sure you do not edit any of the tests. There are some instructions on ways of developing your code at the end of the troubleshooting video._

# Tasks (Make sure you read these carefully)

1. Download the repository to your local machine using Github Desktop or another Git client.
2. Read through the `main.py` file in the 'nearestneighbour' folder.
3. Make sure you can run the tests. Try running `python -m pytest` from your console. If the code does not run due to import errors use `pip install -r requirements.txt` to install *numpy*, *matplotlib* and *pytest*. Make sure that the commands are run in the SCOSourceControl folder (the same folder as requirements.txt).
4. Create and switch to a new branch **before** making any changes.
5. Update the README.md file as detailed above to fix the test badge - this can be your first branch and pull request. Check video for details.
6. Fetch changes from the origin repository, and switch to a new branch to start implementing the functions in `main.py`.
7. Implement the two unimplemented functions in `main.py`, as detailed in their docstrings.
8. When you have finished implementing your function, run the tests to make sure they are correct!
9. Commit your code along with a description of what you have done.
10. Push this commit to the Github repository.
11. Create a pull request to merge in your changes to the main branch. 
12. Keep iterating on your code until all tests pass.
13. Add your university username and real name to the top of the file in the location indicated.

# Additional Tasks

We have included some optional tasks here in case you want to practise your programming!

## Optimisation
Try to write an optimised version of your code, particularly the `find_all_nearest_neighbours` function, which can solve the program as fast as possible. There is a unit test in the code already written to test this, but it is commented out. You can uncomment the code to see how long it takes to run your code.

## Learn some Big O notation
Look up what "computational complexity" is, and try to graph the time taken to calculate the `find_all_nearest_neighbours` function as a function of the size of the point cloud. You should be able to measure the complexity of your algorithm using this graph, and analysing your code.
