# rsa-python
This is a very basic RSA encryption system written in vanilla python. I wanted to better understand RSA, so I thought it would be cool to implement it from scratch.

# Example Usage
```
╭─lucas@macbook ~/fun/rsa-python  ‹main*›
╰─➤  python main.py
Generating 2048 bit key...
Generating 2048 bit key...

Enter a message to encrypt: "This is a test message"
  Message is 190 bits

Encrypted message: 11001357490427476071424721198163602122995219789704949774881876
932267656736992379265819063386702316948280147904704517277791693558577421581131953
963650601556676148504102825907697524308044520758662343872502250558018375101385795
922772319582573382724338928714303988717274816495891408997248512030388195468143574
410321366339103384441915669767959180057565196132629609578443094619774816165891468
509911978987006813979274491120851729233025860477480946778973551625628198252844059
225282783298851081796309619659306440063947292929299822702202847254144399836127075
651853832702245514635259974742495733361187688463075809339572316712661

Decrypted message as integer: 843390131632698784528427720828839926364399630674207200290

Decoded message: "This is a test message"
```

DISCLAIMER: This is by NO MEANS a fully secure encryption tool. It is just a toy program for playing around with basic encryption. 

