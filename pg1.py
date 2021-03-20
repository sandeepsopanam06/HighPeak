def main():
	ip_name = "sample_input.txt"
	op_name = "sample_output.txt"
	goodiesSelect(ip_name,op_name)

def goodiesSelect(ip_name,op_name):

	with open(ip_name,'r') as ip:
		s1,s2 = splitColon( ip.readline() )
		employee = int(s2)
		ip.readline() #empty line
		ip.readline() #title ine
		ip.readline() #empty line
		
		goodies = []
		
		for line in ip:
			s1,s2 = splitColon(line)
			goodies.append((s1,int(s2)))
			
	sortGoodies(goodies)
	
	#calculate difference list
	diff_list = []
	for i in range(len(goodies)-employee):
		diff = goodies[i+employee-1][1]-goodies[i][1]
		diff_list.append(diff)
	
	#find smallest difference
	small_index = 0
	for i in range(len(diff_list)):
		if diff_list[i] < diff_list[small_index]:
			small_index=i;
	
	with open(op_name,'w') as op:
		op.write("The goodies selected for distribution are:\n")
		op.write("\n")
		for i in range(small_index,small_index+employee):
			op.write("%s: %d\n"%(goodies[i][0],goodies[i][1]))
		
		op.write("\n") #empty line
		op.write("And the difference between the chosen goodies with highest price and the lowest price is "+str(diff_list[small_index]))
		

def sortGoodies(g):
	#selection sort
	for i in range(len(g)):
		min = i
		for j in range(i+1, len(g)):
			if g[min][1] > g[j][1]:
				min = j
		temp = g[i]
		g[i] = g[min]
		g[min] = temp
		

def splitColon(str):
	for i in range(len(str)):
		if str[i] == ':':
			return str[:i],str[i+1:]
	return str
	

if __name__ == '__main__':
	main()