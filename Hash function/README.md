This program has created a hash function that converts any incoming message (string data type) into a hash (mishmash). The hash has a dimension of 256 bits and is a number in the hexadecimal number system. The resulting hash string always has two characters "0x" at the beginning and then 64 characters [0-9] and [a-f].

For example, the message "Here is a statement" becomes this hash: "0xd44b94d9bc030cecc46d1ba51d103bf5885d2355222566a1dd3fb6f9fca97f63"

About hash functions    https://en.wikipedia.org/wiki/Hash_function  
In Russian    https://habr.com/ru/post/534596/

At the end of the program, the user can test this hash function. To do this, you need to enter two messages as the variables message1 and message2. Then a hash function is taken from both messages. The counter then counts the number of matching characters in the two hashes. If the number of matches is greater than four, then the hash function is of poor quality. If about four, then good quality.

By Vladimir Romanko, March 2023.
