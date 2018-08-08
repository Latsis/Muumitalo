# Muumitalo

Python based flask server.

## What you need

python
flask

## How to start

```
sh build_muumitalo.sh
```
Server is hosted at ```localhost:5000 ```


## How to use

At endpoint ```localhost:5000/ovi/``` you find muumipappa. He wants you to answer his question right
You do that by sending POST requests to the endpoint.
POST requests content should be in following format ```{"answer":"your guess here"} ```

Answer is his favourite drink vaapukkamehu. After reading too many hacker books he however changed the name to more "l337" speaky. Guess the right spelling of the word by trying different mutations of the word "vaapukkamehu"

Attempt the following mutations:

* Change letters to lower/uppercase
* l337 speakify it. (Pappa isn't too fancy with his leet speak so only characters you have to be worried about are a and e. E can potentially be 3 and a can potentially be 4).

Server will return 404 if you guessed wrong, 200 if you guessed right and something else if it breaks down due to inproper input.
