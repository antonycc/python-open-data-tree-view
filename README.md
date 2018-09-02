Tree View
=========

(python-open-data-tree-view)

A demonstration of individual building data combined with open data to calculate the likelihood that a tree is visible. The calculations are illustrative only, any accuracy is purely coincidental. 

Features:
* Excel as input
* Excel as output
* Remote store realisations (customer data, parameters and data sets)
* Web Render
* Open Data import


Python 3 and libraries
----------------------

Virtualenv:
```shell
$ rm -rf venv
$ pip3 install virtualenv --user
Requirement already satisfied: virtualenv in /Users/antony/Library/Python/3.7/lib/python/site-packages (16.0.0)
Antonys-MacBook-Pro:python-open-data-tree-view antony$ python3 -m virtualenv --no-site-packages venv
Using base prefix '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7'
/Users/antony/Library/Python/3.7/lib/python/site-packages/virtualenv.py:1041: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  import imp
New python executable in /Users/antony/projects/python-open-data-tree-view/venv/bin/python3.7
Also creating executable in /Users/antony/projects/python-open-data-tree-view/venv/bin/python
Installing setuptools, pip, wheel...done.
$ python --version
Python 2.7.10
$ source venv/bin/activate
$ python --version
Python 3.7.0 (default, Sep  2 2018, 14:52:21) 
[Clang 9.1.0 (clang-902.0.39.2)]
$ python3 -m pip install '.'
$ 
```

TODO: Instead of virtualenv use: `python3 -m venv venv` and `. venv/bin/activate`



Trouble shooting
----------------

Manual install for Pandas:

```shell
$ python3 -m pip install pandas --upgrade
$ python3 -m pip install logmatic-python --upgrade
$ python3 -m pip install flask --upgrade
```

Library locations:
* http://pandas.pydata.org/
* http://flask.pocoo.org

Macos Python and clean up and reinstall:
```shell
$ brew uninstall --force python
$ brew uninstall --force python3
$ pip freeze | xargs pip uninstall -y
$ rm -rf /usr/local/lib/python*
$ rm -rf /usr/local/bin/pip*
$ rm -rf /usr/local/bin/python*
$ rm -rf /Users/antony/.pydistutils.cfg
$ brew install python3
$ pip3 install --upgrade pip setuptools wheel
```
Source of (pip freeze): https://stackoverflow.com/questions/11248073/what-is-the-easiest-way-to-remove-all-packages-installed-by-pip


Usage
-----

To run the tests (which generate output)
```shell
$ source venv/bin/activate
$ python3 -m pip install '.'
$ python3 -m unittest discover '.'
```

To avoid this:
`Command "python setup.py egg_info" failed with error code 1 in`
Start with:
```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

Input
-----

Data structures showing size and location of windows on each floor and wall

`My building.csv`

| floor_height | face_direction | window_vertical_position | window_height | window_width |
|--------------|:--------------:|-------------------------:|--------------:|-------------:|
| 0.0 |  0.0 | 0.5 | 1.0 | 0.5 |
| 0.0 |  0.0 | 0.0 | 2.0 | 2.0 |
| 0.0 |  0.0 | 0.5 | 1.0 | 0.5 |
| 0.0 | 90.0 | 0.0 | 2.0 | 2.0 |
| 3.0 | 90.0 | 0.0 | 2.0 | 2.0 |


Output
------

Data structures showing:
* From anywhere in the building, how much of a tree can be viewed
* From each window, is a tree visible (also rendered as pie chart)

As JavaScript:
```javascript
{
   "building_name":"My building",
   "building_id":"ba5ff5f3-eec1-4128-84b7-975f44e96c96",
   "summary":{
      "likelihood_of_seeing_tree_propability":1.0,
      "amount_of_tree_fraction":0.75
   },
   "parameters":{
      "threshold_for_tree_viewing_fraction":0.25,
      "propability_to_amount_of_tree_ration":0.8
   },
   "datasets":[
      {
         "dataset_name":"Tree height",
         "location_url":"http://somedata.nl",
         "obtained_datetime":"2018-09-02T07:46:38Z",
         "file_hash":"20faf4bf0bbb9ca9b3a47282afe713ba53c9e243bc8bdf1d670671cb"
      }
   ],
   "floors":[
      {
         "floor_height_above_ground_meters":0,
         "walls":[
            {
               "face_direction_degrees":0,
               "windows":[
                  {
                     "window_top_height_above_floor_meters":1.5,
                     "window_bottom_height_above_floor_meters":0.5,
                     "window_width_meters":0.5,
                     "likelihood_of_seeing_tree_propability":0.25
                  },
                  {
                     "window_top_height_above_floor_meters":2,
                     "window_bottom_height_above_floor_meters":0,
                     "window_width_meters":2,
                     "likelihood_of_seeing_tree_propability":0.5
                  },
                  {
                     "window_top_height_above_floor_meters":1.5,
                     "window_bottom_height_above_floor_meters":0.5,
                     "window_width_meters":0.5,
                     "likelihood_of_seeing_tree_propability":0.25
                  }
               ]
            },
            {
               "face_direction_degrees":90,
               "windows":[
                  {
                     "window_top_height_above_floor_meters":2,
                     "window_bottom_height_above_floor_meters":0,
                     "window_width_meters":2,
                     "likelihood_of_seeing_tree_propability":0.75
                  }
               ]
            }
         ]
      },
      {
         "floor_height_above_ground_meters":3,
         "walls":[
            {
               "face_direction_degrees":90,
               "windows":[
                  {
                     "window_top_height_above_floor_meters":2,
                     "window_bottom_height_above_floor_meters":0,
                     "window_width_meters":2,
                     "likelihood_of_seeing_tree_propability":1
                  }
               ]
            }
         ]
      }
   ]
}
```

As tabular data (window tree view probability only):

`My building ba5ff5f3-eec1-4128-84b7-975f44e96c96.csv`

| floor_height | face_direction | window_vertical_position | window_height | window_width | tree_propability |
|--------------|:--------------:|-------------------------:|--------------:|-------------:|-----------------:|
| 0.0 |  0.0 | 0.5 | 1.0 | 0.5 | 0.5 | 0.25 |
| 0.0 |  0.0 | 0.0 | 2.0 | 2.0 | 0.5 | 0.5  |
| 0.0 |  0.0 | 0.5 | 1.0 | 0.5 | 0.5 | 0.25 |
| 0.0 | 90.0 | 0.0 | 2.0 | 2.0 | 0.5 | 0.75 |
| 3.0 | 90.0 | 0.0 | 2.0 | 2.0 | 0.5 | 1.0  |


Data Sources
-----------

Tree height:
* The tree height data Ron mentioned in our phone call is the AHN. 
* The AHN is a file with levels measured by airplane. For open terrain, it results in groundlevels. In Urban areas you'll find rooflevels and for locations with trees the AHN gives the top of the vegetation.
* The data can be found here: https://data.overheid.nl/data/dataset/ngr-ahn3-0-5-meter-dsm
* This link refers to raw data. There are also data sets in which vegetation and buildings are filtered out to get groundlevels.
