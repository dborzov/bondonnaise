
# Running the script
The script is written in Python 2.7 which tends to be available on most Linux distributions by default (on MacOSX too). Please refer to, for example, instructions [here](http://docs.python-guide.org/en/latest/) for details on how to install Python if it is not. No packages outside of the standard library are used so all that is needed  in most cases is to clone the repo.

To run it, clone the repo, `cd` into the repo's directory and run:
```
python challenge[12].py
```
The scripts expects to find a `input.csv` file in the directory and will output the result into `challenge[12].csv`.

# Overview of the code structure
Reusable components are a dedicated python module within `bondspread` directory.

Here is a short rundown of it:

* `bondspread/serialize.py` - contains deserializer of the specified Bond's csv format
* `bondspread/closest.py` -functions that identify the  element closest to a point in a sorted list or the range segment that contains a value
* `boundspread/interpolate.py` - contains a linear interpolation function  

## Tests
Unit tests for the more complex parts of the code are within `bondspread/test_*.py` files.

To run all the unit tests use:
```
python -m unittest discover -v
```

# Algorithm
We read the csv and load all the dcitionaries for government bonds in a hash table `bonds_gov`:
```
bonds_gov dict[float(bond's term)]-> list of bonds with this term
```
and the list of unique values for unique government bond's terms.

We then traverse through the list of corporate bonds to identify the closest smaller and higher value with a binary search:
```
low = 0; high = len(l)-1
while low +1 < high:
    mid = (low + high)/2
    if l[mid]==val:
        low = mid
        high = mid
    if l[mid] > val:
        high = mid
    elif l[mid] < val:
        low = mid
return low,high
```
For challenge 1 we get the one closer by absolute value, and for challenge 2 we use those bounds for linear interpolation.
