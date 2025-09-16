#!/usr/bin/python3

entry = input("What's the weather like today? (sunny/rainy/cold): ")

if entry == 'sunny':
    print("Wear a t-shirt and sunglasses.")
elif entry == 'rainy':
    print("Don't forget your umbrella and a raincoat.")
elif entry == 'cold':
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
