### mcrits
##### Visualize CRITs data in Maltego
-------------------------------------------------

mcrits allows you to visualize your CRITs DB via local Maltego transforms.

This is very unpolished code and may or may not see updates in the future
depending upon community feedback. If you use mcrits and have any feedback,
positive or negative, please let us know!

### Requirements

mcrits requires [pycrits](https://github.com/crits/pycrits). The pycrits code
is also in-flux so please be sure to stay up to date with it as the API is
subject to change.

### Installation

Clone the mcrits repository somewhere.

```
$ git clone git@github.com:crits/mcrits.git
```

You now need to configure mcrits for talking to your CRITs server. Copy the
```local/mcrits.conf.sample``` file to ```local/mcrits.conf``` and then edit
```local/mcrits.conf```. The contents of this file should be self-explanatory,
with the exception of ```verify```, which is used to control verification of
the certificate on the CRITs server.

Now that things are configured you need to import the transforms and entities
into Maltego. Do this by opening Maltego and clicking on the Maltego icon.
Select ```Import``` then ```Import Configuration```. Navigate to the
```mcrits.mtz``` file in the mcrits repository and follow the wizard from
there.

The transforms are all local transforms, and as such are configured to run on
my system (I'm trying to find a way to fix this). For now you will need to go
to the ```Manage``` menu and select ```Manage Transforms```. For each of the
CRITs transforms you need to make sure that the ```Working Directory``` points
to your mcrits repository, and that the ```Command line``` points to your
python binary.

On the CRITs server please make sure the API is enabled.

### Using mcrits

To start using mcrits pick an item from the palette and drag it to the main
graph window. As this is your first object you must edit the properties of it
to make sure any missing fields are populated. This always includes the ID
field (this is the ID of the object in CRITs, available on the details page).
Depending  upon the object there may be other fields too. You only need to do
this for the first object.

The next step is to perform a transform on the object you just editied. This
is done by right clicking the object and selecting the transform.

### Todo

- Fix "working directory" problem.
- Stop using CRITs specific entities where it makes sense.
- Probably a ton more... ;)

### Credits

- Thanks to [Brian Warehime](https://twitter.com/brianwarehime) for starting
  this project.
- Thanks to http://www.flaticon.com/ for the icons used in mcrits
