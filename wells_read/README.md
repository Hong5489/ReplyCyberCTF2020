# Wells Read
Description:
```
R-Boy finds the time machine, which Zer0 used to travel to another era. Nearby, lies a copy of HG Wells’ The Time Machine. Could this book from the past help R-Boy travel in time? Unfortunately, R-Boy can’t read or understand it, because the space-time continuum has changed some of the words. Help R-Boy to start his time travels!
```
Files: [coding.zip](coding.zip)

Extract the zip file, we are given two files:
- The Time Machine by H. G. Wells.txt
- words.txt

The first file is just a novel by `H. G. Wells`:
```
Introduction

The Time TGaveller (for so it will be convenient to speak of him) was
expounding a recondiEe matter to us. His pale grey eyes shone and
twinkled, and his usuatly pale face was feushed and animated. The fire
burnt brightly, and the soft rGdiance of the incandescent lights in the
lilies of silver caught the bubblOs that flashed and passed in our
glasses.
...
...
```

By searching online, you can find a same the [text file](http://www.gutenberg.org/files/35/35-0.txt)

And the second file contain many english words, one word each line:
```
2
1080
&c
10-point
10th
11-point
12-point
16-point
18-point
1st
2,4,5-t
2,4-d
20-point
2D
2nd
30-30
...
...
```

Notice some of the words in the first file is written wrongly like `TGaveller`, `recondiEe`, `rGdiance` etc.

I guess we need to **combine all wrong characters together, then we should get the flag.**

I download the [original novel](http://www.gutenberg.org/files/35/35-0.txt) so we can compare it

First, we compare all words in the text file

If is wrong and is one of the words in `words.txt`, we record the wrong character in the word

We used [python script](solve.py) to solve it:
```py
# Split each words
ori = open("original.txt",'r').read().split()
text = open("The Time Machine by H. G. Wells.txt",'r').read().split()
# Split each line
words = open("words.txt").read().split("\n")
flag = ""
for o,t in zip(ori,text):
	# If wrong and one of the words given
	if o!=t and o in words:
		# Loop through each character 
		# to get the wrong one
		for c1,c2 in zip(o,t):
			if c1 != c2:	
				flag += c2
				break
print(flag)
```
Result:
```
EteGOZyIy:otMeUAqDYXVu}gHNp5E6M{BD:HXJYwvjthFpSKd}PC}q5vxfSMC97yllwR74lXl{bSYMLY5{VtZ4{q{RwdP:pNv4AnK43XSl2:FF231hHCwGKQ{sppwhjiyBXy85tp0eM3DvPUwkBIwMFM5JDm7cENCr{DDNqit9rms1kCxHyDaBb68gk{V0x1BieU0H{gUV2_tSJsIbxIE{HIoAFw0p0ZvpPmZu5b}I5UEeH9dSep:Vd_otv1Ouu_LK8{6G_V2o8ga}xj0T29VlC5a0wmU8Ph{5WxJ0M4FCs5JsQq:j38vzR3RFroDXvfBq{EYKdIEARz{6IV34iVIF98aqbaa{Av:9mYAAE8gv}uOiiGYoxbWS101GdyIV:A63c}fO{BMH8WU_b5j{je61W{HkGaqmgkel{5Lf{7lRqNPvl9aXp4vpiw6x38}kOGjcoOMFtQLM847e}uU_s:lqrs:MK_baDC:Rku197CAVdq_r_TDODqLNJ8b_LQy:F:kb{}zcKvajYFVKlebq2zc{Yp_}wqLlVV6odWO7I}252f1J{H}BOQ7h5s4OjoZAhjY{FLG:1_kn0w_3v3ryth1ng_4b0ut_t1m3_tr4v3ls0:w8Wj_SJeGS_og{6k{6NshxTn:INYHC0Fz{:jpXQB28ZksKq{rsEOzF}TaYFXRZ:MA83{TjL04zO{Onxaldtlw6Aquq89K_1ofz1QzQcLjevV{Xlz3v6:BFU1TCwOqVof2kg{s6v4jSXLJSHauo8y:06CMaS:h:UBx4BCKVLj}gRrYoPSAAHtz61cAvL:Dgatm9IyGc2u1j2lJEJoT{uMvU25xmiEN9CkJB4o_zRazXalz}BD5CRFzDw6oVPikFrfSazVzHvGJ{9{aQJW}Fd01gf:EGp8{W_Tbrvc{GHT:MheEVmxXYQrxrDLVLmzut{aLIva780ZBJ9YQkTMr}5T}I2aeJxVyqHdeQegTUfU0MUwOZT{8:jD6h{MIb_8m:6qG{YrkLi3FjwPbhTs_567v:QaYF:TpThGe5fTfSXu2eKUHdEeR}1xE0Mscpfa23zTkG6_5q7UV:w2__NBpdILP4nYDhq9X3akDC6LLsHS0i9Lw5ZJF3Ic}K41jn3b6V5zykM134DlyIp:Y_xyfvlW30C0NMqDFmt1{OO:vqoTvaDtwrjKI_l_HW5G0qCpF2qwyiKNCMT3KSmI:bat9:jC7FSN3}ef6TvCLJ0KC56oBMjBFMl0aIqghx5_8yZvOi8zZi0ZT0IK7BVcl9q3dfQbXQs{l6vyH5TkWGJ}}111qZLyx2dpw{4jm495rBJQQ5R2{_hAG{Ztvp:x4XuKeY2tb00{jaigNl_2_tniQA6DA9KUb_{w5Y3uSihQSffi_UmtS4h6:_AX{DrG6Vo4DTfNjkIUw516}BOuXlb8kpxw1WsMsrc{GA}w}G}T7nmOxxa7QT5OGd6G_u_GGXjklQafi_kaAiZ_s:{jGHKjpk{VU5jkTKMHPag8gj5lNB:y{kPOkBhUZRu:G8gRzacqVgLI101mg
[Finished in 9.7s]
```
Looks like some Base64 encrypted text, but when you search for the flag format: `FLG` you will find the flag!!

## Flag
```
{FLG:1_kn0w_3v3ryth1ng_4b0ut_t1m3_tr4v3ls}
```