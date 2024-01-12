//
// Created by Ethan on 9/13/2023.
//

#include "hackathonbot.h"

HackathonBot::HackathonBot():balance(0),holding(true), upStreak(0),downStreak(0){
    prices.push_back(100);
}

void HackathonBot::takeAction(float price)
{
    if (prices.empty()) {prices.push_back(price);}
    if (price < prices.back())
        {
            upStreak = 0;
            downStreak++;
        }
    else if (price > prices.back())
        {
            upStreak++;
            downStreak = 0;
        }
    else
        {
            upStreak = 0;
            downStreak = 0;
        }
    prices.push_back(price);

    if (holding) // after buying, has purchase price
    {
        float change = (price - purchasePrice) / purchasePrice * 100;
        if (abs(change) <= 5)
        {
            constantStreak++;
            if (constantStreak >= 10)
            {
                this->sell(price);
                constantStreak = 0;
                return;
            }
        }

        int window = prices.size();

        if (downStreak >= 47 || upStreak >= 52 || change > 89 \
            or change < -62)
        {
            this->sell(price);
            return;
        }
        else if(window > 3 && prices[window] <= .75*prices[window-1] && \
        prices[window-1] >= 1.15*prices[window-2] && prices[window-2] <= .85*prices[window-3] && \
        prices[window] <= .55*prices[window-3])
        {
            this->sell(price);
            return;
        }
        else if(window > 3 && prices[window] >= 1.3*prices[window-1] && \
        prices[window-1] <= .85*prices[window-2] && prices[window-2] >= 1.2*prices[window-3] &&\
        prices[window] >= 1.5*prices[window-3])
        {
            this->sell(price);
            return;
        }
    }
    else
    {
        if (price < 52 || downStreak >= 5)
        {
            this->buy(price);
            return;
        }
    }
}

void HackathonBot::buy(float price)
{
    this->holding = true;
    prices.clear();
    balance -= price;
    purchasePrice = price;
    upStreak = 0;
    downStreak = 0;
    prices.push_back(price);
}

void HackathonBot::sell(float price)
{
    this->holding = false;
    prices.clear();
    balance += price;
    upStreak = 0;
    downStreak = 0;
    prices.push_back(price);

}

bool HackathonBot::isHolding()
{
    return this->holding;
}

double HackathonBot::getBalance()
{
    return this->balance;
}
