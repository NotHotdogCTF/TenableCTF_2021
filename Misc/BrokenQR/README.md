In this challenge we were given an image of a qr code with bits erased

To solve this challenge we simply had to reconstruct the qr code

I chose to do this manually

I opened the image in gimp and set my brush to one "block" (12)

We can see that from the damaged parts we have two of the position blocks damaged, we can fix these as they are of fixed size and shape

Next, we can go through and fix all of the blocks that are partially white as in a qr code a block is either entirely white or entirely black

Luckily, this is all the fixing we need to do and we now have a working qr code

If we scan it we get our flag

flag{d4mn_it_w0nt_sc4n}
