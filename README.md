### mcrits
##### Visualize CRITs IOC's in Maltego
-------------------------------------------------

mcrits is a set of Maltego transforms that enable you to visualize your CRIT's DB, which currently includes the ability to view the current campaigns, the types of indicators in each campaign, as well as the indicators for each campaign. There is an abundance of information available in CRITs, so I'm trying to determine the best way to visualize that in Maltego without overloading the user and maintaining some sort of order. If you have any additions you think would be good to mcrits, please let me know.

### Installation

```
$ cd /opt
$ git clone git@github.com:brianwarehime/munk.git
In Maltego, click on Maltego icon > Import > Import Configuration
Select mcrits.mtz
```

Before running mcrits, you will need to edit the configuration file mcrits/local/mcrits.conf. In this file are the necessary variables needed to contact your CRITs server, as well as the credentials and API key to use. 

### Using mcrits

After you edited the configuration file and imported the mcrits.mtz file into Maltego, you are ready to go. To get started, from the palette, under mcrits, drag the "CRITs Server" icon into the main graph window. Right-clicking on this will allow you to list the current campaigns in your CRITs DB. Next, you can select all or one of the indicator type icons under the campaign and right-click to select the "List Indicators" transform. This will list each indicator under the appropriate campaign and type. Below is a screenshot of a sample environment.

<p align="center">
<img src="http://f.cl.ly/items/1X202V2y0F0x2R1G1w2H/Screen%20Shot%202014-11-17%20at%2011.38.04%20AM.png"></p>

