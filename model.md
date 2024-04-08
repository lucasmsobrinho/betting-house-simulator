This is a betting house simulator.

- house
    - how many
- games
    - 
    - odds
- players
    - investment strategy
        - risk model
        - position model
        - allocation model
- bets

## The project target

I want to write an fast, optimized structure to run experiments.

So, you can run a house by choose between initial parameters, and explore things like:

- evaluate which kinds of players win more?
- evaluate which house strategies are more efective?
- which kind of games make the house win more often?
- which kind of odds strategies make the house more prolific?
- what happens to distribution of players if we start to sign off players with less than $x, and add another player in his place?


## The structure

The **house** has a lot of **games** going on, which each **player** can set **bets** upon for certain amount of time until the realization of the **game** (the winner is chosen).

Each **game** is an event with a **probability** for 2 outcomes for winner: Team A or Team B.

The house holds an estimate of winner for each game, which is not necessarily the true probability.

The house also holds an prediction over the distribution of players and total bets for each game.

With these two information, and with the current allocation, the house calculate the odd multiplier for each outcome in the game.

Each player also have an investment strategy, which is composed by:
- risk model: decide on which game to invest
- position model: decide on which side to invest
- allocation model: decide how much to be invested to invest on each side
- (buy out strategy): decide on when and how much money to extract from house
- (rebuy strategy): how much money to buy in to the house

After the experiment is run for N games, it outputs a csv with the whole house history.



