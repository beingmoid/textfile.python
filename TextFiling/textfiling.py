#with open ('X:\\test.txt','w') as file_object:
#    contents=file_object.readlines()
 #   pi_string=''
  #  for line in contents:
   #     pi_string+=line.rstrip()+","
#print(pi_string)
#print(len(pi_string))
#print
 #   file_object.write("i love programming ! <3")
  #  print(file_object )
#with open ('X:\\test.txt','a') as file_object:
 #   file_object.write('Love=Programming')
  #  my=file_object
try:
    while True:
        fst_num=input("First Number")
        last_num =input("Second Number")
        if fst_num=='q':
            break
        if last_num=='q':
            break
        ans=int(fst_num)/int(last_num)


except:
    print("Cant divide by zero")
else:
    print(ans)
