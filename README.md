# Samuel Beckett and  Gray codes
A python script that finds Beckett-Gray, Gray codes. 

**Run**

python beckett_gray.py [-a | -b | -u | -c | -p] [-r] [-f] [-m] number_of_bits

Parameters meaning:

• ```-a```: find and display all codes.

• ```-b```: find and display only Beckett-Gray codes.

• ```-u```: find and display only Beckett-Gray paths (not cycles).

• ```-c```: find and display Beckett-Gray cycles.

• ```-p```: find and display only Gray paths.

• ```-r```: find and display reverse isomorphs.

• ```-f```: displaying of the full binary form of each code.

• ```-m```: display each code in the form of a table.

• ```number_of_bits```: number of bits.

Examples:
```
#  Example 1
python beckett_gray.py -a 3 

or 

python beckett_gray.py 3

#Output

C 01020102
P 0102101
C 01210121

#  Example 2
python beckett_gray.py -b 5

Output 

B 01020132010432104342132340412304
B 01020312403024041232414013234013
B 01020314203024041234214103234103
B 01020314203240421034214130324103
B 01020341202343142320143201043104
B 01023412032403041230341012340124
B 01201321402314340232134021431041
B 01203041230314043210403202413241
B 01203104213043421310342104302402
B 01230121430214340230341420314121
B 01230124234140231410343201434204
B 01230401231340413234202341024212
B 01230401232430423134101432014121
B 01230412320434120343014312041323
B 01234010232430124313401432014121
B 01234010232430201432014132413141

#  Example 3
python beckett_gray.py -b 5 -r

output to the file bgc_cycles_4.txt

# Example 4
python beckett_gray.py -c 4

output to the file gc_cycles_4.txt 

# Example 5 
python beckett_gray.py -u 3

Output : 
U 0102101

# Example 6
python beckett_gray.py -u 4

Output:
U 010213202313020
U 010213212031321
U 012301202301230
U 012301213210321

# Example 7
python beckett_gray.py -b -f 5

output to the file : bgc_5_full.txt

# Example 8 
python beckett_gray.py -u -m 4

U 010213202313020
0 1 1 0 0 0 0 0 1 1 1 1 1 0 0 1
0 0 1 1 1 0 0 0 0 0 0 1 1 1 1 1
0 0 0 0 1 1 1 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 1 1 1 1 0 0 1 1 1 1
U 010213212031321
0 1 1 0 0 0 0 0 0 0 1 1 1 1 1 1
0 0 1 1 1 0 0 0 1 1 1 1 0 0 0 1
0 0 0 0 1 1 1 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 1 1 1 1 1 0 0 1 1 1
U 012301202301230
0 1 1 1 1 0 0 0 1 1 1 0 0 0 0 1
0 0 1 1 1 1 0 0 0 0 0 0 1 1 1 1
0 0 0 1 1 1 1 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 1 1 1 1 0 0 0 0 1 1
U 012301213210321
0 1 1 1 1 0 0 0 0 0 0 0 1 1 1 1
0 0 1 1 1 1 0 0 1 1 1 0 0 0 0 1
0 0 0 1 1 1 1 0 0 0 1 1 1 1 0 0
0 0 0 0 1 1 1 1 1 0 0 0 0 1 1 1
```

**Ever tried. Ever failed. No matter. Try again. Fail again. Fail better.**