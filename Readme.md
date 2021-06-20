# Project structure
This project can be separated in 2 distinct parts:
1. The algorithm part
2. The result part

## Algorithms
The algorithms are implemented in java. The only file of interest here is Odb\src\Validation\PerformanceTest.java, which is a java file that runs the test method to find the accuracy of our algorithm. For more information read from Odb\README.md. NOTE: The database is contained within the Odb folder.
## Results
The results part consists of all the files in the Results folder. Here you will find 3 types of files: .csv files, .py scripts and .png images. the relationship between them is as follows:
### .csv files
They store test runs: they store the parameters with which the method test specified in Odb\src\Validation\PerformanceTest.java was run as well as the results that it produced.
### .py scripts
These scripts "make sense" of the data saved in .csv files. They create the data (param.py), load the data, and visualize the data.
### .png files 
These are files used through my paper to show the data. They are generated from .py files using plotting libraries for Python.