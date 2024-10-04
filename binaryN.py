# Python code for co-binary palindromes 

def convert_into_binary(number): 
	return bin(number).replace("0b","") 

def reverse_it(number): 
	number = str(number) 
	return number[::-1] 

def is_palindrome(number): 
	if number == int(reverse_it(number)) : 
		return True
	else: 
		return False

# starting number 
m = 300

# ending number 
n = 1000
bin_pals = [] 

for i in range(m,n+1): 
	if is_palindrome(i) == True and is_palindrome( 
			int(convert_into_binary(i))): 
		
		bin_pals.append(i) 
		
print(bin_pals) 
