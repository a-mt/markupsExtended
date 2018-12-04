# Markups extended

Create a module to add parsers to markups 3.  
It can be used to add support to new file extensions to ReText or override existing parsers.

Currently, there is one parser:
* `githubMarkdown`: replace `markups` Markdown parser with [mistletoe](https://github.com/miyuchina/mistletoe) (parse Github Flavored Markdown)

## Install

1. Check the version of markups you use

       pip3 show markups

   If you use markups < 3, upgrade it:

       sudo pip3 install markups --upgrade

2. Check in which directories you can put the package:

        python3 -c 'import sys; print("\n".join(sys.path))'

3. Put the folder in the location you chose

        sudo mv markupsExtended /usr/local/lib/python3.6/dist-packages/

4. Install the dependencies

       sudo pip3 install setuptools mistletoe

4. Make sure your folder's name is `markupsExtended` then create the egg-info to extend markups:

       sudo python3 setup.py develop

## Add your own parsers

* Create your parser
* Import it in `__init__.py`
* Add the entry point in `setup.py`
* Update the egg-info with `sudo python3 setup.py develop`
