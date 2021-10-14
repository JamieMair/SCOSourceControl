# SCOSourceControl
![Tests](https://github.com/JamieMair/SCOSourceControl/actions/workflows/python-app.yml/badge.svg)

A project to help learn the basics of source control. The main code of the project is in python and focuses on writing functions which handle nearest neighbour calculations.

The idea of this task is to practise using Git and test driven development. The code you will be implementing will be based on calculating the nearest neighbours of points in a d-dimensional space. The code you need to write for this project is minimal. There are some additional functions to implement to practise plotting in Python.

You should only need to modify `main.py`, and you do not need to change any of the tests.

# Tasks

1. Download the repository to your local machine using Github Desktop or another Git client.
2. Read through the `main.py` file in the 'nearestneighbour' folder. Read the descriptions of the functions and what they are meant to do.
3. Discuss the functions with your group, and decide who is going to do which part. Every student will have to submit their own code.
4. Make sure you can run the tests. Try running `python -m pytest` from your console. If the code does not run due to import errors use `pip install -r requirements.txt` to install *numpy*, *matplotlib* and *pytest*. Make sure that the commands are run in the SCOSourceControl folder (the same folder as requirements.txt).
5. Create and switch to a new branch **before** making any changes.
6. Implement the function you have agreed to with your team. Use the tests to help check your function.
7. When you have finished implementing your function, commit your code along with a description of what you have done.
8. Push this commit to the Github repository.
9. Create a pull request to merge in your changes to the main branch. Have someone else review your code and agree to merge the changes into main.
10. Keep iterating on your code until all tests pass.

# Additional Tasks

We have included some optional tasks here in case you want to practise your programming!

## Optimisation
Try to write an optimised version of your code, particularly the `find_all_nearest_neighbours` function, which can solve the program as fast as possible.

## Learn some Big O notation
Look up what "computational complexity" is, and try to graph the time taken to calculate the `find_all_nearest_neighbours` function as a function of the size of the point cloud. You should be able to measure the complexity of your algorithm using this graph, and analysing your code.