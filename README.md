# Roulette Simulation
This repository contains two Python scripts for simulating roulette.

## First Simulation: roulette_simulation.py
In this simulation, we start with a certain initial amount and bet 1 dollar each time. In case of a win, we return the invested amount and continue playing. In case of a loss, we double the bet to cover previous losses and potentially make a profit. The simulation stops after the first win.

This simulation illustrates the classic roulette strategy, but it is important to note that it is not sustainable in the long run as it does not guarantee a profit.

To run the simulation, use the following commands:

bash
Copy code
python roulette_simulation.py

## Second Simulation: roulette_simulation_2.py
In this simulation, we always bet half of the current amount. It starts with a certain initial amount and bets half of that amount each time. In case of a win, it returns the invested amount and continues playing. This simulation also stops after the first win.

It is important to note that the second simulation has its drawbacks as it reduces the stakes, which can result in losses in the long run.
Actually, second simulation makes no sense, but it looked like a good idea at first sight.

To run this simulation, use the following commands:
bash
Copy code
python roulette_simulation_2.py

# Note
Both simulations are illustrative only, and it is not recommended to use them for real gambling or investment. Roulette is a game of chance, and the results are random. Players should be aware of the risks and gamble responsibly.

