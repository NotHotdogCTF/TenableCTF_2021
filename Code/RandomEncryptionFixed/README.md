This is the fixed version of the Random Encryption Challenge

We are given an encryption program

```
import random
flag = "flag{not_the_flag}"
seeds = []
for i in range(0,len(flag)):
    seeds.append(random.randint(0,10000))

res = []
for i in range(0, len(flag)):
    random.seed(seeds[i])
    rands = []
    for j in range(0,4):
        rands.append(random.randint(0,255))

    res.append(ord(flag[i]) ^ rands[i%4])
    del rands[i%4]
    print(str(rands))

print(res)
print(seeds)
```

And a sample output

```
[249, 182, 79]
[136, 198, 95]
[159, 167, 6]
[223, 136, 101]
[66, 27, 77]
[213, 234, 239]
[25, 36, 53]
[89, 113, 149]
[65, 127, 119]
[50, 63, 147]
[204, 189, 228]
[228, 229, 4]
[64, 12, 191]
[65, 176, 96]
[185, 52, 207]
[37, 24, 110]
[62, 213, 244]
[141, 59, 81]
[166, 50, 189]
[228, 5, 16]
[59, 42, 251]
[180, 239, 144]
[13, 209, 132]
[184, 161, 235, 97, 140, 111, 84, 182, 162, 135, 76, 10, 69, 246, 195, 152, 133, 88, 229, 104, 111, 22, 39]
[9925, 8861, 5738, 1649, 2696, 6926, 1839, 7825, 6434, 9699, 227, 7379, 9024, 817, 4022, 7129, 1096, 4149, 6147, 2966, 1027, 4350, 4272]
```

The only important bits from this is the code and the last two lines of output
The res is our ciphertext and the seeds are the random seeds which will ensure we get the exact same random numbers as in the original run

I wrote the backwards version of the encryption program and it is included here in re.py

Essentially, we loop through every seed -- there is one seed for each character of the actual flag (which is longer than the fake one given)
We then calculate 4 random integers and xor the i%4th one with our res number. This is because XOR is its own reverse function and will return the original value
We then turn it back into a character and append it to our clear string

Once we have gone through all the seeds we have our flag:

flag{Oppsie_LULZ_fixed}

