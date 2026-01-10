# fixitPy

Interface with the iFixit API through Python, easily.

### Current Features

- Guide Retrieval

### WIP Features

- Guide image retrieval
- text based searching for guides

## Installation

To install fixitPy

````bash
pip install fixitpy
````

### Using the library

#### Retrieving a guide *without prerequisites*

This returns a dict that contains information pertaining to the guide

````py
import fixitpy

found_guide = fixitpy.retrieve_guide(123) # call the retrieve_guide function which returns a dict

print(found_guide.get("title"))
print(found_guide.get("difficulty"))
````

#### Retrieving a guide *with prerequisites*

A prerequisite is an optional guide that the retrieved guide recommends you start with before. The prerequisite guide is the same dict structure of what returns from `fixitpy.retrieve_guide`

````py
import fixitpy

found_guide = fixitpy.retrieve_guide(123, get_prerequisites=True) # call the retrieve_guide function which returns a dict

print(found_guide.get("title"))
print(found_guide.get("difficulty"))

first_prerequisite = found_guide.get("prerequisites")[0]
print(first_prerequisite.get("title"))
````

# License

MIT License
