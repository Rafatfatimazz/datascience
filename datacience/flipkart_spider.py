from dputils import scrape
#step 1:get the data s soup obj  
#step 2: create the setup dictionaries
# step 3:pass the dictionaries into the extrct_many()function
#step 4: repeat step 1 to step 3 until data keep coming
# step 5: check and save data into a file

## understanding the url
#url="https://www.flipkart.com/search?q=bags&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=7"
## after ? url parameters
#print(url.split("?"[-1].split("&")))

#step 1:

query="laptop"
pos=2
url=f"https://www.flipkart.com/search?q={query}&page={pos}" ## dynamic website
print(url)
soup=scrape.get_webpage_data(url)

#step 2:
# target dic,item dict,etc

t={'tag':'div','attrs':{'class':'_1YokD2 _3Mn1Gg'}}
rep_items={'tag':'div','attrs':{'_1AtVbE col-12-12'}}
title={'tag':'div','attrs':{'class':'_4rR01T'}}
price={'tag':'div','attrs':{'class':'_30jeq3 _1_WHN1'}}
link={'tag':'a','attrs':{'class':'_1fQZEK'},'output':'href'}

#step 3:

data=scrap.extract_many(
    soup,
    target=t,
    items=rep_items,
    title=title,
    price=price,
    link=link)
print(data)    

laptops=getdata()