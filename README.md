### mcrits
##### Visualize CRITs IOC's in Maltego
-------------------------------------------------

mcrits is a set of Maltego transforms that enable you to visualize your CRIT's DB, which currently includes the ability to view the current campaigns, the types of indicators in each campaign, as well as the indicators and actors in each campaign. There is an abundance of information available in CRITs, so I'm trying to determine the best way to visualize that in Maltego without overloading the user and maintaining some sort of order. If you have any additions you think would be good to mcrits, please let me know.

### Requirements

```
pycrits Python Module
```

### Installation

```
$ cd /opt
$ git clone git@github.com:brianwarehime/mcrits.git
In Maltego, click on Maltego icon > Import > Import Configuration
Select mcrits.mtz
```

Before running mcrits, you will need to create the configuration file mcrits/local/mcrits.conf. It should look something like this (change username and api_key accordingly).

```
[info]
url = https://crits
username = test
api_key = da39a3ee5e6b4b0d3255bfef95601890afd80709
verify = True
```

You will also need to enable API access for mcrits to be able to use CRITs. This can be done by going into CRITs and clicking on the gear icon in the top left, next, select "CRITs Control Panel", then under "SYSTEM", go into "General". There will be an option about 4 lines down, to "Enable API". Once you enable it, do a quick restart ```service apache2 restart``` and you should be good to go.

Please note that this was made for *nix/OS X environments, so, if you are using this is Windows or save the transforms in another directory besides /opt, you'll need to follow the guide below to get it working.

#####Installing in Windows

Using mcrits in Windows isn't that much work, just a few things you'll need to change. In Maltego, click on the Manage tab, then "Manage Tranforms". Once the dialog pops up, click on the search bar in the top right, then type in "List". This will return all the transforms named "List " which all the transforms for mcrits start with. Go into each of the following transforms:

List Actors
List Campaigns
List Indicator Types
List Indicators
Click on each one of those, and for each one, in the bottom right, under "Transform Inputs", change the variables to fit your needs. So, change "Command Line" to where Python is, e.g. C:\Python27\python.exe, then "Command Parameters" can stay the same, lastly change "Working Directory" to where you saved the mcrits transforms, e.g. C:\Transforms\mcrits\transforms\

After that, you should be good to go. Just run the transforms as normal.

### Using mcrits

After you edited the configuration file and imported the mcrits.mtz file into Maltego, you are ready to go. To get started, from the palette, under mcrits, drag the "CRITs Server" icon into the main graph window. Right-clicking on the CRITs server will allow you to list the current campaigns in your CRITs DB. There are two categories of campaigns that will be displayed under the server, one is the campaigns you define, and the other is an "UNKNOWN" default category that will hold all the indicators that aren't assigned to a campaign. So, once the campaigns are displayed, you can right-click on each campaign to either display the indicator types or the actors belonging to that campaign. For now, the actors are the last-object and there is no more transforms available, however, if you right-click on an indicator type, you can list the indicators belonging to that type and that campaign. Below is a screenshot of a sample environment.

<p align="center">
<img src="http://f.cl.ly/items/1Y241U0Z1W2R2W2a0u46/Screen%20Shot%202014-11-18%20at%204.32.11%20PM.png"></p>

After you display the indicators from each type, you can then perform the indicator type specific functions you normally can in Maltego, such as Domain to IP, or Email Address to Social Network accounts.

<p align="center">
<img src="http://f.cl.ly/items/1U351r2o2o1k081D091b/Screen%20Shot%202014-11-18%20at%204.32.31%20PM.png"></p>

Once you display the indicators under each type/campaign, you are able to view additional information about each indicator in the right-hand column under "Properties". Below is a snapshot of some of the available fields.

<p align="center">
<img src="http://cl.ly/image/0T3t041G3831/Screen%20Shot%202014-11-17%20at%205.31.37%20PM.png"></p>

### Todo

- Add relationships to each indicator. When you right-click on an entity, you will be able to view the relationships, which will connect the indicator to other indicators/actors/campaigns that were defined.

### Credits

- Thanks to http://www.flaticon.com/ for the icons used in mcrits
- Thanks to @mjxg and @wxs for their contributions to the project.

