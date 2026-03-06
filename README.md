# TWEED_SC2
This repository hosts part of the material for the 2nd specific course in the TWEED project, held in March 2026 in DTU, Denmark.

## How to start

1. Make sure you have the right development environment setup, i.e., Git, Python and 
MiniConda for environment. Check the [Guide](
development_environment_setup.md) to learn hwow do it.

2. Open you Git terminal, move to the directory you want to put this 
repo, and create a dedicated environment by running:

```
conda create -n tweed_sc2 python=3.13
```

3. Activate the environment and clone the repo here:
```
conda activate tweed_sc2
git clone https://github.com/ju-feng-dk/TWEED_SC2.git
```

4. Install this package, which will install also the necessary libraries:

```
cd TWEED_SC2
pip install -e .
```

Now you have your development environment set up and you are ready to go!

## Content
You can find some useful notes here:
* [Useful Notes](tweed_sc2/useful_notes/README.md)

Also the two final projects here:
* [Wind power forecasting](tweed_sc2/wind_power_forecasting/README.md)
* [Wind turbine fault detection](tweed_sc2/wind_turbine_fault_detection/README.md)