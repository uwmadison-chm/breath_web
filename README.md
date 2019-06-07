[![DOI](https://zenodo.org/badge/189608566.svg)](https://zenodo.org/badge/latestdoi/189608566)

# Web-based breath counting tool

A django + Flash app to help track breath counting

## Overview

This is a very old (2011-vintage) Django-based web app to track breath counting performance. It has a plain HTML interface, as well as a Flash-based interface that communicates with the server.

This documentation is extremely incomplete; I'm writing it in 2019 and haven't worked on the code in about eight years.

## Installation

This is a pretty straightforward, albeit old, Django app. You may need to either install a version of Django that was modern circa 2011, or update the app to run in a modern version.

## Running experiments

To set up an experiment, go to the admin interface and create an Experiment. The following settings will be of interest:

* **URL slug**: The base path for your experiment — after creating your experiment, participants will go to `https://<your_domain>/<app_path>/<experiment_url_slug>`.
* **Run length**: How long (in seconds) you want to collect data
* **Survey url**: After data collection ends, the URL for a followup survey (in Qualtrics or REDCap or whatever)
* **Chime on error**: If you want a little ding to play for a miscount
* **Run instructions**: Custom instructions to show to the participant
* **Guide sound file**: An optional MP3 to play during data collection
* **Breath time key**: For most breaths, press this key. I'm not sure how to specify arrow keys here, but we've done that before I think.
* **End cycle key**: The key to press at the end of a count cycle
* **Cycle length**: How long the breath cycle should be
* **Practice cycles**: How much practice they'll do. There's a guided and unguided practice.
* **Use swf url**: An optional URL for a flash file to show during data collection. If this is blank, participants will see a neutral screen during data collection.



## Citing

If you use this code in your research, please cite [this paper](https://www.frontiersin.org/articles/10.3389/fpsyg.2014.01202/full):

> Levinson, D. B., Stoll, E. L., Kindy, S. D., Merry, H. L., & Davidson, R. J. (2014). A mind you can count on: validating breath counting as a behavioral measure of mindfulness. _Frontiers in psychology,_ 5, 1202.

and reference the project [on Zenodo](https://doi.org/10.5281/zenodo.3236445).

## Contributing

This project is completely unmaintained, and provided for historical and open science purposes only. There are currently no plans to maintain it again. To make changes, please fork this repository and edit in your fork.

Future iterations of this task would probably be more appropriately developed to run on [Pavlovia](https://pavlovia.org/) or [Gorilla](https://gorilla.sc/).

## Credits

This app was developed at the Waisman Center for Brain Imaging, for a study run by [Daniel Levinson](mailto:danlevinson@gmail.com). Web code was written by [Nate Vack](mailto:njvack@wisc.edu) and Flash code was written by [David Gagnon](mailto:djgagnon@wisc.edu) and Nathan Mckenzie (mailto:nathan@icecreambreakfast.com). Art is from [morguefile.com](https://morguefile.com/) and sound is from [freesound.org](https://freesound.org/).
