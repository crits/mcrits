### mcrits
##### Visualize CRITs IOC's in Maltego
-------------------------------------------------

mcrits is a set of Maltego transforms that enable you to visualize your CRIT's DB, which currently includes the ability to view the current campaigns, the types of indicators in each campaign, as well as the indicators and actors in each campaign. There is an abundance of information available in CRITs, so I'm trying to determine the best way to visualize that in Maltego without overloading the user and maintaining some sort of order. If you have any additions you think would be good to mcrits, please let me know.

### Installation

```
$ cd /opt
$ git clone git@github.com:brianwarehime/munk.git
In Maltego, click on Maltego icon > Import > Import Configuration
Select mcrits.mtz
```

Before running mcrits, you will need to edit the configuration file mcrits/local/mcrits.conf. In this file are the necessary variables needed to contact your CRITs server, as well as the credentials and API key to use (You can generate an API key in CRITs, in your user profile setings). You will also need to enable API access for mcrits to be able to use CRITs. This can be done by going into CRITs and clicking on the gear icon in the top left, next, select "CRITs Control Panel", then under "SYSTEM", go into "General". There will be an option about 4 lines down, to "Enable API". Once you enable it, do a quick restart ```service apache2 restart``` and you should be good to go.

### Using mcrits

After you edited the configuration file and imported the mcrits.mtz file into Maltego, you are ready to go. To get started, from the palette, under mcrits, drag the "CRITs Server" icon into the main graph window. Right-clicking on the CRITs server will allow you to list the current campaigns in your CRITs DB. There are two categories of campaigns that will be displayed under the server, one is the campaigns you define, and the other is an "UNKNOWN" default category that will hold all the indicators that aren't assigned to a campaign. So, once the campaigns are displayed, you can right-click on each campaign to either display the indicator types or the actors belonging to that campaign. For now, the actors are the last-object and there is no more transforms available, however, if you right-click on an indicator type, you can list the indicators belonging to that type and that campaign. Below is a screenshot of a sample environment.

Instead of filling up the pallette with tons and tons of icons for each type of indicator, I just assigned a particular icon to match the big sets, such as, Windows, File, Network, DNS, IP Address, etc. So, some icons may be generic, while others have a distinguishing icon, I'll continue to update the icon sets in the future though.

<p align="center">
<img src="http://f.cl.ly/items/1d172D0j0O1g1C1c2H1s/Screen%20Shot%202014-11-18%20at%2010.04.26%20AM.png"></p>

Once you display the indicators under each type/campaign, you are able to view additional information about each indicator in the right-hand column under "Properties". Below is a snapshot of some of the available fields.

<p align="center">
<img src="http://cl.ly/image/0T3t041G3831/Screen%20Shot%202014-11-17%20at%205.31.37%20PM.png"></p>

### Todo

- Add relationships to each indicator. When you right-click on an entity, you will be able to view the relationships, which will connect the indicator to other indicators/actors/campaigns that were defined.
- Continue to add icons for more popular indicator types
