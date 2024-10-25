import webbrowser

chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#the text that you want to search for on the website
search_text = input("Type the name of the item you want to search for: ")



#WEBSITES NORMAL RELEVANCE FILTER / SORT

temu = 'https://www.temu.com/search_result.html?search_key='+search_text+'&search_method=user&refer_page_el_sn=200010&srch_enter_source=top_search_entrance_10005&refer_page_name=home&refer_page_id=10005_1725270977012_s4ohou1qx7&refer_page_sn=10005&_x_sessn_id=u6u95j2hif'

target = 'https://www.target.com.au/search?sEngine=c&text='+search_text
big_w = 'https://www.bigw.com.au/search?text='+search_text
kmart = 'https://www.kmart.com.au/search/?searchTerm='+search_text

chemist_warehouse = 'https://www.chemistwarehouse.com.au/search?searchtext='+search_text+'&fh=1'
priceline = 'https://www.priceline.com.au/search/'+search_text

spudshed = 'https://www.ubereats.com/au/store/spudshed-morley/yPbq1TCTWha0Q78Yr0DqNQ?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMjI0JTIwSHVkc29uJTIwU3RyZWV0JTIyJTJDJTIycmVmZXJlbmNlJTIyJTNBJTIyNWUyYzM1M2YtMWI5ZC01NGRjLTA4Y2ItN2MyMDAwOWJhOWIwJTIyJTJDJTIycmVmZXJlbmNlVHlwZSUyMiUzQSUyMnViZXJfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EtMzEuOTEwOTUxOSUyQyUyMmxvbmdpdHVkZSUyMiUzQTExNS45MTEwMzA1JTdE&storeSearchQuery='+search_text
coles = 'https://www.coles.com.au/search/products?q='+search_text+'&sortBy=relevance'
woolworths = 'https://www.woolworths.com.au/shop/search/products?searchTerm='+search_text+'&pageNumber=1&sortBy=TraderRelevance'

bunnings = 'https://www.bunnings.com.au/search/products?page=1&q='+search_text+'&sort=BoostOrder'
super_cheap_auto = 'https://www.supercheapauto.com.au/search?q='+search_text+'&lang=en_AU'

#WEBSITES UNIT FILTER / SORT

target_unit = 'https://www.target.com.au/search?sEngine=c&text='+search_text
big_w_unit = 'https://www.bigw.com.au/search?text='+search_text
kmart_unit = 'https://www.kmart.com.au/search/?searchTerm='+search_text

chemist_warehouse_unit = 'https://www.chemistwarehouse.com.au/search?searchtext='+search_text+'&fh=1'
priceline_unit = 'https://www.priceline.com.au/search/'+search_text+'?sortCode=price-asc'

coles_unit = 'https://www.coles.com.au/search/products?q='+search_text+'&sortBy=unitPriceAscending'
woolworths_unit = 'https://www.woolworths.com.au/shop/search/products?searchTerm='+search_text+'&pageNumber=1&sortBy=CUPAsc'

bunnings_unit = 'https://www.bunnings.com.au/search/products?page=1&q='+search_text+'&sort=PriceAscending'
super_cheap_auto_unit = 'https://www.supercheapauto.com.au/search?q='+search_text+'&srule=Price%20Ascending&start=0&sz=60'

#WEBSITES CHEAPEST FILTER / SORT

temu_cheap = 'https://www.temu.com/search_result.html?search_key='+search_text+'&search_method=user&refer_page_el_sn=200010&srch_enter_source=top_search_entrance_10005&refer_page_name=home&refer_page_id=10005_1725270977012_s4ohou1qx7&refer_page_sn=10005&_x_sessn_id=u6u95j2hif&filter_items=2%3A0'
aliexpress_cheap = 'https://www.aliexpress.com/w/wholesale-text.html?g=y&SearchText='+search_text+'&sortType=price_asc'
ebay_cheap = 'https://www.ebay.com.au/sch/i.html?_from=R40&_nkw='+search_text+'&_sacat=0&_sop=15'


target_cheap = 'https://www.target.com.au/search?sEngine=c&text='+search_text+'&sortBy=price&sortOrder=ascending&page=1'
big_w_cheap = 'https://www.bigw.com.au/search?text='+search_text+'&sort=price-asc'
kmart_cheap = 'https://www.kmart.com.au/search/?searchTerm='+search_text+'&sortBy=price-low-to-high'

chemist_warehouse_cheap = 'https://www.chemistwarehouse.com.au/search?searchtext='+search_text+'&fh=1'
priceline_cheap = 'https://www.priceline.com.au/search/'+search_text+'?sortCode=price-asc'

coles_cheap = 'https://www.coles.com.au/search/products?q='+search_text+'&sortBy=priceAscending'
woolworths_cheap = 'https://www.woolworths.com.au/shop/search/products?searchTerm='+search_text+'&pageNumber=1&sortBy=PriceAsc'

bunnings_cheap = 'https://www.bunnings.com.au/search/products?page=1&q='+search_text+'&sort=PriceAscending'
super_cheap_auto_cheap = 'https://www.supercheapauto.com.au/search?q='+search_text+'&srule=Price%20Ascending&start=0&sz=60'

#WEBSITES EXPENSIVE FILTER / SORT

temu ='https://www.temu.com/search_result.html?search_key='+search_text+'&search_method=user&refer_page_el_sn=200010&srch_enter_source=top_search_entrance_10005&refer_page_name=home&refer_page_id=10005_1725270977012_s4ohou1qx7&refer_page_sn=10005&_x_sessn_id=u6u95j2hif&filter_items=2%3A1'

target_expensive = 'https://www.target.com.au/search?sEngine=c&text='+search_text+'&sortBy=price&sortOrder=descending&page=1'
big_w_expensive = 'https://www.bigw.com.au/search?text='+search_text+'&sort=price-desc'
kmart_expensive = 'https://www.kmart.com.au/search/?searchTerm='+search_text+'&sortBy=price-high-to-low'

chemist_warehouse_expensive = 'https://www.chemistwarehouse.com.au/search?searchtext='+search_text+'&fh=1'
priceline_expensive = 'https://www.priceline.com.au/search/'+search_text+'?sortCode=price-dsc'

coles_expensive = 'https://www.coles.com.au/search/products?q='+search_text+'&sortBy=priceDescending'
woolworths_expensive = 'https://www.woolworths.com.au/shop/search/products?searchTerm='+search_text+'&pageNumber=1&sortBy=PriceDesc'

bunnings_expensive = 'https://www.bunnings.com.au/search/products?page=1&q='+search_text+'&sort=PriceDescending'
super_cheap_auto_expensive = 'https://www.supercheapauto.com.au/search?q='+search_text+'&srule=Price%20Descending&start=0&sz=60'



#'+search_text+'



allwebsites = [target, big_w, kmart, chemist_warehouse, coles, woolworths, bunnings, super_cheap_auto]
cheapunit_allwebsites = [target_unit, big_w_unit, kmart_unit, chemist_warehouse_unit, coles_unit, woolworths_unit, priceline_unit, bunnings_unit, super_cheap_auto_unit, temu_cheap, aliexpress_cheap, ebay_cheap]
cheapest_allwebsites = [target_cheap, big_w_cheap, kmart_cheap, chemist_warehouse_cheap, coles_cheap, woolworths_cheap, bunnings_cheap, super_cheap_auto_cheap, temu_cheap, aliexpress_cheap, ebay_cheap]
expensive_allwebsites = [target_expensive, big_w_expensive, kmart_expensive, chemist_warehouse_expensive, coles_expensive, woolworths_expensive, bunnings_expensive, super_cheap_auto_expensive]
food = [target_cheap, big_w_cheap, kmart_cheap, chemist_warehouse_cheap, coles_unit, woolworths_unit]
coleswoolies = [coles_unit, woolworths_unit]

#input("Which website would you like to search? Please type one of the following: target, big_w, kmart, chemist_warehouse, coles, woolworths, bunnings, super_cheap_auto: ")

#opens websites with the search text function
def do_search(websitelist):
    browse = webbrowser.get(chromePath)
    for i in websitelist:
        browse.open_new_tab(i)


########################################################################################
#PROGRAM STARTS HERE




#search_text()

question_quick = 'Would you like to search for lowest unit price in Coles and Woolworths? Y/N: '
answer_question_quick = input(question_quick)
if answer_question_quick == 'Y':
    do_search(coleswoolies)
    
elif answer_question_quick == 'N':
    question_typeofsort = 'Would you like to search by "unit", "lowest", "highest" or "relevance" or "food"? '
    answer_question_typeofsort = input(question_typeofsort)
    if answer_question_typeofsort == 'unit':
        do_search(cheapunit_allwebsites)
    elif answer_question_typeofsort == 'lowest':
        do_search(cheapunit_allwebsites)
    elif answer_question_typeofsort == 'highest':
        do_search(cheapunit_allwebsites)
    elif answer_question_typeofsort == 'relevance':
        do_search(allwebsites)
    elif answer_question_typeofsort == 'food':
        do_search(food)







#domain = ''


#webbrowser.get(chromePath).open(big_w)
#webbrowser.get(chromePath).open(kmart)
#imported webbrowser library uses the web browser to open the website

#webbrowser.open(bigw)
#webbrowser.open(kmart)
