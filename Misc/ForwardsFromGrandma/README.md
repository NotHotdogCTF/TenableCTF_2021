In this challenge we are given an email file

From the title we can see that we should look at the forwards in the subject line

```FWD: FWD: RE: FWD:  FWD: RE: FWD: FWD:  FWD: RE:  RE: RE: FWD: { FWD: FWD:  FWD: FWD: RE: RE: FWD: RE:  RE: RE:  FWD: FWD:  FWD: FWD: FWD:  FWD: FWD: FWD:  FWD: FWD: RE: RE: FWD: RE:  FWD: RE:  RE: RE: RE:  FWD: RE: FWD: FWD: }``` (Formatted to remove line breaks)

We can see that there are weird brackets in there almost like a flag

We can also see that the FWDs and REs are broken into several groups

To me this looks a lot like morse code

Since we know the format of flags (flag{}) we can translate flag into morse code ```..-. .-.. .- --.```

This lines up with the part of the coded text before the {, thus we know that FWD: is a . and RE: is a -

We can now translate the entire coded message: 

```..-. .-.. .- --.{ .. ..--.- -- .. ... ... ..--.- .- --- .-..}```

This translates to:

flag{i_miss_aol}
