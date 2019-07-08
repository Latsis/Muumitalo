# Muumitalo

Python based flask server for demonstrating brute force attacks.

## What you need

* python
* flask

## How to start

```
sh build_muumitalo.sh
```
Server is hosted at ```localhost:5000 ```


## How to use

You find Muumipappa at the endpoint ```localhost:5000/ovi/```. You have to answer his question correctly in order to get to Muumitalo. The answering is done by sending a POST request to the endpoint. Content of the request should be in the following format: ```{"answer":"<your guess here>"} ```.

### Task

Muumipappa is a huge hockey fan. When Finland won the world championship in 2019, he was one of the first celebrators at the Muumilaakso market square. Pappa has been listening to the hit song about their acquaintance Mörkö on nonstop ever since, which resulted in Muumimamma losing her temper. After Muumimamma told Muumipappa that he should occasionally listen to something else, he decided to lock himself inside the Muumitalo. Muumipappa said that he will come out only if you help him relive the moment when Finland won the championship by taking him somewhere where his music taste is appreciated.

So, your task is to lure Muumipappa out by sending him a POST request that contains the word ```torille```. Unfortunately, Muumipappa is also a huge fan of hacker movies so he might prefer a "l337 5p34ky" version of it. You have to guess the right spelling of the word by trying different mutations of ```torille```.

Attempt the following mutations:

* Change letters to lower/uppercase
* "l337 5p34k1fy" it. (Only characters you have to be worried about are o, i and e. O can potentially be 0, i can be 1 and e can be 3. The correct word could be for instance t0riLl3).

Server will return 404 if you guessed wrong, 200 if you guessed right and something else if it breaks down due to inproper input.
