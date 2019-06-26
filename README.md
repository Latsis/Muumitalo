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

Muumipappa likes hockey and was at the market square celebrating Finland's world championship, so you know that the password must be ```loikomorkosisaan```. Unfortunately, Muumipappa is also a huge fan of hacker movies so he might be using a "l337 5p34ky" version as the password. You have to guess the right spelling of the word by trying different mutations of ```loikomorkosisaan```.

Attempt the following mutations:

* Change letters to lower/uppercase
* "l337 5p34k1fy" it. (Pappa isn't too fancy with his leet speak so only characters you have to be worried about are o and i. O can potentially be 0 and i can potentially be 1).

Server will return 404 if you guessed wrong, 200 if you guessed right and something else if it breaks down due to inproper input.
