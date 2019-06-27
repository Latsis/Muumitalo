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

Muumipappa is a huge hockey fan. When Finland won the world championship in 2019, he was one of the first celebrators at the Muumilaakso market square. After Muumimamma told him that his hockey fever is getting out of hand, Muumipappa decided to lock himself inside the Muumitalo. He won't let anyone in unless they know the password, which is also his favourite song. After the market square celebrations Muumipappa has listened to only one song non stop, so you know that the password is ```loikomorkosisaan```. Unfortunately, Muumipappa is also a huge fan of hacker movies so he might be using a "l337 5p34ky" spelling. You have to guess the right spelling of the word by trying different mutations of ```loikomorkosisaan```.

Attempt the following mutations:

* Change letters to lower/uppercase
* "l337 5p34k1fy" it. (Pappa isn't too fancy with his leet speak so only characters you have to be worried about are o and i. O can potentially be 0 and i can potentially be 1).

Server will return 404 if you guessed wrong, 200 if you guessed right and something else if it breaks down due to inproper input.
