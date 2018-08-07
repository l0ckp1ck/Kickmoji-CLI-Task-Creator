import csv
import os 

os.system('clear')

print('Kickmoji CLI Task Maker \nMade by Lockpick \n')

try:
    isin = raw_input('isInStock (TRUE or FALSE) : ')
    nl = raw_input('NikeLab (TRUE or FALSE) : ')
    br = raw_input('BootRoom (TRUE or FALSE) : ')
    sr = raw_input('Size Range (No Quotations) : ')
    size = raw_input('Size : ')
    mode = raw_input('Mode (desktop/app) : ')
    region = raw_input('Region (All Caps) : ')
    sku = raw_input('SKU : ')
    proxy = raw_input('Proxy : ')
    ppt = int(raw_input("Tasks Per Profile : "))
    tc = int(raw_input('Number of Tasks : '))

except:
    print('Error Receiving Input')


tasks = []
prof_id = 0
count = 0 
while (tc != 0):
    prof_id = prof_id + 1
    for i in range(0,int(ppt)):
        tasks.append('{}~{}~{}~{}~{}~{}~{}~{}~{}~{}'.format(isin,nl,br,sr,size,mode,region,sku,proxy,prof_id))
        count = count + 1
    tc = tc - count


try:
    with open('tasks.csv', 'w') as file:
        fieldnames = ['IsInStock','IsNikelab', 'IsBootroom', 'sizeRange', 'size', 'mode', 'region', 'sku', 'proxy', 'profile', 'email', 'password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            task = task.split('~')
            writer.writerow({'IsInStock':task[0],'IsNikelab':task[1], 'IsBootroom':task[2], 'sizeRange':task[3], 'size':task[4], 'mode':task[5], 'region':task[6], 'sku':task[7], 'proxy':task[8], 'profile':task[9], 'email':'', 'password':''})
        print ('Tasks saved to tasks.csv!')
except:
    print('Error Saving Tasks')

